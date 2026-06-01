"""Minimal-repair engine: fix the 22 flagged conflicts via 1-for-1 swaps that preserve
each resident's call count and day-of-week distribution. Deterministic, logged."""
import json, datetime
from collections import defaultdict

D = json.load(open('/home/user/Apex_Artifacts/call_analysis/data.json'))
ROT = D['rotations']; PGY = D['pgy']; A = D['assignments']
def dt(s): return datetime.date.fromisoformat(s)

# ---------- shared rule logic ----------
NO_CALL = {'Away','Leave','NICU','Peds Inpatient','Peds ER'}
PTO = {
 'Wohlgemuth':[('2026-09-15','2026-09-19'),('2027-05-17','2027-05-21')],
 'Oehm':[('2027-05-15','2027-05-21'),('2026-10-08','2026-10-09')],
 'Stanek':[('2027-03-18','2027-03-21'),('2027-05-15','2027-05-16')],
 'Schutt':[('2026-07-11','2026-07-12'),('2027-03-15','2027-03-19')],
 'Patel':[('2026-08-06','2026-08-09'),('2027-01-28','2027-02-01')],
 'Strand':[('2026-10-26','2026-11-01')],
 'Bottke':[('2026-09-10','2026-09-10')],
}
NEXPLANON = {'Bottke':'2026-09-10','Patel':'2026-09-10'}
def rotation_on(name, d):
    for s,e,r in ROT[name]:
        if dt(s) <= d <= dt(e): return r
    return None
def on_pto(name, d):
    ds = d.isoformat()
    for s,e in PTO.get(name,[]):
        if dt(s) <= d <= dt(e): return True
    if NEXPLANON.get(name)==ds: return True
    return False
def hard_violation(name, d):
    """Return reason string if assigning `name` call on date `d` is a HARD violation, else None."""
    rot = rotation_on(name, d)
    if rot is None: return None
    dow = d.strftime('%a'); pgy = PGY[name]
    if rot in NO_CALL: return f'no-call rotation {rot}'
    if rot in ('Gynecology','Community Medicine') and dow in ('Sun','Mon','Wed'): return f'GYN/CM {dow}'
    if rot=='Family Med Ambulatory' and d>=datetime.date(2027,1,1) and dow in ('Sun','Mon','Wed'): return f'FM-Amb {dow}'
    if rot=='Pediatrics' and pgy=='R2' and dow=='Thu': return 'R2-Peds Thu'
    if rot=='Dermatology' and dow=='Mon': return 'Derm Mon'
    if rot=='Ultrasound' and dow in ('Sun','Wed'): return f'US {dow}'
    if rot=='Cardiology' and dow=='Tue': return 'Cards Tue'
    if on_pto(name, d): return 'PTO'
    return None
def soft_flag(name, d):
    rot = rotation_on(name,d)
    if rot=='Community Based Practice': return 'CBP'
    if rot=='Orthopaedics' and PGY[name]=='R3': return 'R3-Ortho'
    return None

# ---------- mutable schedule ----------
sched = {a['date']: {'interns':list(a['interns']), 'seniors':list(a['seniors']),
                     'dow':a['dow'], 'line1':a['line1'],'line2':a['line2']} for a in A}
dates_sorted = sorted(sched.keys())
def is_oncall(name, ds):
    e = sched.get(ds)
    return e is not None and (name in e['interns'] or name in e['seniors'])
def neighbors_oncall(name, d):
    return is_oncall(name,(d-datetime.timedelta(days=1)).isoformat()) or \
           is_oncall(name,(d+datetime.timedelta(days=1)).isoformat())

# Night-float weekday intern slots are FIXED (rotation-driven) — never reassign those.
def is_nightfloat_slot(name, d):
    return PGY[name]=='R1' and rotation_on(name,d)=='Night Float' and d.strftime('%a') not in ('Sat','Sun')

DOW_WEIGHT={'Wed':1,'Thu':1,'Mon':2,'Tue':2,'Fri':3,'Sun':3,'Sat':4}

def eligible(name, d, exclude_date=None):
    """Can `name` take call on date d? (strict: no hard violation, not already on, not NF-fixed elsewhere)"""
    ds=d.isoformat()
    if is_oncall(name, ds): return False
    if hard_violation(name, d): return False
    if soft_flag(name, d): return False           # don't move conflicts onto soft-flagged days either
    if neighbors_oncall(name, d): return False     # avoid consecutive-day call
    return True

# ---------- detect current hard+PTO conflicts (seniors and 2nd-half interns) ----------
conflicts=[]
for ds in dates_sorted:
    d=dt(ds); e=sched[ds]
    for role in ('interns','seniors'):
        for name in list(e[role]):
            r = hard_violation(name,d)
            if r:
                # skip night-float fixed slots (shouldn't have violations anyway)
                if is_nightfloat_slot(name,d): continue
                conflicts.append((ds,name,role,r))
# order: no-call rotations first, then others; chronological within
prio = lambda c: (0 if 'no-call' in c[3] else (1 if c[3]=='PTO' else 2), c[0])
conflicts.sort(key=prio)

# ---------- swap solver ----------
changes=[]   # (date_conflict, out_name, in_name, swap_date, reason)
def find_swap(ds, R, role, reason):
    d=dt(ds); dow=d.strftime('%a')
    same_pgy=[n for n in PGY if PGY[n]==PGY[R] and n!=R]
    other_pgy=[n for n in PGY if PGY[n] in (('R2','R3') if role=='seniors' else ('R1',)) and n!=R and PGY[n]!=PGY[R]]
    cand_partners = same_pgy + other_pgy   # prefer same PGY to preserve R2-Sun/R3-Fri structure
    best=None
    for P in cand_partners:
        if role=='seniors' and PGY[P]=='R1': continue
        if role=='interns' and PGY[P]!='R1': continue
        if not eligible(P, d): continue
        # find a date D2 where P is on call (same role slot) and R can take it
        for ds2 in dates_sorted:
            if ds2==ds: continue
            e2=sched[ds2]
            if P not in e2[role]: continue
            d2=dt(ds2)
            if is_nightfloat_slot(P,d2): continue      # don't move P's night-float slot
            # R must be eligible on d2 (temporarily ignoring that P is there / R not there)
            if is_oncall(R, ds2): continue
            if hard_violation(R, d2) or soft_flag(R,d2): continue
            # consecutive check for R at d2 and P at d (already eligible(P,d) checked neighbors)
            if is_oncall(R,(d2-datetime.timedelta(days=1)).isoformat()) or is_oncall(R,(d2+datetime.timedelta(days=1)).isoformat()):
                continue
            score = (0 if d2.strftime('%a')==dow else 1,                       # prefer same DOW
                     abs(DOW_WEIGHT[d2.strftime('%a')]-DOW_WEIGHT[dow]),       # else same weight
                     0 if PGY[P]==PGY[R] else 1,                                # prefer same PGY
                     abs((d2-d).days))                                          # prefer nearby
            if best is None or score<best[0]:
                best=(score,P,ds2)
    return best

for ds,R,role,reason in conflicts:
    # may have been resolved already if R got swapped out by a prior change
    if R not in sched[ds][role]:
        continue
    res=find_swap(ds,R,role,reason)
    if res is None:
        changes.append((ds,R,'<NO SWAP FOUND>','',reason)); continue
    _,P,ds2=res
    # apply swap: P->ds (replace R), R->ds2 (replace P)
    sched[ds][role]=[P if x==R else x for x in sched[ds][role]]
    sched[ds2][role]=[R if x==P else x for x in sched[ds2][role]]
    changes.append((ds,R,P,ds2,reason))

print("="*96)
print(f"MINIMAL-REPAIR SWAPS ({len([c for c in changes if c[2]!='<NO SWAP FOUND>'])} applied)")
print("="*96)
for ds,R,P,ds2,reason in changes:
    d=dt(ds);
    if P=='<NO SWAP FOUND>':
        print(f"  !! {ds} {d.strftime('%a')}  {R:<11} [{reason}]  -> NO SWAP FOUND")
    else:
        d2=dt(ds2)
        print(f"  {ds} {d.strftime('%a')} {R:<11}[{reason:<16}] <-> {P:<11} takes {ds}; {R} takes {ds2} {d2.strftime('%a')}")

# save repaired schedule
json.dump({'sched':sched,'changes':changes},
          open('/home/user/Apex_Artifacts/call_analysis/repaired.json','w'), indent=1, default=str)
print(f"\nTotal conflicts targeted: {len(conflicts)}; swaps applied: {len([c for c in changes if c[2]!='<NO SWAP FOUND>'])}; unresolved: {len([c for c in changes if c[2]=='<NO SWAP FOUND>'])}")

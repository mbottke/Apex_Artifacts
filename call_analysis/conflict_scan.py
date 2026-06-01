"""Scan the preliminary call schedule for rotation conflicts, PTO conflicts, holiday & spacing issues."""
import json, datetime
from collections import defaultdict, Counter

D = json.load(open('/home/user/Apex_Artifacts/call_analysis/data.json'))
ROT = D['rotations']; PGY = D['pgy']; A = D['assignments']
def dt(s): return datetime.date.fromisoformat(s)
A_by_date = {a['date']: a for a in A}

def rotation_on(name, d):
    for s,e,r in ROT[name]:
        if dt(s) <= d <= dt(e): return r
    return None

# ---- restriction rules ----
NO_CALL = {'Away','Leave','NICU','Peds Inpatient','Peds ER'}
def second_half(d): return d >= datetime.date(2027,1,1)

def violations_for(name, d, role):
    rot = rotation_on(name, d)
    if rot is None: return [(rot,'HARD','No rotation found in grid (gap)')] if False else []
    dow = d.strftime('%a'); out=[]
    pgy = PGY[name]
    if rot in NO_CALL:
        out.append((rot,'HARD',f'No-call rotation: {rot}'))
    if rot == 'Community Based Practice':
        out.append((rot,'SOFT','CBP (2 wks away) — avoid call unless necessary'))
    if rot == 'Orthopaedics' and pgy=='R3':
        out.append((rot,'SOFT','R3 Orthopaedics — limited call only'))
    if rot in ('Gynecology','Community Medicine') and dow in ('Sun','Mon','Wed'):
        out.append((rot,'HARD',f'GYN/CM ({rot}) — must avoid Sun/Mon/Wed (LC & GYN coverage)'))
    if rot == 'Family Med Ambulatory' and second_half(d) and dow in ('Sun','Mon','Wed'):
        out.append((rot,'HARD','FM Ambulatory (2nd half) — avoid Sun/Mon/Wed (LC & GYN)'))
    if rot == 'Pediatrics' and pgy=='R2' and dow=='Thu':
        out.append((rot,'HARD','R2 Pediatrics — avoid Thursday (Fri AM peds clinic E.DSM)'))
    if rot == 'Dermatology' and dow=='Mon':
        out.append((rot,'HARD','Dermatology — avoid Monday (Tues Derm clinic)'))
    if rot == 'Ultrasound' and dow in ('Sun','Wed'):
        out.append((rot,'HARD','Ultrasound — avoid Sun/Wed (on-site Mon & Thu only)'))
    if rot == 'Cardiology' and dow=='Tue':
        out.append((rot,'HARD','Cardiology — avoid Tuesday night (Wed personal clinic all day)'))
    return out

# ---- 1. ROTATION CONFLICT SCAN ----
print("="*92)
print("ROTATION-CONFLICT SCAN (every assigned call vs that resident's rotation)")
print("="*92)
hard=[]; soft=[]
for a in A:
    d = dt(a['date'])
    for nm in a['interns']:
        for rot,sev,reason in violations_for(nm,d,'intern'):
            (hard if sev=='HARD' else soft).append((a['date'],a['dow'],nm,PGY[nm],'intern',rot,reason,a['raw']))
    for nm in a['seniors']:
        for rot,sev,reason in violations_for(nm,d,'senior'):
            (hard if sev=='HARD' else soft).append((a['date'],a['dow'],nm,PGY[nm],'senior',rot,reason,a['raw']))

print(f"\n--- HARD conflicts: {len(hard)} ---")
for v in hard:
    print(f"  {v[0]} {v[1]}  {v[2]:<11}({v[3]}/{v[4]:<6})  {v[6]}   [cell:{v[7]}]")
print(f"\n--- SOFT conflicts: {len(soft)} ---")
for v in soft:
    print(f"  {v[0]} {v[1]}  {v[2]:<11}({v[3]}/{v[4]:<6})  {v[6]}   [cell:{v[7]}]")

# ---- 2. PTO CONFLICTS ----
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
print("\n"+"="*92); print("PTO / TIME-OFF CONFLICTS"); print("="*92)
pto_hits=[]
for a in A:
    d=dt(a['date'])
    for nm in a['interns']+a['seniors']:
        for s,e in PTO.get(nm,[]):
            if dt(s)<=d<=dt(e):
                pto_hits.append((a['date'],a['dow'],nm,a['raw'],f'PTO {s}..{e}'))
        if NEXPLANON.get(nm)==a['date']:
            pto_hits.append((a['date'],a['dow'],nm,a['raw'],'Nexplanon training eve — DO NOT schedule 9/10'))
for h in pto_hits:
    print(f"  {h[0]} {h[1]}  {h[2]:<11} {h[4]}   [cell:{h[3]}]")
if not pto_hits: print("  (none)")

# ---- 3. HOLIDAYS ----
HOL = {
 '2026-07-04':'Independence Day (Sat)','2026-09-07':'Labor Day (Mon)',
 '2026-11-26':'Thanksgiving (Thu)','2026-11-27':'Day after Thanksgiving (Fri)',
 '2026-12-24':'Christmas Eve (Thu)','2026-12-25':'Christmas (Fri)',
 '2026-12-31':"New Year's Eve (Thu)",'2027-01-01':"New Year's Day (Fri)",
 '2027-01-18':'MLK Day (Mon)','2027-02-15':'Presidents Day (Mon)',
 '2027-03-28':'Easter (Sun)','2027-05-09':"Mother's Day (Sun)",
 '2027-05-31':'Memorial Day (Mon)','2027-06-19':'Juneteenth (Sat)',
}
print("\n"+"="*92); print("HOLIDAY ASSIGNMENTS"); print("="*92)
for dstr,label in HOL.items():
    a=A_by_date.get(dstr)
    if a:
        who = ", ".join(f"{n}({PGY[n]})" for n in a['interns']+a['seniors'])
        print(f"  {dstr} {label:<32} -> {who}")
    else:
        print(f"  {dstr} {label:<32} -> (no call entry / not in schedule)")

# ---- 4. SPACING: consecutive-day call (excl. night-float runs) ----
print("\n"+"="*92); print("TIGHT SPACING: call on consecutive days (post-call not respected)"); print("="*92)
appear = defaultdict(list)
for a in A:
    d=dt(a['date'])
    for nm in a['interns']:
        rot = rotation_on(nm,d)
        kind = 'NF' if (rot=='Night Float' and d.strftime('%a') not in ('Sat','Sun')) else 'call'
        appear[nm].append((d,kind))
    for nm in a['seniors']:
        appear[nm].append((d,'call'))
spacing=[]
for nm,lst in appear.items():
    lst.sort()
    for i in range(1,len(lst)):
        d0,k0=lst[i-1]; d1,k1=lst[i]
        if (d1-d0).days==1 and not (k0=='NF' and k1=='NF'):
            # ignore NF->NF consecutive (expected). Flag call->call, call->NF, NF->call boundaries that are real 24h adjacency
            if k0=='call' or k1=='call':
                # within an NF week, NF->call at end (Fri night float then Sat 24h) is somewhat expected; flag only call/call truly
                if k0=='call' and k1=='call':
                    spacing.append((nm,PGY[nm],d0.isoformat(),d1.isoformat()))
for s in sorted(spacing,key=lambda x:x[2]):
    print(f"  {s[1]} {s[0]:<11} consecutive 24h call: {s[2]} -> {s[3]}")
if not spacing: print("  (no consecutive 24h-call pairs found)")

json.dump({'hard':hard,'soft':soft,'pto':pto_hits,'spacing':spacing},
          open('/home/user/Apex_Artifacts/call_analysis/conflicts.json','w'),indent=1,default=str)
print(f"\nSUMMARY: {len(hard)} hard rotation conflicts, {len(soft)} soft, {len(pto_hits)} PTO hits, {len(spacing)} consecutive-call pairs")

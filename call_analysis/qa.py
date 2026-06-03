"""Comprehensive QA on a repaired/rebuilt schedule. Re-runs all conflict checks, verifies
counts & day-of-week vs the original preliminary schedule, checks double-booking and spacing."""
import json, datetime, sys
from collections import defaultdict, Counter

WHICH = sys.argv[1] if len(sys.argv)>1 else 'repaired'
BASE='/home/user/Apex_Artifacts/call_analysis/'
D = json.load(open(BASE+'data.json')); ROT=D['rotations']; PGY=D['pgy']; A0=D['assignments']
R = json.load(open(BASE+f'{WHICH}.json')); sched=R['sched']
def dt(s): return datetime.date.fromisoformat(s)

NO_CALL={'Away','Leave','NICU','Peds Inpatient','Peds ER'}
PTO={'Wohlgemuth':[('2026-09-15','2026-09-19'),('2027-05-17','2027-05-21')],
 'Oehm':[('2027-05-15','2027-05-21'),('2026-10-08','2026-10-09')],
 'Stanek':[('2027-03-18','2027-03-21'),('2027-05-15','2027-05-16')],
 'Schutt':[('2026-07-11','2026-07-12'),('2027-03-15','2027-03-19')],
 'Patel':[('2026-08-06','2026-08-09'),('2027-01-28','2027-02-01')],
 'Strand':[('2026-10-26','2026-11-01')],'Bottke':[('2026-09-10','2026-09-10')]}
NEXPLANON={'Bottke':'2026-09-10','Patel':'2026-09-10'}
def rotation_on(n,d):
    for s,e,r in ROT[n]:
        if dt(s)<=d<=dt(e): return r
def on_pto(n,d):
    for s,e in PTO.get(n,[]):
        if dt(s)<=d<=dt(e): return True
    return NEXPLANON.get(n)==d.isoformat()
def hard_violation(n,d):
    rot=rotation_on(n,d)
    if rot is None: return None
    dow=d.strftime('%a'); pgy=PGY[n]
    if rot in NO_CALL: return f'no-call {rot}'
    if rot in ('Gynecology','Community Medicine') and dow in('Sun','Mon','Wed'): return f'GYN/CM {dow}'
    if rot=='Family Med Ambulatory' and d>=datetime.date(2027,1,1) and dow in('Sun','Mon','Wed'): return f'FM-Amb {dow}'
    if rot=='Pediatrics' and pgy=='R2' and dow=='Thu': return 'R2-Peds Thu'
    if rot=='Dermatology' and dow=='Mon': return 'Derm Mon'
    if rot=='Ultrasound' and dow in('Sun','Wed'): return f'US {dow}'
    if rot=='Cardiology' and dow=='Tue': return 'Cards Tue'
    if on_pto(n,d): return 'PTO'
    return None
def soft_flag(n,d):
    rot=rotation_on(n,d)
    if rot=='Community Based Practice': return 'CBP'
    if rot=='Orthopaedics' and PGY[n]=='R3': return 'R3-Ortho'

# rebuild flat assignment list from sched
A=[]
for ds,e in sched.items():
    A.append({'date':ds,'dow':dt(ds).strftime('%a'),'interns':e['interns'],'seniors':e['seniors']})
A.sort(key=lambda x:x['date'])

print("="*92); print(f"QA REPORT — '{WHICH}' schedule"); print("="*92)

# 1. hard + PTO conflicts
hard=[]; soft=[]
for a in A:
    d=dt(a['date'])
    for n in a['interns']+a['seniors']:
        if n not in PGY: continue
        h=hard_violation(n,d)
        if h: hard.append((a['date'],a['dow'],n,h))
        s=soft_flag(n,d)
        if s: soft.append((a['date'],a['dow'],n,s))
print(f"\n[1] HARD rotation/PTO conflicts: {len(hard)}")
for v in hard: print(f"      {v[0]} {v[1]} {v[2]} — {v[3]}")
print(f"[1b] SOFT flags (CBP / R3-Ortho, allowed): {len(soft)}")
for v in soft: print(f"      {v[0]} {v[1]} {v[2]} — {v[3]}")

# 2. counts vs original
c0=Counter(); cN=Counter(); dow0=defaultdict(Counter); dowN=defaultdict(Counter)
for a in A0:
    for n in a['interns']+a['seniors']:
        if n in PGY: c0[n]+=1; dow0[n][a['dow']]+=1
for a in A:
    for n in a['interns']+a['seniors']:
        if n in PGY: cN[n]+=1; dowN[n][dt(a['date']).strftime('%a')]+=1
print(f"\n[2] COUNT & DOW preservation vs preliminary:")
allgood=True
for n in PGY:
    dc=cN[n]-c0[n]
    dowdiff = {k:dowN[n][k]-dow0[n][k] for k in set(dow0[n])|set(dowN[n]) if dowN[n][k]-dow0[n][k]!=0}
    if dc!=0 or dowdiff:
        allgood=False
        print(f"      {n:<11} count {c0[n]}->{cN[n]} (Δ{dc:+d})  DOWΔ {dowdiff}")
print("      ALL COUNTS & DOW IDENTICAL TO PRELIMINARY ✓" if allgood else "      <-- differences above")

# 3. double-booking (same person twice in one day)
dbl=[]
for a in A:
    names=a['interns']+a['seniors']
    for n in set(names):
        if names.count(n)>1: dbl.append((a['date'],n))
print(f"\n[3] Double-booking (same resident twice/day): {len(dbl)}")
for v in dbl: print(f"      {v[0]} {v[1]}")

# 4. coverage: every date still has >=1 intern (where expected) and exactly the same #names
miss=[]
A0_by={a['date']:a for a in A0}
for a in A:
    o=A0_by.get(a['date'])
    if o and len(a['interns'])+len(a['seniors'])!=len(o['interns'])+len(o['seniors']):
        miss.append((a['date'],f"{len(o['interns'])+len(o['seniors'])}->{len(a['interns'])+len(a['seniors'])}"))
print(f"\n[4] Per-day headcount changes vs preliminary: {len(miss)}")
for v in miss: print(f"      {v[0]} {v[1]}")

# 5. spacing: consecutive-day 24h call (exclude night-float runs)
def is_nf(n,d): return PGY[n]=='R1' and rotation_on(n,d)=='Night Float' and d.strftime('%a') not in('Sat','Sun')
appear=defaultdict(list)
for a in A:
    d=dt(a['date'])
    for n in a['interns']: appear[n].append((d,'NF' if is_nf(n,d) else 'call'))
    for n in a['seniors']: appear[n].append((d,'call'))
spacing=[]
for n,lst in appear.items():
    lst.sort()
    for i in range(1,len(lst)):
        (d0,k0),(d1,k1)=lst[i-1],lst[i]
        if (d1-d0).days==1 and k0=='call' and k1=='call':
            spacing.append((n,d0.isoformat(),d1.isoformat()))
print(f"\n[5] Consecutive 24h-call pairs (no post-call day): {len(spacing)}")
for v in sorted(spacing,key=lambda x:x[1]): print(f"      {PGY[v[0]]} {v[0]:<11} {v[1]} -> {v[2]}")

print("\n"+"="*92)
ok = (len(hard)==0 and len(dbl)==0 and allgood)
print(f"QA VERDICT: {'PASS ✓ — 0 hard conflicts, counts/DOW preserved, no double-booking' if ok else 'ISSUES REMAIN — see above'}")
print("="*92)

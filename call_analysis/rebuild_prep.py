"""Extract slot structure for the full rebuild: per-day intern/senior slot counts,
fixed night-float intern assignments, eligibility, holidays. Save to rebuild_prep.json."""
import json, datetime
from collections import Counter, defaultdict
D=json.load(open('/home/user/Apex_Artifacts/call_analysis/data.json'))
ROT=D['rotations']; PGY=D['pgy']; A=D['assignments']
def dt(s): return datetime.date.fromisoformat(s)
INTERNS=[n for n in PGY if PGY[n]=='R1']; R2=[n for n in PGY if PGY[n]=='R2']; R3=[n for n in PGY if PGY[n]=='R3']; SEN=R2+R3
def rot_on(n,d):
    for s,e,r in ROT[n]:
        if dt(s)<=d<=dt(e): return r

NO_CALL={'Away','Leave','NICU','Peds Inpatient','Peds ER'}
PTO={'Wohlgemuth':[('2026-09-15','2026-09-19'),('2027-05-17','2027-05-21')],
 'Oehm':[('2027-05-15','2027-05-21'),('2026-10-08','2026-10-09')],
 'Stanek':[('2027-03-18','2027-03-21'),('2027-05-15','2027-05-16')],
 'Schutt':[('2026-07-11','2026-07-12'),('2027-03-15','2027-03-19')],
 'Patel':[('2026-08-06','2026-08-09'),('2027-01-28','2027-02-01')],
 'Strand':[('2026-10-26','2026-11-01')],'Bottke':[('2026-09-10','2026-09-10')]}
NEXPLANON={'Bottke':'2026-09-10','Patel':'2026-09-10'}
def on_pto(n,d):
    for s,e in PTO.get(n,[]):
        if dt(s)<=d<=dt(e): return True
    return NEXPLANON.get(n)==d.isoformat()
def hard_block(n,d):
    """True if resident n CANNOT take call on date d (hard)."""
    rot=rot_on(n,d)
    # Empty rotation (orientation 7/1-7/4, winter holiday block 12/20-1/2): resident is AVAILABLE.
    if rot is None: return on_pto(n,d)
    dow=d.strftime('%a'); pgy=PGY[n]
    if rot in NO_CALL: return True
    if rot in('Gynecology','Community Medicine') and dow in('Sun','Mon','Wed'): return True
    if rot=='Family Med Ambulatory' and d>=datetime.date(2027,1,1) and dow in('Sun','Mon','Wed'): return True
    if rot=='Pediatrics' and pgy=='R2' and dow=='Thu': return True
    if rot=='Dermatology' and dow=='Mon': return True
    if rot=='Ultrasound' and dow in('Sun','Wed'): return True
    if rot=='Cardiology' and dow=='Tue': return True
    if on_pto(n,d): return True
    return False
def soft_block(n,d):
    rot=rot_on(n,d)
    if rot=='Community Based Practice': return True
    if rot=='Orthopaedics' and PGY[n]=='R3': return True
    return False

# slot counts per day + fixed night-float intern
days=[a['date'] for a in A]
slot_intern={}; slot_senior={}; nf_fixed={}
multi=[]
for a in A:
    d=dt(a['date']); ds=a['date']
    slot_intern[ds]=len(a['interns']); slot_senior[ds]=len(a['seniors'])
    if len(a['interns'])>1 or len(a['seniors'])>1: multi.append((ds,a['interns'],a['seniors']))
    # night-float intern = intern on 'Night Float' rotation, weekday, 1st half
    if d.strftime('%a') not in('Sat','Sun') and d<datetime.date(2027,1,1):
        nfs=[i for i in INTERNS if rot_on(i,d)=='Night Float']
        if len(nfs)==1: nf_fixed[ds]=nfs[0]
        elif len(nfs)>1: nf_fixed[ds]='MULTI:'+','.join(nfs)

print("Slot-count distribution:")
print("  intern slots/day:", Counter(slot_intern.values()))
print("  senior slots/day:", Counter(slot_senior.values()))
print(f"  days with >1 senior or >1 intern: {len(multi)}")
for m in multi: print("    ",m)
print(f"\nNight-float fixed weekday slots: {len([k for k,v in nf_fixed.items() if not str(v).startswith('MULTI')])}")
print("  MULTI-NF days (need attention):", [k for k,v in nf_fixed.items() if str(v).startswith('MULTI')])

# How many NF blocks per intern (fixed weekday load)
nf_per=Counter()
for ds,v in nf_fixed.items():
    if not str(v).startswith('MULTI'): nf_per[v]+=1
print("\nFixed NF weekday shifts per intern:", dict(nf_per))

# preliminary day-type counts per resident (target reference)
dowc=defaultdict(Counter); tot=Counter()
for a in A:
    for n in a['interns']+a['seniors']:
        if n in PGY: dowc[n][dt(a['date']).strftime('%a')]+=1; tot[n]+=1

# eligibility matrices
elig_hard={n:{ds:(not hard_block(n,dt(ds))) for ds in days} for n in PGY}
elig_soft={n:{ds:soft_block(n,dt(ds)) for ds in days} for n in PGY}

HOL={'2026-07-04':'minor','2026-09-07':'minor','2026-11-26':'MAJOR','2026-11-27':'minor',
 '2026-12-24':'MAJOR','2026-12-25':'MAJOR','2026-12-31':'MAJOR','2027-01-01':'MAJOR',
 '2027-01-18':'minor','2027-02-15':'minor','2027-03-28':'minor','2027-05-31':'minor'}
SPECIAL_INTERN=['2026-07-04','2026-09-07','2027-03-28','2027-05-31']  # mix up interns

out={'days':days,'INTERNS':INTERNS,'R2':R2,'R3':R3,'SEN':SEN,
 'slot_intern':slot_intern,'slot_senior':slot_senior,'nf_fixed':nf_fixed,
 'elig_hard':elig_hard,'elig_soft':elig_soft,
 'prelim_dow':{n:dict(dowc[n]) for n in dowc},'prelim_tot':dict(tot),
 'HOL':HOL,'SPECIAL_INTERN':SPECIAL_INTERN}
json.dump(out,open('/home/user/Apex_Artifacts/call_analysis/rebuild_prep.json','w'),default=str)
print("\nPrelim totals:",dict(tot))
print("saved rebuild_prep.json")

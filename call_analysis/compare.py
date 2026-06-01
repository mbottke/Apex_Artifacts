"""Side-by-side comparison: preliminary vs minimal-repair vs full-rebuild.
Reports per-resident totals, day-type mix, weighted load, Saturdays, Sundays, holidays, and rule compliance."""
import json, datetime
from collections import defaultdict, Counter
B='/home/user/Apex_Artifacts/call_analysis/'
D=json.load(open(B+'data.json')); PGY=D['pgy']; ROT=D['rotations']
def dt(s): return datetime.date.fromisoformat(s)
INT=[n for n in PGY if PGY[n]=='R1']; R2=[n for n in PGY if PGY[n]=='R2']; R3=[n for n in PGY if PGY[n]=='R3']; SEN=R2+R3
WT={'Wed':1,'Thu':1,'Mon':2,'Tue':2,'Fri':3,'Sun':3,'Sat':4}
HOL={'2026-07-04':'minor','2026-09-07':'minor','2026-11-26':'MAJOR','2026-11-27':'minor','2026-12-24':'MAJOR',
 '2026-12-25':'MAJOR','2026-12-31':'MAJOR','2027-01-01':'MAJOR','2027-01-18':'minor','2027-02-15':'minor',
 '2027-03-28':'minor','2027-05-31':'minor'}
SPECIAL=['2026-07-04','2026-09-07','2027-03-28','2027-05-31']

def load(which):
    if which=='preliminary':
        a=D['assignments']; return {x['date']:{'interns':x['interns'],'seniors':x['seniors']} for x in a}
    r=json.load(open(B+f'{which}.json'))['sched']; return {k:{'interns':v['interns'],'seniors':v['seniors']} for k,v in r.items()}

def metrics(sched):
    tot=Counter(); dow=defaultdict(Counter); wl=Counter(); hol=defaultdict(list)
    for ds,e in sched.items():
        d=dt(ds); wd=d.strftime('%a')
        for n in e['interns']+e['seniors']:
            if n not in PGY: continue
            tot[n]+=1; dow[n][wd]+=1; wl[n]+=WT[wd]
            if ds in HOL: hol[n].append(HOL[ds])
    return tot,dow,wl,hol

def spread(vals): return f"{min(vals)}..{max(vals)} (Δ{max(vals)-min(vals)})"

names_order=INT+R2+R3
for which in ['preliminary','repaired','rebuilt']:
    s=load(which); tot,dow,wl,hol=metrics(s)
    print("="*100); print(f"### {which.upper()} ###"); print("="*100)
    print(f"{'Name':<11}{'PGY':<4}{'Tot':>4}{'Mon':>4}{'Tue':>4}{'Wed':>4}{'Thu':>4}{'Fri':>4}{'Sat':>4}{'Sun':>4}{'Wload':>7}{'Avg':>6}  Holidays")
    for grp,lab in [(INT,'R1'),(R2,'R2'),(R3,'R3')]:
        for n in grp:
            c=dow[n]; h=hol.get(n,[])
            hs=f"{sum(1 for x in h if x=='MAJOR')}M/{sum(1 for x in h if x=='minor')}m"
            print(f"{n:<11}{PGY[n]:<4}{tot[n]:>4}{c['Mon']:>4}{c['Tue']:>4}{c['Wed']:>4}{c['Thu']:>4}{c['Fri']:>4}{c['Sat']:>4}{c['Sun']:>4}{wl[n]:>7}{wl[n]/max(tot[n],1):>6.2f}  {hs}")
        # cohort spreads
        sat=[dow[n]['Sat'] for n in grp]; wlc=[wl[n] for n in grp]; avg=[wl[n]/max(tot[n],1) for n in grp]; tt=[tot[n] for n in grp]
        print(f"   {lab} spreads: total {spread(tt)} | Sat {spread(sat)} | wload {spread(wlc)} | per-call-avg {min(avg):.2f}..{max(avg):.2f}")
    # rule checks
    r3sun=sum(dow[n]['Sun'] for n in R3)
    special_holders=[n for n in INT if any(ds in SPECIAL for ds,e in s.items() if n in e['interns'])]
    sc=Counter()
    for ds in SPECIAL:
        for n in s.get(ds,{}).get('interns',[]): sc[n]+=1
    print(f"   RULES: R3 total Sundays={r3sun} (target ≤1) | special-4 holiday interns={dict(sc)} (each ≤1)")
    # winter major coverage by interns
    wm={'2026-11-26':'Thx','2026-12-25':'Xmas','2027-01-01':'NYD'}
    wmi={lab:s.get(ds,{}).get('interns',[]) for ds,lab in wm.items()}
    print(f"   Winter-major intern coverage: {wmi}")
    print()

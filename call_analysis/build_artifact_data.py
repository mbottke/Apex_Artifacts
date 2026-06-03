"""Export a compact JSON payload for the apex calendar artifact from a solved schedule."""
import json, datetime, sys
from collections import defaultdict, Counter
B='/home/user/Apex_Artifacts/call_analysis/'
WHICH=sys.argv[1] if len(sys.argv)>1 else 'rebuilt'
D=json.load(open(B+'data.json')); PGY=D['pgy']; ROT=D['rotations']
S=json.load(open(B+f'{WHICH}.json'))['sched']
def dt(s): return datetime.date.fromisoformat(s)
INT=[n for n in PGY if PGY[n]=='R1']; R2=[n for n in PGY if PGY[n]=='R2']; R3=[n for n in PGY if PGY[n]=='R3']
WT={'Wed':1,'Thu':1,'Mon':2,'Tue':2,'Fri':3,'Sun':3,'Sat':4}
HOL={'2026-07-04':'Independence Day','2026-09-07':'Labor Day','2026-11-26':'Thanksgiving',
 '2026-11-27':'Day After Thanksgiving','2026-12-24':'Christmas Eve','2026-12-25':'Christmas',
 '2026-12-31':"New Year's Eve",'2027-01-01':"New Year's Day",'2027-01-18':'MLK Day',
 '2027-02-15':'Presidents Day','2027-03-28':'Easter','2027-05-09':"Mother's Day",
 '2027-05-31':'Memorial Day','2027-06-19':'Juneteenth'}
MAJOR={'2026-11-26','2026-12-24','2026-12-25','2026-12-31','2027-01-01'}
def rot_on(n,d):
    for s,e,r in ROT[n]:
        if dt(s)<=d<=dt(e): return r
    return '—'
days=[]
for ds in sorted(S):
    e=S[ds]; d=dt(ds)
    intern=e['interns'][0] if e['interns'] else None
    senior=e['seniors'][0] if e['seniors'] else None
    days.append({'d':ds,'dow':d.strftime('%a'),'wd':d.weekday(),
                 'intern':intern,'senior':senior,
                 'interns':e['interns'],'seniors':e['seniors'],
                 'hol':HOL.get(ds),'major':ds in MAJOR})
# per-resident stats
stats={}
for n in PGY:
    cnt=Counter(); wl=0; hols=[]
    for ds in S:
        e=S[ds]; d=dt(ds)
        if n in e['interns']+e['seniors']:
            cnt[d.strftime('%a')]+=1; wl+=WT[d.strftime('%a')]
            if ds in HOL: hols.append({'d':ds,'name':HOL[ds],'major':ds in MAJOR})
    tot=sum(cnt.values())
    stats[n]={'pgy':PGY[n],'total':tot,'byDow':dict(cnt),'wload':wl,
              'avg':round(wl/tot,2) if tot else 0,'holidays':hols}
# rotation spans per resident (for tooltips / context)
rspans={n:[{'s':s,'e':e,'r':r} for s,e,r in ROT[n]] for n in PGY}
# eligibility matrices (re-used verbatim from the optimizer prep) -> compact per-resident bitstrings
PREP=json.load(open(B+'rebuild_prep.json'))
EH=PREP['elig_hard']; ES=PREP['elig_soft']
order=[x['d'] for x in days]
elig ={n:''.join('1' if EH[n][ds] else '0' for ds in order) for n in PGY}
eligS={n:''.join('1' if ES[n][ds] else '0' for ds in order) for n in PGY}
SPECIAL=['2026-07-04','2026-09-07','2027-03-28','2027-05-31']
WINTER =['2026-11-26','2026-12-25','2027-01-01']
out={'which':WHICH,'INT':INT,'R2':R2,'R3':R3,'PGY':PGY,
     'days':days,'stats':stats,'rotations':rspans,
     'elig':elig,'eligSoft':eligS,'special':SPECIAL,'winterMaj':WINTER,
     'fullname':{'Hard':'Hanna Hard','Oehm':'Chloe Oehm','Schutt':'Brady Schutt','Stanek':'Kiana Stanek',
      'Strand':'Paul Strand','Wohlgemuth':'Morgan Wohlgemuth','Beutel':'Amy Beutel','Bottke':'Michael Bottke',
      'Bower':'Brooke Bower','Gaspar':'McKenzie Sundall Gaspar','Kendrick':'Nick Kendrick',
      'Sublette':'Brooke Sublette','Patel':'Bansari Patel','Johnson':'Katie Johnson','Lux':'Nate Lux',
      'Mautino':'Dante Mautino','Mudondo':'Tracy Mudondo'}}
json.dump(out,open(B+f'artifact_data_{WHICH}.json','w'),separators=(',',':'))
print(f"exported artifact_data_{WHICH}.json | days={len(days)} residents={len(stats)}")

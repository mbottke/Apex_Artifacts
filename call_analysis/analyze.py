"""Analysis engine: validate counts, scan rotation conflicts, PTO, fairness, holidays, spacing."""
import json, datetime
from collections import defaultdict, Counter

D = json.load(open('/home/user/Apex_Artifacts/call_analysis/data.json'))
ROT = D['rotations']; PGY = D['pgy']; A = D['assignments']
def dt(s): return datetime.date.fromisoformat(s)

INTERNS = [n for n in PGY if PGY[n]=='R1']
R2 = [n for n in PGY if PGY[n]=='R2']
R3 = [n for n in PGY if PGY[n]=='R3']
SENIORS = R2+R3

def rotation_on(name, d):
    for s,e,r in ROT[name]:
        if dt(s) <= d <= dt(e): return r
    return None

# ---------- 1. COUNT VALIDATION vs YTD tab ----------
YTD = {'Hard':56,'Oehm':55,'Schutt':56,'Stanek':57,'Strand':58,'Wohlgemuth':57,
 'Beutel':34,'Bottke':33,'Bower':34,'Gaspar':33,'Kendrick':33,'Patel':35,'Sublette':33,
 'Johnson':33,'Lux':33,'Mautino':33,'Mudondo':33}

counts = Counter()
dow_counts = defaultdict(Counter)  # name -> {Mon:..}
appear = defaultdict(list)  # name -> [date,...]
for a in A:
    d = dt(a['date']); dow = d.strftime('%a')
    for nm in a['interns']+a['seniors']:
        if nm in PGY:
            counts[nm]+=1; dow_counts[nm][dow]+=1; appear[nm].append(d)

print("="*78)
print("COUNT VALIDATION: parsed vs YTD tab (diff should be ~0)")
print("="*78)
print(f"{'Name':<12}{'PGY':<5}{'Parsed':>7}{'YTD':>5}{'Diff':>6}")
tot_p=tot_y=0
for grp,label in [(INTERNS,'R1'),(R2,'R2'),(R3,'R3')]:
    for nm in grp:
        p=counts[nm]; y=YTD[nm]; tot_p+=p; tot_y+=y
        flag = '' if p==y else '  <-- MISMATCH'
        print(f"{nm:<12}{PGY[nm]:<5}{p:>7}{y:>5}{p-y:>6}{flag}")
print(f"{'TOTAL':<12}{'':<5}{tot_p:>7}{tot_y:>5}")

# ---------- DOW grouped (M,T / W,Th / F / Sun / Sat) like YTD ----------
print("\nDay-of-week distribution (parsed):")
print(f"{'Name':<12}{'M+T':>5}{'W+Th':>6}{'F':>4}{'Sun':>5}{'Sat':>5}{'Tot':>5}")
for grp in [INTERNS,R2,R3]:
    for nm in grp:
        c=dow_counts[nm]
        mt=c['Mon']+c['Tue']; wth=c['Wed']+c['Thu']; f=c['Fri']; su=c['Sun']; sa=c['Sat']
        print(f"{nm:<12}{mt:>5}{wth:>6}{f:>4}{su:>5}{sa:>5}{mt+wth+f+su+sa:>5}")

json.dump({'counts':dict(counts),
           'dow':{n:dict(dow_counts[n]) for n in dow_counts},
           'appear':{n:[d.isoformat() for d in appear[n]] for n in appear}},
          open('/home/user/Apex_Artifacts/call_analysis/counts.json','w'), indent=1)

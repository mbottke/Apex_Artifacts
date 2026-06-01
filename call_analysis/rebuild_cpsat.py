"""Full rebuild via CP-SAT. Uniform 1 intern + 1 senior per call-day, night-float fixed.
Hard: eligibility (0 conflicts), no back-to-back (post-call), R3 Sundays<=1, balanced totals & Saturdays.
Objective: equalize weighted-inconvenience load + Saturdays, balance holidays, avoid soft-blocked rotations."""
import json, datetime
from collections import defaultdict, Counter
from ortools.sat.python import cp_model

P=json.load(open('/home/user/Apex_Artifacts/call_analysis/rebuild_prep.json'))
days=P['days']; INT=P['INTERNS']; R2=P['R2']; R3=P['R3']; SEN=P['SEN']
elig_hard=P['elig_hard']; elig_soft=P['elig_soft']; nf=P['nf_fixed']
HOL=P['HOL']; SPECIAL=P['SPECIAL_INTERN']
def dt(s): return datetime.date.fromisoformat(s)
dows={d:dt(d).strftime('%a') for d in days}
WT={'Wed':1,'Thu':1,'Mon':2,'Tue':2,'Fri':3,'Sun':3,'Sat':4}
SAT=[d for d in days if dows[d]=='Sat']; SUN=[d for d in days if dows[d]=='Sun']
consec=[(days[i],days[i+1]) for i in range(len(days)-1) if (dt(days[i+1])-dt(days[i])).days==1]
nf_days_of=defaultdict(set)
for d,v in nf.items():
    if not str(v).startswith('MULTI'): nf_days_of[v].add(d)

m=cp_model.CpModel()
xi={(i,d):m.NewBoolVar(f'i_{i}_{d}') for i in INT for d in days}
xs={(s,d):m.NewBoolVar(f's_{s}_{d}') for s in SEN for d in days}

# coverage: exactly 1 intern + 1 senior per day
for d in days:
    m.Add(sum(xi[i,d] for i in INT)==1)
    m.Add(sum(xs[s,d] for s in SEN)==1)

# eligibility (hard) -> forbid
for d in days:
    for i in INT:
        if not elig_hard[i][d]: m.Add(xi[i,d]==0)
    for s in SEN:
        if not elig_hard[s][d]: m.Add(xs[s,d]==0)

# night-float fixed
for d,v in nf.items():
    if not str(v).startswith('MULTI'): m.Add(xi[v,d]==1)

# no back-to-back (post-call). Interns: allow only NF-run adjacency.
for (d0,d1) in consec:
    for s in SEN: m.Add(xs[s,d0]+xs[s,d1]<=1)
    for i in INT:
        if d0 in nf_days_of[i] and d1 in nf_days_of[i]:
            continue  # within night-float block: allowed
        m.Add(xi[i,d0]+xi[i,d1]<=1)

# NOTE: pure-fairness rebuild treats all seniors uniformly (the preliminary's unwritten
# R2-Sunday / R3-Friday weekend split is NOT imposed here -> every senior gets the same day-mix).

# soft-block (CBP / R3-Ortho): allow but penalize
softpen=[]
for d in days:
    for i in INT:
        if elig_soft[i][d] and elig_hard[i][d]: softpen.append(xi[i,d])
    for s in SEN:
        if elig_soft[s][d] and elig_hard[s][d]: softpen.append(xs[s,d])

# ---- totals ----
itot={i:m.NewIntVar(0,80,f'it_{i}') for i in INT}
stot={s:m.NewIntVar(0,60,f'st_{s}') for s in SEN}
for i in INT: m.Add(itot[i]==sum(xi[i,d] for d in days))
for s in SEN: m.Add(stot[s]==sum(xs[s,d] for d in days))
# balanced totals (interns avg ~59, seniors avg ~32)
for i in INT: m.Add(itot[i]>=58); m.Add(itot[i]<=60)
for s in SEN: m.Add(stot[s]>=31); m.Add(stot[s]<=34)
itot_max=m.NewIntVar(0,80,'itot_max'); itot_min=m.NewIntVar(0,80,'itot_min')
m.AddMaxEquality(itot_max,[itot[i] for i in INT]); m.AddMinEquality(itot_min,[itot[i] for i in INT])
r2tot_mx=m.NewIntVar(0,60,'r2tot_mx'); r2tot_mn=m.NewIntVar(0,60,'r2tot_mn')
r3tot_mx=m.NewIntVar(0,60,'r3tot_mx'); r3tot_mn=m.NewIntVar(0,60,'r3tot_mn')
m.AddMaxEquality(r2tot_mx,[stot[s] for s in R2]); m.AddMinEquality(r2tot_mn,[stot[s] for s in R2])
m.AddMaxEquality(r3tot_mx,[stot[s] for s in R3]); m.AddMinEquality(r3tot_mn,[stot[s] for s in R3])

BYDOW={w:[d for d in days if dows[d]==w] for w in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']}
WEEKEND=BYDOW['Fri']+BYDOW['Sat']+BYDOW['Sun']
def spread_vars(tag, group, daylist, hi=25):
    v={r:m.NewIntVar(0,hi,f'{tag}_{r}') for r in group}
    for r in group: m.Add(v[r]==sum((xi[r,d] if r in INT else xs[r,d]) for d in daylist))
    vmax=m.NewIntVar(0,hi,f'{tag}_max'); vmin=m.NewIntVar(0,hi,f'{tag}_min')
    m.AddMaxEquality(vmax,[v[r] for r in group]); m.AddMinEquality(vmin,[v[r] for r in group])
    return v,vmax,vmin

# ===== HARD RULES (program structure) =====
# R3 take NO Sunday call (single Lux-style exception permitted)
m.Add(sum(xs[s,d] for s in R3 for d in BYDOW['Sun'])<=1)
# R2: 7-8 Sunday calls each; 14-16 weekend (Fri+Sat+Sun) calls each
for s in R2:
    m.Add(sum(xs[s,d] for d in BYDOW['Sun'])>=7); m.Add(sum(xs[s,d] for d in BYDOW['Sun'])<=8)
    m.Add(sum(xs[s,d] for d in WEEKEND)>=14);     m.Add(sum(xs[s,d] for d in WEEKEND)<=16)
# Hard fairness BANDS on every bad day-type (forces even spread; objective then fine-tunes weekdays)
def band(group, daylist, lo, hi):
    for r in group:
        e=sum((xi[r,d] if r in INT else xs[r,d]) for d in daylist)
        m.Add(e>=lo); m.Add(e<=hi)
band(INT, BYDOW['Sat'], 8, 9); band(INT, BYDOW['Sun'], 8, 9); band(INT, BYDOW['Fri'], 8, 9)
band(R2,  BYDOW['Sat'], 4, 5); band(R2,  BYDOW['Fri'], 3, 5)
band(R3,  BYDOW['Sat'], 4, 6); band(R3,  BYDOW['Fri'], 7, 9)

# ===== fairness WITHIN each cohort: balance every day-type =====
DOWW={'Sat':10,'Fri':8,'Sun':8,'Mon':5,'Tue':5,'Wed':4,'Thu':4}
bal_terms=[]
for w in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
    _,imx,imn=spread_vars(f'idow_{w}',INT,BYDOW[w]); bal_terms.append(DOWW[w]*(imx-imn))
    _,r2mx,r2mn=spread_vars(f'r2dow_{w}',R2,BYDOW[w]); bal_terms.append(DOWW[w]*(r2mx-r2mn))
    if w!='Sun':  # R3 Sundays fixed near 0 by rule
        _,r3mx,r3mn=spread_vars(f'r3dow_{w}',R3,BYDOW[w]); bal_terms.append(DOWW[w]*(r3mx-r3mn))

# Saturday vars (all seniors / interns) for reporting
ssat={s:m.NewIntVar(0,20,f'ssat_{s}') for s in SEN}; isat={i:m.NewIntVar(0,20,f'isat_{i}') for i in INT}
for s in SEN: m.Add(ssat[s]==sum(xs[s,d] for d in BYDOW['Sat']))
for i in INT: m.Add(isat[i]==sum(xi[i,d] for d in BYDOW['Sat']))
ssat_max=m.NewIntVar(0,20,'ssat_max'); ssat_min=m.NewIntVar(0,20,'ssat_min')
isat_max=m.NewIntVar(0,20,'isat_max'); isat_min=m.NewIntVar(0,20,'isat_min')
m.AddMaxEquality(ssat_max,[ssat[s] for s in SEN]); m.AddMinEquality(ssat_min,[ssat[s] for s in SEN])
m.AddMaxEquality(isat_max,[isat[i] for i in INT]); m.AddMinEquality(isat_min,[isat[i] for i in INT])

# ---- weighted load (balance within cohort) ----
iwl={i:m.NewIntVar(0,400,f'iwl_{i}') for i in INT}; swl={s:m.NewIntVar(0,400,f'swl_{s}') for s in SEN}
for i in INT: m.Add(iwl[i]==sum(WT[dows[d]]*xi[i,d] for d in days))
for s in SEN: m.Add(swl[s]==sum(WT[dows[d]]*xs[s,d] for d in days))
iwl_max=m.NewIntVar(0,400,'iwl_max'); iwl_min=m.NewIntVar(0,400,'iwl_min')
m.AddMaxEquality(iwl_max,[iwl[i] for i in INT]); m.AddMinEquality(iwl_min,[iwl[i] for i in INT])
r2wl_mx=m.NewIntVar(0,400,'r2wl_mx'); r2wl_mn=m.NewIntVar(0,400,'r2wl_mn')
r3wl_mx=m.NewIntVar(0,400,'r3wl_mx'); r3wl_mn=m.NewIntVar(0,400,'r3wl_mn')
m.AddMaxEquality(r2wl_mx,[swl[s] for s in R2]); m.AddMinEquality(r2wl_mn,[swl[s] for s in R2])
m.AddMaxEquality(r3wl_mx,[swl[s] for s in R3]); m.AddMinEquality(r3wl_mn,[swl[s] for s in R3])
swl_max=m.NewIntVar(0,400,'swl_max'); swl_min=m.NewIntVar(0,400,'swl_min')
m.AddMaxEquality(swl_max,[swl[s] for s in SEN]); m.AddMinEquality(swl_min,[swl[s] for s in SEN])

# ---- holidays ----
WINTER_MAJ=['2026-11-26','2026-12-25','2027-01-01']
ihol={i:m.NewIntVar(0,6,f'ihol_{i}') for i in INT}
for i in INT:
    m.Add(ihol[i]==sum(xi[i,h] for h in HOL)); m.Add(ihol[i]<=3)
    m.Add(sum(xi[i,h] for h in SPECIAL)<=1)
    m.Add(sum(xi[i,h] for h in WINTER_MAJ)<=1)
ihol_max=m.NewIntVar(0,6,'ihol_max'); ihol_min=m.NewIntVar(0,6,'ihol_min')
m.AddMaxEquality(ihol_max,[ihol[i] for i in INT]); m.AddMinEquality(ihol_min,[ihol[i] for i in INT])
shol={s:m.NewIntVar(0,4,f'shol_{s}') for s in SEN}
for s in SEN: m.Add(shol[s]==sum((2 if HOL[h]=='MAJOR' else 1)*xs[s,h] for h in HOL)); m.Add(shol[s]<=2)
shol_max=m.NewIntVar(0,4,'shol_max'); m.AddMaxEquality(shol_max,[shol[s] for s in SEN])

# ---- objective ----
obj = 1000*sum(softpen) \
    + 12*(itot_max-itot_min) + 15*(r2tot_mx-r2tot_mn) + 15*(r3tot_mx-r3tot_mn) \
    + 10*(iwl_max-iwl_min) + 10*(r2wl_mx-r2wl_mn) + 10*(r3wl_mx-r3wl_mn) \
    + sum(bal_terms) \
    + 10*(ihol_max-ihol_min) + 6*shol_max
m.Minimize(obj)

solver=cp_model.CpSolver()
solver.parameters.max_time_in_seconds=240
solver.parameters.num_search_workers=8
solver.parameters.relative_gap_limit=0.02
res=solver.Solve(m)
print("solver status:", solver.StatusName(res))
if res not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print("INFEASIBLE/none — need to relax."); raise SystemExit
print(f"objective={solver.ObjectiveValue():.0f}  softblocks_used={sum(solver.Value(v) for v in softpen)}")
print(f"senior wload spread: {solver.Value(swl_min)}..{solver.Value(swl_max)}  Sat {solver.Value(ssat_min)}..{solver.Value(ssat_max)}")
print(f"intern wload spread: {solver.Value(iwl_min)}..{solver.Value(iwl_max)}  Sat {solver.Value(isat_min)}..{solver.Value(isat_max)}")

# extract schedule
sched={}
for d in days:
    ints=[i for i in INT if solver.Value(xi[i,d])]
    srs=[s for s in SEN if solver.Value(xs[s,d])]
    sched[d]={'interns':ints,'seniors':srs,'dow':dows[d],'line1':'/'.join(ints),'line2':'/'.join(srs)}
json.dump({'sched':sched,'changes':[]},open('/home/user/Apex_Artifacts/call_analysis/rebuilt.json','w'),indent=1)
print("saved rebuilt.json; days:",len(sched))

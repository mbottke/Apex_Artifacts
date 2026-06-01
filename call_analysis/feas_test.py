"""Stage constraints to locate the binding/infeasible one."""
import json, datetime
from collections import defaultdict
from ortools.sat.python import cp_model
P=json.load(open('/home/user/Apex_Artifacts/call_analysis/rebuild_prep.json'))
days=P['days']; INT=P['INTERNS']; R2=P['R2']; R3=P['R3']; SEN=P['SEN']
eh=P['elig_hard']; es_=P['elig_soft']; nf=P['nf_fixed']; HOL=P['HOL']; SPECIAL=P['SPECIAL_INTERN']
def dt(s): return datetime.date.fromisoformat(s)
dows={d:dt(d).strftime('%a') for d in days}
SUN=[d for d in days if dows[d]=='Sun']; SAT=[d for d in days if dows[d]=='Sat']
consec=[(days[i],days[i+1]) for i in range(len(days)-1) if (dt(days[i+1])-dt(days[i])).days==1]
nfd=defaultdict(set)
for d,v in nf.items():
    if not str(v).startswith('MULTI'): nfd[v].add(d)

def test(name, add_bt=False,add_r3sun=False,add_tot=False,add_hol_sen=False,add_hol_int=False,intcap=3):
    m=cp_model.CpModel()
    xi={(i,d):m.NewBoolVar(f'i{i}{d}') for i in INT for d in days}
    xs={(s,d):m.NewBoolVar(f's{s}{d}') for s in SEN for d in days}
    for d in days:
        m.Add(sum(xi[i,d] for i in INT)==1); m.Add(sum(xs[s,d] for s in SEN)==1)
        for i in INT:
            if not eh[i][d]: m.Add(xi[i,d]==0)
        for s in SEN:
            if not eh[s][d]: m.Add(xs[s,d]==0)
    for d,v in nf.items():
        if not str(v).startswith('MULTI'): m.Add(xi[v,d]==1)
    if add_bt:
        for (d0,d1) in consec:
            for s in SEN: m.Add(xs[s,d0]+xs[s,d1]<=1)
            for i in INT:
                if d0 in nfd[i] and d1 in nfd[i]: continue
                m.Add(xi[i,d0]+xi[i,d1]<=1)
    if add_r3sun: m.Add(sum(xs[s,d] for s in R3 for d in SUN)<=1)
    if add_tot:
        for i in INT: m.Add(sum(xi[i,d] for d in days)>=58); m.Add(sum(xi[i,d] for d in days)<=61)
        for s in SEN: m.Add(sum(xs[s,d] for d in days)>=31); m.Add(sum(xs[s,d] for d in days)<=34)
    if add_hol_sen:
        for s in SEN: m.Add(sum((2 if HOL[h]=='MAJOR' else 1)*xs[s,h] for h in HOL)<=2)
    if add_hol_int:
        for i in INT:
            m.Add(sum(xi[i,h] for h in HOL)<=intcap)
            m.Add(sum(xi[i,h] for h in SPECIAL)<=1)
            m.Add(sum(xi[i,h] for h in ['2026-11-26','2026-12-25','2027-01-01'])<=1)
    sv=cp_model.CpSolver(); sv.parameters.max_time_in_seconds=20; sv.parameters.num_search_workers=8
    r=sv.Solve(m)
    print(f"  {name:<55} -> {sv.StatusName(r)}")
    return r in (cp_model.OPTIMAL,cp_model.FEASIBLE)

print("Staged feasibility:")
test("base (coverage+elig+NF)")
test("+ back-to-back", add_bt=True)
test("+ R3-Sun<=1", add_bt=True,add_r3sun=True)
test("+ totals bands", add_bt=True,add_r3sun=True,add_tot=True)
test("+ senior holiday cap", add_bt=True,add_r3sun=True,add_tot=True,add_hol_sen=True)
test("+ intern holiday cap=3", add_bt=True,add_r3sun=True,add_tot=True,add_hol_sen=True,add_hol_int=True,intcap=3)
test("+ intern holiday cap=2", add_bt=True,add_r3sun=True,add_tot=True,add_hol_sen=True,add_hol_int=True,intcap=2)

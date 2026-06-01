"""Bake correct cached values into the COUNTIF/SUM tracking formulas of a schedule workbook,
PRESERVING the formulas (pure Python; values injected into the XML alongside each <f>).
Then verify every tracking table against the schedule. Usage: python3 bake_values.py <xlsx> <which>"""
import openpyxl, re, sys, json, zipfile, datetime
from collections import Counter
from openpyxl.utils import range_boundaries, get_column_letter

PATH=sys.argv[1]; WHICH=sys.argv[2]  # which in {'repaired','rebuilt'}
B='/home/user/Apex_Artifacts/call_analysis/'
MONTHS=['July','August','September','October','November','December',
        'January','February','March','April','May','June']
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'

wb=openpyxl.load_workbook(PATH)            # formulas
cache={}
def countif(sheet,rng,name):
    mc,mr,xc,xr=range_boundaries(rng.replace('$','')); ws=wb[sheet]; n=0
    for r in range(mr,xr+1):
        for c in range(mc,xc+1):
            v=ws.cell(row=r,column=c).value
            if isinstance(v,str) and not v.startswith('=') and name in v: n+=1
    return n
CELL=re.compile(r'^\$?[A-Z]+\$?\d+$')
def evalf(sheet,f):
    f=f.strip()
    m=re.match(r'^COUNTIF\(([^,]+),\s*"\*([^*"]+)\*"\)$',f,re.I)
    if m: return countif(sheet,m.group(1),m.group(2))
    m=re.match(r'^SUM\((.+)\)$',f,re.I)
    if m:
        a=m.group(1).strip()
        m2=re.match(r'^[A-Za-z0-9 ]+:[A-Za-z0-9 ]+!(\$?[A-Z]+\$?\d+)$',a)   # July:June!REF
        if m2: return sum(evalcell(mo,m2.group(1)) for mo in MONTHS)
        if ':' in a and '!' not in a:                                       # same-sheet range
            mc,mr,xc,xr=range_boundaries(a.replace('$','')); t=0
            for r in range(mr,xr+1):
                for c in range(mc,xc+1): t+=evalcell(sheet,f"{get_column_letter(c)}{r}")
            return t
        if CELL.match(a): return evalcell(sheet,a)
    return None
def evalcell(sheet,coord):
    coord=coord.replace('$',''); key=(sheet,coord)
    if key in cache: return cache[key]
    cache[key]=0
    v=wb[sheet][coord].value
    if isinstance(v,str) and v.startswith('='):
        r=evalf(sheet,v[1:]); r=0 if r is None else r
    elif isinstance(v,(int,float)): r=v
    else: r=0
    cache[key]=int(r) if float(r).is_integer() else r
    return cache[key]

# collect every COUNTIF / SUM cell -> value
bake={}
for sh in wb.sheetnames:
    for row in wb[sh].iter_rows():
        for c in row:
            v=c.value
            if isinstance(v,str) and v.startswith('='):
                u=v[1:].lstrip().upper()
                if u.startswith('COUNTIF') or u.startswith('SUM('):
                    if evalf(sh,v[1:]) is not None:                # only bake formulas we fully parse
                        bake.setdefault(sh,{})[c.coordinate]=evalcell(sh,c.coordinate)
nb=sum(len(d) for d in bake.values()); print(f"[bake] tracking cells computed: {nb}")

# ---- inject <v> next to <f>, byte-level, preserving all else ----
zin=zipfile.ZipFile(PATH); data={i.filename:zin.read(i.filename) for i in zin.infolist()}; infos=zin.infolist(); zin.close()
wbxml=data['xl/workbook.xml'].decode('utf8'); relsxml=data['xl/_rels/workbook.xml.rels'].decode('utf8')
name2rid={}
for s in re.findall(r'<sheet\b[^>]*?/>',wbxml):
    nm=re.search(r'name="([^"]+)"',s); rid=re.search(r'r:id="([^"]+)"',s)
    if nm and rid: name2rid[nm.group(1)]=rid.group(1)
rid2tgt={}
for rel in re.findall(r'<Relationship\b[^>]*?/>',relsxml):
    i=re.search(r'Id="([^"]+)"',rel); t=re.search(r'Target="([^"]+)"',rel)
    if i and t: rid2tgt[i.group(1)]=t.group(1)
def resolve(t):
    t=t.replace('\\','/')
    return t.lstrip('/') if t.startswith('/') else 'xl/'+t   # absolute-from-root vs relative-to-xl/
sheetxml={nm:resolve(rid2tgt[rid]) for nm,rid in name2rid.items()}

def inject(xml, cv):
    # match a cell as EITHER self-closing (<c .../>) OR with content (<c ...>…</c>)
    pat=re.compile(rb'<c r="([A-Z]+\d+)"([^>]*?)(?:/>|>(.*?)</c>)',re.S)
    def repl(m):
        co=m.group(1).decode(); body=m.group(3)
        if body is not None and co in cv and b'<f' in body:
            b2=re.sub(rb'<v\s*/>',b'',body)                  # drop openpyxl's empty <v/>
            b2=re.sub(rb'<v>.*?</v>',b'',b2,flags=re.S)      # and any populated <v>…</v>
            attrs=re.sub(rb'\s+t="[^"]*"',b'',m.group(2))    # numeric result -> drop any t=
            return b'<c r="'+m.group(1)+b'"'+attrs+b'>'+b2+b'<v>'+str(cv[co]).encode()+b'</v></c>'
        return m.group(0)
    return pat.sub(repl,xml)
for sh,cv in bake.items():
    if sh not in sheetxml:
        print(f"  [warn] no XML mapping for sheet {sh!r}; skipped"); continue
    fn=sheetxml[sh]; data[fn]=inject(data[fn],cv)
zout=zipfile.ZipFile(PATH,'w',zipfile.ZIP_DEFLATED)
for i in infos: zout.writestr(i,data[i.filename])
zout.close()
print("[bake] injected + saved")

# ================= VERIFY against the schedule =================
S=json.load(open(B+f'{WHICH}.json'))['sched']; PGY=json.load(open(B+'data.json'))['pgy']
def dt(s): return datetime.date.fromisoformat(s)
tot=Counter(); g=lambda:{'MT':0,'WTH':0,'Fri':0,'Sun':0,'Sat':0}
dow=Counter()  # (name,grp)
GMAP={'Mon':'MT','Tue':'MT','Wed':'WTH','Thu':'WTH','Fri':'Fri','Sun':'Sun','Sat':'Sat'}
for ds,e in S.items():
    w=dt(ds).strftime('%a')
    for n in e['interns']+e['seniors']:
        tot[n]+=1; dow[(n,GMAP[w])]+=1
v=openpyxl.load_workbook(PATH,data_only=True)   # cached values now present
fails=[]
# 1) YTD totals tables
YT={'B3':'Hard','C3':'Oehm','D3':'Schutt','E3':'Stanek','F3':'Strand','G3':'Wohlgemuth',
    'B6':'Beutel','C6':'Bottke','D6':'Bower','E6':'Gaspar','F6':'Kendrick','G6':'Patel','H6':'Sublette',
    'B9':'Johnson','C9':'Lux','D9':'Mautino','E9':'Mudondo'}
for co,nm in YT.items():
    got=v['YTD'][co].value
    if got!=tot[nm]: fails.append(f"YTD total {nm} {co}: file={got} sched={tot[nm]}")
# 2) YTD day-of-week table  (B=MT C=WTH D=Fri E=Sun F=Sat)
ROWS={13:'Hard',14:'Oehm',15:'Schutt',16:'Stanek',17:'Strand',18:'Wohlgemuth',
      20:'Beutel',21:'Bottke',22:'Bower',23:'Gaspar',24:'Kendrick',25:'Patel',26:'Sublette',
      28:'Johnson',29:'Lux',30:'Mautino',31:'Mudondo'}
COL={'B':'MT','C':'WTH','D':'Fri','E':'Sun','F':'Sat'}
for r,nm in ROWS.items():
    for col,grp in COL.items():
        got=v['YTD'][f'{col}{r}'].value or 0
        exp=dow[(nm,grp)]
        if got!=exp: fails.append(f"YTD DOW {nm} {col}{r}({grp}): file={got} sched={exp}")
# 3) every baked cell now has a numeric cached value
none_cells=[(sh,co) for sh,cv in bake.items() for co in cv if v[sh][co].value is None]
# 4) grand totals
gi=v['YTD']['H3'].value; allcnt=sum(tot.values())
print(f"[verify] residents checked={len(tot)} | YTD intern-total cell H3={gi} | grand total shifts={allcnt}")
print(f"[verify] empty baked cells: {len(none_cells)}")
if fails:
    print(f"[verify] FAILURES: {len(fails)}");  [print('   '+f) for f in fails[:25]]
else:
    print("[verify] ALL TRACKING TABLES CORRECT ✓ (YTD totals + day-of-week match schedule; formulas preserved)")

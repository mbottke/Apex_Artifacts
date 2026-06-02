"""Inject the schedule data JSON into the calendar artifact template -> standalone HTML.

Also server-renders the full-year calendar grid (and bakes the day count) into static
HTML so the schedule is visible even in contexts that don't run page scripts (e.g. iOS
file previews / QuickLook). When scripts DO run, the JS re-renders the same grid and adds
all interactivity (selection, search, day detail, the switch planner)."""
import json, sys, calendar, datetime
B='/home/user/Apex_Artifacts/call_analysis/'
which=sys.argv[1] if len(sys.argv)>1 else 'rebuilt'
out=sys.argv[2] if len(sys.argv)>2 else 'deliverables/26-27_Call_Calendar_apex.html'
tpl=open(B+'calendar_artifact_template.html').read()
raw=open(B+f'artifact_data_{which}.json').read()
D=json.loads(raw)

# ---- server-side render of the year grid (mirror of the template's monthHTML/nameSpan) ----
PGY=D['PGY']; FULL=D['fullname']; byDate={x['d']:x for x in D['days']}
MNAME=['January','February','March','April','May','June','July','August','September','October','November','December']
DOW=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
MONTHS=[(2026,6),(2026,7),(2026,8),(2026,9),(2026,10),(2026,11),
        (2027,0),(2027,1),(2027,2),(2027,3),(2027,4),(2027,5)]
def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
def rc(nm):
    p=PGY[nm]; return 'i' if p=='R1' else 's2' if p=='R2' else 's3'
def nspan(nm,ds):
    return (f'<span class="nm {rc(nm)}" data-nm="{esc(nm)}" tabindex="0" role="button" '
            f'title="{esc(FULL.get(nm,nm))} · {PGY[nm]} · {ds}">{esc(nm)}</span>')
def month_html(y,m):
    start=datetime.date(y,m+1,1).weekday()            # Monday=0
    dim=calendar.monthrange(y,m+1)[1]
    cells=''.join('<div class="cell empty"></div>' for _ in range(start))
    for d in range(1,dim+1):
        ds=f"{y}-{m+1:02d}-{d:02d}"; rec=byDate.get(ds)
        we=datetime.date(y,m+1,d).weekday()>=5
        cls='cell'+(' we' if we else '')+(' hol' if rec and rec.get('hol') else '')
        inner=f'<span class="num">{d}</span>'
        if rec and rec.get('hol'): inner+=f'<span class="star" title="{esc(rec["hol"])}">★</span>'
        if rec:
            for nm in rec.get('interns',[]): inner+=nspan(nm,ds)
            for nm in rec.get('seniors',[]): inner+=nspan(nm,ds)
        cells+=f'<div class="{cls}" data-d="{ds}">{inner}</div>'
    head=''.join(f'<span class="{"we" if x in ("Sat","Sun") else ""}">{x[0]}</span>' for x in DOW)
    return (f'<section class="month"><h3>{MNAME[m]} <span class="yr">{y}</span></h3>'
            f'<div class="dow-head">{head}</div><div class="days">{cells}</div></section>')
months_html=''.join(month_html(y,m) for y,m in MONTHS)

# bake the day count + the server-rendered grid into the static HTML
assert '<b id="ndays">—</b>' in tpl, "ndays placeholder missing"
tpl=tpl.replace('<b id="ndays">—</b>', f'<b id="ndays">{len(D["days"])}</b>')
marker='<div class="months" id="months" aria-label="Year overview"></div>'
assert marker in tpl, "months container missing"
tpl=tpl.replace(marker, marker.replace('></div>', f'>{months_html}</div>'))

# embed the data payload for the interactive layer
data=raw.replace('</','<\\/')   # guard against </script> breaking the inline JSON block
assert '/*__DATA__*/' in tpl, "data placeholder missing"
html=tpl.replace('/*__DATA__*/',data)
open('/home/user/Apex_Artifacts/'+out,'w').write(html)
print(f"wrote {out}  ({len(html)//1024} KB) | SSR months={len(MONTHS)} | ndays={len(D['days'])}")

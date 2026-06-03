"""Generate a print-optimized PDF-ready HTML call calendar from artifact_data_{which}.json."""
import json, sys, calendar, datetime
B='/home/user/Apex_Artifacts/call_analysis/'
which=sys.argv[1] if len(sys.argv)>1 else 'rebuilt'
label=sys.argv[2] if len(sys.argv)>2 else 'Full Rebuild'
out=sys.argv[3] if len(sys.argv)>3 else B+f'print_cal_{which}.html'
D=json.load(open(B+f'artifact_data_{which}.json'))
days={d['d']:d for d in D['days']}; PGY=D['PGY']; stats=D['stats']; full=D['fullname']
INT,R2,R3=D['INT'],D['R2'],D['R3']
MONTHS=[(2026,7),(2026,8),(2026,9),(2026,10),(2026,11),(2026,12),
        (2027,1),(2027,2),(2027,3),(2027,4),(2027,5),(2027,6)]
MN=['','January','February','March','April','May','June','July','August','September','October','November','December']
DOW=['M','T','W','T','F','S','S']
VCOLOR='#2f6d45' if which=='repaired' else '#243a8f'
def role(n): return 'i' if PGY[n]=='R1' else ('s2' if PGY[n]=='R2' else 's3')
def cell(y,m,d):
    ds=f"{y:04d}-{m:02d}-{d:02d}"; rec=days.get(ds); wd=datetime.date(y,m,d).weekday()
    cls='cell'+(' we' if wd>=5 else '')+(' hol' if rec and rec.get('hol') else '')
    h=['<div class="'+cls+'"><span class="dn">'+str(d)+'</span>']
    if rec and rec.get('hol'): h.append('<span class="hs" title="'+rec['hol']+'">★</span>')
    if rec:
        for nm in rec.get('interns',[]): h.append('<span class="nm '+role(nm)+'">'+nm+'</span>')
        for nm in rec.get('seniors',[]): h.append('<span class="nm '+role(nm)+'">'+nm+'</span>')
    return ''.join(h)+'</div>'
def month_html(y,m):
    first=calendar.monthrange(y,m)[0]; ndays=calendar.monthrange(y,m)[1]
    cells=''.join('<div class="cell empty"></div>' for _ in range(first))
    cells+=''.join(cell(y,m,d) for d in range(1,ndays+1))
    head=''.join('<span class="'+('we' if i>=5 else '')+'">'+w+'</span>' for i,w in enumerate(DOW))
    return ('<section class="month"><h3>'+MN[m]+' <span class="yr">'+str(y)+'</span></h3>'
            '<div class="dh">'+head+'</div><div class="days">'+cells+'</div></section>')
def rh(rng):
    return ('<div class="rh"><span>2026–2027 Resident Call Calendar</span>'
            '<span class="vl">'+label+'</span><span>'+rng+'</span></div>')
def cal_page(p, legend=''):
    grp=''.join(month_html(*MONTHS[i]) for i in range(p,p+4))
    rng=MN[MONTHS[p][1]]+'–'+MN[MONTHS[p+3][1]]
    return '<div class="calpage">'+rh(rng)+legend+'<div class="mgrid">'+grp+'</div></div>'
LEGEND=('<div class="legend"><b>Legend</b>'
  '<span class="k"><span class="sw" style="background:#eef1fb;border-color:#2f49a8"></span>Intern (R1)</span>'
  '<span class="k"><span class="sw" style="background:#ecf4ee;border-color:#2f6d45"></span>Senior R2</span>'
  '<span class="k"><span class="sw" style="background:#f8efe6;border-color:#a8521f"></span>Senior R3</span>'
  '<span class="k"><span class="sw" style="background:#fbf3df"></span>★ Holiday</span>'
  '<span class="k"><span class="sw" style="background:#f4f1ea"></span>Weekend</span>'
  '<span style="color:#9a958b">· one intern + one senior each night</span></div>')
def srow(n):
    s=stats[n]; bd=s['byDow']; wk=bd.get('Fri',0)+bd.get('Sat',0)+bd.get('Sun',0)
    return ('<tr><td>'+full.get(n,n)+'</td><td class="pg '+role(n)+'">'+PGY[n]+'</td><td>'+str(s['total'])
            +'</td><td>'+str(bd.get('Sat',0))+'</td><td>'+str(bd.get('Sun',0))+'</td><td>'+str(wk)
            +'</td><td>'+str(len(s['holidays']))+'</td><td>'+str(s['avg'])+'</td></tr>')
def sep(t): return '<tr class="sep"><td colspan="8">'+t+'</td></tr>'
sumrows=sep('Interns — R1')+''.join(srow(n) for n in INT)+sep('Seniors — R2')+''.join(srow(n) for n in R2)\
        +sep('Seniors — R3')+''.join(srow(n) for n in R3)
summary=('<div class="calpage">'+rh('Per-resident summary')
  +'<table class="sum"><thead><tr><th>Resident</th><th>Yr</th><th>Total</th><th>Sat</th><th>Sun</th>'
  '<th>Wknd</th><th>Hol</th><th>Avg incon.</th></tr></thead>'+sumrows+'</table>'
  '<p class="foot">Each call day is staffed by one intern + one senior. “Avg inconvenience” weights each call '
  'by day (Wed/Thu 1 · Mon/Tue 2 · Fri/Sun 3 · Sat 4). UnityPoint Health Family Medicine Residency.</p></div>')

CSS='''@page{ size:Letter landscape; margin:0.4in }
*{box-sizing:border-box}
body{margin:0;font-family:"Liberation Sans","Helvetica Neue",Arial,sans-serif;color:#1c1b19;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.calpage{break-after:page} .calpage:last-child{break-after:auto}
.rh{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #1c1b19;
  padding-bottom:5px;margin-bottom:9px;font-size:10px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.rh .vl{color:#fff;background:%VC%;padding:2px 9px;border-radius:9px;font-size:9px;letter-spacing:.06em}
.mgrid{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:9px 13px;height:7.0in}
.month{border:1px solid #d9d3c4;border-radius:5px;overflow:hidden;display:flex;flex-direction:column}
.month h3{font-size:12.5px;font-weight:700;padding:3px 8px;border-bottom:1px solid #ece7da;margin:0;
  font-family:"Liberation Serif",Georgia,serif}
.month h3 .yr{font-size:9px;color:#9a958b;font-weight:400}
.dh{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;padding:2px 4px 0;font-size:7.5px;font-weight:700;color:#9a958b}
.dh span{text-align:center} .dh .we{color:#9d3611}
.days{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;padding:3px 4px 4px;flex:1}
.cell{border:1px solid #efece3;border-radius:3px;padding:1px 2px;background:#fcfbf8;overflow:hidden}
.cell.empty{background:transparent;border:0} .cell.we{background:#f4f1ea} .cell.hol{background:#fbf3df}
.dn{font-size:7px;color:#9a958b;font-weight:700;line-height:1.1;font-family:"DejaVu Sans Mono",monospace}
.hs{float:right;color:#caa53b;font-size:7px}
.nm{display:block;font-size:8px;font-weight:700;line-height:1.28;white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis;border-radius:2px;padding:0 2px;margin-top:1px;letter-spacing:-.02em}
.nm.i{color:#2f49a8;background:#eef1fb} .nm.s2{color:#2f6d45;background:#ecf4ee} .nm.s3{color:#a8521f;background:#f8efe6}
.legend{display:flex;gap:14px;font-size:9px;color:#5c574f;margin:-2px 0 8px;flex-wrap:wrap;align-items:center}
.legend b{font-size:8.5px;letter-spacing:.08em;text-transform:uppercase;color:#9a958b}
.legend .k{display:inline-flex;align-items:center;gap:4px}
.sw{width:11px;height:11px;border-radius:2px;border:1px solid rgba(0,0,0,.12);display:inline-block}
table.sum{width:100%;border-collapse:collapse;font-size:11px;margin-top:4px}
table.sum th{text-align:left;font-size:8.5px;letter-spacing:.06em;text-transform:uppercase;color:#7c776e;
  border-bottom:1.5px solid #cfc7b4;padding:5px 8px}
table.sum th:nth-child(n+3),table.sum td:nth-child(n+3){text-align:center}
table.sum td{padding:4px 8px;border-bottom:1px solid #ece7da}
table.sum tr.sep td{background:#f4f1ea;font-weight:700;font-size:9px;letter-spacing:.06em;text-transform:uppercase;color:#5c574f}
td.pg{font-weight:700;font-size:9px} td.pg.i{color:#2f49a8} td.pg.s2{color:#2f6d45} td.pg.s3{color:#a8521f}
.foot{font-size:9px;color:#7c776e;margin-top:12px;line-height:1.5;max-width:62em}'''.replace('%VC%',VCOLOR)

body=cal_page(0,LEGEND)+cal_page(4)+cal_page(8)+summary
HTML='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Call Calendar — '+label+\
     '</title><style>'+CSS+'</style></head><body>'+body+'</body></html>'
open(out,'w').write(HTML)
print('wrote '+out+' ('+str(len(HTML)//1024)+' KB)')

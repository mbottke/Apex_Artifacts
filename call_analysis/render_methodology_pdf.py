from playwright.sync_api import sync_playwright
import pathlib
src='file://'+str(pathlib.Path('call_analysis/methodology_doc.html').resolve())
out='deliverables/26-27_Call_Schedule_Methodology.pdf'
foot='<div style="font-size:8px;width:100%;text-align:center;color:#928c82;font-family:sans-serif;">'\
     '<span class="pageNumber"></span>&nbsp;/&nbsp;<span class="totalPages"></span></div>'
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page()
    errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
    pg.goto(src,wait_until='networkidle'); pg.wait_for_timeout(500)
    pg.pdf(path=out, format='Letter', print_background=True,
           display_header_footer=True, header_template='<div></div>', footer_template=foot,
           margin={'top':'0.62in','bottom':'0.58in','left':'0.72in','right':'0.72in'},
           prefer_css_page_size=False)
    b.close()
    print('pageerrors:',errs[:4])
import os
print('PDF bytes:',os.path.getsize(out))

#!/usr/bin/env python3
"""Generate the PWA / Add-to-Home-Screen icon set by rasterizing an SVG with
headless Chromium. Writes full-bleed square PNGs (iOS/Android apply their own
mask) into ../assets/. Run:  python3 call_analysis/make_icons.py"""
import math, pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path("/home/user/Apex_Artifacts/assets"); OUT.mkdir(exist_ok=True)

def star(cx, cy, outer, inner, n=5, rot=-math.pi/2):
    pts=[]
    for i in range(n*2):
        r=outer if i%2==0 else inner
        a=rot+i*math.pi/n
        pts.append(f"{cx+r*math.cos(a):.1f} {cy+r*math.sin(a):.1f}")
    return "M"+" L".join(pts)+" Z"

SVG = f"""<svg xmlns='http://www.w3.org/2000/svg' width='{{N}}' height='{{N}}' viewBox='0 0 512 512'>
  <defs>
    <linearGradient id='bg' x1='0' y1='0' x2='1' y2='1'>
      <stop offset='0' stop-color='#2a86ff'/><stop offset='1' stop-color='#0056d6'/>
    </linearGradient>
    <filter id='sh' x='-30%' y='-30%' width='160%' height='160%'>
      <feDropShadow dx='0' dy='12' stdDeviation='16' flood-color='#00337f' flood-opacity='0.35'/>
    </filter>
  </defs>
  <rect width='512' height='512' fill='url(#bg)'/>
  <g filter='url(#sh)'>
    <rect x='140' y='168' width='232' height='198' rx='34' fill='#ffffff'/>
    <path d='M140 202 q0-34 34-34 h164 q34 0 34 34 v20 H140 Z' fill='#0a6cff'/>
    <rect x='190' y='148' width='20' height='48' rx='10' fill='#dbe9ff'/>
    <rect x='302' y='148' width='20' height='48' rx='10' fill='#dbe9ff'/>
    <path d='{star(256, 300, 62, 26)}' fill='#f5b400' stroke='#e0a200' stroke-width='2' stroke-linejoin='round'/>
  </g>
</svg>"""

SIZES = {"icon-512.png":512, "icon-192.png":192, "apple-touch-icon.png":180, "favicon-32.png":32}

with sync_playwright() as p:
    b=p.chromium.launch()
    for fname,n in SIZES.items():
        page=b.new_page(viewport={"width":n,"height":n}, device_scale_factor=1)
        page.set_content("<!doctype html><html><head><style>html,body{margin:0;padding:0;background:#0056d6}</style></head>"
                         f"<body>{SVG.replace('{N}',str(n))}</body></html>")
        page.wait_for_timeout(120)
        page.screenshot(path=str(OUT/fname), clip={"x":0,"y":0,"width":n,"height":n})
        print("wrote", OUT/fname, f"{n}x{n}")
    b.close()

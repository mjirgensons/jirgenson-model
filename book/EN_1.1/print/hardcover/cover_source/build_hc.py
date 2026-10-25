#!/usr/bin/env python3
"""Hardcover wrap-cover variants (KDP case laminate 6x9, 240 pp, premium white): 14.327 x 10.417 in."""
import sys, os, json
from playwright.sync_api import sync_playwright

W, H = 14.327, 10.417
ART = "/home/claude/hc/art"
OUT = "/home/claude/hc/out"
ASPECT = 941 / 1672

BACK = """
<p><em>Most owners run their business by feel.</em> They solve problems in the order they arrive, react when the numbers have already turned bad, and work harder when the plan stops working.</p>
<p><b>Steer, Don’t Guess</b> offers another way. The Jirgenson Model takes the logic engineers use to steer ships, aircraft and factories and turns it into a practical routine for a small business, a family budget or a teenager’s savings: write down your goals in the order you would give them up, measure honestly where you are, see the gap and its zones, find the levers you really control, and set a rhythm of checks.</p>
<p>Through the story of Andrew and his coffee shop, The Corner, you will learn to:</p>
<ul>
<li>separate goals from methods and decide what you protect to the last;</li>
<li>set red lines before a crisis, not in the middle of one;</li>
<li>forecast instead of reacting, and change the plan without abandoning the goal;</li>
<li>work back from a distant goal to what needs doing this week.</li>
</ul>
<p>Every chapter works on three levels, from everyday examples to formulas. The appendices contain a canon and a prompt that turn a language model into an assistant working by the model: in a blind test it scored 88.9 out of 100, against 55.9 without them.</p>
"""
BIO = ("Martin Jirgenson is a researcher in control systems and a management practitioner. "
       "He builds tools that turn the laws of control theory into everyday practice for business and life.")

VARIANTS = {
    "A_dashboard": dict(
        name="A. Dashboard",
        front=dict(img="dashboard.png", h=12.0, left=7.57, top=-0.75, ov=0.45, ovh=4.6),
        back=dict(img="warning.png", pos="50% 72%", box=(0.9, 7.75, 5.4, 2.4)),
    ),
    "B_wheel": dict(
        name="B. Hands on the wheel",
        front=dict(img="hands_road.png", h=5.0, left=9.7, top=3.75, ov=0.35, ovh=4.4),
        back=dict(img="river.png", pos="50% 85%", box=(0.9, 7.75, 5.4, 2.4)),
    ),
    "C_funnel": dict(
        name="C. Funnel: from noise to one signal",
        front=dict(img="funnel.png", h=10.417, left=7.95, top=0.0, ov=0.55, ovh=4.7),
        back=dict(img="device_ring.png", pos="50% 62%", box=(0.9, 7.75, 5.4, 2.4)),
    ),
    "D_surfer": dict(
        name="D. The wave under the surface",
        front=dict(img="surfer_block.png", h=4.7, left=9.8, top=4.3, ov=0.3, ovh=2.4),
        back=dict(img="waves.png", pos="50% 62%", box=(0.9, 7.75, 5.4, 2.4)),
    ),
    "E_book": dict(
        name="E. Open book, light of the model",
        front=dict(img="book_open.png", h=12.0, left=7.57, top=-1.55, ov=0.2, ovh=4.0),
        back=dict(img="cars.png", pos="50% 80%", box=(0.9, 7.75, 5.4, 2.4)),
    ),
}


def html(v):
    f, b = v["front"], v["back"]
    fw = f["h"] * ASPECT
    bx = b["box"]
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
@font-face {{ font-family:'InterX'; src:url('file:///usr/share/fonts/opentype/inter/Inter-Regular.otf'); font-weight:400; }}
@font-face {{ font-family:'InterX'; src:url('file:///usr/share/fonts/opentype/inter/Inter-Bold.otf'); font-weight:700; }}
@font-face {{ font-family:'LoraX'; src:url('file:///usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'); font-weight:400 700; font-style:normal; }}
@font-face {{ font-family:'LoraX'; src:url('file:///usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'); font-weight:400 700; font-style:italic; }}
@page {{ size:{W}in {H}in; margin:0 }}
* {{ box-sizing:border-box; margin:0; padding:0 }}
html,body {{ width:{W}in; height:{H}in; background:#050824; overflow:hidden }}
.page {{ position:relative; width:{W}in; height:{H}in; overflow:hidden;
  background: linear-gradient(180deg,#02051a 0%,#070c30 50%,#160d40 100%); }}
.abs {{ position:absolute }}
.front-art {{ left:{f['left']}in; top:{f['top']}in; width:{fw}in; height:{f['h']}in;
  background:url('file://{ART}/{f['img']}') center/100% 100% no-repeat;
  -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 8%, #000 92%, transparent 100%), linear-gradient(180deg, {'transparent 0, #000 6%' if f['top']>0.5 else '#000 0, #000 0'}, #000 {'88%' if f['top']+f['h']>H-0.6 else '100%'}, {'transparent 100%' if f['top']+f['h']>H-0.6 else '#000 100%'});
  -webkit-mask-composite: source-in; mask-composite: intersect;
          mask-image: linear-gradient(90deg, transparent 0, #000 8%, #000 92%, transparent 100%), linear-gradient(180deg, {'transparent 0, #000 6%' if f['top']>0.5 else '#000 0, #000 0'}, #000 {'88%' if f['top']+f['h']>H-0.6 else '100%'}, {'transparent 100%' if f['top']+f['h']>H-0.6 else '#000 100%'}); }}
.front-art-wrap {{ left:7.54in; top:0; width:{W-7.54}in; height:{H}in; overflow:hidden }}
.front-art-wrap .front-art {{ left:{f['left']-7.54}in }}
.front-ov {{ left:7.54in; top:0; width:{W-7.54}in; height:{f['ovh']}in;
  background:linear-gradient(180deg, rgba(2,5,26,{f['ov']}) 0%, rgba(2,5,26,0) 100%) }}
.front-ov2 {{ left:7.54in; top:{H-1.7}in; width:{W-7.54}in; height:1.7in;
  background:linear-gradient(0deg, rgba(2,5,26,.55) 0%, rgba(2,5,26,0) 100%) }}
.back-art {{ left:{bx[0]}in; top:{bx[1]}in; width:{bx[2]}in; height:{bx[3]}in;
  background:url('file://{ART}/{b['img']}') {b['pos']}/cover no-repeat; opacity:.9;
  -webkit-mask-image: radial-gradient(ellipse at 50% 55%, #000 35%, transparent 78%);
          mask-image: radial-gradient(ellipse at 50% 55%, #000 35%, transparent 78%); }}
.spine {{ left:6.79in; top:0; width:.752in; height:{H}in; background:rgba(2,4,20,.55) }}
.label {{ left:8.21in; top:1.5in; font:400 10.7pt/1 InterX; letter-spacing:.27em; color:#b1dbef; text-transform:uppercase; white-space:nowrap }}
.title {{ left:8.16in; top:1.62in; font:700 54pt/1.04 InterX; color:#fff; letter-spacing:-.005em; white-space:nowrap }}
.sub {{ left:8.21in; top:3.88in; font:400 14.7pt/1.38 InterX; color:#fff; width:4.6in }}
.author {{ left:8.2in; top:8.88in; font:400 20.7pt/1.2 LoraX; color:#fff; white-space:nowrap }}
.back {{ left:1.19in; top:1.32in; width:4.86in; font:400 10.7pt/1.37 LoraX; color:#fff; hyphens:auto; -webkit-hyphens:auto }}
.back p {{ margin:0 0 .95em 0 }}
.back em {{ font-style:italic; font-size:11.7pt }}
.back ul {{ list-style:none; margin:0 0 .95em 0 }}
.back li {{ position:relative; padding-left:.9em; margin:0 0 .12em 0 }}
.back li:before {{ content:'\\2022'; position:absolute; left:.1em; color:#b1dbef }}
.bio {{ left:1.24in; top:7.02in; width:4.85in; font:italic 400 9.3pt/1.4 LoraX; color:#b1dbef; hyphens:auto; -webkit-hyphens:auto }}
.sp1 {{ left:7.163in; top:2.37in; transform:translateX(-50%); writing-mode:vertical-rl; text-orientation:sideways; font:700 14pt/1 InterX; letter-spacing:.06em; color:#fff; white-space:nowrap }}
.sp2 {{ left:7.163in; top:7.07in; transform:translateX(-50%); writing-mode:vertical-rl; text-orientation:sideways; font:400 11pt/1 InterX; letter-spacing:.14em; color:#b1dbef; white-space:nowrap }}
</style></head><body><div class="page">
<div class="abs back-art"></div>
<div class="abs front-art-wrap"><div class="abs front-art"></div></div>
<div class="abs front-ov"></div><div class="abs front-ov2"></div>
<div class="abs spine"></div>
<div class="abs back" lang="en">{BACK}</div>
<div class="abs bio" lang="en">{BIO}</div>
<div class="abs sp1">STEER, DON’T GUESS</div>
<div class="abs sp2">MARTIN JIRGENSON</div>
<div class="abs label">The Jirgenson Model</div>
<div class="abs title">Steer,<br>Don’t Guess</div>
<div class="abs sub">Setting Priorities, Reading the Numbers and Correcting Course in Business and Life</div>
<div class="abs author">Martin Jirgenson</div>
</div></body></html>"""


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        for key, v in VARIANTS.items():
            path = f"{OUT}/{key}.html"
            open(path, "w").write(html(v))
            pg = br.new_page(viewport={"width": round(W * 96), "height": round(H * 96)}, device_scale_factor=1.25)
            pg.goto("file://" + path)
            pg.wait_for_timeout(600)
            pg.screenshot(path=f"{OUT}/{key}.png")
            pg.close()
            print("ok", key)
        br.close()


if __name__ == "__main__":
    main()

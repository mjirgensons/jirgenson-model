import re, numpy as np
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
import build_hc as B
W,H=B.W,B.H
# 1) upscale art 3x (lanczos + gentle sharpen + fine grain to hide upscaling)
rng=np.random.default_rng(7)
for n in ["dashboard","warning"]:
    im=Image.open(f"{B.ART}/{n}.png").convert("RGB")
    im=im.resize((im.width*3,im.height*3),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2.2,70,2))
    a=np.asarray(im).astype(np.float32)+rng.normal(0,2.2,(im.height,im.width,1))
    Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save(f"/home/claude/hc/art_hi/{n}.png")
B.ART="/home/claude/hc/art_hi"
v=B.VARIANTS["A_dashboard"]
v["front"]=dict(img="dashboard.png",h=10.54,left=7.77,top=0.04,ov=0.45,ovh=4.6)
v["back"]["box"]=(0.55,7.45,5.0,2.3)   # keep triangle clear of KDP barcode zone (x 4.14-6.14, y 8.25-9.45)
html=B.html(v)
# 2) background-only render (hide text) at 300 dpi
bg_html=html.replace("</style>",".label,.title,.sub,.author,.back,.bio,.sp1,.sp2{visibility:hidden}</style>")
open("final/bg.html","w").write(bg_html)
with sync_playwright() as p:
    br=p.chromium.launch()
    pg=br.new_page(viewport={"width":int(W*96)+1,"height":int(H*96)+1},device_scale_factor=300/96)
    pg.goto("file:///home/claude/hc/final/bg.html"); pg.wait_for_timeout(1500)
    pg.screenshot(path="final/bg_raw.png",clip={"x":0,"y":0,"width":W*96,"height":H*96})
    im=Image.open("final/bg_raw.png").convert("RGB").resize((round(W*300),round(H*300)),Image.LANCZOS)
    im.save("final/bg.png"); print(im.size)
    # 3) final html: bg image + live vector text
    fin=html.replace('<div class="page">',f'<div class="page"><img src="file:///home/claude/hc/final/bg.png" style="position:absolute;left:0;top:0;width:{W}in;height:{H}in">',1)
    # drop raster art layers (already in bg)
    for cls in ["back-art","front-art-wrap","front-ov","front-ov2","spine"]:
        fin=re.sub(r'<div class="abs %s">(<div class="abs front-art"></div>)?</div>'%cls,'',fin) if cls=="front-art-wrap" else fin.replace(f'<div class="abs {cls}"></div>','')
    open("final/cover.html","w").write(fin)
    pg2=br.new_page(); pg2.goto("file:///home/claude/hc/final/cover.html"); pg2.wait_for_timeout(1500)
    pg2.pdf(path="final/cover_rgb.pdf",width=f"{W}in",height=f"{H}in",print_background=True,margin=dict(top="0",bottom="0",left="0",right="0"))
    br.close()

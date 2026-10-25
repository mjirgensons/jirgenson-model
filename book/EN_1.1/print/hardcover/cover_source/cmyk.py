import re, io, numpy as np, pikepdf
from PIL import Image, ImageCms
Image.MAX_IMAGE_PIXELS=None
ICC="/usr/share/texlive/texmf-dist/tex/generic/colorprofiles/FOGRA39L_coated.icc"
srgb=ImageCms.createProfile("sRGB"); cm=ImageCms.getOpenProfile(ICC)
flags=ImageCms.Flags.BLACKPOINTCOMPENSATION
tr=ImageCms.buildTransform(srgb,cm,"RGB","CMYK",renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,flags=flags)
bg=Image.open("bg.png").convert("RGB")
c=np.asarray(ImageCms.applyTransform(bg,tr)).astype(np.float32)/255
tot=c.sum(2)
lim=2.9; k=np.where(tot>lim,1,0)
over=tot>lim
scale=np.ones_like(tot); cmy=c[...,:3].sum(2)
scale[over]=np.clip((lim-c[...,3][over])/np.maximum(cmy[over],1e-6),0,1)
c[...,:3]*=scale[...,None]
print("max ink %",(c.sum(2).max()*100).round(0),"over-limit px",int(over.sum()))
cm_img=Image.fromarray((c*255+.5).astype(np.uint8),"CMYK")
buf=io.BytesIO(); cm_img.save(buf,"JPEG",quality=93,subsampling=0); jpg=buf.getvalue()
def kcol(r,g,b):
    px=Image.new("RGB",(1,1),(round(r*255),round(g*255),round(b*255)))
    v=np.asarray(ImageCms.applyTransform(px,tr))[0,0]/255.
    return " ".join(f"{x:.4f}" for x in v)
pdf=pikepdf.open("cover_rgb.pdf"); pg=pdf.pages[0]
cs=pg.Contents.read_bytes() if not isinstance(pg.Contents,pikepdf.Array) else b"".join(x.read_bytes() for x in pg.Contents)
first=cs.split(b"\n",1)[0]+b"\n"
i=cs.index(b"/X5 Do\nQ\n")+len(b"/X5 Do\nQ\n")
rest=cs[i:]
if rest.startswith(b"Q\n"): rest=rest[2:]
def rep(m):
    rgb=tuple(float(x) for x in m.group(1).split())
    col=kcol(*rgb).encode()
    return col+(b" K" if m.group(2)==b"RG" else b" k")
rest=re.sub(rb"([\d\.]+ [\d\.]+ [\d\.]+) (RG|rg)\b",rep,rest)
rest=rest.rstrip()
if rest.endswith(b"Q\nQ"): rest=rest[:-2]
rest+=b"\n"
new=b"q 1031.544 0 0 750.024 0 0.936 cm /X5 Do Q\n"+first+rest
assert b" rg" not in rest and b" RG" not in rest
x=pg.Resources.XObject.X5
x.write(jpg,filter=pikepdf.Name.DCTDecode)
x.ColorSpace=pikepdf.Name.DeviceCMYK; x.BitsPerComponent=8
x.Decode=pikepdf.Array([1,0,1,0,1,0,1,0])
for k_ in ["/SMask","/Mask"]:
    if k_ in x: del x[k_]
x.Width,x.Height=cm_img.size
if "/Pattern" in pg.Resources: del pg.Resources["/Pattern"]
pg.Contents=pdf.make_stream(new)
box=pikepdf.Array([0,0.936,1031.544,750.96])
for n in ["/MediaBox","/CropBox","/TrimBox","/BleedBox","/ArtBox"]: pg[n]=box
pdf.docinfo["/Title"]="Steer, Don't Guess — hardcover cover (EN 1.1)"
pdf.save("Jirgenson_Steer_Dont_Guess_EN_1.1_hardcover_cover_NEW.pdf")

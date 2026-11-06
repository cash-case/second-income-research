import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('S','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('SB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
W,H=letter
IN,OUT,TOP,BOT=0.75*inch,0.5*inch,0.6*inch,0.6*inch
c=canvas.Canvas(sys.argv[1],pagesize=letter,initialFontName='S',initialFontSize=10)  # avoid non-embedded Helvetica
c.setTitle("Glaze Test & Kiln Firing Log (DRAFT)"); c.setAuthor("DRAFT - author not set"); c.setCreator("build_interior.py")
page=[0]
def margins():
    odd=(page[0]%2==1)  # page 1 is recto
    left=IN if odd else OUT
    right=W-(OUT if odd else IN)
    return left,right
def newpage():
    if page[0]: c.showPage()
    page[0]+=1
def footer():
    l,r=margins(); c.setFont('S',8); c.setFillGray(0.4)
    c.drawCentredString((l+r)/2,BOT-0.25*inch,str(page[0])); c.setFillGray(0)
def field(x,y,w,label,h=0.32*inch):
    c.setFont('S',8); c.drawString(x,y+2,label)
    c.setLineWidth(0.5); c.line(x,y-h+10,x+w,y-h+10)
def box(x,y,w,h,label):
    c.setLineWidth(0.5); c.rect(x,y-h,w,h)
    c.setFont('S',8); c.drawString(x+4,y-11,label)
# title page
newpage(); l,r=margins()
c.setFont('SB',26); c.drawCentredString((l+r)/2,H*0.62,"Glaze Test & Kiln Firing Log")
c.setFont('S',13); c.drawCentredString((l+r)/2,H*0.62-30,"80 test-tile pages · 12 firing-log pages · tile index")
c.setFont('S',10); c.drawCentredString((l+r)/2,H*0.62-60,"This log belongs to: ______________________________")
c.setFont('S',8); c.setFillGray(0.5); c.drawCentredString((l+r)/2,BOT,"DRAFT — not for sale. Interior layout generated with AI tools; requires owner review.")
c.setFillGray(0)
# blank verso
newpage()
# how-to page: left for owner
newpage(); l,r=margins()
c.setFont('SB',16); c.drawString(l,H-TOP-20,"How to use this log")
c.setFont('S',10); c.setFillGray(0.45)
c.drawString(l,H-TOP-50,"[OWNER TO WRITE in his own words: how he records tests in his studio.]")
c.setFillGray(0); footer()
# index pages 4-7: 80 rows across 4 pages (20/page)
for p in range(4):
    newpage(); l,r=margins(); w=r-l
    c.setFont('SB',14); c.drawString(l,H-TOP-14,"Tile Index" + (" (cont.)" if p else ""))
    cols=[("Tile #",0.09),("Page",0.08),("Recipe / glaze",0.38),("Cone",0.08),("Result 1–5",0.12),("Keep?",0.1),("Notes",0.15)]
    y=H-TOP-40; x=l
    c.setFont('SB',8)
    for name,f in cols: c.drawString(x+2,y,name); x+=w*f
    rowh=(y-BOT-20)/20
    for i in range(21):
        yy=y-6-i*rowh; c.setLineWidth(0.4); c.line(l,yy,r,yy)
    x=l
    for name,f in cols:
        c.line(x,y-6,x,y-6-20*rowh); x+=w*f
    c.line(r,y-6,r,y-6-20*rowh)
    c.setFont('S',8)
    for i in range(20): c.drawString(l+3,y-6-i*rowh-rowh/2-3,str(p*20+i+1))
    footer()
# 80 test pages
for t in range(1,81):
    newpage(); l,r=margins(); w=r-l
    y=H-TOP-14
    c.setFont('SB',14); c.drawString(l,y,f"Test Tile #{t}")
    c.setFont('S',9); c.drawRightString(r,y,"Date: ______________")
    y-=30
    half=(w-12)/2
    for a,b in [("Glaze / recipe name","Clay body"),("Cone / target temp","Atmosphere (ox / red / other)"),("Application (dip / brush / spray / pour)","Thickness / number of coats"),("Firing program / schedule","Peak temp & hold"),("Slow cool? (Y/N, details)","Kiln & shelf position")]:
        field(l,y,half,a); field(l+half+12,y,half,b); y-=0.42*inch
    y-=6
    box(l,y,w*0.58,2.0*inch,"Recipe (ingredient — amount — %)")
    box(l+w*0.62,y,w*0.38,2.0*inch,"Tile photo / sketch")
    yy=y-22
    c.setLineWidth(0.3)
    for k in range(6): c.line(l+6,yy-k*0.28*inch,l+w*0.58-6,yy-k*0.28*inch)
    y-=2.0*inch+14
    box(l,y,w,1.0*inch,"Layers (order, coats, glaze on glaze)")
    y-=1.0*inch+14
    box(l,y,w,y-BOT-50-(y-BOT-50-2.3*inch) if False else 2.3*inch,"Result notes (surface, colour, crazing, running, pinholes)")
    y-=2.3*inch+18
    c.setFont('S',9)
    c.drawString(l,y,"Result:  1   2   3   4   5          Keep?  Yes / No / Retest          Next change: ______________________")
    footer()
# 12 firing log pages
for f in range(1,13):
    newpage(); l,r=margins(); w=r-l
    y=H-TOP-14
    c.setFont('SB',14); c.drawString(l,y,f"Kiln Firing Log — Firing #____")
    y-=30; half=(w-12)/2
    for a,b in [("Date","Kiln"),("Firing type (bisque / glaze / luster / other)","Program / schedule"),("Cone / peak temperature reached","Hold or slow cool"),("Element firing count (this kiln)","Witness cones / results")]:
        field(l,y,half,a); field(l+half+12,y,half,b); y-=0.42*inch
    y-=6
    box(l,y,w,2.6*inch,"Load contents (shelf by shelf, tile #s)")
    y-=2.6*inch+14
    box(l,y,w,2.4*inch,"Results & notes")
    footer()
# Notes page(s) to reach an even count. A page with no drawing is dropped by
# reportlab on save, so the filler must have content (earlier draft shipped 99 pages).
if page[0]%2:
    newpage(); l,r=margins(); w=r-l
    c.setFont('SB',14); c.drawString(l,H-TOP-14,"Notes")
    c.setLineWidth(0.4)
    yy=H-TOP-0.7*inch
    while yy>BOT+0.3*inch: c.line(l,yy,r,yy); yy-=0.32*inch
    footer()
c.save(); print("pages",page[0])  # verify with pdfinfo

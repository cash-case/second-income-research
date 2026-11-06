# Cover draft: 100 pages, white paper, black ink, 8.5x11, bleed 0.125
# Spine = 100 x 0.002252 in (KDP G201953020). All values in inches.
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('S','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('SB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
PAGES=100; B=0.125; TW,TH=8.5,11.0
SP=PAGES*0.002252
W=B+TW+SP+TW+B; H=B+TH+B
c=canvas.Canvas(sys.argv[1],pagesize=(W*inch,H*inch),initialFontName='S',initialFontSize=10); c.setTitle("Glaze Test & Kiln Firing Log cover (DRAFT)"); c.setAuthor("DRAFT - author not set"); c.setCreator("build_cover.py")
clay=CMYKColor(0.05,0.45,0.65,0.25); cream=CMYKColor(0.0,0.03,0.12,0.0); ink=CMYKColor(0,0,0,1)
c.setFillColor(cream); c.rect(0,0,W*inch,H*inch,fill=1,stroke=0)
fx=B+TW+SP  # front cover left edge (trim)
# front band
c.setFillColor(clay); c.rect(fx*inch,(B+6.2)*inch,(TW+B)*inch,2.6*inch,fill=1,stroke=0)
c.setFillColor(cream); c.setFont('SB',40)
cx=(fx+TW/2)*inch
c.drawCentredString(cx,(B+7.9)*inch,"Glaze Test &"); c.drawCentredString(cx,(B+7.1)*inch,"Kiln Firing Log")
c.setFillColor(ink); c.setFont('S',16)
c.drawCentredString(cx,(B+5.5)*inch,"80 test-tile pages · 12 firing logs · tile index")
c.setFont('S',13); c.drawCentredString(cx,(B+5.0)*inch,"Cone, atmosphere, layers, firing schedule & results")
c.setFont('S',11); c.drawCentredString(cx,(B+0.8)*inch,"[AUTHOR / IMPRINT NAME — owner to choose]")
# spine (>=79 pages allows text). keep 0.0625 in from spine edges
c.setFillColor(clay); c.rect((B+TW)*inch,0,SP*inch,H*inch,fill=1,stroke=0)
c.saveState(); c.translate((B+TW+SP/2)*inch,(H/2)*inch); c.rotate(-90)
c.setFillColor(cream); c.setFont('SB',9); c.drawCentredString(0,-3,"GLAZE TEST & KILN FIRING LOG"); c.restoreState()
# back cover
bx=B
c.setFillColor(ink); c.setFont('SB',18); c.drawString((bx+0.75)*inch,(B+9.4)*inch,"Keep every test. Repeat the good ones.")
c.setFont('S',11); y=B+8.8
for line in ["[BACK-COVER COPY — owner to write in his own words.]","","Inside:","• 80 test-tile pages: recipe, clay body, cone, atmosphere,","   application, thickness, layers, firing program, results","• 12 kiln firing-log pages: firing type, program, peak temp,","   holds and slow cools, load contents, element firing count","• Tile index to find any test fast","","8.5 × 11 in · 100 pages"]:
    c.drawString((bx+0.75)*inch,y*inch,line); y-=0.3
# barcode clear zone (KDP places barcode if none supplied): keep 2 x 1.2 in clear, lower right of back
c.setStrokeColor(CMYKColor(0,0,0,0.3)); c.setDash(3,3)
c.rect((B+TW-0.25-2.0)*inch,(B+0.25)*inch,2.0*inch,1.2*inch,fill=0,stroke=1)
c.setFont('S',7); c.setFillColor(CMYKColor(0,0,0,0.4)); c.drawCentredString((B+TW-0.25-1.0)*inch,(B+0.8)*inch,"barcode area — keep clear (guide; remove before upload)")
c.save(); print(f"cover {W:.4f} x {H:.4f} in, spine {SP:.4f} in")

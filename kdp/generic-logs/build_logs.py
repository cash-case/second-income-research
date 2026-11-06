#!/usr/bin/env python3
"""KDP 6x9 log-book builder (research drafts - not for publication).
Builds vehicle-maintenance-log and daily-expense-log interiors + covers.
Fonts: DejaVu Sans / DejaVu Sans Bold (Bitstream Vera license, commercial OK), embedded subsets.
Specs verified against KDP help: trim 6x9 (432x648pt), 110pp B&W white paper,
spine = 110 * 0.002252in = 17.84pt, cover = bleed+back+spine+front+bleed = 899.84x666pt.
"""
from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DVS", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVSB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

import os, sys
OUT = (sys.argv[1] if len(sys.argv)>1 else "./out") + "/"
os.makedirs(OUT, exist_ok=True)
W, H = 6*inch, 9*inch
PAGES = 110
SPINE_IN = PAGES * 0.002252          # inches
SPINE = SPINE_IN * inch              # points (17.84)
CW = (0.125 + 6 + SPINE_IN + 6 + 0.125) * inch   # 899.84pt
CH = 9.25 * inch                     # 666pt
BLEED = 0.125 * inch
HDR_H, ROW_H = 0.30*inch, 0.40*inch  # 21.6pt header, 28.8pt data rows
DATA_ROWS = 18

def interior(path, page_title, title_page, cols):
    c = canvas.Canvas(path, pagesize=(W, H), initialFontName="DVS")  # no stray non-embedded Helvetica
    c.setTitle(title_page + " - Interior (Draft)")
    c.setAuthor("")  # author unresolved - do not invent an imprint
    # title page
    c.setFont("DVSB", 20); c.drawCentredString(W/2, H-3*inch, title_page)
    c.setFont("DVS", 9);  c.drawCentredString(W/2, 1.0*inch, "Name: ______________________")
    c.showPage()
    for n in range(2, PAGES+1):
        c.setFont("DVSB", 13); c.drawCentredString(W/2, H-0.6*inch, page_title)
        x0, ytop = 0.5*inch, H-1.0*inch   # table starts 1in from top
        y = ytop
        # header row
        cx = x0
        c.setFont("DVS", 8)
        for name, wpt in cols:
            c.rect(cx, y-HDR_H, wpt, HDR_H)
            c.drawString(cx+3, y-HDR_H+5.1, name)
            cx += wpt
        y -= HDR_H
        for _ in range(DATA_ROWS):
            cx = x0
            for name, wpt in cols:
                c.rect(cx, y-ROW_H, wpt, ROW_H)
                cx += wpt
            y -= ROW_H
        c.setFont("DVS", 7); c.drawCentredString(W/2, 0.32*inch, str(n))
        c.showPage()
    c.save(); print("built", path)

def cover(path, title, subtitle, bg, fg):
    c = canvas.Canvas(path, pagesize=(CW, CH), initialFontName="DVS")
    c.setTitle(title + " - Cover (Draft)")
    c.setAuthor("")
    c.setFillColor(bg); c.rect(0, 0, CW, CH, fill=1, stroke=0)
    spine_cx = BLEED + 6*inch + SPINE/2          # 449.92pt, centered between folds 441 / 458.84
    fx = BLEED + 6*inch + SPINE                  # front cover left edge 458.84pt
    front_cx = fx + 3*inch                       # 674.84pt
    # spine text (8pt bold, rotated; glyph band ~8pt -> >=4.9pt clearance each fold)
    c.saveState(); c.translate(spine_cx, CH/2); c.rotate(90)
    c.setFillColor(fg); c.setFont("DVSB", 8)
    c.drawCentredString(0, -2.3, title); c.restoreState()
    # front title + subtitle
    c.setFillColor(fg)
    c.setFont("DVSB", 22.5); c.drawCentredString(front_cx, CH-3.2*inch, title)
    c.setFont("DVS", 12);    c.drawCentredString(front_cx, CH-3.7*inch, subtitle)
    # back cover
    bx = BLEED + 3*inch
    c.setFont("DVS", 9); c.drawCentredString(bx, CH-2.5*inch, "Track what matters, one line at a time.")
    c.save(); print("built", path)

VCOLS = [("Date",0.95*inch),("Odometer",0.85*inch),("Service / Repair",1.6*inch),("Cost",0.75*inch),("Notes",0.85*inch)]
ECOLS = [("Date",0.9*inch),("Description",1.6*inch),("Category",0.9*inch),("Amount",0.8*inch),("Notes",0.8*inch)]

interior(OUT+"vehicle-maintenance-log-interior.pdf", "Vehicle Maintenance Log", "Vehicle Maintenance Log Book", VCOLS)
interior(OUT+"daily-expense-log-interior.pdf", "Daily Expense Log", "Daily Expense Log Book", ECOLS)
cover(OUT+"vehicle-maintenance-log-cover.pdf", "Vehicle Maintenance Log Book",
      "Service records, mileage and costs", Color(31/255,59/255,86/255), HexColor("#F5F1E8"))
cover(OUT+"daily-expense-log-cover.pdf", "Daily Expense Log Book",
      "A simple record of where the money goes", Color(38/255,65/255,40/255), HexColor("#F7F3EE"))

#!/usr/bin/env python3
"""Text-art proof set: 6 original typographic scripture compositions.
DRAFT, not for sale. The verse wording is KJV placeholder text (public domain in the US);
the final translation (ESV / The Message) is pending the rights holders' permission.
Each design is laid out natively per size (proportional), as a vector PDF.
Usage: python3 build_text_art.py <outdir>
"""
import os, sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(HERE, "fonts")
for name, fn in [("Corm", "CormorantGaramond-VF.ttf"), ("Cinzel", "Cinzel-VF.ttf"),
                 ("EBG", "EBGaramond-VF.ttf"), ("Pinyon", "PinyonScript-Regular.ttf")]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FD, fn)))

OUT = (sys.argv[1] if len(sys.argv) > 1 else "out")
os.makedirs(OUT, exist_ok=True)
SIZES = [(8, 10), (11, 14), (16, 20), (18, 24)]
CREAM, INK, WARM = HexColor("#F3EEE4"), HexColor("#26231F"), HexColor("#8A6F4E")
NAVY, SAND = HexColor("#1F2A33"), HexColor("#E9DFCC")

class Art:
    def __init__(self, c, W, H):
        self.c, self.W, self.H = c, W, H
        self.u = min(W, H * 0.8) / 8.0   # 1 design unit = 1 inch at 8x10
    def bg(self, col):
        self.c.setFillColor(col); self.c.rect(0, 0, self.W, self.H, fill=1, stroke=0)
    def text(self, s, font, size_in, y_frac, col, track=0.0, align="c", x=None):
        c = self.c; sz = size_in * self.u; cs = track * sz
        c.setFont(font, sz); c.setFillColor(col)
        w = pdfmetrics.stringWidth(s, font, sz) + cs * (len(s) - 1)
        y = self.H * y_frac
        if align == "c": x0 = (self.W - w) / 2
        elif align == "l": x0 = x
        else: x0 = x - w
        c.drawString(x0, y, s, charSpace=cs)
        return w
    def fit(self, s, font, y_frac, col, max_w_frac, max_size, track=0.0):
        sz = max_size
        while sz > 0.05:
            w = pdfmetrics.stringWidth(s, font, sz * self.u) + track * sz * self.u * (len(s) - 1)
            if w <= self.W * max_w_frac: break
            sz *= 0.97
        self.text(s, font, sz, y_frac, col, track)
        return sz
    def rule(self, y_frac, w_frac, col, lw=0.012):
        c = self.c; c.setStrokeColor(col); c.setLineWidth(lw * self.u)
        c.line(self.W * (0.5 - w_frac / 2), self.H * y_frac, self.W * (0.5 + w_frac / 2), self.H * y_frac)
    def draft(self, col):
        self.text("DRAFT  ·  placeholder text (KJV)  ·  not for sale", "EBG", 0.11, 0.022, col, 0.05)

def d1_be_still(a):
    a.bg(CREAM)
    a.fit("Be still,", "Corm", 0.56, INK, 0.74, 1.55)
    a.text("AND KNOW THAT", "Cinzel", 0.22, 0.44, INK, 0.32)
    a.text("I AM GOD", "Cinzel", 0.22, 0.395, INK, 0.32)
    a.rule(0.335, 0.08, WARM)
    a.text("PSALM 46:10", "Cinzel", 0.12, 0.29, WARM, 0.35)
    a.draft(WARM)

def d2_new_every_morning(a):
    a.bg(CREAM)
    a.text("HIS COMPASSIONS FAIL NOT", "Cinzel", 0.16, 0.70, INK, 0.28)
    a.text("THEY ARE", "Cinzel", 0.16, 0.655, INK, 0.28)
    a.fit("new every", "Pinyon", 0.53, INK, 0.80, 1.25)
    a.fit("morning", "Pinyon", 0.40, INK, 0.80, 1.25)
    a.text("great is thy faithfulness", "EBG", 0.26, 0.30, WARM)
    a.text("LAMENTATIONS 3:22–23", "Cinzel", 0.11, 0.24, WARM, 0.35)
    a.draft(WARM)

def d3_fear_not(a):
    a.bg(SAND)
    x = a.W * 0.16
    for i, wd in enumerate(["FEAR", "THOU", "NOT"]):
        a.text(wd, "Cinzel", 1.05, 0.70 - i * 0.135, NAVY, 0.04, align="l", x=x)
    c = a.c; c.setStrokeColor(WARM); c.setLineWidth(0.02 * a.u)
    c.line(x, a.H * 0.375, x + a.W * 0.22, a.H * 0.375)
    a.text("for I am with thee", "EBG", 0.36, 0.30, NAVY, align="l", x=x)
    a.text("ISAIAH 41:10", "Cinzel", 0.12, 0.25, WARM, 0.35, align="l", x=x)
    a.draft(WARM)

def d4_come_unto_me(a):
    a.bg(CREAM)
    lines = ["Come unto me,", "all ye that labour", "and are heavy laden,", "and I will give you"]
    for i, s in enumerate(lines):
        a.text(s, "EBG", 0.46, 0.73 - i * 0.065, INK)
    a.fit("rest", "Pinyon", 0.36, INK, 0.6, 2.2)
    a.rule(0.29, 0.06, WARM)
    a.text("MATTHEW 11:28", "Cinzel", 0.12, 0.25, WARM, 0.35)
    a.draft(WARM)

def d5_behold_door(a):
    a.bg(NAVY)
    c = a.c; c.setStrokeColor(SAND); c.setLineWidth(0.025 * a.u)
    w = a.W * 0.46; x0 = (a.W - w) / 2; yb = a.H * 0.24; yt = a.H * 0.66
    p = c.beginPath(); p.moveTo(x0, yb); p.lineTo(x0, yt)
    p.arcTo(x0, yt - w / 2, x0 + w, yt + w / 2, startAng=180, extent=-180)
    p.lineTo(x0 + w, yb); c.drawPath(p, stroke=1, fill=0)
    a.text("BEHOLD,", "Cinzel", 0.22, 0.63, SAND, 0.3)
    a.text("I stand", "Corm", 0.62, 0.545, SAND)
    a.text("at the door,", "Corm", 0.62, 0.475, SAND)
    a.text("and knock", "Corm", 0.62, 0.405, SAND)
    a.text("REVELATION 3:20", "Cinzel", 0.11, 0.30, SAND, 0.35)
    a.draft(SAND)

def d6_courage(a):
    a.bg(NAVY)
    a.text("BE STRONG", "Cinzel", 0.62, 0.64, SAND, 0.12)
    a.text("AND OF A GOOD", "Cinzel", 0.22, 0.575, SAND, 0.32)
    a.fit("courage", "Pinyon", 0.44, SAND, 0.78, 1.7)
    a.text("be not afraid, for the Lord thy God is with thee", "EBG", 0.19, 0.33, SAND)
    a.text("JOSHUA 1:9", "Cinzel", 0.11, 0.28, SAND, 0.35)
    a.draft(SAND)

DESIGNS = [("01-be-still", d1_be_still), ("02-new-every-morning", d2_new_every_morning),
           ("03-fear-thou-not", d3_fear_not), ("04-come-unto-me", d4_come_unto_me),
           ("05-behold-i-stand-at-the-door", d5_behold_door), ("06-be-strong-courage", d6_courage)]

for slug, fn in DESIGNS:
    for (wi, hi) in SIZES:
        path = os.path.join(OUT, f"{slug}_{wi}x{hi}.pdf")
        c = canvas.Canvas(path, pagesize=(wi * inch, hi * inch), initialFontName="EBG")
        c.setTitle(f"{slug} {wi}x{hi} (DRAFT, placeholder text)"); c.setAuthor("DRAFT - author not set")
        c.setCreator("build_text_art.py")
        fn(Art(c, wi * inch, hi * inch)); c.showPage(); c.save()
print("built", len(DESIGNS) * len(SIZES), "PDFs in", OUT)

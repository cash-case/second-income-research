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

OUT = next((x for x in sys.argv[1:] if not x.startswith("--")), "out")
os.makedirs(OUT, exist_ok=True)
SIZES = [(8, 10), (11, 14), (16, 20), (18, 24)]
PALETTES = {  # name: (background, main ink, accent)
    "cream": (HexColor("#F3EEE4"), HexColor("#26231F"), HexColor("#8A6F4E")),
    "sand":  (HexColor("#E9DFCC"), HexColor("#1F2A33"), HexColor("#8A6F4E")),
    "navy":  (HexColor("#1F2A33"), HexColor("#E9DFCC"), HexColor("#C9B48F")),
    "forest":(HexColor("#24312A"), HexColor("#EDE6D6"), HexColor("#C2AC80")),
}

class Art:
    def __init__(self, c, W, H):
        self.c, self.W, self.H = c, W, H
        # 1 design unit = 1 inch at 8x10. Landscape keeps the same type-to-height ratio as portrait.
        self.u = H / 10.0 if W > H else min(W, H * 0.8) / 8.0
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
        self.text("DRAFT  ·  placeholder text (KJV excerpt)  ·  not for sale", "EBG", 0.11, 0.022, col, 0.05)

def d1_be_still(a, P):
    bg, ink, acc = P; a.bg(bg)
    a.fit("Be still,", "Corm", 0.56, ink, 0.74, 1.55)
    a.text("AND KNOW THAT", "Cinzel", 0.22, 0.44, ink, 0.32)
    a.text("I AM GOD …", "Cinzel", 0.22, 0.395, ink, 0.32)
    a.rule(0.335, 0.08, acc)
    a.text("PSALM 46:10  ·  EXCERPT", "Cinzel", 0.12, 0.29, acc, 0.35)
    a.draft(acc)

def d2_new_every_morning(a, P):
    bg, ink, acc = P; a.bg(bg)
    a.text("… HIS COMPASSIONS FAIL NOT.", "Cinzel", 0.16, 0.70, ink, 0.28)
    a.text("THEY ARE", "Cinzel", 0.16, 0.655, ink, 0.28)
    a.fit("new every", "Pinyon", 0.53, ink, 0.80, 1.25)
    a.fit("morning:", "Pinyon", 0.40, ink, 0.80, 1.25)
    a.text("great is thy faithfulness.", "EBG", 0.26, 0.30, acc)
    a.text("LAMENTATIONS 3:22–23  ·  EXCERPT", "Cinzel", 0.11, 0.24, acc, 0.35)
    a.draft(acc)

def d3_fear_not(a, P):
    bg, ink, acc = P; a.bg(bg)
    x = a.W * 0.16
    for i, wd in enumerate(["FEAR", "THOU", "NOT;"]):
        a.text(wd, "Cinzel", 1.05, 0.70 - i * 0.135, ink, 0.04, align="l", x=x)
    c = a.c; c.setStrokeColor(acc); c.setLineWidth(0.02 * a.u)
    c.line(x, a.H * 0.375, x + a.W * 0.22, a.H * 0.375)
    a.text("for I am with thee …", "EBG", 0.36, 0.30, ink, align="l", x=x)
    a.text("ISAIAH 41:10  ·  EXCERPT", "Cinzel", 0.12, 0.25, acc, 0.35, align="l", x=x)
    a.draft(acc)

def d4_come_unto_me(a, P):
    bg, ink, acc = P; a.bg(bg)
    lines = ["Come unto me,", "all ye that labour", "and are heavy laden,", "and I will give you"]
    for i, s in enumerate(lines):
        a.text(s, "EBG", 0.46, 0.73 - i * 0.065, ink)
    a.fit("rest.", "Pinyon", 0.36, ink, 0.6, 2.2)
    a.rule(0.29, 0.06, acc)
    a.text("MATTHEW 11:28", "Cinzel", 0.12, 0.25, acc, 0.35)
    a.draft(acc)

def d5_behold_door(a, P):
    bg, ink, acc = P; a.bg(bg)
    c = a.c; c.setStrokeColor(ink); c.setLineWidth(0.025 * a.u)
    w = min(a.W * 0.46, a.H * 0.368); x0 = (a.W - w) / 2; yb = a.H * 0.24; yt = a.H * 0.66
    p = c.beginPath(); p.moveTo(x0, yb); p.lineTo(x0, yt)
    p.arcTo(x0, yt - w / 2, x0 + w, yt + w / 2, startAng=180, extent=-180)
    p.lineTo(x0 + w, yb); c.drawPath(p, stroke=1, fill=0)
    a.text("BEHOLD,", "Cinzel", 0.22, 0.63, ink, 0.3)
    a.text("I stand", "Corm", 0.62, 0.545, ink)
    a.text("at the door,", "Corm", 0.62, 0.475, ink)
    a.text("and knock …", "Corm", 0.62, 0.405, ink)
    a.text("REVELATION 3:20  ·  EXCERPT", "Cinzel", 0.10, 0.30, acc, 0.3)
    a.draft(acc)

def d6_courage(a, P):
    bg, ink, acc = P; a.bg(bg)
    a.text("BE STRONG", "Cinzel", 0.62, 0.64, ink, 0.12)
    a.text("AND OF A GOOD", "Cinzel", 0.22, 0.575, ink, 0.32)
    a.fit("courage;", "Pinyon", 0.44, ink, 0.78, 1.7)
    a.fit("be not afraid, … for the LORD thy God is with thee …", "EBG", 0.33, ink, 0.80, 0.19)
    a.text("JOSHUA 1:9  ·  EXCERPT", "Cinzel", 0.11, 0.28, acc, 0.35)
    a.draft(acc)

DESIGNS = [("01-be-still", d1_be_still, "cream"), ("02-new-every-morning", d2_new_every_morning, "cream"),
           ("03-fear-thou-not", d3_fear_not, "sand"), ("04-come-unto-me", d4_come_unto_me, "cream"),
           ("05-behold-i-stand-at-the-door", d5_behold_door, "navy"), ("06-be-strong-courage", d6_courage, "navy")]

def build(slug, fn, pal, wi, hi):
    orient = "portrait" if hi >= wi else "landscape"
    path = os.path.join(OUT, f"{slug}_{pal}_{wi}x{hi}.pdf")
    c = canvas.Canvas(path, pagesize=(wi * inch, hi * inch), initialFontName="EBG")
    c.setTitle(f"{slug} {pal} {wi}x{hi} {orient} (DRAFT, KJV placeholder excerpt)")
    c.setAuthor("DRAFT - author not set"); c.setCreator("build_text_art.py")
    fn(Art(c, wi * inch, hi * inch), PALETTES[pal]); c.showPage(); c.save()

n = 0
ALL = "--all-palettes" in sys.argv
for slug, fn, default in DESIGNS:
    for pal in (PALETTES if ALL else [default]):
        for (wi, hi) in SIZES:
            build(slug, fn, pal, wi, hi); build(slug, fn, pal, hi, wi); n += 2
print("built", n, "PDFs in", OUT)

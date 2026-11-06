# Text-art proof set: DRAFT, not for sale

These are six original typographic scripture compositions. **Cash approved the direction** (PR #2, 6697749758). That's direction only: it isn't translation clearance or approval to sell. He also asked for landscape versions and affordable framing options; both are below. The text is the design: no AI imagery, no photos, and no competitor layouts copied.

**The verse wording is placeholder text.** It's KJV (public domain in the US), used only to show the typography. The final translation will be ESV or The Message, which needs the rights holders' **written permission** first (see `reports/esv-msg-rights-reference.md` on PR #2). Every file is marked "DRAFT · placeholder text (KJV) · not for sale".

**Excerpt standard** (per Instinct, 6697749758): every partial verse shows its omissions with "…" and is labeled "EXCERPT" next to the reference. Matthew 11:28 is the full verse. Josh 1:9 now reads "be not afraid, … for the LORD thy God is with thee …", restoring "LORD" in capitals and marking the omitted "neither be thou dismayed:".

| # | Design | Reference | Palette |
|---|---|---|---|
| 01 | Be still, | Psalm 46:10 | cream / ink |
| 02 | new every morning | Lamentations 3:22–23 | cream / ink |
| 03 | FEAR THOU NOT | Isaiah 41:10 | sand / navy |
| 04 | Come unto me… rest | Matthew 11:28 | cream / ink |
| 05 | Behold, I stand at the door, and knock (arch) | Revelation 3:20 | navy / sand |
| 06 | Be strong… courage | Joshua 1:9 | navy / sand |

The references follow Hark's verse input and the invite-and-listen brief. Revelation 3:20 is the "invite" verse.

## Files
- `out/<design>_<palette>_<W>x<H>.pdf`: vector PDFs in **portrait 8×10, 11×14, 16×20, 18×24 and landscape 10×8, 14×11, 20×16, 24×18**. Each is laid out natively for its size, with fonts embedded.
- `out/*_8x10.png` and `out/*_10x8.png`: 300 DPI PNGs (2400×3000 and 3000×2400). For other sizes, use `pdftoppm -r 300 -png -singlefile <pdf> <name>`.
- `proof-sheet-portrait.png`, `proof-sheet-landscape.png`: the six designs in their default palette.
- `palette-options-8x10.png`: every design in four palettes (cream, sand, navy, forest). Run `python3 build_text_art.py out --all-palettes` to build all 192 PDFs.
- Rebuild the default set with `python3 build_text_art.py out`.

## Font licence log (checked at source 2026-11-06)
All fonts come from the Google Fonts repository (github.com/google/fonts, `ofl/`), and each one's `OFL.txt` is copied next to the font in `fonts/`.

| Font | Licence | Source |
|---|---|---|
| Cormorant Garamond (variable; renders at its default Light weight) | SIL OFL 1.1 | google/fonts `ofl/cormorantgaramond` |
| Cinzel (variable; default Regular) | SIL OFL 1.1 | `ofl/cinzel` |
| EB Garamond (variable; default Regular) | SIL OFL 1.1 | `ofl/ebgaramond` |
| Pinyon Script | SIL OFL 1.1 | `ofl/pinyonscript` |

OFL 1.1 preamble [V]: the fonts may be "used, studied, modified and redistributed freely as long as they are not sold by themselves", and "the requirement for fonts to remain under this license does not apply to any document created using the fonts". [A] Selling prints *made with* these fonts is allowed; selling the font files is not. Keeping the font files in this repo is redistribution, which OFL permits with the licence included.

## Open
- Cash's yes or no on direction comes **before any variants**.
- Translation rights are [T]. There's no demand evidence; Etsy is robots-blocked for us.
- POD print-file specs (pixel size per product, bleed) need checking against the chosen provider before upload.

## Framing options: POD base costs (Printful public catalog API, read 2026-11-06) [V]
Prices are Printful's listed USD variant prices **before shipping, tax and any Etsy fees**. They aren't a merchant's final cost. The source is `https://api.printful.com/products/{id}`.

| Size | Unframed poster (id 1, enhanced matte) | Framed (id 2; black / white / red oak, same price) | Framed with mat (id 795) |
|---|---|---|---|
| 8×10 | $7.03 | $20.76 | n/a |
| 11×14 | $9.83 | $30.69 | n/a |
| 12×16 | $11.11 | $32.20 | $36.41 |
| 16×20 | $12.13 | $42.61 | $45.73 |
| 18×24 | $13.15 | $46.30 | $50.93 |

### Product = printed + framed + shipped to the buyer (Cash, via Instinct, 6697835547)
US shipping for a single item comes from Printful's shipping page (https://www.printful.com/shipping, read 2026-11-06) [V]:
- Framed small (8×10 to 16×16): **$10.89** first item, +$4.50 each additional.
- Framed medium (16×20, 18×18, 18×24): **$14.49**, +$4.95.
- **US holiday surcharge: $0.40 per order, Oct 15 2026 to Jan 17 2027.**
- Fulfilment takes 2–5 business days, then standard shipping 3–4 business days. Printful says these times aren't guaranteed.

Delivered base cost per framed print (base + US shipping + surcharge; one item to one US address; excludes sales tax and Etsy fees) [A arithmetic on V inputs]:

| Size | Framed | Framed + mat |
|---|---|---|
| 8×10 | 20.76 + 10.89 + 0.40 = **$32.05** | n/a |
| 11×14 | 30.69 + 10.89 + 0.40 = **$41.98** | n/a |
| 12×16 | 32.20 + 10.89 + 0.40 = **$43.49** | 36.41 + 10.89 + 0.40 = **$47.70** |
| 16×20 | 42.61 + 14.49 + 0.40 = **$57.50** | 45.73 + 14.49 + 0.40 = **$60.62** |
| 18×24 | 46.30 + 14.49 + 0.40 = **$61.19** | 50.93 + 14.49 + 0.40 = **$65.82** |

**Fee-covering sale price on Etsy** [A]: the price P where P − Etsy fees = delivered base cost. Fees are 6.5% transaction + 3% + $0.25 processing + $0.20 listing, so P = (base + 0.45) / 0.905. Shipping is treated as included in P (free shipping), and fees are taken on the whole P.
- 8×10 framed: **$35.91**. 11×14: **$46.88**. 16×20: **$64.03**. 18×24: **$68.11**.
- **These are the prices at which the sale earns $0**, not price recommendations. They exclude sales tax, refunds, discounts, Offsite Ads (+15% of P if attributed) and any per-item margin.

**Timing** [A]: delivery is roughly 5–9 business days after an order (2–5 fulfilment + 3–4 shipping) and isn't guaranteed. That bears on the pre-Thanksgiving (Nov 26) goal, along with the open rights and consensus gates.

[A] Earlier notes on "affordable framing". Per Cash, the product is the framed and shipped print; buyer's-own-frame is **a fallback note only**:
- Our four sizes all match **standard retail frame sizes** (8×10, 11×14, 16×20, 18×24). So the cheapest framing route for a buyer is an unframed print or a digital download dropped into a store-bought frame. A listing can say "fits a standard 8×10 frame" at no cost to us.
- A POD frame roughly **triples the base cost at 8×10** ($7.03 to $20.76) and about **3.5× at 18×24**. A framed **8×10 at $20.76** is the lowest-cost framed entry.
- Printify's framed-poster page wouldn't render (JavaScript only), so its prices are [T]. File specs (pixels, bleed) for the chosen provider are [T] before any upload.

# Text-art proof set: DRAFT, not for sale

These are six original typographic scripture compositions for Cash's direction review (approved to build on PR #2, comment 6697613557). The text is the design: no AI imagery, no photos, and no competitor layouts copied.

**The verse wording is placeholder text.** It's KJV (public domain in the US), used only to show the typography. The final translation will be ESV or The Message, which needs the rights holders' **written permission** first (see `reports/esv-msg-rights-reference.md` on PR #2). Every file is marked "DRAFT · placeholder text (KJV) · not for sale".

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
- `out/*_{8x10,11x14,16x20,18x24}.pdf`: vector PDFs, each laid out natively for its size, with fonts embedded.
- `out/*_8x10.png`: 2400×3000 px at 300 DPI. Other sizes come from `pdftoppm -r 300 -png -singlefile <pdf> <name>`.
- `proof-sheet-8x10.png`: all six side by side, for review.
- Rebuild with `python3 build_text_art.py out`.

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

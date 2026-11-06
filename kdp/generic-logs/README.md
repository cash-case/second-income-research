# Generic KDP logs (vehicle maintenance, daily expense): DRAFT, not for sale

`build_logs.py` is the research side's generator (shared on PR #2, comment 6687661596; no private data), with two changes:
- the output directory is an argument;
- `initialFontName="DVS"`, so the raw output has no non-embedded Helvetica. Before, this relied on a gs prepress pass.

Run: `python3 build_logs.py <outdir>`. The PDFs aren't committed. The held copies live on the coordination side.

## Reproduced QA, 2026-11-06 [V local rebuild by Claude, unless marked]
| Check | Result |
|---|---|
| Interior | 110 pp, 432×648 pt (6×9) |
| Margins | 0.5 in on all sides; table bottom at 36 pt; folio at 23 pt (≥ 18 pt) |
| Rows | 1 header (21.6 pt) + 18 data rows at 28.8 pt (0.40 in) per page |
| Cover | 899.84×666 pt = 12.4977×9.25 in; spine 17.84 pt (110 × 0.002252 in) |
| Spine text | Font box x 446.14–454.14 pt vs folds 441.0 / 458.84 → 5.1 / 4.7 pt clear (≥ 4.5 pt). Instinct's ink extent gives 446.15–453.94 |
| Front title | Vehicle title 388.3 pt wide on a 432 pt panel → about 12.9 pt clear of the 0.125 in safe line on each side |
| Fonts | DejaVu subsets only, embedded (with the initialFontName fix) |
| Metadata | Per-book title "... (Draft)", author blank |

## Open
- Column fit risk [A]: no next-due field (vehicle); no payment method or total (expense). Deferred by the research side for width.
- Back-cover copy is a one-line placeholder. Demand and differentiation versus existing generic logs are unverified [T].
- Visual review on screen beyond the low-res render, and a physical proof [T], are unassigned.

## Differentiation check, 2026-11-06 (partial; non-Amazon sources only)
- Free substitutes exist for both logs [V]. A free daily spending log ([worldofprintables.com](https://worldofprintables.com/daily-spending-log/)) has Date, Store/vendor, Description, Category, Amount, **Payment method**, Notes, which covers more than our 5 columns. A free vehicle log ([wordlayouts.com](https://www.wordlayouts.com/spreadsheet/vehicle-maintenance-log-pdf/)) has 13 service-type columns, mileage, and room for next service due.
- So on content, both drafts are currently **less complete than free printables** [A]. Any differentiation would have to come from the physical bound-book format, or from columns the free versions lack. That's unproven [T].
- Searches also return many low-quality "printable" pages on unrelated or hijacked domains. That signals supply and SEO spam, not demand. **Nothing here shows buyer demand.**

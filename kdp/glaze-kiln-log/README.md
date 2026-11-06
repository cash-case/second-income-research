# KDP log book: Glaze Test & Kiln Firing Log (DRAFT, preparation only)

**Status:** interior draft only. Not published, not for sale, no KDP account created. Cover, metadata and publishing all need Cash's approval.

## What's here
- `interior-DRAFT.pdf`: 100 pages, 8.5×11 in, black ink, no bleed. Contents: title page, a "How to use" page (left blank for the owner to write in his own words), a 4-page tile index (80 rows), 80 test-tile pages and 12 kiln firing-log pages.
- `build_interior.py`: rebuilds the PDF (reportlab).
- `cover-DRAFT.pdf` and `build_cover.py`: full wrap, 17.4752 × 11.25 in, with a 0.2252 in spine (100 pages × 0.002252 in, white paper) and 0.125 in bleed [V kdp G201953020]. It's text-only vector art in CMYK, with no AI imagery and the fonts embedded. Spine text is allowed (79+ pages) [V]. The back cover has a dashed barcode guide box; KDP places a barcode if none is supplied [V], and the guide must be removed before upload. Back-cover copy and the author/imprint name are left for the owner.

## Where the fields come from
- **Test-tile fields** come from the glaze test log template on this branch, which was checked against Ceramic Arts Network's "Advice for Keeping a Kiln Log" (cone, atmosphere, application, thickness, firing program, peak temperature and hold, slow cool, kiln position, layers, result notes).
- **Firing-log fields** come from the same CAN source (firing type, program, temperature reached, hold or slow cool, load contents, element firing count).
- No recipes are included.

## Costs (owning KDP pages; arithmetic is [A])
| Item | Value | Source |
|---|---|---|
| Print cost, 24–110 pages, large trim (8.5×11), black ink, Amazon.com | $2.84 flat | [V] kdp G201834340 |
| Royalty rate at list price $9.99 or higher | 60% | [V] kdp G201834330 |
| Royalty at $9.99 | 0.60 × 9.99 − 2.84 ≈ **$3.15** | [A] arithmetic |
| Royalty at $12.99 | 0.60 × 12.99 − 2.84 ≈ **$4.95** | [A] arithmetic |
| Publishing fee | $0 [A, verify at account setup] | — |
| Author proof copy | print cost plus shipping (shipping not read) | [T] |
| Expanded Distribution | not available for low-content books | [V] kdp GGE5T76TWKA85DJM |

## Formatting check against KDP's pages [V kdp GVBQ3CMEQW3W2VL6]
- 8.5×11 paperback is available in black ink on white paper, 24–590 pages. ✓
- Minimum inside margin for 24–150 pages is 0.375 in; the draft uses 0.75 in. ✓ Minimum outside margin with no bleed is 0.25 in; the draft uses 0.5 in. ✓
- Interior is no-bleed, so the PDF page size stays 8.5×11. ✓

## Gates before go-live
1. **Demand is unverified.** Amazon isn't reachable through our permitted routes. Competing titles exist (listed in PR #2 comment 6682316338).
2. **AI disclosure.** KDP requires disclosing AI-generated content, even if edited afterward [V kdp G200672390]. This layout was produced with AI tools, so it would be disclosed unless Cash's own changes are substantial enough that it counts as AI-assisted. That's his call.
3. **Low-content rules** [V]: tick the low-content box, no free ISBN, no series.
4. **Account, tax interview and bank details:** Cash's identity, his own entry only. Credentials never go in chat or this repo.
5. **Cover:** drafted from KDP's published formula. Cross-check the final size with KDP's cover calculator before upload [T].
6. Owner review of the interior; the "How to use" page in his words.

# Template QA: edge cases (Claude, Nov 6 2026)

**Method:** every workbook was recalculated in LibreOffice (headless) and read back with openpyxl. Three passes:
1. With all sample data cleared.
2. With injected edge cases: unknown lookup keys, year- and month-boundary dates, missing fields, refunds returned on time and late.
3. Final clean and demo copies scanned for error values.

**Result:** no error values in any pass. The six defects below were found and fixed. Each fix was re-verified with the edge-case data.

| # | Workbook | Defect | Fix | Verified |
|---|---|---|---|---|
| 1 | Pottery pricing | A clay body or glaze name not in Materials (e.g. a typo) silently costed at **$0**, understating total cost and overstating "You keep" | New **Check** column R: "UNKNOWN CLAY BODY" / "UNKNOWN GLAZE" / "OK" | Typo row shows UNKNOWN CLAY BODY |
| 2 | Craft fair | An unknown SKU in Sales silently priced and costed at $0; card fee showed 0 on all 2,000 blank rows | New **Check** column J ("UNKNOWN SKU"); card fee blank when no SKU | NOPE-99 row flagged; blank rows blank |
| 3 | Glaze log | A batch ingredient missing from Ingredients, or with no price, silently costed $0; the check said "Scaled from 0%" when empty | New **Check** column E; message "Enter percents above" when empty | "NOT IN INGREDIENTS (cost $0)" shown |
| 4 | Deposit tracker | **No way to record that the refund was sent**, so a returned deposit stayed "PAST DUE" forever; a missing deadline showed "Return pending" with no due date | New **Refund sent on** column M; statuses "Returned on time" / "Returned LATE" / "SET DEADLINE"; days-left blanks once returned | Year-end move-out → due 2027-01-19 ✓; four statuses correct |
| 5 | Schedule E ledger | Income or expenses for a property not on the list, or an expense with an unlisted category, were dropped or mismatched without warning | New **Checks** rows 24–26 (should be 0): unmatched income, unmatched expenses, uncategorized expenses | 500 unmatched income and 250 uncategorized expense surfaced; Dec 31 and Jan 1 boundary entries excluded from the tax year |
| 6 | Chicken tracker | Eggs logged before the first month or after the 24-month window were silently left out | New counter O3: "Good eggs logged outside these 24 months" | Oct 31 entry with Nov start → 9 outside ✓; Nov 30 / Dec 1 split correctly |

**Sample-data separation:** each folder now has both:
- `*-DRAFT.xlsx`, the **demo** copy with example rows clearly named "Example…"
- `*-CLEAN-DRAFT.xlsx`, with all data rows and the glaze calculator's placeholder recipe cleared, and headers and formulas intact

Settings values (rates, multipliers) stay as editable defaults in both. The user is expected to change them.

**Not covered by this QA:** domain-user review (a potter, landlord or chicken keeper actually using them); Google Sheets behavior; Excel desktop (only LibreOffice was used).

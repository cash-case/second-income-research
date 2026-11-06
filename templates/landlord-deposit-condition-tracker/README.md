# Security deposit & move-in/move-out condition tracker: draft

**Status:** draft for review. Not for sale and not customer-ready. Nothing is listed or launched.

**Provenance:** built by an AI tool (Claude). Formulas were checked by recalculating in LibreOffice only, and no domain user has reviewed them yet. Leaving the Instructions sheet blank avoids false content, but it is not evidence of human authorship. Source citations below are leads to re-check at the named source, not established facts.

## What it is
An Excel workbook (it also opens in Google Sheets) for small landlords.
- **Tenancies:** up to 100. For each tenancy it calculates the deposit return due date (from a deadline the landlord enters), total deductions, refund due, days left, and a status of Active, Return pending or PAST DUE.
- **Condition:** a room-by-room checklist with move-in and move-out condition dropdowns, photo references, and a deduction amount and reason for each item. It comes pre-filled with 10 common rooms and items.

## Deliberately excluded
No state deposit law is built in. Return deadlines and allowed deductions vary by state and city, so the landlord enters their own deadline. Instructions must say this is not legal advice.

## Verified
All formulas were recalculated in LibreOffice. In the example, a $1,500 deposit with move-out on 2026-10-31 and a 30-day deadline is due back by 2026-11-30. A $180 wall-damage deduction leaves a $1,320 refund. The status shows "Return pending", and the days-left count follows today's date.

## Needs Cash: required before any listing
- [ ] Write the Instructions sheet in your own words, including the "not legal advice" note.
- [ ] Approve the look.

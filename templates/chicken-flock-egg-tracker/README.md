# Backyard flock & egg tracker: draft

**Status:** draft for review. Not for sale. Nothing is listed or launched.

## What it is
An Excel workbook (it also opens in Google Sheets) for backyard and homestead chicken keepers. It tracks:
- each bird's breed, hatch date, laying status and age
- daily egg counts, with cracked eggs subtracted
- expenses by category: feed, bedding, health, equipment, birds, other

It turns these into a 24-month summary showing eggs, dozens, feed cost, total cost, **cost per dozen**, egg value and value minus expenses.

This niche has the most purchase evidence of the livestock options checked: the top chicken tracker listing has 14 item reviews (hand-verified by Instinct).

## Sheets
- **Instructions:** blank on purpose. The seller writes it, per Etsy's Oct 22, 2026 policy.
- **Settings:** egg value per dozen.
- **Flock:** up to 100 birds, with a status dropdown and an automatic count of hens laying.
- **Egg Log:** 1,000 rows of daily counts.
- **Expenses:** 500 rows, with a category dropdown.
- **Egg Sales:** dozens sold and price per dozen.
- **Health:** vaccinations, illness, injury and deaths.
- **Monthly Summary:** 24 months, starting from the month you set in O1.

## Verified
All formulas were recalculated in LibreOffice. With the example inputs (7 eggs collected, 1 cracked, $33.48 spent), November shows 6 good eggs, 0.5 dozen, $66.96 per dozen and -$30.98 value minus expenses. The examples are placeholders, not real data.

## Domain validation against an extension-service record (research only)
Compared with the [University of Vermont 4-H Poultry Layer Record](https://www.uvm.edu/d10-files/documents/2024-08/poultry-layer-record.pdf):

| UVM field | This tracker |
| --- | --- |
| Daily egg counts and monthly totals | Covered (Egg Log, Monthly Summary) |
| Feed type, pounds fed and cost | **Added** a Feed (lb) column to Expenses and the summary |
| Bedding and other expenses | Covered |
| Health and vaccination: date, condition, treatment, cost | **Added** a Health sheet |
| Mortality | **Added** a "Death" event in Health, with a count |
| Eggs sold (dozens) × price, and profit or loss | **Added** an Egg Sales sheet; the summary now shows dozens sold, sales income, and sales minus expenses |
| Breed, source, start and end inventory | Partly covered: the Flock sheet has breed and status, but no source field |

UVM doesn't compute cost per dozen. This tracker does, which is its distinct value. Recalculated in LibreOffice after these changes. A chicken keeper's review is still needed.

## Needs Cash: required before any listing
- [ ] Have someone who keeps chickens confirm the tracker covers what they actually log. This is a gap: Cash's expertise is pottery, not poultry.
- [ ] Write the Instructions sheet in your own words.
- [ ] Approve the look.

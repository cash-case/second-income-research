# Craft fair inventory & sales log: draft

**Status:** draft for review. Not for sale. Nothing is listed or launched.

## What it is
An Excel workbook (it also opens in Google Sheets) for potters and makers who sell at markets. It tracks:
- a product list with unit cost and price
- every sale, logged by event, SKU, quantity and payment method, with optional price overrides
- card-reader fees

It calculates, automatically:
- stock remaining and revenue for each product
- profit for each event, after booth fee, travel, other costs, cost of goods and card fees

## Verified
All formulas were recalculated in LibreOffice. Example inputs: 2 mugs sold at $32 by card and 1 bowl discounted to $50 in cash, at a market with a $75 booth fee, $20 travel and $10 other costs. That gives $114 revenue, $31 cost of goods, $2.01 card fees and -$24.01 profit. Remaining stock comes out at 22 mugs and 9 bowls.

## Checked against a published method

Source: The Craft Map, craft fair inventory checklist (https://www.thecraftmap.com/blog/craft-fair-inventory-checklist-template).

| Their recommendation | This template |
|---|---|
| Per-product name/SKU and price | Products sheet |
| Packed, sold and left counts per show | Event Packing sheet (added) |
| Reconcile packed − left against sales | Event Packing: "Sold by count" vs "Sold in Sales log", flags CHECK on mismatch (added) |
| Restock flag | Event Packing "Restock?" column (added) |
| Show header: name, date, booth fee, starting cash | Events sheet; starting cash column added |
| Revenue per item and profit per show | Products revenue; Events profit after COGS, card fees, booth, travel |
| (Not in source) payment method and card fees | Sales sheet: extra beyond the source |

Verified by recalculating in LibreOffice: example rows reconcile (12 packed − 10 left = 2 sold = 2 logged, OK).

## Needs Cash: required before any listing
- [ ] Check it against how you actually run a market day, and change anything that doesn't fit.
- [ ] Write the Instructions sheet in your own words.
- [ ] Approve the look.

# Pottery pricing & cost calculator: pilot draft

**Status:** draft for review. Not for sale and not customer-ready. Nothing is listed or launched.

**Provenance:** built by an AI tool (Claude). Formulas were checked by recalculating in LibreOffice only, and no domain user has reviewed them yet. Leaving the Instructions sheet blank avoids false content, but it is not evidence of human authorship. Source citations below are leads to re-check at the named source, not established facts.

## What it is
An Excel workbook (it also opens in Google Sheets) that works out a potter's true cost per piece and suggests wholesale and retail prices. Costs covered:
- clay
- glaze
- kiln electricity
- labor
- packaging
- studio overhead

It also shows what the seller keeps after Etsy fees.

## Sheets
- **Instructions:** left blank on purpose for the seller to write. Etsy's Oct 22, 2026 policy requires buyer-facing instructions to be the seller's own work.
- **Settings:** labor rate, electricity rate, kiln energy per load, pieces per load, overhead, price multipliers, Etsy fees.
- **Materials:** clay bodies and glazes, converted to cost per lb and cost per gram.
- **Pricing:** up to 50 pieces, with dropdowns for clay and glaze. Calculates cost, wholesale, retail and Etsy take-home.

## Verified
Every formula was recalculated in LibreOffice. The example mug comes to $27.49 total cost, $54.97 wholesale and $109.94 retail, with $71.56 kept after Etsy fees. Those results come from the example inputs, not real data.

## Domain validation against published methods (research only)
| Check | Source | Result |
| --- | --- | --- |
| Cost build-up: materials + labor + overhead, wholesale = cost x 2, retail = wholesale x 2 | [Ceramic Arts Network, "Pricing Artwork"](https://ceramicartsnetwork.org/pottery-making-illustrated/pottery-making-illustrated-article/In-the-Studio-Pricing-Artwork) | **Matches.** Both multipliers are editable. |
| Kiln electricity: kW x hours x rate x duty cycle (about 50%), plus optional kiln wear (example: about $5 per load) | [Big Ceramic Store, tip 16](https://bigceramicstore.com/info/ceramics/tips/tip16_calc_costs.html) | **Changed to match.** The first draft asked for kWh per load, which most potters don't know. It now takes the kiln's nameplate kW, firing hours, duty cycle and wear per firing. |
| Shipping priced separately | Ceramic Arts Network (same article) | **Matches.** Shipping isn't in the cost. To add: an instructions note saying so. |
| Labor is not profit | Ceramic Arts Network (same article) | **Gap.** Profit comes only from the multipliers. Possible addition: an optional profit-margin line. |
| Implied hourly wage check (price / labor hours) | Ceramic Arts Network (same article) | **Gap.** Possible addition: an "effective hourly rate" column. |

Still needed: review by a working potter, to check that the assumptions match real studio practice.

## Needs Cash: required human involvement before any listing
- [ ] Check that the cost model matches how a real potter prices work, and change it if not.
- [ ] Replace the example inputs with realistic defaults.
- [ ] Write the Instructions sheet in your own words.
- [ ] Approve the look, or ask for changes.

## Not done yet
- Listing copy, tags and preview screenshots. These come after Cash's review.
- Google Sheets copy-link version.

# Non-Etsy channels for the six template drafts (Claude, Nov 6 2026)

This is research only. No accounts were created and nothing has been listed. Labels: [V] verified on the official page, [S] seller or third-party claim, [A] assumption, [T] test to run.

## The core question: who brings the buyer?

| Channel | Fee | Does the channel bring buyers? | Hands-off once live? |
|---|---|---|---|
| Payhip, free plan | 5% per sale, $0/month [V payhip.com/payhip-vs-gumroad]; card processing on top [A] | Very little. It's a checkout and storefront, so traffic has to come from somewhere else [A]. Competing pottery and chicken products are already there [V payhip.com/b/AB3vM, payhip.com/b/7iUuS] | Delivery is automatic, but traffic is not |
| Gumroad | 10% + $0.50 per sale, processing excluded [V gumroad.com/help/article/66]; Discover sales cost more (30% was reported earlier) [S] | Only through Discover, which is crowded with creator products [A] | Delivery is automatic, but traffic is not |
| Amazon KDP, printed low-content log books | No upfront cost [A, to confirm at signup]. Royalty = 60% × list price − print cost at list price $9.99 or above [V kdp G201834330] | Yes. Amazon search is the buyer traffic. This is the only option here, besides Etsy, with built-in buyers | Mostly yes. Amazon prints, ships and handles customer service [V KDP model] |

My takeaway: Payhip and Gumroad don't solve the traffic problem, so they're second checkouts, not new demand. KDP is the one real non-Etsy channel with buyers already searching.

## KDP numbers [V]

- Print cost: a black-ink paperback of 24–110 pages costs a flat $2.30, or $2.84 for large trim such as 8.5×11 [V kdp G201834340].
- Example: an 8.5×11, 100-page "Glaze test & kiln log" at $9.99 earns 0.60 × 9.99 − 2.84 = **$3.15 per copy** before tax. This is royalty, not profit.
- Low-content rules [V kdp GGE5T76TWKA85DJM]: no ISBN required, no free KDP ISBN, no Expanded Distribution, no series, the "Low-content" category box must be ticked, and no limit on title count is stated.
- AI rules [V kdp G200672390]: AI-generated content must be disclosed, even if edited afterward. AI-assisted content doesn't need disclosure.

## Paid demand and competition

- Pottery logs: "Keep Calm and Glaze On / Open The Kiln: Pottery Project Book, 80 project sheets" is in wide retail distribution, and a Lulu "Kiln Firing Log" also exists [V search results]. Demand is real but the niche is already served [A].
- Chicken logs: there are many titles, for example "Chicken Record Keeping Log Book" (ISBN 9781953557186). Miller Mfg / Little Giant even sells a physical "Backyard Poultry Egg Log" through farm-supply channels [V search results]. Buyers pay, but the niche is crowded [A].
- I have no sales counts for any of these. Amazon BSR (Best Sellers Rank) has to be read by hand on each product page [T].

## Failure cases

- Low-content KDP is heavily saturated, and new titles with no reviews can sit unseen [A].
- $3.15 per copy means $5k/month needs roughly 1,600 copies a month. **KDP alone does not reach the goal.** It's an add-on [A].
- AI-designed interiors need disclosure. A pottery log designed from the validated template structure, with Cash reviewing it, is the cleaner path [A].

## What AI can do vs what needs Cash

- **AI:** interior PDF layout from the validated templates, cover drafts, keyword research, and a royalty calculator.
- **Needs Cash:** creating the KDP account, the tax interview and bank details (Cash enters these himself, never in chat or the repo), approving each title and cover, and deciding on AI disclosure.

## Cheap validation test [T]

With no account, read BSR by hand on 5 pottery logs and 5 chicken logs. A BSR under about 300,000 in Books suggests regular sales [A, rule of thumb, not verified]. If at least 3 of 10 clear that bar, a KDP pottery log is worth asking Cash about. Instinct or Cash can do this by hand in about 15 minutes.

## For Instinct

Please ask Cash this directly and quote his answer back: "Do you want Claude to draft a printed pottery glaze/kiln log book for Amazon KDP? Drafting costs nothing, but publishing needs your own KDP account, tax interview and approval." Until Cash answers, I'll only draft the interior layout on the PR #3 branch, and nothing gets published.

## Addendum: affiliate and B2B first pass (Nov 6, about 08:30Z)

| Idea | Paid-demand evidence | Screen result |
|---|---|---|
| Kiln/wheel affiliate, using Cash's pottery audience | No public US kiln-retailer program found. Kiln Crafts UK on Awin: rate on request, 30-day cookie [V ui.awin.com/merchant-profile/117821]. Best Ceramics on Awin: 15%, tableware only [V ui.awin.com/advertiser-terms/116501] | Add-on only. Kill as an engine unless a US pottery-supply program pays 5% or more |
| Pottery-class directory (one student is worth $200+ to a studio vs a ~$20/month fee, so it passes Hark's criterion 2 [A]) | Existing directories are free and ad-supported: potterystudios.pages.dev (302 listings, AdSense), find-a-pottery-class.pages.dev (no price shown) [V], plus The Ceramic Shop's studio directory | **Fails criterion 1**: no visible paid placement. Clone-style sites point to scaled-content risk |
| Pottery studio management software | Several products in the field: Kiln Fire, WheelOwl, Kilnfox, MudBuddy, 24hr Pottery [V search listings] | Studios do pay for software, but building SaaS is neither low-cost nor hands-off. Killed |
| Food-safety / HACCP log templates | Plenty of free versions (SafetyCulture public library, many free PDFs) [V search] | Free substitutes are everywhere. Killed |
| Airbnb welcome-book templates | Sold on Etsy, Gumroad, Payhip and Creative Market, plus Fiverr services [V search] | Paid demand is real but saturated. Killed for a new entrant |

## Screen: marketplaces that own customer service end to end (Nov 6, about 08:30Z)

Columns follow Instinct's spec. Every candidate assumes a catalog of many small titles, where income scales with titles rather than Cash's hours.

| Platform | (1) Account owner and Cash-only one-time steps | (2) AI rules at owning source | (3) Evidence buyers search there | (4) Fee or royalty per sale | (5) Recurring work after N titles |
|---|---|---|---|---|---|
| **Amazon KDP, low-content paperbacks** | Cash: account, tax interview and bank details, entered by him only | AI-generated content must be disclosed, even if edited afterward; AI-assisted needs no disclosure [V kdp G200672390] | Amazon search. Many competing pottery and chicken log books exist [V], but sales volume is unmeasured [T: hand-check BSR] | 60% × list price − print cost at $9.99+; print is $2.84 flat for 24–110 pages at large trim [V kdp G201834330, G201834340]. That gives $3.15 at $9.99 [V terms, A arithmetic] | Near zero. Amazon prints, ships and handles customer service. The team monitors BSR and adjusts prices |
| **Adobe Stock, illustrations and vectors** | Cash: contributor account, tax form and payout details | Gen-AI allowed if the "Created using generative AI tools" box is ticked. No artist or real-person names in prompts. Near-duplicate variations count as spam [V helpx generative-ai-content] | Adobe's buyer search, but the supply is flooded: about half of all images are AI-generated [S petapixel 2025-05-22]. One contributor with 6,200 assets saw downloads fall from 50–60/week to 10–20/week [S community.adobe.com, Jan 2026] | 33% royalty, video 35%. Minimum $0.33–0.38 per download on large subscriptions [V helpx royalty-rates-assets] | Near zero for customer service, since Adobe licenses. Ongoing uploads are needed to stay visible [A] |
| **Redbubble** | Cash: account and payout details | Not yet read at source [T] | Redbubble's own marketplace search [A, unmeasured] | Default 10% markup on base price. Platform fee or excess-markup fee on non-Pro accounts, capped at $150 per period [V help.redbubble.com 202270799] | Fulfillment by partners [V]. Who handles customer service isn't stated on that page [T] |
| **Amazon Merch on Demand** | Cash: application or invite, tax, bank | Not yet read at source [T] | Amazon search [A] | From June 1 2026, tiers are based on the share of *external* traffic. Organic-only sellers drop to the "Creator" tier: about $2.44 on a $19.99 tee [S merchtitans.com, not Amazon's own page] | Near zero for customer service. **But the tier change rewards outside promotion, which is the opposite of hands-off** [A] |

### Read [A]
- Every one of these keeps Cash's recurring load near zero after one-time setup. That's the hands-off shape the brief needs.
- None shows evidence of $5k a month for a new entrant. Adobe Stock earns roughly $0.33–$1+ per download against a flooded supply. Merch now pays organic-only sellers less. KDP pays about $3.15 a copy.
- The honest combined picture is a catalog spread across 2–3 of these channels. That's a slow-build, small-but-durable income stream, not a $5k engine, unless BSR and download checks show more demand than we can see now.
- [T] The cheapest decisive test is still the KDP BSR hand-check on 10 log books, about 15 minutes, with no account needed.

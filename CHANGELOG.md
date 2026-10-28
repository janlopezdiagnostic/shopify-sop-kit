# Changelog

## 0.2.1 - 2026-10-28

Cold start for the planning module. The operator needs nothing prepared:
no measurements, no floor plan, no answers in advance.

- modules/back-of-house-planning.md: "Start cold" section. Rough inputs
  (paces, estimates, deliveries described in carts and boxes) are usable
  for a first draft, tagged as rough, and the tape walk converts them to
  measured facts before any purchase rests on them. A text-grid zone
  sketch convention, and default zone shares for a generic single-room
  back of house, all tagged [DEFAULT].
- skill/SKILL.md: the spatial section now states the cold-start rule.

## 0.2.0 - 2026-10-28

Module 4: back-of-house spatial planning. The kit now follows the
operator's work end to end: write the SOPs, then plan the room they run in.

- modules/back-of-house-planning.md: zone plan, flow rules, clearances
  (guidance labeled as guidance; exit routes sent to professional checks),
  capacity math with the work shown, and the number rule: every number
  tagged [MEASURED], [STATED], [GUIDANCE], or [DEFAULT]. A plan is a
  planning aid, never labeled compliant or safe.
- templates/layout-planning-worksheet.md: the plan's structure, including
  a professional-checks list and a decisions log.
- skill/interview.md: questions 22 to 29 for the planning interview.
- skill/SKILL.md: spatial planning outputs section; the test for a plan is
  physical (tape walk, path trace, peak dry run), not follow-it-cold.
- docs/grounding.md: planning sources and their limits.

## 0.1.1 - 2026-10-28

Audit fixes, same day. Found by a full re-read, mechanical checks, live
Help Center spot-checks, and a coworker dry run of the fulfillment module.

- Fixed invalid YAML frontmatter in skill/SKILL.md (an unquoted colon broke
  parsing; the description is now quoted).
- Fulfillment module: added the Shopify Shipping path (buying a label
  creates the fulfillment; do not also mark fulfilled; voiding as the
  rescue), the check ordering rule (all checks before the label is bought),
  read-back fallbacks where there is no scanner, a corrected label check,
  branch pruning by interview answers, and proposed defaults for design
  mode.
- Transfers module: rejected quantities are accounted for (they do not stay
  Incoming); the two supplier routes (PO-linked vs blank origin) are now
  distinguished.
- CSV module: the strip-columns rule is scoped to updates; new-product
  intake uses the full template. POS Pro caveat carried into receiving.
- START-HERE and prompt.md: the same four files everywhere; design mode
  turns an "I don't know" into a proposed default; Skill install notes the
  plan requirement.
- docs/grounding.md travels inside the core and Skill ZIPs now, so the
  modules' source citations resolve offline.
- scripts/check.py now also validates internal links.

## 0.1.0 - 2026-10-28

First working draft.

- PROBLEM.md: the operator's actual situation, from their own answers, and
  the five conditions an SOP must meet to count as useful.
- Core SOP Writer skill: interview first, never invent, [TO CONFIRM]
  markers, associate-first structure, follow-it-cold ending.
- Modules for fulfillment (wrong-item prevention), transfers and receiving
  (state machine, PO-linked receiving), and product intake by CSV
  (pre-flight checks, channel tags, release-for-sale checks).
- Templates: SOP template and follow-it-cold checklist.
- Grounding notes with sources, verification dates, and open unknowns.
- Examples folder deliberately empty until practitioner-tested material
  exists.

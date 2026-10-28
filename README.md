# Shopify SOP Kit

Plain-English instruction files that teach Claude to help a Shopify store
operator write SOPs an associate can actually follow: fulfilling orders from a
retail store, transferring and receiving inventory, and uploading products by
CSV from a vendor purchase order.

Start with [PROBLEM.md](PROBLEM.md). It describes the exact situation this kit
was built for, and why generic AI-written SOPs fail at it.

## Status

Version 0.1, working draft. Built from Shopify Help Center documentation
(verified October 2026, sources in [docs/grounding.md](docs/grounding.md)) and
one real operator's draft SOP and answers, genericized so no store, brand, or
person is identifiable. See [PRIVACY.md](PRIVACY.md).

**Practitioner gate:** this kit does not count as tested until the operator
runs each module on a real SOP, follows the draft cold, and the failures found
are fixed. Until then, treat every output as a draft.

## What is inside

- `skill/SKILL.md` - the core SOP Writer: interview first, never invent a
  step, mark unknowns, write for associates.
- `skill/interview.md` - the questions the writer must ask before drafting,
  per workflow.
- `modules/fulfillment.md` - order fulfillment from a retail store, built
  around preventing wrong-item shipments.
- `modules/inventory-transfers.md` - transfers and receiving as a state
  machine, including purchase-order receiving.
- `modules/product-upload-csv.md` - PO to CSV to Shopify PO to transfer to
  received stock, with the CSV pre-flight checks.
- `templates/` - the SOP template and the follow-it-cold test checklist.
- `examples/` - empty on purpose. Examples get written from the operator's
  corrected real outputs, not invented.

## Use it

See [START-HERE.md](START-HERE.md). Short version: upload the files to a
Claude Project, or paste the starter prompt, and answer the interview
questions in your own words.

Free under the MIT license. Feedback by GitHub Issues only.

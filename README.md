# Shopify SOP Kit

Plain-English instruction files that teach an AI assistant to help a
Shopify store operator write SOPs an associate can actually follow:
fulfilling orders from a retail store, transferring and receiving inventory,
and uploading products by CSV from a vendor purchase order.

Works with Claude, ChatGPT, Gemini, and any other assistant that can read
uploaded files or follow a pasted prompt. The files are plain markdown.
Nothing here is locked to one tool: see START-HERE.md for each tool's path,
or grab the ZIPs from the Releases page and skip the file picking entirely.

Start with [PROBLEM.md](PROBLEM.md). It describes the exact situation this kit
was built for, and why generic AI-written SOPs fail at it.

## Status

Version 0.2.1, working draft. Built from Shopify Help Center documentation
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
- `modules/back-of-house-planning.md` - planning the stockroom itself:
  zones, flow, clearances, capacity math with provenance tags, and a
  physical test (tape walk, path trace, peak dry run). Usable cold, with
  no measurements prepared: the interview runs as you go and rough inputs
  are tagged until the tape walk replaces them. A planning aid, not a
  floor-plan generator.
- `templates/` - the SOP template, the follow-it-cold test checklist, and
  the back-of-house layout planning worksheet.
- `prompt.md` - a self-contained starter prompt that carries the core rules
  on its own, for assistants where file upload is awkward.
- `docs/grounding.md` - sources, verification dates, and the open unknowns.
- `PRIVACY.md` - what never goes into this repo, and the scrub rule.
- `AGENTS.md` and `CLAUDE.md` - pointers for AI coding assistants working
  in this repo.
- `examples/` - empty on purpose. Examples get written from the operator's
  corrected real outputs, not invented.

## Use it

See [START-HERE.md](START-HERE.md). Short version: upload the four files
START-HERE names, paste the starter prompt from `prompt.md`, and answer the
interview questions in your own words. Or download a ZIP from the Releases
page: full kit, core upload set, or the Claude Skill bundle.

Free under the MIT license. Feedback by GitHub Issues only.

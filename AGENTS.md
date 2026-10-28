# For AI assistants working in this repo

This repo is the Shopify SOP Kit: plain-markdown instruction files that turn
an AI assistant into an interview-first SOP writer for Shopify store
operations. If you are an AI assistant pointed at this repo, read these
first, in order:

1. `PROBLEM.md` - the exact problem, and the conditions an SOP must meet.
2. `skill/SKILL.md` - the operating rules (interview first, Document mode vs
   Design mode, never invent, [TO CONFIRM] markers, associate copies carry
   no open markers).
3. The relevant file in `modules/` for platform facts, with its verified-on
   date.

Hard constraints for any work in this repo:

- Privacy: no store, brand, or person names; no real SKUs, prices, or order
  details; invented example data only, marked as invented. See PRIVACY.md.
- Platform facts must be sourced and dated (docs/grounding.md). If you
  cannot verify a Shopify claim, mark it, do not state it.
- No em dashes in any file.
- Examples stay empty until they come from practitioner-tested real outputs
  (examples/README.md).

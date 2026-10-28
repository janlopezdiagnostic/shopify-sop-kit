# The problem this kit exists to solve

This kit was built for one real situation. It is described here in full because a
solution that does not match the problem is just more AI slop.

## Who has the problem

An ecommerce lead at a retail brand that sells through Shopify and a physical
store. Part of the job is writing the standard operating procedures (SOPs) that
store associates use to do operational tasks. The three tasks that matter first:

1. Fulfilling a Shopify order from the retail store.
2. Transferring and receiving inventory in Shopify.
3. Uploading products into Shopify from a vendor purchase order, by CSV, and
   receiving that stock at the store.

## What is true today (from the operator's answers, paraphrased)

- **There is no established process.** Asked for the main challenge with
  the current process, the operator's answer was, in substance, that there
  is no process for creating these at all. Both readings hold: most of these
  SOPs do not exist, and there is no set way of creating them either. One
  working draft does exist, for product upload. The intake module in this
  kit was genericized from it. The other SOPs start from nothing.
- **The readers are associates, not managers.** The bar the operator set:
  an associate reads the SOP and can figure out how to do the task from it,
  unaided. That rules out summaries and anything that assumes the reader
  already knows the job.
- **The store fulfills its own orders.** The retail store, not a warehouse
  and not a 3PL, fulfills the orders placed with it.
- **The error the operator named is wrong-item shipment.** The SOPs exist
  largely to prevent the wrong product being shipped. (Our reasoning: a
  wrong item shipped means a return, a reshipment, and a customer problem.
  The checks exist because the operator named the error.)
- **Product intake is purchase-order driven.** A store manager orders from
  vendors. The ecommerce lead turns that PO into products in Shopify with a
  CSV, creates the Shopify purchase order, and generates the internal
  barcodes. When the shipment arrives, retail staff receive it against a
  transfer, count it, and apply barcode labels. A mistake early
  in that chain (wrong SKU, wrong price, wrong channel setting) surfaces
  later as wrong stock counts or products visible in a channel they were
  never meant for.
- **AI use at the workplace is unsettled, either way.** Nothing the operator
  shared establishes that AI tools are permitted or forbidden at work, and
  whether the store's Shopify can be connected to an AI assistant is
  unconfirmed. Nothing in this kit may depend on a live connection, or on
  any one AI tool.

## Why generic AI output does not solve this

Ask a chatbot to "write an SOP for fulfilling a Shopify order" and you get
fluent, confident, generic steps. For this reader and this store that fails:
it invents steps an associate cannot tell from real ones, it writes the
average store's process instead of this store's (no wrong-item checks, no
PO-driven intake, no channel rules), and its platform facts go stale, because
Shopify changed transfer, purchase-order, and variant behavior in 2025 and
2026 (docs/grounding.md). Worst, it produces a document nobody tests.

## What would actually solve it

An SOP is useful here only if all of these hold:

1. Every step is either a verified Shopify platform fact (sourced, dated) or
   a store fact the operator supplied or approved. Nothing is filled in to
   sound complete.
2. Where no process exists yet, the kit may propose a default, labeled as a
   proposal, for the operator to approve or edit step by step. A proposal is
   never presented as "how the store does it."
3. Missing store facts are asked, not guessed, and stay visibly marked in the
   working draft until the operator answers. The copy handed to associates
   has no open markers in its steps.
4. The output is written for an associate standing in the store: short steps,
   one action per step, checks where errors actually happen.
5. Each SOP gets tested: someone who did not write it follows it on a real
   task, and what breaks gets fixed before it counts as done.

## The next job (why this kit grows)

The same operator's work does not stop at SOPs. The next task is spatially
planning the store's back of house: receiving, staging, storage, and the
pack station. It is the same underlying problem in a new form. The plan has
to come from the operator's real room, real deliveries, and real pain
points, or it is generic advice with measurements attached. So the kit
grows by module, on the same rules: interview first, sourced facts kept
separate from store facts, proposals labeled, and a physical test (tape
walk, path trace, peak dry run) before the plan counts as final. See
modules/back-of-house-planning.md.

## Non-goals

- Not a general ecommerce course, and not a replacement for Shopify's own
  documentation.
- Not an automation tool. This kit never writes to a live store.
- Not finished. Version 0.1 is a working draft until the operator has
  test-run each module on a real task (see the practitioner gate in README).

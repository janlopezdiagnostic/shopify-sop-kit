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

## What is true today (from the operator, in his words where quoted)

- **There is no established process.** Asked for his main challenge with the
  current process, he answered: "There is no process creating it." Read both
  ways, both are true here: most of these SOPs do not exist, and there is no
  set way of creating them either. One working draft does exist, for product
  upload (his version 0.3, not yet approved). It is the seed the intake module
  in this kit was genericized from. The other SOPs start from nothing.
- **The readers are associates, not managers.** His bar: "Associates are
  reading the SOPs (someone should be able to read them and figure out how to
  do the task)." That rules out summaries and anything that assumes the reader
  already knows the job.
- **The store fulfills its own orders.** "Our retail store will fulfill the
  orders." Not a warehouse, not a 3PL workflow.
- **The error he named is wrong-item shipment.** "It needs to prevent wrong
  product being shipped." (Our reasoning, not his words: a wrong item shipped
  means a return, a reshipment, and a customer problem. The checks exist
  because he named the error.)
- **Product intake is purchase-order driven.** A store manager orders from
  vendors. The ecommerce lead turns that PO into products in Shopify with a
  CSV, creates the Shopify purchase order, and generates the internal
  barcodes. When the shipment arrives, retail staff receive it against a
  transfer, count it, and apply barcode labels and hang tags. A mistake early
  in that chain (wrong SKU, wrong price, wrong channel setting) surfaces
  later as wrong stock counts or products visible in a channel they were
  never meant for.
- **AI is not prohibited, and not set up.** His words: "They never said don't
  use Claude." Whether his store's Shopify can be connected to Claude is
  unconfirmed, so nothing in this kit may depend on a live connection.

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

## Non-goals

- Not a general ecommerce course, and not a replacement for Shopify's own
  documentation.
- Not an automation tool. This kit never writes to a live store.
- Not finished. Version 0.1 is a working draft until the operator has
  test-run each module on a real task (see the practitioner gate in README).

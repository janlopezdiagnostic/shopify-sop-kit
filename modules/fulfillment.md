# Module: fulfilling an order from a retail store

Verified against Shopify Help Center, October 27, 2026.
Sources: docs/grounding.md. Store facts below come from the operator this kit
was built for. Anything else about a store must come from the interview.

## The store reality this module assumes

- The retail store fulfills its own orders. No warehouse, no 3PL.
- The readers and doers are store associates.
- The costliest mistake is shipping the wrong product. Every check in this
  module exists to prevent that.

If a different store does not match this, the interview answers override this
section. Do not quietly blend the two.

## Platform facts (use as the skeleton, confirm the branches)

- Fulfillment mode is set in Settings, then General, then "Order processing".
  Manual is the default; automatic and partial modes exist. Older guides that
  point to Checkout settings are stale.
- Manual flow: open the order, in the "Unfulfilled" or "In progress" section
  choose "Mark as fulfilled", add tracking and carrier if the label was not
  bought in Shopify, and choose whether the customer gets a notification.
- A 3PL or fulfillment service is a different branch: use "Request
  fulfillment"; the store does not mark those orders fulfilled itself. Custom
  email fulfillment services are emailed when the order is marked fulfilled.
  Neither applies to this store today, but the interview must confirm that,
  because the steps diverge completely.
- Holds block fulfillment until released, and some holds are placed
  automatically (for example by checkout or market apps). An SOP must tell the
  associate what a held order looks like and what to do: nothing, until the
  hold clears or a manager releases it.
- An order can be fulfilled in parts (partial fulfillment), and split across
  locations. Each fulfillment can trigger its own customer notification,
  depending on the notification choice made when fulfilling. The mobile app
  cannot split or merge fulfillments.

## The checks that prevent wrong-item shipments

These checks are this kit's designed safeguards, proposed for the operator
to approve or replace in design mode. They are not a description of a
process the store already runs. Place them in the SOP as explicit steps:

1. **Pick by identifier, not by eye.** Pick from the order's SKU or barcode,
   and scan or read back the item code before leaving the shelf. Two products
   that look alike are the normal failure, not a rare one.
2. **Variant check at the pick.** Scan the item, then compare the variant on
   the item's label (size, color) against the order line. Similar variants
   are where wrong-item shipments come from.
3. **Barcode problem means stop.** If an item will not scan, or the scan
   does not match the order line, do not hand-key a guess and do not swap in
   a lookalike. Set the item aside and escalate. A bad barcode is usually an
   intake error, and shipping past it spreads it.
4. **Second check at the pack.** Before anything is sealed, compare every
   item in the box against the order lines one more time. This is the last
   cheap moment to catch an error.
5. **Label check.** After the label prints, match the name and order number
   on the label to the order on screen before it goes on the box. A correct
   box with the wrong label is still the wrong shipment.

## Branches the SOP must cover

- Item out of stock at this location after the order routed here, including
  the shelf race: the last unit was sold in the store between routing and
  picking.
- The order is for local pickup, not shipping (different completion step,
  different customer notification).
- The order routed to the wrong location.
- Part of the order available, part not (partial fulfillment, and what the
  customer is told).
- Order on hold.
- Damaged item found at pick or pack.
- Address problem flagged by Shopify or the carrier.
- What the associate does when any of these happens: who decides, who
  contacts the customer, and what is never the associate's call alone.

Each branch's store-specific answers come from the interview. If an answer is
missing, the branch goes in as [TO CONFIRM], never as invented procedure.

## Verified-on

Platform facts verified October 27, 2026. Shopify changes this surface
often. Re-verify against the Help Center before relying on this module after
April 2027.

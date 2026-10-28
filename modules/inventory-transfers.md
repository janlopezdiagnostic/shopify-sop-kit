# Module: inventory transfers and receiving

Verified against Shopify Help Center, October 27, 2026.
Sources: docs/grounding.md.

## Why this module is a state machine, not a list of steps

A transfer is not one action. It is stock moving through states, and each
action the associate takes has a different, specific effect on the numbers.
An SOP that says "transfer the items and receive them" without the states is
how inventory counts quietly rot. Receiving supplier stock is now done on a
transfer linked to the purchase order (Shopify moved supplier
receiving onto transfers in 2026; see docs/grounding.md), so older
instructions that say "receive the PO" are stale.

## The states (Shopify's own definitions)

- **On hand** = Committed + Unavailable + Available. The total physically
  there.
- **Available** = sellable now. Incoming stock is not in Available until it
  is received.
- **Committed** = promised: unfulfilled orders, draft-order reserves, and
  transfers marked "Ready to ship".
- **Incoming** = on its way, not sellable yet.

## The transfer lifecycle (inter-location)

1. **Create** in admin: Products, then Transfers, then "Create transfer".
   Choose origin and destination. A blank origin means an external or
   supplier source. Add products by search or barcode scan, with quantities.
2. **Draft.** Saving creates a Draft. Nothing is committed. Everything is
   still editable. Origin and destination lock once processing starts.
3. **Ready to ship** (optional) commits the stock at the origin.
   **In transit** moves it to "In progress": the stock becomes Incoming at
   the destination, and a shipment is created automatically. A transfer can
   have several shipments, each with its own ID and tracking, received
   separately.
4. **Receive** at the destination, per item:
   - **Accept** makes the quantity Available at the destination. If the
     product is not stocked there yet, the receiver chooses whether to stock
     and fulfill from that location or not now.
   - **Reject** records the rejection and changes **no quantities at all**.
     The rejected quantity is then accounted for: it does not stay Incoming
     and needs no second action. Rejected items do not go back
     automatically. The SOP must say what physically happens to them, from
     the interview.
   - **Cancel** is for stock that never shipped. On an inter-location
     transfer the quantity returns to Available at the origin. On a supplier
     transfer it simply removes the expectation.
5. **Partial receiving** leaves the transfer In progress until the rest
   arrives or is resolved.

## Supplier receiving (purchase orders)

- The purchase order is the commercial agreement. The **linked transfer** is
  the receiving document. One linked transfer at a time per PO.
- Two supplier routes exist. Use the PO-linked transfer whenever a purchase
  order exists. A manual transfer with a blank origin is for supplier stock
  that is not tied to a purchase order.
- Receive against the transfer in admin or in POS, counting against the PO
  quantities.
- This is the flow the product intake SOP uses: see
  modules/product-upload-csv.md, section D and E.

## Hazards the SOP must guard

- Entering or scanning a quantity greater than Available at the origin can
  push the origin location negative. The SOP needs a stop-and-check step
  before confirming any transfer quantity that exceeds what the shelf shows.
- Rule for the SOP, stated plainly: count first, then Accept. The receiving
  count against the PO or packing document is a check step, not a courtesy.
- Transfers are created in admin only. POS can fulfill and receive them, and
  only at POS Pro locations. POS cannot buy or print transfer shipping
  labels.

## Interview branches

Movement types (own locations, supplier, both), who creates vs who receives,
the counting document, mismatch handling (short, over, damaged), and whether
POS is involved. Answers come from skill/interview.md, questions 12 to 16.
Anything unanswered stays [TO CONFIRM].

## Verified-on

Platform facts verified October 27, 2026. Re-verify before relying on this
module after April 2027.

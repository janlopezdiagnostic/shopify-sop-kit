# Grounding: sources, dates, and open unknowns

## Platform sources (Shopify Help Center unless noted)

All opened and verified October 27, 2026.

- Order processing settings and fulfillment modes:
  help.shopify.com/en/manual/checkout-settings/order-processing
  (The setting itself now lives under Settings, then General, then "Order
  processing"; the Help Center URL keeps its legacy checkout-settings slug.)
- Fulfilling orders, bulk fulfillment, custom and app fulfillment services:
  help.shopify.com/en/manual/fulfillment/fulfilling-orders/
- Shopify Shipping labels, including voiding a label from the Fulfilled
  section (which confirms that buying a label creates the fulfillment):
  help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels/managing-labels/voiding-labels
- Split fulfillment behavior: shopify.dev, split fulfillment orders.
- Inventory states (on hand, available, committed, incoming):
  help.shopify.com/en/manual/inventory-and-locations/fundamentals/inventory-states
- Creating and processing transfers:
  help.shopify.com/en/manual/inventory-and-locations/inventory-transfers/creating-and-processing-transfers
- Receiving and managing transfers:
  help.shopify.com/en/manual/inventory-and-locations/inventory-transfers/receiving-and-managing-transfers
- POS transfer fulfilling and receiving (POS Pro):
  help.shopify.com/en/manual/sell-in-person/shopify-pos/inventory-management/fulfilling-and-receiving-transfers
- Purchase orders create linked transfers for receiving:
  help.shopify.com/en/manual/inventory-and-locations/purchase-orders/creating-inventory-transfers
- Importing products and CSV rules and hazards:
  help.shopify.com/en/manual/products/import-export/import-products and
  help.shopify.com/en/manual/products/import-export/using-csv

## Recent platform changes

Recorded from the same verification pass. The modules rely on the
purchase-order change directly; the rest are recorded so nobody
reintroduces stale facts from older guides.

- Variant limit is 2,048 per product (was 100), since October 2025. Max 3
  options still applies.
- Purchase orders create a linked transfer for receiving (June 2026; the
  exact announcement date is contested between sources, the mechanism is
  Help Center verified). Receiving happens on the transfer, not the PO.
- Stocky is discontinued as of August 31, 2026. No module may reference it
  as a live tool.
- Products have an Unlisted status alongside Draft, Active, and Archived.

## Back of house planning sources (researched October 28, 2026)

- Zone and flow practice (receiving at the entry, staging next to
  receiving, pick face on the route to the floor, quarantine separate from
  sellable stock, aisles sized for the busiest cart): retail stockroom
  layout guides (Direct Shop Fittings stockroom layout guide; Rackline
  back-of-house storage guide). Trade guidance, not standards.
- Exit routes: OSHA 29 CFR 1910.36(g)(2) (exit access at least 28 inches
  wide at all points; width also sized to occupant load) and 1910.37(a)(3)
  (exit routes free and unobstructed, no temporary storage). Regulation
  text read at osha.gov, October 28, 2026. Local fire code may require
  more; the module sends all exit-route questions to a professional check.
- Materials handling: OSHA 29 CFR 1910.176 (safe clearances for the
  equipment in use, permanent aisles marked, storage stable and secure).
  OSHA sets no general aisle width; the 36 inch foot-only and 48 to 60
  inch push-cart figures in the module are published planning guidance
  (Wolverine Building Group mezzanine floor plan guide; retrieved
  October 28, 2026), labeled [GUIDANCE], not code.

## Store facts (from the operator, genericized)

- Most SOPs do not exist yet; one product-upload draft does. The work
  is creating them, not fixing them.
- Readers and doers are store associates. A good SOP is followable cold.
- The retail store fulfills its own orders.
- Costliest named error: shipping the wrong product.
- Product intake is PO-driven, CSV-based, received at the store, with
  channel classification by tags (labels, not controls).
- AI use at the workplace is unsettled either way. Whether an AI
  assistant can connect to the store's Shopify is unconfirmed.

## Open unknowns (never guess these)

- Label source for outbound orders (Shopify Shipping or carrier accounts).
- Location count, and whether transfers run between locations, from
  suppliers, or both beyond the PO intake flow.
- The store's SKU and barcode scheme and its owner.
- Mismatch approval procedure at receiving.
- Whether AI projects, skills, or a Shopify connection are permitted and
  enabled on the operator's work accounts.
- Any claimed "batch fulfillment" limit: a single secondary source mentioned
  one; no primary confirmation was found, so no module states one.

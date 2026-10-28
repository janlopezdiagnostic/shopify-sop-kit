# Grounding: sources, dates, and open unknowns

## Platform sources (Shopify Help Center unless noted)

All opened and verified October 27, 2026.

- Order processing settings and fulfillment modes:
  help.shopify.com/en/manual/checkout-settings/order-processing
  (The setting itself now lives under Settings, then General, then "Order
  processing"; the Help Center URL keeps its legacy checkout-settings slug.)
- Fulfilling orders, bulk fulfillment, custom and app fulfillment services:
  help.shopify.com/en/manual/fulfillment/fulfilling-orders/
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

## Recent platform changes baked into the modules

- Variant limit is 2,048 per product (was 100), since October 2025. Max 3
  options still applies.
- Purchase orders create a linked transfer for receiving (June 2026; the
  exact announcement date is contested between sources, the mechanism is
  Help Center verified). Receiving happens on the transfer, not the PO.
- Stocky is discontinued as of August 31, 2026. No module may reference it
  as a live tool.
- Products have an Unlisted status alongside Draft, Active, and Archived.

## Store facts (from the operator, genericized)

- No SOPs exist yet. The work is creating them, not fixing them.
- Readers and doers are store associates. A good SOP is followable cold.
- The retail store fulfills its own orders.
- Costliest named error: shipping the wrong product.
- Product intake is PO-driven, CSV-based, received at the store, with
  channel classification by tags (labels, not controls).
- Claude use has not been forbidden. A Shopify connector connection is
  unconfirmed.

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

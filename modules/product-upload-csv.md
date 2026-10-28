# Module: product intake, CSV upload, and receiving

Verified against Shopify Help Center, October 27, 2026.
Sources: docs/grounding.md.

This module encodes one real store workflow, genericized: products start as a
vendor purchase order, become products in Shopify through a CSV import, get a
Shopify purchase order, and are received at the store against a transfer
before they can be sold. Roles are generic: store manager, ecommerce lead,
retail associates.

## A. Purchase order and handoff

1. The store manager places the vendor order and records it in the store's
   PO document, including the intended sales channel per product.
2. The manager hands the completed PO to the ecommerce lead. The PO is the
   source of truth for product details, ordered quantities, retail prices,
   and wholesale costs.
3. Missing information, and any price or quantity change, goes back to the
   manager for confirmation before upload. Never guess a price or a SKU.

## B. Prepare the CSV

1. Start from the store's CSV template. One row per product or variant.
2. Populate from the PO: handle, title, description, vendor, product
   category and type, variant SKU, price, cost per item, variants, and the
   agreed tags. Type is what the product is (for example: apparel, footwear, home goods);
   it drives reporting, so it is not optional decoration.
3. New products stay **Draft** and unpublished while setup is checked.
   Unreceived inventory is never made sellable.
4. Leave the CSV's inventory quantity columns out of the intake file (or at
   zero). Stock enters Shopify only through receiving on the transfer
   (section E). Quantities set at import and then received again count the
   same units twice.
4. Internal barcodes: the ecommerce lead generates and assigns them.
   [TO CONFIRM: the store's SKU and barcode scheme, and who owns changes.]

### Channel tags are labels, not controls

Many stores classify channel with tags meaning store only, online only, or
both, plus a tag identifying the purchase order. Tags classify. They do not
publish, unpublish, or allocate stock. The SOP must check the actual
location availability and sales-channel publishing separately, every time.
[TO CONFIRM: the store's current tag names and scheme.]

## C. Import, with the pre-flight that prevents CSV damage

CSV import is the destructive step in this workflow. Verified hazards:

- Products match by **handle only**. A wrong handle updates or duplicates
  the wrong product.
- **Overwrite is opt-in and literal.** A column included with a blank value
  erases the existing value. A column left out entirely is preserved.
  Including a SKU without the option name and value columns can delete the
  variant option.
- 15 MB maximum file size, UTF-8, headers must match the template exactly,
  including case and stray spaces.
- A started import cannot be canceled, and there is no undo.

Pre-flight, every time:

1. Export a backup of the current products first.
2. Strip the file to only the columns this upload is changing.
3. Test the import with one product before running the batch.
4. Check the filename, the preview row, and the product count in the import
   dialog before confirming.

Import: Products, then "Import", add the file, review, then "Import
products". A confirmation email follows. If an error appears, read it first,
then check the CSV for missing required fields, header mismatches, and stray
spaces before retrying.

After import: spot-check the imported products at the top of the product
list. SKU, price, cost, tags, and inventory settings must match the PO.

## D. Create the Shopify purchase order

Products must exist in Shopify before a PO can link to them, which is why
the CSV comes first.

1. Products, then "Purchase orders", create new.
2. Select the supplier (create it from the vendor details if needed) and the
   destination location that will receive.
3. Add the products from the PO, by search or by the PO tag. Save, then
   "Mark as ordered".
4. When the shipment is en route, create the linked transfer from the PO and
   move it to in transit. Receiving happens on the transfer, per
   modules/inventory-transfers.md.

## E. Receiving and release for sale

1. When the shipment arrives, receive items on the transfer, entering counted
   quantities and choosing Accept per item.
2. Count against the PO. Short, over, or damaged quantities follow the
   store's mismatch procedure. [TO CONFIRM: who approves a mismatch and how
   it is recorded.]
3. Print and apply barcode labels. Then verify the labels:
   scan each printed barcode once and confirm it pulls up the right product
   and variant. A mislabeled item here becomes a wrong-item shipment later.
4. **Release-for-sale checks, all four, before stock becomes available:**
   - Received quantity matches the PO.
   - Price, SKU, barcode, and variant match the physical item.
   - No damaged or missing units are available for sale.
   - Product status, POS availability, and online availability match the
     intended channel.
5. Only then set the product Active and publish it to its intended channel.

## Verified-on

Platform facts verified October 27, 2026. Re-verify before relying on this
module after April 2027.

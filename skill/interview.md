# The interview

Ask these before drafting, one topic at a time, in the operator's own words.
Short answers are fine. An "I don't know" becomes a [TO CONFIRM] marker, not
a guess. Skip a topic only when the module does not need it for this SOP.
Ask question 1 first. It decides the mode (see SKILL.md): if no process
exists yet, stop interviewing for recall and switch to proposing defaults
for approval, using the remaining questions as the approval checklist.
Questions 2 to 6 are asked in both modes; they define the design.

## Always

1. Does a process for this task exist today, even an unwritten one? Or are
   we designing it from scratch?
2. Who does this task, and who is the SOP written for? (Role names only.)
3. What triggers the task? What does the associate see when it starts?
4. What does done and correct look like? How would anyone check afterwards?
5. What is the costliest mistake in this task, and has it actually happened?
6. What are the known exceptions: the times the standard path does not apply?

## Fulfilling an order (see modules/fulfillment.md)

7. Which orders does your location fulfill: online orders routed to the
   store, in-store purchases, local pickup, or a mix?
8. Where do labels come from: bought in Shopify, carrier accounts, or
   printed another way?
9. What does the associate check before the box is sealed, and how: visual,
   barcode scan, a second person?
10. How are partial orders, out-of-stock items, and held orders handled?
11. Who gets told, and how, when something cannot ship as ordered?

## Transfers and receiving (see modules/inventory-transfers.md)

12. Which movements exist: between your own locations, receiving from
    suppliers against purchase orders, or both?
13. Who creates the transfer, who ships, who receives? Same person or not?
14. Are quantities counted at receiving against a document? Which one?
15. What happens when the count does not match: short, over, damaged?
16. Is Shopify POS used to receive or fulfill transfers? (Receiving in POS
    needs a POS Pro location.)

## Products and CSV upload (see modules/product-upload-csv.md)

17. Where does product data start: a vendor PO, a spreadsheet, a catalog?
18. Who owns each stage: ordering, CSV prep, import, barcodes, receiving,
    release for sale?
19. Manual adds, CSV import, or both? How many products in a typical batch?
20. What are the store's rules for SKU and barcode creation, tags, product
    type, and which sales channel a product belongs to?
21. What must be true before a product goes Active and visible: stock
    received and counted, price checked, images, anything else?

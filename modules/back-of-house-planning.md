# Module: planning the back of house

Sources read October 28, 2026: docs/grounding.md. This module is a
planning aid. It helps an operator think, measure, and decide. It does not
produce a build-ready floor plan, and nothing in a plan it helps write may
be labeled compliant or safe. Fire, egress, load, and electrical questions
end with a licensed professional or the local authority, every time.

## What this module produces

Not an SOP. A layout plan document with these parts, in this order:

1. **Measured facts:** the room's real dimensions, ceiling height, door
   widths and swings, and every fixed element (columns, radiators, panels,
   sinks, sprinklers), all measured, none estimated.
2. **What must live here:** the zones, equipment, and functions the room
   has to hold, on a normal day and at peak.
3. **Zone plan:** which zone goes where, and what each zone holds.
4. **Flow:** the path stock takes from delivery door to shelf to pack
   station to out the door, and the path people take, drawn or listed step
   by step.
5. **Capacity math:** how much the plan holds, with the arithmetic and the
   assumptions shown, never just a total.
6. **Decisions and defaults:** every choice logged, and every default the
   kit proposed marked as a default.
7. **Professional checks:** the fire, egress, load, and electrical items a
   licensed professional or local authority must confirm.
8. **Unknowns blocking the plan:** what must be measured, confirmed, or
   professionally checked before anything is bought or moved.
9. **Tested:** the tape walk, path trace, and peak dry run, with dates and
   what failed.

## The number rule (this module's hard rule)

Spatial planning runs on numbers, and invented numbers get built into
shelving someone pays for. So:

- Every number in the plan carries a tag: **[MEASURED]** (the operator
  measured it), **[STATED]** (the operator provided it), **[GUIDANCE]**
  (a published guideline, source in docs/grounding.md), **[REGULATION]**
  (a legal requirement, cited, still to verify locally), or **[DEFAULT]**
  (a kit proposal to verify).
- Capacity and clearance math is shown, not just answered. If the inputs
  are [TO CONFIRM], the output is a range or a blank, never a point value.
- The plan never says a layout is compliant, code-approved, or safe. It
  lists the checks a professional or the local code must confirm.

## Zones (the standard set; prune or add by interview)

- **Receiving:** at the delivery entry, so stock travels the shortest
  distance before anyone handles it. Sized for the largest normal delivery
  plus the cart or equipment that moves it. [GUIDANCE]
- **Staging and processing:** next to receiving. Count, check, label, and
  ticket here, before stock goes anywhere else. This is where the intake
  SOP (modules/product-upload-csv.md) physically happens. [GUIDANCE]
- **Pack and ship:** the fulfillment workstation. Supplies, scale, printer,
  and the order staging shelf live here, on the route out. [GUIDANCE]
- **Pick face:** fast movers on the direct route to the sales floor, at
  reachable heights. Replenishment trips should be short and frequent, not
  long and rare. [GUIDANCE]
- **Reserve storage:** slow and bulk stock higher, deeper, or further from
  the main routes. [GUIDANCE]
- **Quarantine:** returns, damaged, and wrong-item stock, physically
  separate from sellable stock. Quarantine that bleeds into general storage
  becomes shrinkage and bad counts. [GUIDANCE]
- **Supplies and non-stock:** packaging, tools, cleaning, office. Off the
  floor and out of the stock zones, labeled. [GUIDANCE]

Zones fail by bleeding into each other. If receiving doubles as overflow
storage, every delivery starts with moving boxes. The zone plan must state,
per zone, what is never allowed to land there.

## Flow rules

- One direction where the room allows it: in at receiving, through staging,
  to storage or pack, out. Stock should not cross its own path.
- People flow and stock flow are planned separately, then checked against
  each other. The busiest cart or cage sets the aisle it travels, not the
  narrowest one. [GUIDANCE]
- Receiving to pick face to sales floor is the highest-frequency route in
  most stores. Measure it. Shorten it first.

## Clearances (guidance, plus one regulation)

- Aisles are sized from the widest thing that travels them, plus working
  room: a person picking alone needs less than two people passing with
  carts. Published planning guidance commonly puts foot-only aisles around
  36 inches and push-cart aisles around 48 to 60 inches. [GUIDANCE]
- Exit routes are regulation, not guidance: under US federal OSHA rules
  for employee workplaces, an exit access must be at least 28 inches wide
  at all points, and exit routes must stay free and unobstructed with
  nothing stored in them, even temporarily. Treat 28 inches as a legal
  floor, never as a width to design to: the required width also grows with
  occupant load, and local fire code may require more. Any aisle that is
  part of an exit route goes on the professional-check list, and no storage
  is ever planned inside it.
  [REGULATION: OSHA 29 CFR 1910.36(g)(2), 1910.37(a)(3); verify locally]
- Materials handling areas need safe clearances for the equipment actually
  used, and permanent aisles marked. OSHA sets no general aisle width; it
  judges clearance against the equipment and loads in use. [GUIDANCE:
  OSHA 29 CFR 1910.176]
- The plan flags these for professional confirmation and states no
  numbers for them: storage height below sprinkler heads, and clear access
  to electrical panels, exits, and fire extinguishers. Until a professional
  confirms the clearances, the plan leaves those areas empty.

## Capacity math (show the work)

For each storage zone, the plan states:

- Usable footprint: zone length x width, minus aisles and dead corners.
- Linear shelf feet: shelves per unit x unit width x number of units, per
  level actually reachable.
- Volume or unit estimate: only from the operator's own counts (units per
  shelf foot for their actual product, measured on their actual stock).
  The kit supplies no units-per-foot ratios of its own.
- Peak factor: the plan is tested against the operator's peak delivery and
  peak season volume, from the interview, not against an average day.

## The test (replaces follow-it-cold for this module)

A plan is not final until all three have happened:

1. **Tape walk:** tape the zone boundaries and aisle widths on the floor
   at full size. Walk every route with the real cart. Anything that does
   not fit on tape will not fit in shelving.
2. **Path trace:** one full delivery, traced on paper or in the room, from
   door to shelf, and one order from shelf to pack to out. Note every
   crossing, backtrack, and blocked point.
3. **Peak dry run:** stage a peak-sized delivery's worth of boxes in the
   receiving and staging tape zones. If peak does not fit on the floor
   plan, it does not fit in the plan.

## Interview branches

Room measurements and fixed elements, what must live in the room, delivery
sizes and frequency, equipment that moves stock, what hurts now, what
cannot move, peak volumes, and who else uses the room. Answers come from
skill/interview.md, questions 22 to 29. Anything unanswered stays
[TO CONFIRM] and lands in the unknowns list, not in the plan as a guess.

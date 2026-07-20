# Module 04 — Cover bins sketch

**Module id:** module04-cover-bins
**Lab:** cover-bins
**Tracks:** A (planning docs) · B (browser lab)

## Slide 1 — Cover bins sketch

Coverage closes when defined bins get hits. A coverpoint names what you sample; bins partition the interesting space. A hole is a defined bin with zero hits. Sketching bins before you code them keeps random stimulus honest about what “done” means.

## Slide 2 — Sample, hit, hole

You sample a value into the coverpoint; matching bins increment. Coverage percent is bins hit over bins defined. Hitting mid once on a four-bin nibble point is twenty-five percent with three holes left—not “mostly done.” Values outside named bins are a modeling question, not an automatic hole.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the cover-bins lab, load the starter nibble point with low, mid, high, and top; mid already hit from sample five. Sample into other bins, switch opcode or FIFO presets, and close holes on purpose. Challenges ask you to hit a named hole and to finish all bins—not to spam random blindly.

## Slide 4 — Planning docs practice

Sketch one coverpoint with four named bins for a data nibble or opcode set. Mark which bin you would hit with a directed sample first. Note one value that sits outside your bins and decide whether to add a bin or ignore it deliberately.

## Slide 5 — Pitfalls to watch

Do not confuse “more random” with hole closure. Do not redefine holes as every unseen number in nature—only defined bins count. Do not skip naming bins because cross coverage feels advanced; start with clear singles. And remember the lab is a sketch, not your simulator’s coverage DB.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Close or name holes on a small bin sketch, then take the quiz and continue to coverage closure.

# Game That Integration

> **Intent block:** Apply the Euclidean canon engine to the Game That canvas so every transition, spawn, and UI fold is a scheduled rebind under Morph Law, not a cut or fade. Expected outcome: Game That declares binding types (color, text, geometry, position, media, state) at mount, and every interaction is a rebind passing through a Euclidean mask.

## The problem it solves

Game That's canvas is where the game draws. Before this integration, movement between states was undefined at the doctrine level — each feature would invent its own transition. That violates Morph Law (same pixels, new coordinates, zero dead time) and leaves the surface unaccountable: you cannot audit what you cannot schedule.

## How the canon drives the game

### Level transitions

A level change is not a page load. It is a rebind of position across the whole canvas. The Euclidean mask schedules which regions activate in which order. Pulses = number of active regions per cycle. Steps = the cycle granularity. Rotation = where the player enters.

### Enemy spawn schedules

Spawn timing is a talea. The binary mask decides which spawn points fire. A canon offset (second voice) creates patrol waves that never collide with the first wave when rotations tile as a mosaic — no two voices on the same node at the same step.

### UI rail folds

RomThat's Focus / Rail / Wide states fold chrome to give the canvas back. The fold itself is a morph: geometry rebinds, nothing swaps. The Euclidean seed can gate when the fold is allowed — e.g., only fold on a pulse.

### Phone controller input

RomThat's QR-paired phone sends button-only events scoped to the session. A button press rotates the canon seed. One finger, one rotation, the whole tiling shifts. The controller cannot open menus, saves, or accounts — it only conducts.

## Binding declarations

Every Game That surface declares its bindings at mount, same as ACT V4 cassettes:

- color
- text
- geometry
- position
- media
- state

A surface without declared bindings cannot mount. The mount sequence: Valid Intent gate, bindings check, SHA resolve, then render.

## Render backend question (open)

Unreal (Nanite, Lumen) and Unity (UI toolkit, input system) are the industry heavyweights. The open decision: do they become render backends behind the same rebind verb, or separate skins? Morph Law sits above both as the contract they must honor. The canon engine is backend-agnostic — it emits masks and schedules, not pixels.

## Weights mapping

See `weights-ledger.md`. The 64-weight fractal maps onto the Euclidean cycle: one sixty-fourth is the cell (XS bubble), sixteen is a cassette, sixty-four is the planet (3X large). A docked weight is a dropped note in the chord.

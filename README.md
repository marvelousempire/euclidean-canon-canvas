# Euclidean Canon Canvas

> **Intent block (audit-ready):** This repository exists to give the nine-node CCK profile, the contractor's conscience weights ledger, and the Game That canvas a shared, deterministic, audible rhythm engine. The goal is one seed that drives visual activation, pay marks, and sound simultaneously. Expected outcome: any actor, cassette, or game surface can declare a Euclidean seed and receive a consistent binary mask, node activation pattern, and MIDI note stream without custom code per surface.

## What this is

A live visual canvas and doctrine library for **Euclidean rhythms** applied to the nine-node nonagon lattice. One three-number seed — pulses, steps, rotation — generates a binary activation mask via the Björklund algorithm. That mask lights nodes on a circle. A second voice at a phase offset creates a rhythmic canon. When both voices hit the same node, it double-glows: the covalent bond, the shared electron.

This is not a toy demo. It is the **locomotion layer** for Game That, wired through Morph Law, fed by stack-that's bubble catalog, addressed by RomThat's MIDI grammar, and paid by the contractor's conscience weights.

## Why it matters

Before this, every transition in Game That was a cut, a fade, or a page swap. Morph Law forbids that: same pixels, new coordinates, zero dead time. But Morph Law needs a *schedule* — a rule for when pixels move. Euclidean canon is that schedule. It is deterministic, compact, and maps onto structures the family already uses: the nonagon, the sixty-fourths fractal, the MIDI dotted addresses, the isorhythmic talea-and-color pairing from medieval polyphony.

The realistic magic: change one number in the seed and the visual canvas, the weight ledger, and the audible score all shift together. The aces can *hear* a docked actor before they read the sheet.

## How to use it

### 1. Open the canvas

Open `canvas.html` in any modern browser. No server, no build, no dependencies.

- **Pulses** — how many nodes fire per cycle (k in the Euclidean pair)
- **Steps** — the cycle length (n); should be >= pulses
- **Rotation** — shifts where the pattern starts on the nine-node circle
- **Canon offset** — phase offset for voice 2, creating the second tiling voice

Color key: blue = voice 1, orange = voice 2, pink = both (canon collision / covalent bond).

### 2. Generate a pattern in code

```python
from bjorklund import bjorklund

mask = bjorklund(pulses=3, steps=8, rotation=0)
# [1, 0, 0, 1, 0, 0, 1, 0]
```

Walk the mask. Every 1 activates the next tentacle in the nine-node circle and assigns the next weight from the color sequence. Every 0 rests.

### 3. Declare it as a seed string

Compact form: `(3,8,0)` — pulses, steps, rotation. This is the one-line entry for every journal, stub, and CCK profile. RomThat's dotted MIDI address (`zone.portion.slot`) can carry it as a parameter.

### 4. Bind it to Game That

See `game-that-integration.md` for the full application: how the canon drives level transitions, enemy spawn schedules, UI rail folds, and the phone-controller rotation input from RomThat's QR-paired controller.

## Repository structure

| File | Purpose |
|------|--------|
| `canvas.html` | Live interactive nine-node circle, two voices, real-time re-tile |
| `bjorklund.py` | Canonical Björklund generator (bucket method, rotation support) |
| `mapping.md` | Musical object to system object table (talea, color, rotation, canon) |
| `doctrine.md` | Session synthesis: one seed, one function, one mask, nine nodes |
| `game-that-integration.md` | How this engine drives the Game That canvas, Morph Law binding declarations, Unreal/Unity render-backend question |
| `weights-ledger.md` | How Euclidean masks map onto the 64-weight contractor's conscience fractal |
| `images/` | Visual references and captured frames (to be populated — see note below) |

## Images and captures

**Note:** Image generation is not available in the current voice session. The `images/` directory is reserved for captured frames from the live canvas, annotated diagrams of the nine-node nonagon with Euclidean overlays, and screenshots of the Game That integration. These should be added by a human or an agent with rendering access, then committed with an intent block stating what each capture demonstrates.

## Audit posture

Every file in this repository carries or points to an intent block: what we set out to accomplish, what we did, and the expected observable outcome. The aces (Super Rick, Scrappy Doo, Doc, and the open Clubs seat) can walk in cold and trace from seed to mask to node activation to weight to note without asking anyone. Missed marks dock weights per the contractor's conscience mechanic in philosophy-chromatophore.

## Lineage

- **philosophy-chromatophore** — nonagon, octopus, chromatophore, morph-law doctrine
- **stack-that** — bubble catalog, nine sizes XS through 3X large, mitochondria engine metaphor
- **gameThat** — the game platform this canvas serves
- **RomThat** — MIDI grammar, phone controller, responsiveness DNA
- **contract-that** — actor binding, weights pay structure
- **skillTHAT** — packet 0029 brick-by-brick as governed capability
- **define-that** — language files naming every node, weight, and rotation
- **Automata** — ACT surface binding law, the spine underneath

## The one-line promise

One seed. One mask. Nine nodes. Two voices. Zero teleports.

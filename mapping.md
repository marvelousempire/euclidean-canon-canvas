# Mapping into the System

| Musical object | Your existing object | What it actually does |
|---|---|---|
| Euclidean (k, n) | Nine-node CCK profile | Distributes k active tentacles across n steps with maximal evenness |
| Björklund output | Binary activation mask | Exact 0/1 sequence that decides which nodes fire |
| Talea | Rhythm layer | The repeating binary pattern (from Björklund) |
| Color | Weight / pitch sequence | The ordered list of node values or MIDI notes |
| Rotation | Offset parameter | Shifts the pattern so different nodes start the cycle |
| Rhythmic canon | Multi-site / multi-canvas | Multiple child sites run the same talea at different phase offsets |
| TidalCycles `(k,n,rot)` | Compact seed string | One-line expression that can be stubbed and stored |

## Seed → Activation

1. CCK profile stores three numbers: `pulses`, `steps`, `rotation`.
2. Björklund generates the binary mask.
3. Every `1` activates the next tentacle and assigns the next weight.
4. Child sites receive the same mask with different rotations.
5. Each activated node emits its weight as a MIDI note.

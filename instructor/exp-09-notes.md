---
title: "Instructor Notes — Experiment 9: Eigenmodes and Degeneracy"
short_title: 9. Eigenmodes (instructor)
label: inst-exp-09
---

# Instructor Notes — Experiment 9

## Prep (2 h the first year, 15 min thereafter)

- **Build the box once, well.** Stout plywood or 12 mm acrylic, glued and
  sealed, roughly $30 \times 20 \times 15\ \text{cm}$ inside. A leaky or
  flimsy box has panel resonances that pollute the spectrum and make the
  assignment step frustrating.
- **Mount the driver and the microphone in opposite corners.** Every mode has
  a pressure antinode at a corner, so a corner-to-corner geometry couples to
  all of them. A face-centre driver is blind to every mode with an odd index
  in that direction, and students will spend the period wondering why half the
  predicted modes are missing.
- Make a snug insert that shortens $L_x$ by a measured $5$–$10\%$ for Part B.
- Write and test the sweep-and-transfer-function script in advance; put it on
  the shared drive.
- Deburr the Chladni plate and check the bolt is tight. Fine sand, not coarse.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Sealed rectangular cavity | build | ~$30 in materials |
| Small full-range speaker + amp | ✓ | |
| Electret mic + preamp | ✓ | Into a sound card or ADC |
| Chladni plate + driver | ✓ | |
| Fine sand or salt | consumable | |
| Thermometer | ✓ | Needed for $v(T)$ |

## Expected results

For $30 \times 20 \times 15\ \text{cm}$ at $v = 343\ \text{m/s}$, the ten
lowest modes:

| $f$ (Hz) | $(n_x,n_y,n_z)$ |
|---|---|
| 571.7 | (1,0,0) |
| 857.5 | (0,1,0) |
| 1030.6 | (1,1,0) |
| 1143.3 | (0,0,1) **and** (2,0,0) — degenerate |
| 1278.3 | (1,0,1) |
| 1429.2 | (0,1,1) **and** (2,1,0) — degenerate |
| 1539.3 | (1,1,1) |
| 1616.9 | (2,0,1) |

Note the built-in degeneracies at $1143.3$ and $1429.2\ \text{Hz}$, because
$L_z = L_x/2$. These are *accidental* — not required by any symmetry of the
box — and make an excellent talking point, since the hydrogen atom's
$\ell$-degeneracy is of exactly this apparently-accidental character.

- **Mode count below 3 kHz: 45 exactly.** The leading Weyl term gives 25; with
  the surface term, 44. Students who use only the leading term will be
  confused, which is why the handout gives both. Reward the comparison.
- Cubic box of side $20\ \text{cm}$: lowest distinct frequencies $857.5$ (×3),
  $1212.7$ (×3), $1485.2$ (×1), $1715.0$ (×3), $1917.4$ (**×6**), … The first
  degeneracy above 3 is at $1917.4\ \text{Hz}$ — answer to question 2.
- Electron in a $1\ \text{nm}$ cube: $E_{111} = 1.128\ \text{eV}$,
  $E_{211} = 2.256\ \text{eV}$ (×3), $E_{221} = 3.384\ \text{eV}$ (×3).
  $k_BT = 0.0259\ \text{eV}$, so the levels are far above thermal — the point
  of question 3.
- $v(20°\text{C}) = 343.2\ \text{m/s}$; the fitted $v$ should land within a
  few m/s.
- Fitted $L_i$ typically within $1$–$3\%$ of the ruler values. $L_x$ (the
  longest) is best determined, since it fixes the lowest and most cleanly
  measured mode.

## Where groups get stuck

1. **Misassignment.** By far the dominant difficulty. Enforce the
   work-upward strategy and the change-$L_x$ test for identifying non-cavity
   peaks.
2. **Speaker and panel resonances mistaken for modes.** They do not move when
   $L_x$ changes. This test is the fix and is worth demonstrating.
3. **Sweeping too fast.** A fast sweep smears narrow resonances. Slow
   logarithmic sweeps, or stepped tones.
4. **Driving too loud.** Nonlinearity, plus a hearing hazard.

## Grading notes

- The four-parameter simultaneous fit is the analysis that separates good
  reports. Groups that fit each mode independently should be pushed toward it.
- Question 9 (Coulomb symmetry versus screened potential) is the bridge to
  Week 11; read the answers before teaching it.
- The density-of-states question connects back to Chapter 6. Look for students
  who notice that the surface term matters at these frequencies.

## Safety

Sound pressure only. Keep levels conversational.

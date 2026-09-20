---
title: "Instructor Notes — Experiment 2: The Speed of Light"
short_title: 2. Speed of Light (instructor)
label: inst-exp-02
---

# Instructor Notes — Experiment 2

## Prep (2 h the first year, 30 min thereafter)

- Build and test the pulser. A microcontroller GPIO pin alone gives a
  $\sim50\ \text{ns}$ edge, far too slow. Use a MOSFET gate driver
  (TC4427 or similar) driving a red laser diode or a high-speed IR LED;
  measured edges of $2$–$4\ \text{ns}$ are achievable.
- Match the two BNC cables and mark them as a pair. Measure their delay
  difference once and write it on the box.
- Mark the folded beam path on the floor with tape and check head clearance.
- Verify there is no electrical crosstalk: block the beam and confirm the
  signal channel is flat. Fixing this after the fact wastes a period.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| ≥100 MHz oscilloscope with averaging | ✓ | 200 MHz preferred |
| Laser diode module + gate driver | build | ~$25 |
| Two fast photodiode/TIA boards | build | BPW34 + OPA657 or an off-the-shelf module, ~$40 each |
| Front-surface mirrors ×2 | ✓ | |
| Tape measure, 10 m | ✓ | |
| RG-58 matched pair | ✓ | Measure and label |

## Expected results

- $c$ to $1$–$3\%$ with 128× averaging and an $8$–$12\ \text{m}$ path range.
  Better than 1% means check for a fortuitous cancellation.
- Fitted $\tau$: tens of nanoseconds, dominated by the photodiode and cable
  delays. It should be *positive* and stable across the run.
- Time scale reference: $3.34\ \text{ns/m}$. Over a $10\ \text{m}$ swing the
  total delay change is $33\ \text{ns}$; with $0.4\ \text{ns}$ timing
  resolution that is a $1.2\%$ measurement.
- $\sigma_L = 5\ \text{mm}$ contributes only $17\ \text{ps}$ — negligible, and
  students should demonstrate that rather than assume it.

## Where groups get stuck

1. **Beam not centred on the detector after moving a mirror.** Produces a
   curved residual and a systematically wrong $c$. This is the failure mode to
   watch for; the warning in the handout is there because it happens every
   year.
2. **Electrical crosstalk mistaken for signal.** The block-the-beam control
   catches it. Make it a checkpoint if a group looks confused.
3. **Timing on the peak instead of the 50% crossing.** The two pulses have
   different shapes; peak timing gives a path-length-dependent bias.
4. **Dividing $L$ by $\Delta t$ for a single point.** Give them post-lab
   question 7 early if they start doing this.

## Grading notes

- The slope method versus the single-point method is the conceptual core.
  Question 7 makes them quantify the error they would have made.
- Check whether the cable-swap control was done and reported.
- A report that quotes $c$ with no discussion of $\tau$'s physical
  reasonableness has missed half the experiment.

## Safety

If a laser diode is used rather than an LED, the folded path crosses the room
at head height. Tape the path on the floor and keep the aisle clear.

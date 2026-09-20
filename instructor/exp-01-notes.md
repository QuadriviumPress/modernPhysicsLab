---
title: "Instructor Notes — Experiment 1: Michelson Interferometer"
short_title: 1. Michelson (instructor)
label: inst-exp-01
---

# Instructor Notes — Experiment 1

## Prep (45 min)

- Pre-align each interferometer to visible circular fringes and leave it that
  way. Groups that must find fringes from scratch lose an hour, and the
  measurement is not what the hour teaches.
- Verify the micrometer's calibration against gauge blocks or a dial
  indicator. The old bench units on this rig read $10\ \mu\text{m}$ per
  division; two of them have historically been off by a few percent, which
  propagates directly into $\lambda$.
- Check tables for vibration. If the building's HVAC cycles, note the times.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Michelson bench interferometer | ✓ | Aging but serviceable |
| Thorlabs EDU-MINT1 | ✓ | Better for the rotation part (Part C) |
| HeNe laser | ✓ | $632.816\ \text{nm}$ in air |
| 650 nm diode module | ✓ | Cheap backup; short coherence length |
| $f=-25\ \text{mm}$ diverging lens | ✓ | |
| Tally counters | — | ~$5 each; buy four, they get lost |

## Expected results

- $\lambda = 633 \pm 1\ \text{nm}$ is a good result; $\pm3\ \text{nm}$ is
  typical. Accepted: $632.816\ \text{nm}$ (air).
- Backlash shows up as a $5$–$20\ \mu\text{m}$ intercept when the origin is not
  forced. Groups that reverse direction mid-run get scatter far exceeding
  their propagated uncertainty; this is the intended lesson.
- Detection threshold in Part C: typically $0.1$–$0.3$ fringes.
- Resulting ether bound with $L = 0.30\ \text{m}$ and $\Delta N_{\min}=0.2$:
  $v_{\max} \approx 140\ \text{km/s} \approx 5\times10^{-4}c$ — about five
  times the Earth's orbital speed, so the experiment *cannot* rule out the
  ether. Students should say so plainly. Michelson and Morley's $L=11\ \text{m}$
  is exactly the point: $L \approx 13\ \text{m}$ is needed for a $0.4$-fringe
  signal at $29.8\ \text{km/s}$.
- Expected fringe shift on rotation at $L=0.30\ \text{m}$: $\sim9\times10^{-3}$
  fringes. Unobservable — any shift they see is flexure.

## Where groups get stuck

1. **Cannot find fringes with a diode laser.** Coherence length. Equalize the
   arms with a ruler to within a few millimetres first.
2. **Fringes drift on their own.** Someone leaning on the table, an unlocked
   mount, or an air current. Check the mounts before blaming the building.
3. **Factor of two.** The single most common error, and it produces
   $\lambda \approx 316\ \text{nm}$ or $\approx 1266\ \text{nm}$. Checkpoint 2
   exists to catch it in the room.
4. **Counting past a hundred without a tally counter.** They miscount. Insist
   on the counter and on the partner calling out every 50.

## Grading notes

- The ether bound is where reports differentiate. A report that computes
  $v_{\max}$, notes that it exceeds $29.8\ \text{km/s}$, and concludes honestly
  that the measurement is not sensitive enough should score higher than one
  that claims to have "confirmed the null result".
- Look for whether the origin-forced and free-intercept fits were both done.
  The intercept is a measurement of backlash and should be discussed.

## Safety

Class 2 for the HeNe. The main risk is a student bending to beam height to
look along the arm. Say this out loud at the start of the period.

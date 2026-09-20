---
title: "Instructor Notes — Experiment 7: The Quantum Eraser"
short_title: 7. Quantum Eraser (instructor)
label: inst-exp-07
---

# Instructor Notes — Experiment 7

## The point to defend

Every year some students will write that they observed quantum behaviour or
single-photon interference. They did not: a milliwatt-class laser is a
classical field, and every result in this experiment follows from classical
electromagnetism with polarized waves. The handout says so in an
`{important}` box, and question 8 tests it. **Grade this hard** — it is the
single most valuable transferable lesson in the experiment, and popular
science accounts are actively working against you here.

## Prep (1 h)

- Assemble the EDU-QE1 per its manual and leave it assembled between sections.
  Realignment eats a period.
- Check the slit polarizers' extinction ratio; degraded film polarizers are
  the usual cause of a poor $V \to 0$ at $\theta = 0$.
- Set the rotation mount's zero against a known polarizer and mark it.
- Lay out the laser eyewear. This is the one Class 3R source in the course.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Thorlabs EDU-QE1 kit | ✓ | 532 nm, Class 3R |
| Laser safety eyewear, 532 nm | ✓ | Check OD and count them |
| Camera or scanning photodiode | ✓ | Shared with Exps 4–5 |
| Rotation mount, 1° scale | ✓ | |
| ND filter set | ✓ | Essential — the kit laser saturates everything |
| Thorlabs EDU-BT1 kit | ✓ | Optional Part E |

## Expected results

- Fringe spacing at $\lambda = 532\ \text{nm}$, $d = 0.25\ \text{mm}$,
  $L = 1.5\ \text{m}$: $3.19\ \text{mm}$, about 1060 pixels on a $3\ \mu\text{m}$
  sensor. Very comfortable.
- Baseline visibility $V_0$: $0.7$–$0.9$ with good alignment. Below $0.6$,
  send them back to alignment.
- With orthogonal slit polarizers: residual $V$ of $0.02$–$0.10$, set by
  polarizer extinction and uneven slit illumination.
- $V(\theta) = |\sin 2\theta|$, $D(\theta) = |\cos 2\theta|$;
  $V^2 + D^2 = 1$ exactly in theory. **Raw** measured values give
  $V^2 + D^2 \approx 0.6$–$0.9$; after dividing $V$ by $V_0$ they should sit
  close to 1 and always at or below it.
- de Broglie answers for question 4: $50\ \text{eV}$ electron
  $0.173\ \text{nm}$; $100\ \text{eV}$ $0.123\ \text{nm}$ (both comparable to
  crystal lattice spacings — hence Davisson–Germer); thermal neutron at
  $300\ \text{K}$ $\approx0.145\ \text{nm}$ (also crystal-scale);
  $C_{60}$ at $200\ \text{m/s}$ $2.77\ \text{pm}$ (needs a nanofabricated
  grating — hence 1999, not 1927). $100\ \text{keV}$ electron:
  $3.70\ \text{pm}$ relativistic versus $3.88\ \text{pm}$ non-relativistic, a
  4.6% difference.

## Where groups get stuck

1. **Saturation.** A clipped maximum lowers the measured $V$ and drags every
   point inside the unit circle for the wrong reason. Check at Checkpoint 1.
2. **Letting $k$ float in the fringe fit.** It chases noise at low visibility.
   Fix it from Part A.
3. **Forgetting the baseline correction** and then concluding complementarity
   is violated in the safe direction. Ask them which direction a violation
   would have to be in.
4. **Rushing past the $\pm45°$ sum control.** It is the conceptual heart of
   Part C; make it Checkpoint 2 and actually look at it.

## Grading notes

- Question 8 and the classical-versus-quantum framing: heavily weighted.
- The $V$–$D$ plot should have error bars on both axes and the unit circle
  overlaid.
- Reward groups that report both raw and baseline-corrected $V^2 + D^2$.

## Safety

Class 3R at 532 nm — the wavelength of peak eye sensitivity and above the
blink-reflex protection threshold. Eyewear required whenever the beam is
unenclosed. Do a verbal briefing at the start of the period, not just a
reference to the safety section.

---
title: "Instructor Notes — Experiment 10: Balmer Series"
short_title: 10. Balmer (instructor)
label: inst-exp-10
---

# Instructor Notes — Experiment 10

**Full-report week.**

## Prep (45 min)

- Check the hydrogen tube's hours. Tubes degrade and the molecular bands
  strengthen relative to the atomic lines as they age; a tired tube makes
  H$\delta$ effectively invisible. Keep a fresh spare.
- Post a table of the mercury calibration lines at the bench, and a second
  table of the *molecular* hydrogen band regions so groups can recognize what
  to reject.
- Focus and set each spectrometer, then lock the parts students should not
  touch.
- Remind groups at the start: **do not move anything between calibration and
  measurement.** This is the whole experiment.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Hydrogen discharge tube | consumable | Keep 2 spare |
| Mercury, helium tubes | ✓ | |
| Grating or constant-deviation spectrometer | ✓ | |
| EDU-SPEB1 kit | ✓ | Alternative |
| HV tube supply | ✓ | |

## Expected results

Predicted air wavelengths from $R_{\text{H}} = 1.0967758\times10^7\ \text{m}^{-1}$
with $n_{\text{air}} = 1.000277$:

| Line | Vacuum (nm) | Air (nm) | Accepted air (nm) |
|---|---|---|---|
| H$\alpha$ | 656.470 | 656.288 | 656.279 |
| H$\beta$ | 486.274 | 486.139 | 486.135 |
| H$\gamma$ | 434.173 | 434.053 | 434.047 |
| H$\delta$ | 410.294 | 410.180 | 410.174 |

- Series limit: $364.60\ \text{nm}$ (air). Lyman-$\alpha$: $121.57\ \text{nm}$
  vacuum. Both outside the visible — question 2.
- Typical student $R_{\text{H}}$: within $0.1$–$0.5\%$ with a vernier
  spectrometer; $0.5$–$2\%$ with a compact USB spectrometer, where the
  calibration residual dominates.
- $R_\infty/R_{\text{H}} = 1.000545$, i.e. $0.0545\%$ — at $656\ \text{nm}$
  that is $0.358\ \text{nm}$. Comfortably larger than the $0.13\ \text{nm}$
  resolution of a good grating, so a careful group *can* distinguish them.
  Most will not, and should say so with a number.
- Air-index correction: $0.18\ \text{nm}$ at H$\alpha$ — half the size of the
  reduced-mass effect, so groups that skip it and then claim to see the
  reduced-mass shift are fooling themselves. Watch for this specifically.
- $m_e/M_p = 5.446\times10^{-4}$ if they get there.
- Doppler width of H$\alpha$: $8.1\ \text{pm}$ FWHM at $300\ \text{K}$
  ($R = 81000$ needed) and $33\ \text{pm}$ at $5000\ \text{K}$
  ($R = 20000$). Neither is resolvable with bench equipment — question 10 asks
  them to establish that, not to measure it.

## Where groups get stuck

1. **Disturbing the instrument between calibration and measurement.** Fatal
   and undetectable at analysis time. Say it three times.
2. **Molecular hydrogen bands mistaken for atomic lines.** Especially near
   H$\gamma$ and H$\delta$. The rejection log in step 9 is there for this.
3. **Not converting air to vacuum.** Introduces a $0.027\%$ bias.
4. **H$\delta$ too faint.** Widen the slit, then re-measure H$\alpha$ at the
   same width to check for a slit-dependent shift.
5. **Averaging four separate $R$ values** instead of fitting the line.

## Grading notes

Full-report criteria. Specifically:

- The calibration residual must appear as a quantified systematic, not a
  hand-wave.
- Question 8 must be answered with numbers (difference between $R_{\text{H}}$
  and $R_\infty$ versus their $\sigma_R$), not with "we could not tell".
- Question 9 — features neither Bohr nor Schrödinger explain — good answers:
  fine structure (needs Dirac / spin–orbit), the Lamb shift (needs QED),
  hyperfine structure (needs nuclear spin), and relative line intensities
  (needs transition matrix elements).

## Safety

Several kilovolts at the tube supply, and hot glass. Power down and wait
before swapping tubes.

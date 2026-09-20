---
title: "Instructor Notes — Experiment 12: Molecular Fluorescence"
short_title: 12. Fluorescence (instructor)
label: inst-exp-12
---

# Instructor Notes — Experiment 12

## Prep (1 h, including solution making)

- Make the stock solutions the day before: fluorescein in $0.1\ \text{M}$
  NaOH (the anion is the strongly fluorescent form — in neutral water the
  spectrum shifts and weakens), or quinine sulfate in $0.1\ \text{M}$
  H$_2$SO$_4$. Label with concentration and date.
- Set up one bench as a demonstration of the $90°$ excitation geometry with
  the long-pass filter in place, and leave it assembled.
- Check the long-pass filter's own fluorescence: illuminate it alone with the
  excitation LED and confirm the spectrometer sees nothing.
- Put out matched cuvettes and lint-free wipes. Fingerprints on the optical
  faces are a real error source.
- Confirm the spectrometer's wavelength calibration; kit calibrations drift.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| EDU-SPEA1 / SPEB1 kit with cuvette holder | ✓ | |
| White LED / tungsten source | ✓ | For absorption |
| 365, 405, 470 nm LEDs | ✓ | Shared with Exp 6 |
| Long-pass filters (500 nm, 420 nm) | ? | ~$30 each |
| Quartz or plastic cuvettes, 1 cm | consumable | Quartz needed below 350 nm |
| Fluorescein, quinine sulfate | consumable | |
| Volumetric flasks, micropipettes | ✓ | |

## Expected results

- Fluorescein (anion): absorption peak $\approx490\ \text{nm}$, emission
  $\approx512$–$514\ \text{nm}$.
  $\varepsilon \approx 7.6\times10^{4}\ \text{M}^{-1}\text{cm}^{-1}$.
  $A = 1.0$ in a $1\ \text{cm}$ cell at $1.32\times10^{-5}\ \text{M}$, i.e.
  $4.4\ \text{mg/L}$ — students are usually surprised how dilute this is.
- Stokes shift $490 \to 514\ \text{nm}$: $953\ \text{cm}^{-1}$,
  $118\ \text{meV}$. Compare with $k_BT = 209\ \text{cm}^{-1} = 25.9\ \text{meV}$:
  roughly $4.6\,k_BT$, or a handful of vibrational quanta.
- Quinine: absorption $\approx347\ \text{nm}$, emission $\approx450\ \text{nm}$;
  a much larger Stokes shift ($\approx6600\ \text{cm}^{-1}$) and needs the
  UV LED and quartz cuvettes.
- Beer–Lambert linear to $A \approx 1.5$–$2$; above that, stray light
  (typically $0.1\%$, giving a hard ceiling near $A = 3$) and then aggregation.
- Emission spectra should be independent of excitation wavelength to within
  noise (Kasha's rule). Departures almost always mean an inner-filter problem,
  not a physics result.
- Chlorophyll (optional): absorption $\approx430$ and $662\ \text{nm}$,
  emission $\approx668\ \text{nm}$ — a strikingly small Stokes shift.

## Where groups get stuck

1. **Concentration too high for the emission measurement.** The inner filter
   effect red-shifts the emission and fakes a larger Stokes shift. This is the
   dominant systematic; step 7's $A \lesssim 0.1$ rule is not negotiable.
2. **Forgetting the $\lambda^2$ Jacobian** when converting to a wavenumber
   axis. Shifts the apparent emission peak by tens of $\text{cm}^{-1}$ and is
   the most common analysis error. Flag it in the pre-lab briefing.
3. **Scattered excitation light in the emission spectrum.** $90°$ geometry
   plus the long-pass filter. A sharp peak at the excitation wavelength means
   the geometry is wrong.
4. **Quoting the Stokes shift in nanometres.** Insist on wavenumbers.
5. **Solvent Raman peak** mistaken for a vibronic feature. The blank
   subtraction removes it; make sure they take a blank.

## Grading notes

- The distinction between an instrumental limit ($A > 2$) and a physical
  breakdown (aggregation, peak shift) on the Beer–Lambert plot is worth
  probing; question 5 asks for it.
- Question 8 (distinguishing inner-filter from self-quenching): the good
  answer is a path-length or geometry variation — front-face excitation, or a
  thinner cell — since the inner filter effect depends on path length and
  self-quenching does not.
- Question 10 (where the energy went): vibrational relaxation into the
  solvent, i.e. heat. Watch for students who invoke "energy loss" without
  saying where.

## Safety

The $365\ \text{nm}$ LED is a genuine UV hazard with no blink reflex — shield
it. Ethanol/acetone away from the lamp. Gloves for the dyes.

---
title: "Instructor Notes — Experiment 6: Planck's Constant from LEDs"
short_title: 6. LEDs and Planck (instructor)
label: inst-exp-06
---

# Instructor Notes — Experiment 6

This experiment replaces the PASCO EX-5549A photoelectric apparatus. Be
explicit with students about what is gained and lost — the honesty about the
systematic is a large part of the pedagogical value, and question 10 asks them
to articulate it.

## Prep (1 h the first year)

- Assemble LED boards: each LED in a socket with a $100\ \Omega$ series
  resistor, on a small board with test points. Sockets, not soldered — LEDs
  get destroyed.
- **Do not include white LEDs.** Blue chip plus phosphor; the spectrum is
  meaningless for this measurement. Remove them from the drawer.
- Write the microcontroller sweep sketch once and put it on the shared drive.
  A sweep of 200 points takes ten seconds and transforms the quality of the
  data over knob-turning.
- Verify the spectrometer kit reaches into the near infrared if you intend to
  include the $940\ \text{nm}$ LED — many compact spectrometers stop near
  $850\ \text{nm}$. If it does not, drop that LED rather than using its
  nominal wavelength.
- Put the tungsten lamp on a ceramic tile with a "hot" sign.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| LEDs: 405, 470, 525, 590, 630, 940 nm | ✓ | Buy 10 of each; ~$15 total |
| EDU-SPEA1 / SPEB1 spectrometer kit | ✓ | Check IR range |
| Microcontroller with DAC or filtered PWM | ✓ | |
| Two DMMs per bench | ✓ | |
| 6 V clear-envelope lamp | consumable | Automotive #1156 or torch bulb |
| Bench supply 0–8 V, 2 A, 4-wire sense | ✓ | |

## Expected results

- Photon energies: $470\ \text{nm} = 2.638\ \text{eV}$,
  $525 = 2.362$, $590 = 2.102$, $630 = 1.968\ \text{eV}$.
- Expected slope: $hc/e = 1239.84\ \text{V}\cdot\text{nm}$.
- **Typical measured $h$: 10–20% low**, with a positive intercept of a few
  tenths of a volt. This is the expected outcome and should not be treated as
  a failed experiment. The sign is set by the thermal tail and by emission
  peaking below $E_g$.
- Groups using nominal rather than measured peak wavelengths pick up an
  additional 2–4% error.
- Diode ideality: a $100\ \text{mV}$ step changes the current by a factor of
  about 7 at $n = 2$. Question 3 uses this to kill the "when it visibly
  glows" definition.
- Tungsten: $R/R_0 = 12.7$ at $2500\ \text{K}$. With $R_0 = 0.9\ \Omega$,
  the hot current at $6\ \text{V}$ is $0.52\ \text{A}$ against a cold inrush
  of $6.7\ \text{A}$ — a factor of 13, which is why lamps fail at switch-on.
- Stefan–Boltzmann exponent: typically $n = 3.6$–$4.1$. Dropping the lowest
  temperature points pushes it up toward 4, because lead conduction is a
  larger fraction of the loss at low $T$. Expect and reward that observation.
- Wien at $2500\ \text{K}$: $\lambda_{\max} = 1159\ \text{nm}$ — deep in the
  infrared, which is question 9's point about incandescent lighting.

## Where groups get stuck

1. **Measuring across the LED *and* the resistor.** Gives a slope that is
   nonsense. Check the probe placement at the bench.
2. **Different current windows for different LEDs.** Destroys comparability.
   Insist on one window, applied uniformly, stated in the report.
3. **Saturated spectra.** Flat-topped emission peaks give a wrong $\lambda_p$.
4. **Sensing the lamp voltage at the supply.** Lead resistance is comparable
   to the cold filament resistance; this is a large error.
5. **Not waiting for thermal equilibrium** at each lamp voltage.

## Grading notes

- The intercept discussion is where the credit is. A report that gets $h$ to
  5% by luck and says nothing about the intercept should score below one that
  gets 15% and explains it.
- Require both the statistical uncertainty and the window-choice systematic.
- Question 10 (what the photoelectric experiment establishes that this does
  not) is the one to read carefully: the answer is that the photoelectric
  effect shows the *radiation field* is quantized in its interaction with
  matter, with a threshold frequency independent of intensity, whereas the LED
  shows only that a semiconductor emits at its gap energy.

## Safety

The filament envelope stays dangerously hot for minutes. The $405\ \text{nm}$
LED is bright and near-UV; do not let students look into it.

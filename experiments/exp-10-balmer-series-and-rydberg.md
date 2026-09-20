---
title: The Balmer Series and the Rydberg Constant
short_title: 10. Balmer Series
label: exp-balmer
numbering:
  enumerator: "10.%s"
---

# Experiment 10 — The Balmer Series and the Rydberg Constant

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 10, *The Hydrogen Atom*
**Apparatus** Hydrogen discharge tube, calibration lamps, grating spectrometer or Thorlabs EDU-SPEB1 kit
**You will measure** four Balmer wavelengths and the Rydberg constant to $\sim0.1\%$
**Report** **Full report** — this is one of the three
:::

## Objectives

By the end of this experiment you should be able to:

- Calibrate a spectrometer against known lines and quantify the residual
  calibration uncertainty.
- Measure the visible hydrogen emission wavelengths and assign them to
  transitions.
- Extract the Rydberg constant from a linear fit and compare it with the
  accepted value at the level of your uncertainty.
- Explain why the hydrogen spectrum was the decisive test of the Bohr model
  and remains the reference case for atomic structure.

## Textbook connection

Read §10.1–10.5. The Bohr and Schrödinger treatments both give

$$
E_n = -\frac{13.6\ \text{eV}}{n^2} ,
$$

and the transitions among these levels are the spectrum you will measure. The
Balmer series — transitions down to $n = 2$ — is the part that happens to fall
in the visible, which is why a formula fitted to it in 1885 preceded any
theory of atomic structure by nearly thirty years.

## Theory

### The Rydberg formula

Transitions from level $n_i$ to level $n_f$ emit photons with

$$
\frac{1}{\lambda} = R_{\text{H}}\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right) .
$$ (eq-rydberg)

For the Balmer series $n_f = 2$, and the visible lines are

:::{list-table} The visible Balmer lines
:header-rows: 1

* - Line
  - Transition
  - Accepted $\lambda$ (air, nm)
  - Colour
* - H$\alpha$
  - $3 \to 2$
  - 656.279
  - deep red
* - H$\beta$
  - $4 \to 2$
  - 486.135
  - cyan
* - H$\gamma$
  - $5 \to 2$
  - 434.047
  - blue-violet
* - H$\delta$
  - $6 \to 2$
  - 410.174
  - violet, faint
:::

Rearranged, [](#eq-rydberg) says that a plot of $1/\lambda$ against
$(1/4 - 1/n_i^2)$ is a straight line through the origin with slope
$R_{\text{H}}$. That is the fit you will do, and it uses all four lines at once
rather than averaging four separate estimates.

```{figure} ../images/exp10-energy-levels-concept.svg
:label: fig:exp10-energy-levels
:alt: Hydrogen energy levels from n=1 to the continuum, with the four Balmer transitions from n=3,4,5,6 down to n=2 marked in color, and one representative Lyman and Paschen transition shown in gray for context.

The Balmer series is one column in a larger structure: every visible line you measure is a transition landing on $n=2$; Lyman lines land on $n=1$ (in the UV) and Paschen lines on $n=3$ (in the IR) — neither visible to the eye, which is why Balmer's formula came first.
```

### Which Rydberg constant?

Two constants appear in the literature and they are not the same:

$$
R_\infty = \frac{m_e e^4}{8\varepsilon_0^2 h^3 c} = 1.0973731568\times10^{7}\ \text{m}^{-1}
$$

is the value for an *infinitely heavy* nucleus, and

$$
R_{\text{H}} = \frac{R_\infty}{1 + m_e/M_p} = 1.0967758\times10^{7}\ \text{m}^{-1}
$$

is the value for hydrogen, corrected for the finite proton mass through the
reduced mass $\mu = m_eM_p/(m_e + M_p)$. They differ by $1$ part in $1836$,
i.e. by $0.054\%$. **If your measurement is good to $0.1\%$ you cannot tell
them apart; if it is good to $0.02\%$ you can, and you have measured the
proton-to-electron mass ratio.** Say in your report which one your data can
distinguish.

### Air versus vacuum

Wavelengths measured in air are shorter than in vacuum by the refractive index
of air, $n \approx 1.00027$ in the visible — a $0.027\%$ effect, comparable to
the reduced-mass correction above. Tabulated "air wavelengths" (the values in
the table above) already include it. Be explicit about which convention you
are using, or you will chase a systematic of exactly the size of the physics
you are trying to see.

## Pre-lab

:::{exercise}
:label: q-balmer-01

Using [](#eq-rydberg) with $R_{\text{H}} = 1.0967758\times10^{7}\ \text{m}^{-1}$,
compute the vacuum wavelengths of H$\alpha$ through H$\delta$. Convert to air
wavelengths by dividing by $n_{\text{air}} = 1.000277$ and compare with the
table. Do they agree to the digits given?
:::

:::{exercise}
:label: q-balmer-02

Compute the series limit ($n_i \to \infty$) of the Balmer series, and the
wavelength of the Lyman-$\alpha$ line ($2\to1$). Why are neither of these
visible to the eye?
:::

:::{exercise}
:label: q-balmer-03

Your spectrometer will be calibrated against a mercury lamp. Look up the four
strongest visible Hg lines and tabulate them. Which of them bracket the
Balmer lines, and which Balmer line will therefore have the largest
calibration uncertainty?
:::

:::{exercise}
:label: q-balmer-04

To distinguish $R_{\text{H}}$ from $R_\infty$ you need a relative precision
better than $0.054\%$. At $656\ \text{nm}$, what absolute wavelength
uncertainty is that? Compare with the resolving power you computed in
[](#q-diff-07). Is it achievable with the instrument on the bench?
:::

## Apparatus

- Hydrogen discharge tube with a high-voltage power supply
- Mercury and helium discharge tubes, for calibration
- Either: a constant-deviation or grating spectrometer with a vernier
  circle, or the Thorlabs EDU-SPEB1 spectrometer kit, or a compact USB
  spectrometer with a fibre input
- Entrance slit of adjustable width
- Thermometer and barometer, if you intend to make the air-index correction
  yourself

:::{danger}
Discharge tube supplies run at several kilovolts. Switch off and wait before
changing a tube; the supply and the tube itself store charge. Tubes get hot
and the glass is fragile. Hydrogen tubes have a limited life at full current —
run them at the recommended setting and switch them off between measurements.
:::

```{figure} ../images/exp10-balmer-spectrometer-schematic.svg
:label: fig:exp10-spectrometer
:alt: Light from a hydrogen discharge tube passes through an adjustable entrance slit and a collimating lens, then diffracts off a grating mounted on a vernier turntable, spreading the Balmer lines to different angles.

The grating spectrometer. Collimated light from the entrance slit meets the grating; each Balmer line diffracts to its own angle, read off the turntable vernier and converted to wavelength.
```

## Procedure

### Part A — Calibration

1. Set up the spectrometer and focus it on the entrance slit. Narrow the slit
   until the lines are sharp; note that narrowing further past this point
   costs intensity without improving resolution.
2. With the mercury lamp, measure the angular position (or pixel/wavelength
   readout) of at least five known lines across the visible.
3. Fit the calibration: for a grating spectrometer, fit
   $\sin\theta = m\lambda/d$ and extract $d$ and the zero-angle offset; for a
   spectrometer kit or USB spectrometer, fit a low-order polynomial of
   wavelength against pixel.
4. **Quantify the calibration residuals.** The RMS residual of the calibration
   fit is a systematic uncertainty that applies to every subsequent
   measurement, and it usually dominates the final answer.
5. Add the helium lamp as an independent check: predict its line positions
   from the mercury calibration and see how well they land.

**[ ] Checkpoint 1.** Show the instructor your calibration
fit and its residuals. If the residuals exceed a few tenths of a nanometre,
find out why before you touch the hydrogen tube — a bad calibration cannot be
repaired at the analysis stage.

### Part B — The Balmer lines

6. Replace the calibration lamp with the hydrogen tube, *without disturbing
   the spectrometer in any way*. Any adjustment to the slit position, the
   grating angle, or the fibre invalidates the calibration.
7. Measure each of the four Balmer lines. Measure each **at least five times**,
   approaching from alternating directions to expose backlash in the vernier.
8. H$\delta$ is faint. Widen the slit for it if necessary, but then re-measure
   H$\alpha$ at the same slit width, so you can check whether the slit width
   shifts the apparent line centre.
9. Watch for the strong molecular hydrogen bands — the tube emits from H$_2$
   as well as H, giving a rich fine structure that is *not* the Balmer series.
   The Balmer lines are sharp and bright; the molecular bands are broad and
   clustered. Note in your notebook which features you rejected and why.

### Part C — Re-calibration

10. Return the mercury lamp and re-measure two lines. Any shift is drift, and
    it belongs in your systematic budget.

## Analysis

### Wavelengths

Apply the calibration to each measured position, propagating both the
statistical scatter of your repeats and the calibration residual. Quote each
$\lambda$ with an uncertainty, and compare each with the accepted value
individually before you fit anything.

### The Rydberg constant

```python
import numpy as np
from scipy.optimize import curve_fit

ni  = np.array([3, 4, 5, 6])
lam = np.array([...])                 # measured, metres, VACUUM
slam= np.array([...])

x   = 0.25 - 1.0 / ni**2
y   = 1.0 / lam
sy  = slam / lam**2                   # propagate 1/lambda

popt, pcov = curve_fit(lambda x, R: R * x, x, y,
                       sigma=sy, absolute_sigma=True)
R, sR = popt[0], np.sqrt(pcov[0, 0])
print(f"R_H = {R:.7g} +/- {sR:.2g} 1/m")
```

Convert your measured air wavelengths to vacuum first
($\lambda_{\text{vac}} = n_{\text{air}}\lambda_{\text{air}}$) — the accepted
$R_{\text{H}}$ is defined for vacuum wavelengths, and skipping this step
introduces a $0.027\%$ bias, which is half the size of the reduced-mass effect
you may be trying to see.

Fit both with the intercept forced to zero and with it free. A significantly
nonzero intercept means a calibration offset, not new physics.

### The reduced-mass question

If $\sigma_R/R < 5\times10^{-4}$, compute

$$
\frac{m_e}{M_p} = \frac{R_\infty}{R_{\text{H,measured}}} - 1
$$

and compare with $1/1836.15$. Report it even if the uncertainty is large — a
result of $(6 \pm 9)\times10^{-4}$ is an honest and informative outcome.

## Post-lab questions

:::{exercise}
:label: q-balmer-05

Report your four wavelengths and $R_{\text{H}}$ with uncertainties. Compare
$R_{\text{H}}$ with the accepted value in units of $\sigma$.
:::

:::{exercise}
:label: q-balmer-06

Which contributed more to $\sigma_R$: the scatter of your repeated readings,
or the calibration residual? Support the claim with numbers, and say what you
would change first.
:::

:::{exercise}
:label: q-balmer-07

Plot your residuals from the Rydberg fit against $n_i$. Is there a trend? A
systematic drift with $n_i$ would indicate a wavelength-dependent calibration
error; a random scatter would not. Which do you see?
:::

:::{exercise}
:label: q-balmer-08

Can your data distinguish $R_{\text{H}}$ from $R_\infty$? Answer with a
number, not a word: state the difference between them in your units and
compare with your $\sigma_R$.
:::

:::{exercise}
:label: q-balmer-09

The Bohr model and the Schrödinger equation give identical energies for
hydrogen. Name two experimentally observed features of the hydrogen spectrum
that *neither* accounts for, and say what theory is needed for each.
:::

:::{exercise}
:label: q-balmer-10

Estimate the temperature of the gas in the discharge from the Doppler width of
H$\alpha$, if your instrument resolved it — or, if it did not, compute the
Doppler width you would expect at $300\ \text{K}$ and at $5000\ \text{K}$ and
state what resolving power would be needed to see the difference.
:::

## Going further

- **The deuterium isotope shift.** A deuterium lamp's H$\alpha$ sits
  $0.18\ \text{nm}$ from hydrogen's, because the reduced mass differs. That
  requires $\lambda/\Delta\lambda \approx 3600$ — within reach of a good
  grating spectrometer, and a direct, visible measurement of the mass of the
  neutron's contribution to the nucleus. This is how deuterium was discovered
  in 1931.
- **Sodium as a contrast case.** Measure the sodium doublet on the same
  instrument, and note that no simple Rydberg formula fits it. Explaining why
  is Week 11.
- **Balmer in absorption.** The same lines appear as *dark* lines in the
  spectra of A-type stars. A small telescope with a grating in front of the
  objective will show them, and identifying the Balmer series in Vega with the
  calibration you built today is one of the more satisfying evenings available
  to an undergraduate.

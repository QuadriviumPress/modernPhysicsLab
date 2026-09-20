---
title: Alkali Spectra, Screening, and the Quantum Defect
short_title: 11. Alkali Spectra
label: exp-quantum-defect
numbering:
  enumerator: "11.%s"
---

# Experiment 11 — Alkali Spectra, Screening, and the Quantum Defect

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 11, *Many-Electron Atoms*
**Apparatus** Sodium (and mercury, helium) discharge lamps, calibrated grating spectrometer
**You will measure** the sodium D doublet splitting and the quantum defects $\delta_s$, $\delta_p$, $\delta_d$
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Resolve the sodium D doublet and measure its splitting, and interpret it as
  spin–orbit coupling.
- Assign observed alkali lines to series and extract quantum defects from a
  Rydberg-like fit.
- Explain why the quantum defect decreases sharply with increasing $\ell$, in
  terms of the penetration of the valence orbital into the core.
- Explain why hydrogen's $\ell$-degeneracy is absent in every other atom.

## Textbook connection

Read §11.1–11.6. Chapter 10 established that hydrogen's energies depend only
on $n$. Chapter 11 explains why every other atom is different: the valence
electron of an alkali sees a nuclear charge that is *screened* by the closed
inner shells, and the degree of screening depends on how much the orbital
penetrates the core — which depends on $\ell$. This experiment measures that
$\ell$-dependence directly.

The X-ray apparatus this laboratory once used for Moseley's law is no longer
serviceable. The quantum defect measured here probes exactly the same physics
— screening of the nuclear charge by inner electrons — from the valence side
rather than the core side.

## Theory

### The quantum defect

For a single valence electron outside a closed-shell core, the energy levels
are well described by a Rydberg formula with a shifted principal quantum
number:

$$
E_{n\ell} = -\frac{hcR_{\text{A}}}{(n - \delta_\ell)^2} ,
$$ (eq-qd-energy)

where $\delta_\ell$ is the **quantum defect**. It is very nearly independent of
$n$ for a given $\ell$ — a fact that is not obvious and is the reason the
description is useful — and it decreases rapidly with $\ell$. For sodium the
approximate values are

$$
\delta_s \approx 1.373, \qquad
\delta_p \approx 0.883, \qquad
\delta_d \approx 0.010, \qquad
\delta_f \approx 0.000 .
$$

These are quoted to three decimal places for a reason: the transition energy
depends on the *difference* of two terms, each of which is sensitive to its
defect, so a change of $0.02$ in $\delta_s$ moves the predicted D-line
wavelength by tens of nanometres. Quantum defects have to be known well to be
useful, and your measurement has to be correspondingly good.

```{figure} ../images/exp11-quantum-defect-concept.svg
:label: fig:exp11-quantum-defect
:alt: For n=3 and n=4, the hydrogenic energy is shown as a dashed horizontal line, and the actual s, p, d, f sodium levels are marked below it; the s and p levels sit well below the hydrogenic line while d and f sit almost on it.

Quantum defects, for $n=3$ and $n=4$. If sodium's valence electron were hydrogenic, every $\ell$ would sit on the dashed line for its $n$. Instead $s$ and $p$ are pulled well below it — pulled hardest for $s$, which penetrates the core most — while $d$ and $f$ are nearly hydrogenic.
```

The physical reading: a low-$\ell$ orbital has appreciable probability density
near the nucleus, where it sees the *unscreened* nuclear charge $Z$ rather
than the screened $Z_{\text{eff}} \approx 1$. It is therefore bound more
tightly than a hydrogenic level of the same $n$, and $\delta_\ell$ measures the
extra binding in units of a principal quantum number. High-$\ell$ orbitals are
kept out of the core by the centrifugal barrier $\ell(\ell+1)\hbar^2/2mr^2$,
see almost pure $Z_{\text{eff}} = 1$, and are almost exactly hydrogenic — which
is why $\delta_d \approx 0$.

### The series

Transitions in an alkali obey $\Delta\ell = \pm1$, and the classical
spectroscopic series are

:::{list-table} Sodium series (all terminating on or starting from low-lying states)
:header-rows: 1

* - Series
  - Transition
  - Historical name's origin
* - Principal
  - $np \to 3s$
  - Strongest in absorption; includes the D lines at $n=3$
* - Sharp
  - $ns \to 3p$
  - Narrow lines
* - Diffuse
  - $nd \to 3p$
  - Broader-looking (unresolved fine structure)
* - Fundamental
  - $nf \to 3d$
  - In the infrared
:::

The letters $s$, $p$, $d$, $f$ — now the standard orbital labels throughout
physics and chemistry — are the initials of *sharp*, *principal*, *diffuse*,
and *fundamental*: the names of these spectral series, assigned before anyone
knew what an orbital was.

### Spin–orbit splitting

The D "line" of sodium is two lines, at $588.995$ and $589.592\ \text{nm}$ —
a separation of $0.597\ \text{nm}$, or about $17.2\ \text{cm}^{-1}$. The
$3p$ level is split by the spin–orbit interaction into $3p_{1/2}$ and
$3p_{3/2}$; the $3s$ ground state, having $\ell = 0$, is not split. The
splitting scales roughly as $Z_{\text{eff}}^4/n^3\ell(\ell+1)$, which is why it
is $0.6\ \text{nm}$ in sodium, $2\ \text{nm}$ in potassium, and unmeasurably
small in hydrogen's Balmer lines with the same instrument.

Measuring this splitting is a direct measurement of a relativistic effect —
the interaction between the electron's spin magnetic moment and the magnetic
field it experiences in the nucleus's rest frame — with a bench spectrometer.

## Pre-lab

:::{exercise}
:label: q-qd-01

Using [](#eq-qd-energy) with $\delta_s = 1.373$ and $\delta_p = 0.883$ and
$R_{\text{A}} = 1.0974\times10^{7}\ \text{m}^{-1}$, compute the wavelength of
the $3p \to 3s$ transition in sodium and compare with $589.3\ \text{nm}$. Then
recompute with $\delta_s = 1.35$ and with $\delta_s = 1.30$, and comment on
the sensitivity.
:::

:::{exercise}
:label: q-qd-02

Compute the ionization energy of sodium from [](#eq-qd-energy) with $n = 3$,
$\ell = 0$, and compare with the accepted $5.14\ \text{eV}$. Do the same
calculation treating sodium as hydrogenic with $n = 3$ (i.e. $\delta = 0$) and
comment on the size of the discrepancy.
:::

:::{exercise}
:label: q-qd-03

Convert the D-line splitting of $0.597\ \text{nm}$ at $589\ \text{nm}$ into
(a) a wavenumber difference in $\text{cm}^{-1}$, (b) an energy in
$\text{meV}$, and (c) the required resolving power $\lambda/\Delta\lambda$.
Compare (c) with the resolving power you measured in [](#q-diff-07).
:::

:::{exercise}
:label: q-qd-04

Look up, in the NIST Atomic Spectra Database, the wavelengths and assignments
of the six strongest sodium lines between $400$ and $700\ \text{nm}$.
Tabulate them with their upper and lower terms. You will use this table to
assign your measured lines, so bring it.
:::

## Apparatus

- Sodium discharge lamp (or a sodium spectral tube), with the warm-up time it
  needs — a cold Na lamp emits mostly neon and looks red
- Mercury and helium lamps for calibration
- Grating spectrometer with the best resolving power available, or the
  EDU-SPEB2 kit; a narrow entrance slit is essential. The kit resolves the
  sodium D doublet, but the weaker-series objective is exploratory and depends
  on detector sensitivity.
- Neutral-density filters (the D lines are extremely bright and will saturate
  a detector that is set correctly for the weaker series members)
- Optionally: potassium or lithium lamps, for the $Z$ dependence

:::{danger}
Discharge tube supplies at several kilovolts; lamps get hot. Sodium lamps in
particular run hot and take many minutes to cool. See [](#lab-safety).
:::

```{figure} ../images/exp11-sodium-spectrometer-schematic.svg
:label: fig:exp11-spectrometer
:alt: The same grating spectrometer as the Balmer experiment, now fed by a sodium discharge lamp, with the closely spaced D1 and D2 lines diffracting to nearly the same angle.

The same spectrometer at its highest resolving power. The sodium D lines sit close enough together that resolving them is itself a test of the instrument, not just of the source.
```

## Procedure

### Part A — Calibration, again

1. Calibrate exactly as in [](#exp-balmer), using mercury, and check against
   helium. Push the resolution: narrow the slit until the mercury yellow
   doublet at $576.96$ and $579.07\ \text{nm}$ is cleanly separated.
2. Record the calibration residuals.

**[ ] Checkpoint 1.** Demonstrate that you can resolve the
mercury yellow doublet ($\Delta\lambda = 2.1\ \text{nm}$). If you cannot, you
will certainly not resolve the sodium D lines at $0.6\ \text{nm}$, and you
should fix the instrument before continuing.

### Part B — The D doublet

3. Let the sodium lamp warm up fully. Attenuate it.
4. Locate the D lines and resolve them. Narrow the slit until the splitting is
   clear, then narrow it further until the lines stop getting sharper.
5. Measure both wavelengths, at least five times each, alternating the
   approach direction.
6. Record the slit width and, if possible, repeat at two slit widths to check
   for a slit-dependent shift.

**[ ] Checkpoint 2.** Show the instructor the resolved
doublet and your measured splitting before moving on.

### Part C — The series

7. Remove the attenuation and search the visible for the weaker sodium lines
   from your NIST table. They are much fainter than the D lines; work in a
   darkened room and give the detector time.
8. Measure as many as you can find. Treat six lines beyond the doublet as an
   aspirational target, not a pass/fail requirement: the D lines are much
   brighter than the higher-series lines, so report the detection limit and any
   unassigned lines.
9. Assign each to a transition using your table, and record which assignments
   you are confident in and which you are not. An honest "unassigned" is
   better than a forced assignment.

### Part D (optional) — Another alkali

10. If a potassium or lithium lamp is available, measure its principal doublet
    and compare the splitting with sodium's. Lithium's is far smaller,
    potassium's far larger.

## Analysis

### The splitting

Report $\Delta\lambda$ and convert to $\Delta E$:

$$
\Delta E = hc\left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right) .
$$

Note that this is again a small difference of two nearly equal numbers, so
propagate carefully; the fractional uncertainty on $\Delta E$ is far larger
than that on either $\lambda$. See the warning in [](#uncertainty).

### Quantum defects

For each assigned line, the transition energy is the difference of two levels
from [](#eq-qd-energy). Work in wavenumbers, $\tilde\nu = 1/\lambda$. For the
sharp series, $ns \to 3p$:

$$
\tilde\nu = \frac{R_{\text{A}}}{(3-\delta_p)^2} - \frac{R_{\text{A}}}{(n-\delta_s)^2} ,
$$

and analogously for the diffuse series with $\delta_d$ in place of $\delta_s$.
Fit the defects to all the assigned lines simultaneously:

```python
import numpy as np
from scipy.optimize import curve_fit

R = 1.0973731568e7      # 1/m; the alkali core correction is well below our precision

# rows: (series_id, n)   series_id 0 = sharp (ns->3p), 1 = diffuse (nd->3p)
series = np.array([...])
n_up   = np.array([...])
nu     = 1.0 / lam                       # measured wavenumbers, 1/m
snu    = slam / lam**2

def model(idx, d_s, d_p, d_d):
    s, n = idx[:, 0], idx[:, 1]
    d_up = np.where(s == 0, d_s, d_d)
    return R / (3 - d_p)**2 - R / (n - d_up)**2

idx = np.column_stack([series, n_up])
popt, pcov = curve_fit(model, idx, nu, p0=[1.373, 0.883, 0.010],
                       sigma=snu, absolute_sigma=True)
```

The D lines alone constrain the combination $\delta_s$–$\delta_p$; you need at
least one member of a second series to separate them. Say in the report which
of your parameters is well determined and which is only constrained in
combination — and check the off-diagonal elements of `pcov` to support the
claim.

### Screening

Convert each quantum defect into an effective nuclear charge seen by the
valence electron, by asking what $Z_{\text{eff}}$ would give the same binding
energy in a hydrogenic level of the same $n$:

$$
\frac{Z_{\text{eff}}^2}{n^2} = \frac{1}{(n-\delta_\ell)^2}
\qquad\Longrightarrow\qquad
Z_{\text{eff}} = \frac{n}{n-\delta_\ell} .
$$

Report $Z_{\text{eff}}$ for the $3s$, $3p$, and $3d$ states of sodium and
compare with $Z = 11$ (bare nucleus) and $Z_{\text{eff}} = 1$ (fully screened).

## Post-lab questions

:::{exercise}
:label: q-qd-05

Report the D-line splitting in nm, $\text{cm}^{-1}$, and meV, with
uncertainties, and compare with the accepted $17.2\ \text{cm}^{-1}$.
:::

:::{exercise}
:label: q-qd-06

Report $\delta_s$, $\delta_p$, $\delta_d$ with uncertainties. Explain the
ordering $\delta_s > \delta_p > \delta_d$ physically, referring to the radial
probability density near the nucleus and to the centrifugal barrier.
:::

:::{exercise}
:label: q-qd-07

Report $Z_{\text{eff}}$ for the $3s$ and $3d$ states. The $3d$ value should be
close to 1. Explain what that means about where a $3d$ electron in sodium
spends its time.
:::

:::{exercise}
:label: q-qd-08

In hydrogen, $2s$ and $2p$ are degenerate. In sodium, $3s$ and $3p$ are
separated by $2.1\ \text{eV}$. Explain what symmetry hydrogen has that sodium
lacks — and connect this to the degeneracy-splitting you measured
mechanically in [](#exp-eigenmodes).
:::

:::{exercise}
:label: q-qd-09

The spin–orbit splitting scales roughly as $Z_{\text{eff}}^4$. Given sodium's
$17.2\ \text{cm}^{-1}$, predict the splitting for potassium's principal
doublet and compare with the accepted $57.7\ \text{cm}^{-1}$
($766.5$/$769.9\ \text{nm}$). Does the scaling work? What does the discrepancy
tell you about the crudeness of the $Z_{\text{eff}}^4$ rule?
:::

:::{exercise}
:label: q-qd-10

Moseley found that the square root of the frequency of the characteristic
X-ray $K_\alpha$ line varies linearly with $Z$, with a screening constant of
about 1. Explain what is being screened in his case and what is being screened
in yours, and why the two screening constants are so different (about 1 versus
about 10).
:::

## Going further

- **The Zeeman effect.** With a strong permanent magnet or a small
  electromagnet around a discharge tube, the sodium D lines split further in a
  magnetic field. The $D_1$ line splits into four components and $D_2$ into
  six — the *anomalous* Zeeman effect, which was inexplicable before electron
  spin and which is the most direct optical evidence for it.
- **Absorption instead of emission.** A sodium vapour cell heated in the path
  of a white-light source gives the D lines in absorption — the same
  Fraunhofer D lines catalogued in the solar spectrum in 1814, a decade before
  anyone knew what sodium was doing in the Sun.
- **Rydberg states.** With a good spectrometer the sharp series can be
  followed to high $n$, where the levels crowd toward the series limit. Fitting
  the limit gives the ionization energy directly, and the near-constancy of
  $\delta_\ell$ across a dozen values of $n$ is the strongest evidence that the
  quantum defect is a real property of the core rather than a fitting fudge.

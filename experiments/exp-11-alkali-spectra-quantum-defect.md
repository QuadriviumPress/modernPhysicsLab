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
**You will measure** the sodium D splitting if resolved and, if weaker lines are detected, state-specific $s$, $p$, and $d$ quantum defects using a tabulated ionization limit
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Test whether the spectrometer resolves the sodium D doublet, measure its
  splitting if it does, and interpret it as spin–orbit coupling.
- Assign observed sodium lines to transitions and, where the faint lines are
  detected, infer state-specific quantum defects from their level energies
  and an independent ionization limit.
- Explain why the quantum defect decreases sharply with increasing $\ell$, in
  terms of the penetration of the valence orbital into the core.
- Explain why hydrogen's simple-Coulomb $\ell$ degeneracy is generally
  broken in many-electron atoms.

## Textbook connection

Read §11.1–11.6. Chapter 10 established that hydrogen's energies depend only
on $n$. Chapter 11 explains why every other atom is different: the valence
electron of an alkali sees a nuclear charge that is *screened* by the closed
inner shells, and the degree of screening depends on how much the orbital
penetrates the core — which depends on $\ell$. The optional weak-line
measurements probe that $\ell$ dependence.

The X-ray apparatus this laboratory once used for Moseley's law is no longer
serviceable. Quantum defects and Moseley's law both involve electron
screening, but they probe different orbitals and different energy scales.

## Theory

### The quantum defect

For a single valence electron outside a closed-shell core, an energy level
measured relative to the ionization limit is often described by a Rydberg
formula with a shifted principal quantum number:

$$
E_{n\ell j} = -\frac{hcR_{\text{Na}}}{(n - \delta_{n\ell j})^2} ,
$$ (eq-qd-energy)

where $\delta_{n\ell j}$ is the **quantum defect**, $j$ identifies a resolved
fine-structure level, and $R_{\text{Na}}$ includes the sodium ion's reduced
mass. A defect changes slowly with $n$ within a series but is not strictly
constant, especially for low-$n$ $s$ states. For sodium, representative values
for the lowest available states are

$$
\delta_{3s} \approx 1.373, \qquad
\delta_{3p} \approx 0.883, \qquad
\delta_{3d} \approx 0.010, \qquad
\delta_{4f} \approx 0.001 .
$$

These values use the [NIST sodium levels and ionization limit](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable5_a.htm)
and its [extended Na I level compilation](https://www.nist.gov/system/files/documents/srd/jpcrd3720081763p.pdf)
with a leading-order Rydberg model. The $5s$ defect is about $1.353$, so
carrying $\delta_{3s}=1.373$ unchanged to another $n$ can matter. The D-line
prediction is sensitive to the rounded $3s$ and $3p$ defects; compare it at
the precision the model and wavelength convention support.

```{figure} ../images/exp11-quantum-defect-concept.svg
:label: fig:exp11-quantum-defect
:alt: For n=3 the s, p, and d sodium levels are below a dashed hydrogenic reference; for n=4 the s, p, d, and f levels are below another reference. There is no n=3 f orbital. Low angular momentum states shift downward most.

Quantum defects for allowed states at $n=3$ and $n=4$. The dashed lines show a
hydrogenic reference for each $n$; penetration into the core pulls $s$ and
$p$ levels down most. The orbital labels obey $\ell<n$.
```

The physical reading: a low-$\ell$ orbital has appreciable probability density
near the nucleus, where it sees the *unscreened* nuclear charge $Z$ rather
than the long-range ionic-core charge near $+1$. It is therefore bound more
tightly than a hydrogenic level of the same $n$, and $\delta_{n\ell j}$ measures the
extra binding in units of a principal quantum number. High-$\ell$ orbitals are
kept out of the core by the centrifugal barrier $\ell(\ell+1)\hbar^2/2mr^2$,
see a long-range Coulomb charge near $+1$, and are almost hydrogenic — which
is why $d$ and $f$ defects are much smaller than $s$ defects.

### The series

Transitions in an alkali obey $\Delta\ell = \pm1$, and the classical
spectroscopic series are

:::{list-table} Sodium series (all terminating on or starting from low-lying states)
:header-rows: 1

* - Series
  - Transition
  - Accessible member or note
* - Principal
  - $np \to 3s$
  - Strongest in absorption; includes the D lines at $n=3$
* - Sharp
  - $ns \to 3p$
  - Includes the visible $5s\to3p$ pair near 615 nm
* - Diffuse
  - $nd \to 3p$
  - Includes the visible $4d\to3p$ group near 568 nm
* - Fundamental
  - $nf \to 3d$
  - In the infrared
:::

The letters $s$, $p$, $d$, $f$ — now the standard orbital labels throughout
physics and chemistry — are the initials of *sharp*, *principal*, *diffuse*,
and *fundamental*: the names of these spectral series, assigned before anyone
knew what an orbital was.

### Spin–orbit splitting

The D "line" of sodium is two standard-air lines, at $588.995$ and
$589.592\ \text{nm}$ — a separation of $0.597\ \text{nm}$, or about
$17.2\ \text{cm}^{-1}$. The $3p$ level is split by the spin–orbit
interaction into $3p_{1/2}$ and
$3p_{3/2}$; the $3s$ ground state has no spin–orbit doublet. Potassium's
principal doublet is near $766.5/769.9\ \text{nm}$, outside the range of
some visual spectrometers and detectors. Its different splitting reflects
both nuclear charge and the valence electron's orbital penetration; no
universal $Z_{\text{eff}}^4$ rule predicts it from sodium alone.

Measuring this splitting tests the relativistic spin–orbit interaction in an
atomic spectrum. The simple magnetic-field picture is only an approximation
for an alkali electron moving through a screened core potential.

## Pre-lab

:::{exercise}
:label: q-qd-01

Using [](#eq-qd-energy) with $\delta_{3s} = 1.373$,
$\delta_{3p} = 0.883$, and
$R_{\text{Na}}\approx1.09735\times10^{7}\ \text{m}^{-1}$,
compute the approximate *vacuum* wavelength of
$3p \to 3s$. Compare with the D lines near $589\ \text{nm}$ in air, noting
the wavelength convention and unresolved fine structure. Then recompute
with $\delta_{3s} = 1.35$ and $1.30$ to test sensitivity.
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
Compare (c) with the grating-only limit you calculated in [](#q-diff-07)
and the measured width of your complete spectrometer.
:::

:::{exercise}
:label: q-qd-04

Use the [NIST Na I line data](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable2.htm)
to list the D doublet near 589 nm, the $4d\to3p$ group near 568 nm, and
the $5s\to3p$ pair near 615 nm. Look up their upper and lower $j$ values
in the Atomic Spectra Database. Which pair near 568.8 nm is too close
to treat as two independently resolved centers on a typical teaching
spectrometer? Calculate the resolving power needed and compare with the
measured instrument width.
:::

## Apparatus

- Sodium discharge lamp or sodium spectral tube, with the warm-up time specified
  for that source; some sodium lamps show startup-gas lines before stabilizing
- Mercury and helium lamps for calibration
- Calibrated grating spectrometer or EDU-SPEB2 kit. Test the actual resolution
  with nearby reference lines; a narrow slit helps only until signal and the
  instrument profile limit the result. Weak-line detection depends on source
  brightness, detector sensitivity, and spectral coverage.
- Neutral-density filters for a detector that would saturate on the D lines
  at the settings needed for weaker members
- Optionally: potassium or lithium lamps for a qualitative doublet comparison

:::{danger}
Discharge supplies can run at high voltage, and lamps can remain hot after
shutdown. Use the equipment's specified shutdown and cooling procedure
before changing a tube or touching the lamp. See [](#lab-safety).
:::

```{figure} ../images/exp11-sodium-spectrometer-schematic.svg
:label: fig:exp11-spectrometer
:alt: A sodium lamp illuminates an entrance slit and collimator before a reflective grating. The nearby D1 and D2 directions return on the incident side; their separation is exaggerated for clarity.

The reflective-grating layout from Experiment 10, now with sodium. The D-ray
separation is exaggerated; resolve the pair experimentally before reporting
two centers.
```

## Procedure

### Before you search for weak lines

- Use [](#fig:exp11-spectrometer) to identify the same calibrated spectrometer
  geometry used in Experiment 10. The labeled D rays show why resolution is
  needed; their separation in the drawing is deliberately exaggerated.
- Warm the alkali lamp until its intensity is stable. Keep the lamp supply
  covered, switch it off before exchanging lamps, and avoid touching a hot
  envelope.
- Record grating, slit width, spectral order, and viewing or detector method.
  For a detector, record integration time and gain and save a dark spectrum
  for each setting used for faint lines.
- Prepare a search list from the NIST reference data, with predicted
  wavelength, transition, observed wavelength, trial count, signal-to-noise
  ratio, and assignment confidence. Also keep an “unassigned” list.
- Take an overview spectrum before narrowing the slit. Use that spectrum to
  navigate, but use unsaturated high-resolution scans for line centers; do not
  extract the D splitting from a clipped overview.

### Part A — Calibration, again

1. Calibrate the actual grating geometry or pixel scale as in [](#exp-balmer),
   using resolved mercury lines and, if needed to cover 615 nm, the helium
   line near 667.8 nm as a calibration anchor or held-out check. State which
   role each line has.
   Resolve the mercury yellow lines at $576.96$ and $579.07\ \text{nm}$
   as a preliminary instrument check.
2. Record calibration residuals and a held-out check. Measure the width of
   an isolated narrow reference line near the D region at the same slit and
   detector settings. A width well below $0.6\ \text{nm}$ and adequate
   sampling are needed to attempt the D splitting; resolving the 2.1 nm
   mercury pair alone does not demonstrate this.

**[ ] Checkpoint 1.** Show the calibration and measured reference-line
width. Decide whether the instrument can plausibly separate the D lines,
and record the limitation if it cannot.

### Part B — The D doublet

3. Let the sodium lamp warm up fully. Attenuate it.
4. Locate the D feature. Narrow the slit while tracking signal and line width;
   fit or read two centers only if the pair is resolved under those settings.
5. If resolved, measure both wavelengths at least five times each. Alternate
   approach direction on a vernier instrument to expose backlash. If not
   resolved, record one feature and a resolution limit instead.
6. Record the slit width and, if possible, repeat at two slit widths to check
   for a slit-dependent shift.

**[ ] Checkpoint 2.** Show the instructor the D profile, your measured
splitting or resolution limit, and the settings used.

### Part C — The series

7. Remove attenuation, adjust exposure without saturating, and search for the
   $4d\to3p$ group near 568 nm and $5s\to3p$ pair near 615 nm. These are
   much fainter than the D lines; measure background at each detector setting.
8. Measure as many independent centers as the instrument can resolve. In
   particular, the two components near 568.819 and 568.821 nm will normally
   form one blend. Report non-detections with the achieved sensitivity rather
   than inventing six extra lines.
9. Assign each to a transition using your table, and record which assignments
   you are confident in and which you are not. An honest "unassigned" is
   better than a forced assignment. Recheck a blue and red calibration line
   at the settings used for the weak lines and include any drift.

### Part D (optional) — Another alkali

10. If a potassium lamp and suitable near-IR detector are available, test its
    principal doublet near 766.5/769.9 nm. If using lithium near 671 nm,
    check whether the instrument can actually resolve its much closer pair
    before reporting a splitting.

## Analysis

### The splitting

If both D centers are resolved, report their separation and convert to
$\Delta E$ using *vacuum* wavelengths, with $\lambda_1$ the shorter:

$$
\Delta E = hc\left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right) .
$$

This is a small difference of two nearby numbers. Propagate the covariance
of the calibrated line centers: a common wavelength offset can largely
cancel in the splitting, while uncertainty in the dispersion scale does
not. See [](#uncertainty). If unresolved, report the observed width and
the inability to determine the splitting under those settings. An upper
limit requires a justified instrument-profile model.

### Quantum defects

Use measured vacuum wavenumbers to reconstruct levels above the $3s$ ground
state. D$_1$ is $3p_{1/2}\to3s$ and D$_2$ is $3p_{3/2}\to3s$.
The visible sharp-series line near 615.4225 nm is
$5s_{1/2}\to3p_{1/2}$; the unblended diffuse-series line near
568.2633 nm is $4d_{3/2}\to3p_{1/2}$. These assignments and approximate
standard-air wavelengths come from the [NIST Na I line data](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable2.htm)
and [level compilation](https://www.nist.gov/system/files/documents/srd/jpcrd3720081763p.pdf).
Thus, in inverse metres,

$$
T_{3p_{1/2}}=\tilde\nu_{\mathrm{D1}},\qquad
T_{5s}=\tilde\nu_{\mathrm{D1}}+\tilde\nu_{615.4},\qquad
T_{4d_{3/2}}=\tilde\nu_{\mathrm{D1}}+\tilde\nu_{568.3}.
$$

With the independent [NIST Na I ionization limit](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable5_a.htm)
$T_\infty=41449.451\ \text{cm}^{-1}$, derive a defect for each measured
state from

$$
\delta_{n\ell j}=n-\sqrt{\frac{R_{\text{Na}}}{T_\infty-T_{n\ell j}}}.
$$ (eq-qd-from-level)

Here $R_{\text{Na}}\approx1.097347\times10^7\ \text{m}^{-1}$ accounts
approximately for the reduced mass of the sodium ion. A term-average
$3p$ level can be formed as $(T_{3p_{1/2}}+2T_{3p_{3/2}})/3$; the
weights are the fine-structure degeneracies $2j+1$. Keep the
$j$-resolved levels when comparing individual observed lines.

The following code assumes all four indicated centers were measured.
Supply their *vacuum* wavelengths in the specified order and the full
wavelength covariance matrix, including shared calibration terms:

```python
import numpy as np

R_Na = 1.097347e7          # m^-1, approximate sodium reduced-mass value
T_limit = 41449.451 * 100  # m^-1, external NIST reference
lam = np.array([...])       # vacuum meters: D1, D2, 615.4225, 568.2633
C_lam = np.array([...])     # 4 x 4 covariance of these wavelengths, m^2

def defects(wavelengths):
    nu = 1.0 / wavelengths
    T_p = (nu[..., 0] + 2 * nu[..., 1]) / 3  # 3p term average
    T_s = nu[..., 0] + nu[..., 2]           # 5s from D1 and 615.4
    T_d = nu[..., 0] + nu[..., 3]           # 4d_3/2 from D1 and 568.3
    T = np.stack([T_p, T_s, T_d], axis=-1)
    return np.array([3, 5, 4]) - np.sqrt(R_Na / (T_limit - T))

delta = defects(lam)        # 3p average, 5s, 4d_3/2
rng = np.random.default_rng(11)
draws = rng.multivariate_normal(lam, C_lam, size=10000)
s_delta = defects(draws).std(axis=0, ddof=1)
for name, value, uncertainty in zip(("3p", "5s", "4d_3/2"), delta, s_delta):
    print(f"delta_{name} = {value:.4f} +/- {uncertainty:.4f}")
```

Use the line-center covariance from calibration and repeats when estimating
these uncertainties. Vary the air-index conversion and ionization limit if
their uncertainties matter at your precision. The measured D pair and
external limit can give a $3p$ defect; $5s$ and $4d$ defects require their
respective weak lines. The $3s$ defect computed from the external limit
alone is a **reference value**, not a quantity measured by this experiment.
Compare $5s$ with that reference, noting that an $n$-independent $s$ defect
is only an approximation.

### Screening

For each measured state, calculate an **energy-equivalent** effective charge:
the charge that would give the same binding energy in a hydrogenic formula
at the same $n$:

$$
\frac{Z_{\text{eq}}^2}{n^2} = \frac{1}{(n-\delta_{n\ell j})^2}
\qquad\Longrightarrow\qquad
Z_{\text{eq}} = \frac{n}{n-\delta_{n\ell j}} .
$$

Report $Z_{\text{eq}}$ only for states whose defects you determined. This
single number summarizes binding energy; the physical screening varies
with radius and is not a measured constant charge. Compare the values
with the long-range ionic-core charge $+1$ and bare nuclear charge $+11$.

## Post-lab questions

:::{exercise}
:label: q-qd-05

If resolved, report the D-line splitting in nm, $\text{cm}^{-1}$, and meV,
with uncertainties, and compare with $17.2\ \text{cm}^{-1}$. If unresolved,
report the measured profile and resolution limit.
:::

:::{exercise}
:label: q-qd-06

Report defects only for states supported by measured lines and the independent
ionization limit. For a complete data set, these are $\delta_{5s}$,
$\delta_{3p}$, and $\delta_{4d}$. Compare them with the reference
$\delta_{3s}$ and $\delta_{3d}$ values, and explain the trend with orbital
penetration and the centrifugal barrier.
:::

:::{exercise}
:label: q-qd-07

Report the energy-equivalent $Z_{\text{eq}}$ for your measured states.
Why should the $4d$ value be closer to 1 than the $5s$ value? Explain
why neither number is a literal radius-independent screened charge.
:::

:::{exercise}
:label: q-qd-08

In the nonrelativistic Coulomb model, hydrogen's $2s$ and $2p$ levels are
degenerate. Sodium's $3s$ and $3p$ levels differ by about $2.1\ \text{eV}$.
Explain the role of the Coulomb potential and core penetration, then compare
this with the symmetry-breaking cavity experiment in [](#exp-eigenmodes).
State one limit of that analogy.
:::

:::{exercise}
:label: q-qd-09

Potassium's principal doublet lies near $766.5$ and $769.9\ \text{nm}$,
with a wavenumber splitting near $57.7\ \text{cm}^{-1}$. Compare this
with sodium's $17.2\ \text{cm}^{-1}$. Why does a single $Z_{\text{eq}}^4$
factor from the binding energies fail as a quantitative prediction for
two different alkali atoms?
:::

:::{exercise}
:label: q-qd-10

Moseley's approximate $K_\alpha$ relation uses a core-electron screening
constant near 1. Contrast its inner-shell transition with the outer-valence
states studied here. Why should one avoid treating your energy-equivalent
$Z_{\text{eq}}$ as a direct measurement of a fixed ten-electron screening
constant?
:::

## Going further

- **The Zeeman effect.** With an approved magnet and optical geometry, the
  sodium D profiles can show additional polarization-dependent components.
  Predict the allowed $m_j$ transitions and compare their separation with
  your measured instrumental width before attempting to resolve them.
- **Absorption instead of emission.** With an approved heated sodium vapor
  cell and broadband source, the D lines can appear in absorption, as
  they do among the solar Fraunhofer lines.
- **Rydberg states.** With wider spectral coverage and adequate sensitivity,
  follow several members of one series toward its limit. Fit their level
  energies to determine the ionization limit and examine how its quantum
  defect changes with $n$; a visible-only scan of the D and weak pairs does
  not establish the series limit.

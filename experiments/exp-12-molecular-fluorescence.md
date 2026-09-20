---
title: Molecular Fluorescence, the Stokes Shift, and Franck–Condon
short_title: 12. Molecular Fluorescence
label: exp-fluorescence
numbering:
  enumerator: "12.%s"
---

# Experiment 12 — Molecular Fluorescence, the Stokes Shift, and Franck–Condon

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 12, *Molecular Structure*
**Apparatus** Spectrometer kit, UV/blue LEDs, cuvettes, fluorescein or quinine solutions
**You will measure** absorption and emission spectra, a molar absorptivity, and a Stokes shift
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure an absorption spectrum and verify the Beer–Lambert law over a range
  of concentrations.
- Measure a fluorescence emission spectrum and determine the Stokes shift.
- Interpret the Stokes shift and the approximate mirror symmetry of the two
  spectra in terms of the Franck–Condon principle and vibrational relaxation.
- Estimate a vibrational energy quantum from spectroscopic data and compare it
  with $k_BT$.

## Textbook connection

Read §12.4–12.7. Chapter 12 builds molecular energy levels as a hierarchy:
electronic states separated by a few eV, vibrational levels within them
separated by tenths of an eV, and rotational levels by meV. Everything you
measure this afternoon is a consequence of that hierarchy and of the fact that
electronic transitions happen far faster than nuclei can move.

## Theory

### Why absorption and emission are not at the same wavelength

The Franck–Condon principle: an electronic transition occurs so quickly
compared with nuclear motion that the nuclei do not move during it. On a
potential-energy diagram, transitions are therefore **vertical**.

The excited electronic state generally has a different equilibrium bond length
from the ground state. So a vertical transition upward from the ground state's
$v=0$ level lands on a *vibrationally excited* level of the excited electronic
state. The molecule then relaxes non-radiatively to $v'=0$ of the excited
state, in picoseconds, dumping that vibrational energy into the solvent. Only
then does it emit — and the vertical transition back down lands on a
vibrationally excited level of the *ground* state, which again relaxes.

The consequence: **emission is always at lower photon energy than absorption**,
by the sum of the two relaxation energies. That difference is the **Stokes
shift**,

$$
\Delta\tilde\nu_{\text{Stokes}} = \tilde\nu_{\text{abs,max}} - \tilde\nu_{\text{em,max}},
$$ (eq-stokes)

conventionally quoted in $\text{cm}^{-1}$ because it is an energy difference,
not a wavelength difference. (Quoting a Stokes shift in nanometres is common
and nearly meaningless, since the same energy shift corresponds to very
different wavelength shifts in different parts of the spectrum. Do it in
wavenumbers.)

### The mirror-image rule

If the vibrational level spacings are similar in the ground and excited
electronic states — usually roughly true — then the *pattern* of
Franck–Condon factors going up is the same as going down. The emission
spectrum is therefore approximately the mirror image of the absorption
spectrum, reflected about the $0$–$0$ transition energy. Finding that mirror
line in your data locates the $0$–$0$ transition, which is a real
spectroscopic quantity you cannot read directly off either spectrum.

### Beer–Lambert

Light of intensity $I_0$ entering a sample of path length $\ell$ and
concentration $c$ emerges with

$$
I = I_0\,10^{-\varepsilon c \ell},
\qquad
A \equiv \log_{10}\frac{I_0}{I} = \varepsilon c \ell ,
$$ (eq-beer)

where $A$ is the absorbance and $\varepsilon$ the molar absorptivity, in
$\text{M}^{-1}\text{cm}^{-1}$. The law is linear in $c$ only while the
molecules absorb independently; at high concentration, aggregation and
re-absorption break it. Finding where it breaks is part of the experiment.

## Pre-lab

:::{exercise}
:label: q-fluor-01

Convert to wavenumbers and to eV: $\lambda = 490\ \text{nm}$ and
$\lambda = 514\ \text{nm}$. What is the Stokes shift between them, in
$\text{cm}^{-1}$ and in meV? Compare with $k_BT$ at room temperature
($207\ \text{cm}^{-1}$, $25.7\ \text{meV}$).
:::

:::{exercise}
:label: q-fluor-02

Fluorescein has $\varepsilon \approx 7.6\times10^{4}\ \text{M}^{-1}\text{cm}^{-1}$
at its peak. What concentration gives $A = 1.0$ in a $1.00\ \text{cm}$
cuvette? Express it in molarity and in mg/L ($M_r = 332\ \text{g/mol}$ for the
free acid).
:::

:::{exercise}
:label: q-fluor-03

Explain why an absorbance much above about 2 cannot be measured accurately
with a simple spectrometer. Compute the transmitted fraction at $A = 2$ and at
$A = 3$, and compare with the stray-light level of a typical compact
spectrometer ($\sim0.1\%$).
:::

:::{exercise}
:label: q-fluor-04

Sketch a potential-energy diagram with a ground and an excited electronic
state whose minima are offset in bond length. Mark the absorption transition,
the vibrational relaxation, the emission transition, and the Stokes shift.
:::

## Apparatus

- Thorlabs EDU-SPEA1/SPEB1 spectrometer kit, or a compact USB spectrometer
  with a fibre and a cuvette holder
- Broadband white LED or tungsten lamp, for the absorption measurement
- Excitation LEDs: $405\ \text{nm}$ and $470\ \text{nm}$, and a $365\ \text{nm}$
  UV LED if quinine is used
- Long-pass filter to block scattered excitation light from the emission
  measurement
- $1\ \text{cm}$ cuvettes; volumetric glassware; micropipettes
- Fluorophores: fluorescein in dilute NaOH, or quinine sulfate in
  $0.1\ \text{M}$ H$_2$SO$_4$, or tonic water; optionally rhodamine 6G in
  ethanol, and a chlorophyll extract from spinach in acetone
- Cuvette rack, lint-free wipes

:::{danger}
The $365\ \text{nm}$ and $405\ \text{nm}$ LEDs are bright and in or near the
ultraviolet, where there is no blink reflex and no visual warning of
overexposure. Never look at them directly, and shield the excitation path.
Ethanol and acetone are flammable; keep them away from the lamp. Gloves for
the dyes. See [](#lab-safety).
:::

```{figure} ../images/exp12-fluorescence-schematic.svg
:label: fig:exp12-fluorescence
:alt: Panel (a), an excitation LED illuminates a cuvette from the side, and a long-pass filter blocks the excitation light before the emitted fluorescence reaches the spectrometer at 90 degrees. Panel (b), a white lamp shines through the same cuvette in-line to the spectrometer for the absorption measurement.

Two geometries, one cuvette. (a) Excitation at 90 degrees to detection, with a long-pass filter, keeps the weak fluorescence from being swamped by scattered excitation light. (b) In-line transmission gives the absorption spectrum.
```

## Procedure

### Part A — Spectrometer setup

1. Record a **dark spectrum** (source blocked) and a **reference spectrum**
   (solvent-only cuvette in the beam). Every absorbance is computed from these
   two, so retake them whenever the geometry or integration time changes.
2. Verify the wavelength calibration against a mercury or a known LED line;
   the kit calibration can drift.
3. Confirm you are not saturating: the reference spectrum's peak should sit at
   roughly 70% of full scale.

**[ ] Checkpoint 1.** Show the instructor your dark and
reference spectra, and a solvent-only "absorbance" spectrum, which should be
flat and near zero. A sloping baseline here will masquerade as a spectral
feature later.

### Part B — Absorption and Beer–Lambert

4. Prepare a dilution series: at least six concentrations spanning two orders
   of magnitude, made by serial dilution from a stock. Record the actual
   volumes and propagate their uncertainties.
5. Record the absorbance spectrum of each. Note the peak wavelength and peak
   absorbance.
6. Note the concentration at which the peak absorbance passes about 2, and the
   concentration at which the peak *wavelength* starts to move — the second is
   evidence of aggregation and marks where [](#eq-beer) has failed physically,
   not just instrumentally.

### Part C — Emission

7. Choose a dilute sample, $A \lesssim 0.1$ at the excitation wavelength. This
   matters: at higher absorbance the excitation is absorbed in the first
   millimetre of the cuvette and the emitted light is re-absorbed on its way
   out — the **inner filter effect** — which distorts the emission spectrum
   toward longer wavelengths and will fake a larger Stokes shift.
8. Illuminate from the side, at $90°$ to the collection axis, so that
   unabsorbed excitation light does not enter the spectrometer.
9. Add the long-pass filter in front of the collection fibre.
10. Record the emission spectrum. Record also a blank (solvent only, same
    excitation) and subtract it — it removes Raman scattering from the solvent
    and any filter fluorescence.
11. Repeat with a second excitation wavelength. The emission spectrum should
    be **independent of excitation wavelength** (Kasha's rule); verifying this
    is a real test of the relaxation picture in the Theory section.

### Part D — Concentration and quenching

12. Record emission spectra across your dilution series at fixed excitation
    and geometry. Plot integrated emission against concentration. It should
    rise linearly and then bend over and fall — the inner filter effect and,
    at high concentration, self-quenching.

### Part E (optional) — Chlorophyll

13. Extract chlorophyll from spinach with acetone, filter, and record
    absorption and emission. Chlorophyll's Stokes shift is remarkably small,
    and the reason — a rigid conjugated ring whose geometry barely changes on
    excitation — is exactly the Franck–Condon argument run in reverse.

## Analysis

### Beer–Lambert

```python
import numpy as np
from scipy.optimize import curve_fit

A  = np.array([...])           # peak absorbance
sA = np.array([...])
c  = np.array([...])           # molarity
sc = np.array([...])

sel = A < 1.5                  # stay in the linear, measurable region
popt, pcov = curve_fit(lambda c, eps: eps * 1.0 * c,      # ell = 1.00 cm
                       c[sel], A[sel], sigma=sA[sel], absolute_sigma=True)
eps, seps = popt[0], np.sqrt(pcov[0, 0])
```

Plot all the points, but fit only the linear region, and show on the figure
where you cut. Report $\varepsilon$ with its uncertainty and compare with the
literature value.

### Stokes shift and the mirror line

Convert both spectra to a wavenumber axis before comparing peaks. **Also
convert the intensities**: a spectrum recorded per unit wavelength must be
multiplied by $\lambda^2$ to become a spectrum per unit wavenumber, because
$I_{\tilde\nu} = I_\lambda\,|d\lambda/d\tilde\nu| = I_\lambda \lambda^2$.
Skipping this shifts the apparent emission peak by tens of $\text{cm}^{-1}$
and is one of the most common errors in undergraduate fluorescence reports.

```python
nu_abs = 1e7 / lam_abs                    # cm^-1 from nm
I_nu   = I_lam * lam**2                   # Jacobian for the axis change
```

Find both peaks by fitting a low-order polynomial or a Gaussian to the top
20% of each band, rather than by taking the argmax of noisy data. Report
$\Delta\tilde\nu_{\text{Stokes}}$ with uncertainty.

Then find the mirror line: reflect the absorption spectrum about a trial
wavenumber $\tilde\nu_{00}$ and vary $\tilde\nu_{00}$ to maximize the overlap
with the emission spectrum. That optimum is your estimate of the $0$–$0$
transition energy, and half the Stokes shift on each side is the relaxation
energy in each electronic state.

### A vibrational quantum

If your spectra show resolved vibronic structure — likely for quinine and for
a cooled or rigid sample, unlikely for fluorescein in water at room
temperature — measure the spacing of successive peaks. That spacing is the
vibrational quantum $\hbar\omega$ of the mode coupled to the transition.
Report it in $\text{cm}^{-1}$ and meV, and compare with $k_BT$ to explain why
essentially all molecules start from $v = 0$.

If no structure is resolved, estimate an upper bound on the vibrational
spacing from the fact that it is unresolved, and say so — a bound is a result.

## Post-lab questions

:::{exercise}
:label: q-fluor-05

Report $\varepsilon$ at the absorption peak with its uncertainty and compare
with the literature. Over what absorbance range was [](#eq-beer) linear in
your data, and what limited it at each end?
:::

:::{exercise}
:label: q-fluor-06

Report the Stokes shift in $\text{cm}^{-1}$ and eV. Compare it with $k_BT$ and
with a typical molecular vibrational quantum. How many vibrational quanta are
dissipated per absorbed photon?
:::

:::{exercise}
:label: q-fluor-07

Did your emission spectrum depend on the excitation wavelength? State what
Kasha's rule predicts and whether your data support it, with numbers.
:::

:::{exercise}
:label: q-fluor-08

Explain, using your data, how you could tell the inner filter effect from
genuine self-quenching. What measurement would distinguish them?
:::

:::{exercise}
:label: q-fluor-09

The mirror-image rule worked well or badly for your molecule. Either way,
explain what its success or failure implies about the vibrational frequencies
in the two electronic states.
:::

:::{exercise}
:label: q-fluor-10

A photon absorbed at $470\ \text{nm}$ and emitted at $514\ \text{nm}$ has lost
energy. Where did it go? Account for it explicitly, and explain why this does
not violate energy conservation.
:::

## Going further

- **Fluorescence quantum yield.** Comparing integrated emission against a
  standard of known yield (quinine sulfate, $\Phi = 0.546$ in
  $0.1\ \text{M}$ H$_2$SO$_4$) gives the fraction of absorbed photons that are
  re-emitted. It is a genuinely useful measurement and requires careful
  attention to the absorbance matching between sample and standard.
- **Iodine vapour.** A sealed I$_2$ cell in a white beam shows hundreds of
  resolved vibronic lines in absorption. Fitting the band-head spacings to a
  Morse potential gives the vibrational constant $\omega_e$, the anharmonicity
  $\omega_e x_e$, and — by Birge–Sponer extrapolation — the dissociation
  energy of the molecule. This is the definitive undergraduate molecular
  spectroscopy experiment and is a good full-report or project topic.
- **Fluorescence lifetime.** With a fast LED driver, a photodiode, and the
  oscilloscope from Week 2, the nanosecond decay of the excited state is
  measurable. Combined with the quantum yield, it separates the radiative and
  non-radiative decay rates.

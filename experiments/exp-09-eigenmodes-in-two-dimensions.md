---
title: Eigenmodes, Degeneracy, and Nodal Patterns
short_title: 9. Eigenmodes and Degeneracy
label: exp-eigenmodes
numbering:
  enumerator: "9.%s"
---

# Experiment 9 — Eigenmodes, Degeneracy, and Nodal Patterns

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 9, *Quantum Mechanics in Three Dimensions*
**Apparatus** Rigid rectangular acoustic cavity with two nearly equal sides, speaker, microphone, function generator or sound card; Chladni plate
**You will measure** cavity resonances and symmetry-related splitting, and photograph plate nodal patterns
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure resonances of a three-dimensional cavity and assign candidate
  quantum numbers $(n_x,n_y,n_z)$ where peaks are resolved.
- Predict the splitting of a symmetry-related pair when one of two equal
  cavity dimensions changes, and compare it with observation.
- Compare detected resonance peaks with a model count that includes
  degeneracy and missing or unresolved modes.
- Distinguish plate nodal lines from cavity pressure nodes and hydrogenic
  wavefunction nodes.

## Textbook connection

Read §9.1–9.4. The particle in a three-dimensional box is the first genuinely
three-dimensional quantum problem in the book. Separable spatial modes and
symmetry-related degeneracies have an acoustic analog, although the wall
conditions and frequency–energy relations differ.

The Helmholtz equation for a sound wave in a rigid cavity,

$$
\nabla^2 p + k^2 p = 0, \qquad k = \frac{2\pi f}{v},
$$

is the same equation as the time-independent Schrödinger equation for a free
particle in a box,

$$
\nabla^2\psi + \frac{2mE}{\hbar^2}\psi = 0 ,
$$

with the identification $k^2 \leftrightarrow 2mE/\hbar^2$. The boundary
conditions differ — a rigid wall forces $\partial p/\partial n = 0$ while an
infinite potential wall forces $\psi = 0$. Acoustic mode indices may include
zero and quantum box indices may not. Their leading large-wavenumber count
has the same geometric form; their low modes and boundary corrections differ.

## Theory

### Modes of a rectangular cavity

For a rigid-walled box of dimensions $L_x, L_y, L_z$, the resonant frequencies
are

$$
f_{n_x n_y n_z} = \frac{v}{2}
\sqrt{\left(\frac{n_x}{L_x}\right)^2
    + \left(\frac{n_y}{L_y}\right)^2
    + \left(\frac{n_z}{L_z}\right)^2},
\qquad n_i = 0,1,2,\ldots
$$ (eq-modes-box)

(with not all $n_i$ zero), where $v$ is the speed of sound. The quantum
counterpart, with $\psi = 0$ walls, is

$$
E_{n_x n_y n_z} = \frac{\pi^2\hbar^2}{2m}
\left[\left(\frac{n_x}{L_x}\right)^2
    + \left(\frac{n_y}{L_y}\right)^2
    + \left(\frac{n_z}{L_z}\right)^2\right],
\qquad n_i = 1,2,3,\ldots
$$ (eq-modes-quantum)

Same sum of squares; the frequency goes as its square root while the energy
goes as the sum itself, because $E \propto k^2$ for a massive particle and
$f \propto k$ for a wave in a non-dispersive medium. Keeping that distinction
straight is one of the things this experiment is for.

### Degeneracy and symmetry

If two dimensions are equal, say $L_y=L_z$, then $(n_x,n_y,n_z)$ and
$(n_x,n_z,n_y)$ have the same frequency: a symmetry-related **degeneracy**.
Changing one of those two lengths splits the pair. A cube has larger
permutation degeneracies; some unrelated triples can also share a sum of
squares without being related by a symmetry.

For small detuning, the pair's frequency difference grows approximately
linearly with the changed length. This illustrates symmetry breaking, but
it is not a quantitative Zeeman model: a magnetic field couples to angular
momentum, whereas the cavity perturbation changes a boundary.

### Density of states

Count the modes with frequency below $f$. Each mode is a lattice point in
$(n_x,n_y,n_z)$ space, and the number below $f$ is the volume of the
corresponding octant of an ellipsoid:

$$
N(f) \approx \frac{4\pi}{3}\,\frac{V f^{3}}{v^{3}}
      + \frac{\pi}{4}\,\frac{S f^{2}}{v^{2}}
      + \cdots ,
$$ (eq-dos)

where $V$ is volume and $S$ is total wall area. This is an **asymptotic,
smoothed count with multiplicity** for rigid-wall pressure modes, excluding
the static zero-frequency mode. The positive surface term reflects the
Neumann wall condition. For a $30\times20\times20\ \text{cm}$ box at
$3\ \text{kHz}$ the two terms are about $34$ and $19$; discrete edge and
corner terms and oscillations still matter. An observed peak count is usually
smaller because degenerate modes share peaks and the driver or microphone
can miss modes.

```{figure} ../images/exp09-mode-counting-concept.svg
:label: fig:exp09-mode-counting
:alt: A grid of nonnegative n_x and n_y values, excluding the zero mode, with a quarter-circle contour for an equal-sided rigid cavity; points on the axes are valid acoustic modes.

Mode counting for an equal-sided rigid cavity in two dimensions: axis points
are acoustic modes, and the origin is the excluded static mode. The quarter
disk area gives only the leading high-frequency count; boundary points add a
lower-order correction.
```

Differentiating the leading term gives a density of states proportional to
$f^2$. The analogous electromagnetic count has **two polarizations** and,
under classical equipartition, leads to the Rayleigh–Jeans ultraviolet
catastrophe. The acoustic spectrum offers a way to inspect geometric mode
counting over a limited frequency range, not a test of blackbody radiation.
Real media also have finite microscopic degrees of freedom and quantum
mode occupancies.

### Chladni figures

A thin plate driven at resonance develops a bending pattern. Sand migrates
from strong motion toward **nodal lines**. Circular-plate modes may show
diametral and circular nodes, depending on drive and mounting. They give a
visual analogy for angular and radial nodal structure, but a stiff plate
obeys a fourth-order bending equation, unlike the second-order acoustic and
Schrödinger equations. Hydrogenic angular nodes are surfaces in three
dimensions, so their counts are not interchangeable with plate lines.

## Pre-lab

:::{exercise}
:label: q-modes-01

For a box with $L_x=30.0\ \text{cm}$ and $L_y=L_z=20.0\ \text{cm}$,
with $v=343\ \text{m/s}$, list the ten lowest **mode triples** and their
frequencies from [](#eq-modes-box). Group equal frequencies and state how
many distinct peaks an ideal detector would show.
:::

:::{exercise}
:label: q-modes-02

For a *cubic* box of side $20.0\ \text{cm}$, list the lowest six distinct
frequencies and the degeneracy of each. Which is the first level with
degeneracy greater than 3?
:::

:::{exercise}
:label: q-modes-03

Using [](#eq-modes-quantum) for an electron in a cubic box of side
$1.0\ \text{nm}$, compute the ground-state energy in eV and the energies of
the first two excited levels with their degeneracies. Compare the level
spacing with $k_BT$ at room temperature.
:::

:::{exercise}
:label: q-modes-04

Estimate from [](#eq-dos) how many modes the example box has below
$3\ \text{kHz}$ using one and then two terms. Why is neither estimate an
exact integer count or a prediction of the number of visible peaks? What
additional measurement would tell you when nearby peaks become unresolved?
:::

## Apparatus

- Rigid rectangular cavity: a stout plywood or acrylic box, roughly
  $30\times20\times20\ \text{cm}$ internally, with two sides equal within
  measurement uncertainty. A small speaker and microphone near opposite
  corners couple well to ideal pressure modes, though real ports and driver
  response can still hide them. Both ports must remain inside the cavity
  when the partition moves. Record the exact internal dimensions and
  port locations.
- A close-fitting, well-sealed insert or movable partition to change one
  of the equal dimensions while keeping both ports within the active volume
- Small full-range speaker and amplifier
- Electret microphone with preamp, into a sound card or a microcontroller ADC
- Function generator, or a microcontroller/laptop generating a swept sine
- Thin circular metal Chladni plate with a documented mount and an off-center
  mechanical drive or edge bow so non-axisymmetric modes can be excited;
  fine sand or salt
- Thermometer (the speed of sound depends on temperature)

:::{warning}
Keep the drive level modest, especially at resonance. Avoid sustained loud
tones, reduce gain before a new sweep, and stop if the sound is uncomfortable.
Keep loose sand contained on the plate and away from the driver and
electronics.
:::

```{figure} ../images/exp09-eigenmodes-schematic.svg
:label: fig:exp09-eigenmodes
:alt: Panel (a), a rectangular cavity with speaker and microphone near opposite corners, a partition that shortens one side while leaving both ports in the cavity, and signal connections. Panel (b), an illustrative circular plate with sand tracing nodal lines, a center support, and an off-center drive.

Two different standing-wave systems. (a) A swept sine drives the rectangular
cavity while a corner microphone records its pressure response. (b) Sand on
a Chladni plate collects near bending-mode nodal lines; the pattern is
illustrative, not a calculated plate eigenfunction.
```

## Procedure

### Before you sweep

- Use [](#fig:exp09-eigenmodes) to distinguish the rectangular acoustic cavity
  from the circular Chladni plate; they are two analog systems measured with
  different drivers and should have separate notebook tables.
- Measure internal cavity dimensions at three locations along each axis and
  record the mean and spread. Photograph or sketch the speaker and microphone
  locations, since coupling can hide modes even when their frequencies are
  unchanged.
- Check the microphone and drive-reference channels, then close and seal
  every removable panel. Record sample rate, sweep rate, drive amplitude,
  microphone gain, and room temperature. Keep gain and drive below clipping.
- Predict and tabulate the first ten mode triples before sweeping. Group
  equal predictions and add columns for observed peak, linewidth, candidate
  triples, residual, and confidence in the assignment.
- For the Chladni plate, start with a very thin, even sand layer and low drive
  amplitude. Increase amplitude only enough to move the grains; excessive
  drive mixes modes and throws sand from the plate.

### Part A — The mode spectrum

1. Measure $L_x$, $L_y$, $L_z$ to the inside faces, with uncertainties.
   Measure the air temperature.
2. Drive the speaker with a slow logarithmic sweep from $200\ \text{Hz}$ to
   $3\ \text{kHz}$ and record the microphone signal.
3. Compute a transfer response from the microphone channel divided by the
   **measured electrical drive reference**, if available. A raw microphone
   spectrum can be used if the drive is demonstrably flat. Peaks are
   *candidate* modes; speaker, room, and panel resonances also appear.
4. For each identified peak, go back and drive at a fixed frequency, scanning
   finely to locate the maximum. A sweep finds the modes; a fixed-frequency
   scan measures them.
5. Record all resolved candidate peaks up to the frequency where linewidths,
   drive response, or signal-to-noise prevent reliable assignments. Aim for
   ten confident assignments; distinguish a peak from the number of mode
   triples it may represent.

**[ ] Checkpoint 1.** Before recording all twenty, assign
your first resolved peaks to candidate triples and compare them with your
pre-lab table. The longest-axis fundamental is expected near
$f_{100}=v/(2L_x)$, but a weak or missing peak can also reflect driver,
microphone, or room response; test the competing explanations.

### Part B — Breaking the symmetry

6. Move the sealed partition to shorten $L_y$ (one of the initially equal
   sides) by a measured $5$–$10\%$, without changing the speaker or
   microphone settings. Re-measure the low-frequency peaks.
7. Track the pair initially predicted as $(0,1,0)$ and $(0,0,1)$:
   shortening $L_y$ raises the former and leaves the latter approximately
   fixed. Compare the measured separation with [](#eq-modes-box). If the
   initial sides were only nearly equal, include their initial separation.

### Part C — Nodal patterns

8. Mount the plate on the driver, sprinkle sand thinly, and sweep slowly
   upward, pausing at each frequency where the sand organizes itself.
9. Photograph several distinct, stable patterns with their frequencies and
   mount and drive positions; record how many could be reproduced.
10. Describe apparent nodal diameters and circles, marking ambiguous or
    distorted lines. Do not assign a plate mode number solely from a
    photograph without the plate boundary conditions and a model.

### Part D — Computational

11. Plot several square-well densities from
    $\psi_{n_xn_y}\propto\sin(n_x\pi x/L)\sin(n_y\pi y/L)$.
    Compare the *idea* of nodes with a Chladni photograph, while noting the
    different equation and boundary conditions.
12. From Chapter 9, tabulate radial and angular node counts for hydrogenic
    $2p$, $3d$, and $3s$ states. Sketch or plot one orbital density and
    explain which nodal feature has no direct plate counterpart.

## Analysis

### Assigning modes and fitting

Assign each resolved peak one representative triple or a set of unresolved
candidate triples from [](#eq-modes-box). Count a peak once in a fit even
when it represents degenerate modes; repeated entries would give one
measurement excess weight. Hold the independently measured internal
dimensions fixed and fit the sound speed:

```python
import numpy as np
from scipy.optimize import curve_fit

n = np.array([[1,0,0], [0,1,0], [1,1,0], ...])  # one row per resolved peak
f = np.array([...])                             # measured frequencies, Hz
sf = np.array([...])                            # absolute frequency errors
L = np.array([Lx, Ly, Lz])                       # independently measured, m

def modes(n, v):
    return 0.5 * v * np.sqrt(((n / L) ** 2).sum(axis=1))

popt, pcov = curve_fit(modes, n, f, p0=[343.0],
                       sigma=sf, absolute_sigma=True)
v_fit, sv_fit = popt[0], np.sqrt(pcov[0, 0])
residual = f - modes(n, v_fit)
```

Here $L_x,L_y,L_z$ are the measured inside dimensions. The covariance
uncertainty on $v$ is conditional on those dimensions, assignments, and the
ideal-cavity model. Refit using plausible dimensions to assess geometric
sensitivity, and inspect residuals for systematic shifts. Compare $v$ with
$331.3\sqrt{1+T_C/273.15}\ \text{m/s}$ for approximate dry-air speed at
temperature $T_C$ in °C; humidity and gas composition also matter.

Do **not** fit $v$ and all three lengths as unrestricted parameters from
frequencies alone: multiplying all four by the same factor leaves
[](#eq-modes-box) unchanged. The data determine the three ratios
$v/(2L_i)$, not an absolute length and speed separately. As a cross-check,
use resolved axial fundamentals to infer length ratios and compare them
with ruler measurements.

:::{tip} Getting the assignment right
Work upward using frequency, linewidth, and how a peak moves when $L_y$
changes. A model may predict multiple triples at one frequency, and real
coupling may hide some. A peak with no plausible cavity assignment could
come from the speaker, room, or box panels; check whether it follows the
predicted shift under partition movement before rejecting it.
:::

### Degeneracy splitting

Plot the $(0,1,0)$ and $(0,0,1)$ peak frequencies against
$\Delta L_y/L_y$. For a small change with other conditions fixed,
$\Delta f_{010}\approx-f_{010}\Delta L_y/L_y$ while
$\Delta f_{001}\approx0$. Compare the measured *change in separation*
with this prediction and resolve whether the initial pair was already
split. If the peaks overlap within their linewidths, report a bound on
splitting rather than claiming two measured frequencies.

### Density of states

Enumerate [](#eq-modes-box) through the measured frequency range, retaining
one entry per triple and excluding $(0,0,0)$. Plot its exact staircase count,
the leading and two-term smooth approximations in [](#eq-dos), and the
**observed distinct-peak count** separately. Their differences reveal
degeneracy, unresolved linewidths, and weak coupling; the observed curve
is not a complete density-of-states measurement. For the two-term smooth
model $N=Af^3+Bf^2$ with positive $A,B$, its local log-slope lies
**between 2 and 3**, not above 3. A power-law fit to a short discrete
spectrum need not recover that smooth slope.

## Post-lab questions

:::{exercise}
:label: q-modes-05

Report fitted $v$ and its fit and geometry sensitivities, and compare it
with the temperature-based estimate. Use any resolved axial fundamentals
to estimate a length ratio and compare it with the measured ratio. Explain
why the frequencies alone cannot identify $v$ and all three lengths
independently.
:::

:::{exercise}
:label: q-modes-06

Report the measured or bounded change in separation of the
$(0,1,0)$ and $(0,0,1)$ pair as $L_y$ changes. State which symmetry is
broken. Explain one reason this geometric perturbation is only a qualitative
analogy to Zeeman splitting.
:::

:::{exercise}
:label: q-modes-07

Compare the exact model count, observed distinct peaks, and both smooth
forms of [](#eq-dos). Explain why the electromagnetic count has a
polarization factor and why classical $k_BT$ per mode leads to the
Rayleigh–Jeans ultraviolet problem. State what Planck changed.
:::

:::{exercise}
:label: q-modes-08

Compare one Chladni photograph with a square-well $|\psi|^2$ plot from
Part D. Identify one shared nodal feature and two reasons the patterns
are not exact counterparts.
:::

:::{exercise}
:label: q-modes-09

Ignoring spin and relativistic corrections, hydrogen's $n=2$ level has
four spatial states ($2s$ and three $2p$). A screened *central* potential
retains rotational symmetry and the threefold $m_\ell$ degeneracy of a
$p$ level, but generally separates $s$ from $p$. Explain which extra
Coulomb-specific degeneracy is lost. You will examine this in Week 11.
:::

## Going further

- **The cubic box.** A box with all three dimensions equal has permutation
  degeneracies. It also has coincidences not related by exchanging axes:
  $(3,3,3)$ and $(5,1,1)$ both have a sum of squares of $27$.
  Contrast such a numerical coincidence with hydrogen's additional
  Coulomb-specific degeneracy, which has a hidden symmetry.
- **A cylindrical cavity.** Its acoustic pressure modes involve
  Bessel-function conditions in the circular cross section. A circular
  plate also has angular separation and Bessel-related functions, but its
  bending equation and boundary conditions give different eigenvalues.
- **Damping and linewidth.** Measure the full width at half maximum
  $\Delta f$ of an isolated power resonance and the free **energy-decay**
  time $\tau_E$ after stopping the drive. For a single weakly damped
  Lorentzian mode, $\Delta f\,\tau_E\approx1/(2\pi)$. State the linewidth
  and decay-time definitions: this is a classical Fourier/damping
  relation, not a measurement of a quantum uncertainty principle.

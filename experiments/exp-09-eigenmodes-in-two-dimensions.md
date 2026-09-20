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
**Apparatus** Rigid rectangular acoustic cavity, speaker, microphone, microcontroller or function generator; Chladni plate
**You will measure** an eigenvalue spectrum, identify its degeneracies, and photograph nodal patterns
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure the resonant spectrum of a three-dimensional cavity and assign
  quantum numbers $(n_x, n_y, n_z)$ to the observed modes.
- Explain the origin of degeneracy in terms of symmetry, and demonstrate that
  breaking the symmetry splits the degenerate levels.
- Relate a measured mode spectrum to the density of states, and to the mode
  counting that produced the ultraviolet catastrophe in Chapter 6.
- Connect the observed nodal structure to the angular and radial nodes of
  hydrogenic wavefunctions.

## Textbook connection

Read §9.1–9.4. The particle in a three-dimensional box is the first genuinely
three-dimensional quantum problem in the book, and everything interesting
about it — separation of variables, three quantum numbers, degeneracy from
symmetry, and the lifting of that degeneracy when the symmetry is broken — has
an exact acoustic analogue you can hear and measure this afternoon.

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
infinite potential wall forces $\psi = 0$ — but the *eigenvalue spectrum* has
the same structure, and the counting of states is identical.

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

If two dimensions are equal, say $L_x = L_y$, then $(n_x, n_y, n_z)$ and
$(n_y, n_x, n_z)$ give the same frequency: the level is **degenerate**, and the
degeneracy is a consequence of the symmetry of the box under exchange of $x$
and $y$. If all three are equal, the cube has degeneracies of order 3 and 6.

Detune one dimension slightly and the degeneracy **splits**, by an amount
proportional to the detuning. This is exactly the mechanism by which a
magnetic field splits the $m_\ell$ levels of hydrogen (the Zeeman effect of
§9.5): a perturbation that breaks a symmetry lifts the degeneracy that
symmetry protected.

### Density of states

Count the modes with frequency below $f$. Each mode is a lattice point in
$(n_x,n_y,n_z)$ space, and the number below $f$ is the volume of the
corresponding octant of an ellipsoid:

$$
N(f) \approx \frac{4\pi}{3}\,\frac{V f^{3}}{v^{3}}
      + \frac{\pi}{4}\,\frac{S f^{2}}{v^{2}}
      + \cdots ,
$$ (eq-dos)

where $V$ is the volume and $S$ the total wall area. The leading term is the
volume of the positive octant of an ellipsoid in $(n_x,n_y,n_z)$ space; the
second is a surface correction, and for a box of laboratory size at audio
frequencies it is *not* small — for a $30\times20\times15\ \text{cm}$ box at
$3\ \text{kHz}$ the two terms are roughly $25$ and $19$. Expect your measured
count to sit well above the leading term alone, and use the comparison to show
that the correction is needed.

Differentiating, the density of states grows as $f^2$. That $f^2$ is precisely
the mode counting that, multiplied by $k_BT$ per mode, produced the
Rayleigh–Jeans law and the ultraviolet catastrophe of Chapter 6. You are about
to verify the counting experimentally — and to see that in the acoustic case
the catastrophe does not arise only because the medium itself cuts off at
atomic scales.

### Chladni figures

A thin plate driven at a resonance develops a standing-wave pattern; sand
sprinkled on it migrates away from the antinodes and collects on the **nodal
lines**, making the mode visible. The nodal patterns of a circular plate have
$m$ diameters and $n$ circles — the same $(n, \ell, m)$ nodal bookkeeping as a
hydrogenic orbital, for the same reason: both come from separating a
Laplacian in a symmetric coordinate system.

## Pre-lab

:::{exercise}
:label: q-modes-01

For a box with $L_x = 30.0\ \text{cm}$, $L_y = 20.0\ \text{cm}$,
$L_z = 15.0\ \text{cm}$ and $v = 343\ \text{m/s}$, compute the ten lowest
frequencies from [](#eq-modes-box) and list them with their $(n_x,n_y,n_z)$.
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

Estimate from [](#eq-dos) how many modes your box has below $3\ \text{kHz}$,
using the leading term alone and then both terms. Given that a resonance has a
finite width, at what frequency do you expect individual modes to stop being
resolvable? This tells you where to stop taking data.
:::

## Apparatus

- Rigid rectangular cavity: a stout plywood or acrylic box, roughly
  $30 \times 20 \times 15\ \text{cm}$, with a small speaker sealed into one
  corner and a microphone port in the opposite corner. **Corners are
  essential** — every mode has an antinode at a corner, so a corner-mounted
  driver and receiver couple to all of them. A driver at the centre of a face
  is deaf to half the spectrum.
- A close-fitting insert or movable partition, to change one dimension
- Small full-range speaker and amplifier
- Electret microphone with preamp, into a sound card or a microcontroller ADC
- Function generator, or a microcontroller/laptop generating a swept sine
- Thin metal plate on a central bolt over a speaker driver; fine sand or salt
- Thermometer (the speed of sound depends on temperature)

:::{warning}
Keep the drive level modest. At resonance the sound pressure inside the box is
much higher than outside, and prolonged exposure at high level is a hearing
hazard. Sweeps should be quiet enough to hold a conversation over.
:::

```{figure} ../images/exp09-eigenmodes-schematic.svg
:label: fig:exp09-eigenmodes
:alt: Panel (a), a rectangular cavity with a corner-mounted speaker and an opposite-corner microphone, driven by a function generator and read by a sound card. Panel (b), a circular Chladni plate driven from below by a speaker on a central bolt, with sand collecting along the nodal lines.

Two ways to see standing-wave eigenmodes. (a) A swept sine drives the rectangular cavity while a corner microphone records the resonance spectrum. (b) Sand on a Chladni plate collects along the nodal lines of a driven bending mode.
```

## Procedure

### Part A — The mode spectrum

1. Measure $L_x$, $L_y$, $L_z$ to the inside faces, with uncertainties.
   Measure the air temperature.
2. Drive the speaker with a slow logarithmic sweep from $200\ \text{Hz}$ to
   $3\ \text{kHz}$ and record the microphone signal.
3. Compute the transfer function — the ratio of received to driven amplitude —
   as a function of frequency. Peaks are modes.
4. For each identified peak, go back and drive at a fixed frequency, scanning
   finely to locate the maximum. A sweep finds the modes; a fixed-frequency
   scan measures them.
5. Record **at least twenty** modes with their frequencies and uncertainties.

**[ ] Checkpoint 1.** Before recording all twenty, assign
your first three peaks to $(n_x,n_y,n_z)$ and check them against your pre-lab
table. If the lowest peak does not match $f_{100} = v/2L_x$, your box has a
leak, the driver is not in a corner, or you are seeing a speaker resonance
rather than a cavity mode.

### Part B — Breaking the symmetry

6. Insert the partition to change $L_x$ by a measured $5$–$10\%$ and re-measure
   the lowest ten modes.
7. If your box has two nearly equal dimensions, find a near-degenerate pair
   and follow it through the detuning: it should split by an amount
   proportional to the change.

### Part C — Nodal patterns

8. Mount the plate on the driver, sprinkle sand thinly, and sweep slowly
   upward, pausing at each frequency where the sand organizes itself.
9. Photograph each pattern with its frequency. Get at least six.
10. Count the nodal diameters and circles in each and label the pattern
    $(m, n)$.

### Part D — Computational

11. Solve the two-dimensional Schrödinger equation for a square infinite well
    numerically, plot the first several $|\psi|^2$, and compare their nodal
    structure with your Chladni photographs.
12. Plot $|\psi_{n\ell m}|^2$ for the hydrogenic $2p$, $3d$, and $3s$ states,
    and count radial and angular nodes.

## Analysis

### Assigning modes and fitting

Assign each measured frequency to a triple by matching to
[](#eq-modes-box). Then fit *all* the assignments simultaneously, taking $v$,
$L_x$, $L_y$, $L_z$ as free parameters:

```python
import numpy as np
from scipy.optimize import curve_fit

n = np.array([[1,0,0], [0,1,0], [1,1,0], ...])       # assigned quantum numbers
f = np.array([...])                                   # measured frequencies, Hz
sf = np.array([...])

def modes(n, v, Lx, Ly, Lz):
    L = np.array([Lx, Ly, Lz])
    return 0.5 * v * np.sqrt(((n / L) ** 2).sum(axis=1))

popt, pcov = curve_fit(modes, n, f, p0=[343, 0.30, 0.20, 0.15],
                       sigma=sf, absolute_sigma=True)
```

The fitted $L_i$ should agree with your ruler measurements, and the fitted $v$
with $v = 331.3\sqrt{1 + T/273.15}\ \text{m/s}$ at your measured temperature.
Agreement on four parameters at once is a much stronger test of the model than
matching a single frequency, and disagreement in one parameter localizes the
problem.

:::{tip} Getting the assignment right
Misassignment is the main failure mode here. Work upward: the lowest three
modes are unambiguous, and each subsequent one can be predicted from the
parameters fitted so far. If a measured peak has no predicted partner within a
few percent, it is probably not a cavity mode — speaker resonances, room
modes, and the box panels' own flexural modes all appear in the spectrum.
Identify them by seeing whether they move when you change $L_x$.
:::

### Degeneracy splitting

Plot the split pair's two frequencies against the detuning $\Delta L_x/L_x$.
The splitting should be linear in the detuning for small detunings; report the
slope and compare with what [](#eq-modes-box) predicts by direct
differentiation.

### Density of states

Plot the cumulative count $N(f)$ against $f$ and overlay both the leading
$f^3$ term of [](#eq-dos) and the two-term expression. Fit a power law to your
data and compare the exponent with 3. It will come out *above* 3 over your
frequency range, because the surface term is still contributing — that is the
expected result, not a failure. Discuss which term dominates where.

## Post-lab questions

:::{exercise}
:label: q-modes-05

Report the fitted $v$, $L_x$, $L_y$, $L_z$ with uncertainties, and compare
each with its independently measured value. Which one is best determined by
the acoustic data, and why?
:::

:::{exercise}
:label: q-modes-06

Report the measured degeneracy splitting as a function of detuning. Explain
the analogy with the Zeeman effect: what plays the role of the magnetic field,
what plays the role of $m_\ell$, and what is the analogue of the $g$-factor?
:::

:::{exercise}
:label: q-modes-07

Report your measured $N(f)$ against both forms of [](#eq-dos). Explain in two or three sentences how
the same counting, applied to electromagnetic modes in a cavity and combined
with $k_BT$ per mode, gives the Rayleigh–Jeans law — and what Planck changed.
:::

:::{exercise}
:label: q-modes-08

Compare one of your Chladni photographs with the corresponding $|\psi|^2$ plot
from Part D. Where does the analogy hold exactly, and where does it break
down? (Consider the order of the differential equation for a stiff plate.)
:::

:::{exercise}
:label: q-modes-09

For the hydrogen atom, the $n=2$ level is fourfold degenerate ($2s$ and three
$2p$) in the non-relativistic Coulomb problem, but *not* in a multi-electron
atom. Using the symmetry argument from this experiment, explain what symmetry
the Coulomb potential has that a screened potential does not. You will measure
the consequence in Week 11.
:::

## Going further

- **The cubic box.** A box with all three dimensions equal shows the full
  degeneracy structure, including the accidental degeneracy of
  $(3,3,3)$ with $(5,1,1)$ — $27 = 27$ — which is not required by any symmetry
  of the box. Accidental degeneracies of exactly this kind occur in the
  hydrogen atom and turn out not to be accidental at all.
- **A cylindrical cavity.** The modes involve Bessel-function zeros instead of
  integers, which is the same mathematics as the circular Chladni plate and as
  the two-dimensional hydrogen-like problems of §9.3.
- **Damping and linewidth.** Measure the width of a resonance and its $Q$.
  The relation $\Delta f \cdot \tau \approx 1/2\pi$ between linewidth and decay
  time is the classical form of the energy–time uncertainty relation, and
  measuring both for the same mode makes the point concretely.

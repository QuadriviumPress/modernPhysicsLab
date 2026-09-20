---
title: Tunneling by Frustrated Total Internal Reflection
short_title: 8. Tunneling by FTIR
label: exp-ftir-tunneling
numbering:
  enumerator: "8.%s"
---

# Experiment 8 — Tunneling by Frustrated Total Internal Reflection

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 8, *The Schrödinger Equation*
**Apparatus** Right-angle prism, long-radius plano-convex lens, diode laser, USB microscope or camera; plus Python
**You will measure** the exponential decay of an evanescent wave across a barrier, and compare it with a numerical solution of the Schrödinger equation
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Explain the mathematical correspondence between an evanescent electromagnetic
  wave and a quantum wavefunction inside a classically forbidden region.
- Measure the transmission through a variable air gap and extract the decay
  constant $\kappa$.
- Solve the one-dimensional Schrödinger equation numerically for a
  rectangular barrier and compare the transmission coefficient with the
  analytic result.
- Explain why tunneling probability is exponentially sensitive to barrier
  width, and what that implies for scanning tunneling microscopy and alpha
  decay.

## Textbook connection

Read §8.4–8.7, on the rectangular barrier and tunneling. The correspondence
exploited here is exact at the level of the differential equations: in a
classically forbidden region the Schrödinger equation and the wave equation
for light beyond the critical angle are both

$$
\frac{d^2\psi}{dz^2} = \kappa^2\psi ,
$$

with a real $\kappa$ and hence exponentially decaying — not oscillating —
solutions. Everything that follows from that equation, including the
exponential sensitivity to barrier width, follows in both systems.

## Theory

### The evanescent wave

Light inside glass of index $n$ striking a glass–air interface at an angle
$\theta$ greater than the critical angle $\theta_c = \arcsin(1/n)$ is totally
internally reflected. But the field does not stop at the interface: it
continues into the air as an **evanescent wave** whose amplitude decays as
$e^{-\kappa z}$ with

$$
\kappa = \frac{2\pi}{\lambda}\sqrt{n^2\sin^2\theta - 1} .
$$ (eq-ftir-kappa)

For $n = 1.52$ at $\theta = 45°$ and $\lambda = 650\ \text{nm}$, $1/\kappa$ is
about $260\ \text{nm}$ — the field is gone within a wavelength.

### Frustrating it

Bring a second piece of glass close to the first. If the gap $d$ is comparable
to $1/\kappa$, the evanescent field still has appreciable amplitude when it
reaches the second surface, where it can couple back into a propagating wave.
Light appears on the far side of a gap that classical ray optics says it
cannot cross. To leading order the transmitted intensity is

$$
I(d) = I_0\, e^{-2\kappa d} + I_{\text{stray}} ,
$$ (eq-ftir-transmission)

the factor of 2 appearing because intensity is amplitude squared. (The full
expression includes Fresnel and polarization factors and a weak $d$-dependent
prefactor; the exponential dominates, and the correction is a good topic for
the discussion section.)

### The quantum barrier

A particle of energy $E$ incident on a rectangular barrier of height
$V_0 > E$ and width $L$ has, inside the barrier, a wavefunction decaying as
$e^{-\kappa_q z}$ with

$$
\kappa_q = \frac{\sqrt{2m(V_0 - E)}}{\hbar} ,
$$ (eq-ftir-kappa-q)

and, for $\kappa_q L \gg 1$, a transmission coefficient

$$
T \approx \frac{16E(V_0 - E)}{V_0^2}\, e^{-2\kappa_q L} .
$$ (eq-ftir-T)

Compare [](#eq-ftir-kappa) with [](#eq-ftir-kappa-q) and
[](#eq-ftir-transmission) with [](#eq-ftir-T). The correspondence is
term-by-term: the gap is the barrier, $\kappa$ is $\kappa_q$, and the
exponential is the same exponential.

### The Newton's-rings trick

Controlling a sub-micrometre gap mechanically is difficult. Instead, use
geometry: press a plano-convex lens of radius of curvature $R$ against the
prism face. The gap between them at radial distance $r$ from the contact point
is

$$
d(r) = \frac{r^{2}}{2R} ,
$$ (eq-ftir-gap)

so a *single image* of the contact region contains a continuous, calculable
range of gaps. For $R = 1000\ \text{mm}$, $d = 500\ \text{nm}$ at
$r = 1.0\ \text{mm}$ — a comfortable field of view for a USB microscope.

You get the whole transmission curve from one photograph, with no moving
parts. Independently, the same contact region viewed in *reflected*
monochromatic light shows Newton's rings, whose radii give you $R$ — a
built-in calibration of the very quantity [](#eq-ftir-gap) depends on.

## Pre-lab

:::{exercise}
:label: q-ftir-01

Compute $\theta_c$ for $n = 1.52$. Then evaluate [](#eq-ftir-kappa) at
$\theta = 45°$ and $\lambda = 650\ \text{nm}$, and report the intensity decay
length $1/(2\kappa)$ in nanometres.
:::

:::{exercise}
:label: q-ftir-02

Using [](#eq-ftir-gap) with $R = 1000\ \text{mm}$, find the radius at which
the gap is $100$, $250$, $500$, and $1000\ \text{nm}$. Over what range of
radii does the transmitted intensity fall by a factor of $10^3$?
:::

:::{exercise}
:label: q-ftir-03

An electron of energy $E = 1.0\ \text{eV}$ meets a barrier of height
$V_0 = 5.0\ \text{eV}$. Compute $\kappa_q$ and evaluate [](#eq-ftir-T) for
$L = 0.10$, $0.20$, and $0.50\ \text{nm}$. By what factor does $T$ change per
$0.1\ \text{nm}$ of barrier? This number is the working principle of the
scanning tunneling microscope — explain how.
:::

:::{exercise}
:label: q-ftir-04

State the correspondence explicitly: write a table with three columns —
quantity, optical system, quantum system — and fill in rows for the decay
constant, the barrier width, the transmitted quantity, and the "energy"
parameter that sets $\kappa$.
:::

## Apparatus

- Right-angle prism, $n \approx 1.52$, faces clean
- Plano-convex lens of long radius of curvature, $R \approx 500$–$2000\ \text{mm}$,
  with $R$ known or measurable
- Adjustable clamp or spring mount to press the lens against the hypotenuse
  face, with a fine adjustment
- Diode laser, $650\ \text{nm}$, with beam expander
- USB microscope or a camera with a macro lens; alternatively a photodiode
  behind a pinhole on a micrometer stage
- Neutral-density filters, lens tissue and isopropanol

:::{warning}
Clean both surfaces immediately before contact and work in as dust-free a spot
as you can. A single dust particle holds the surfaces apart over its whole
neighbourhood, and the contact point then sits at an unknown nonzero gap — the
most common failure of this experiment. If your fitted intensity does not
saturate at small $r$, suspect exactly this.
:::

:::{danger}
Class 2 laser plus prism faces that produce reflections in several directions.
Map every beam before powering up. See [](#lab-safety).
:::

```{figure} ../images/exp08-ftir-schematic.svg
:label: fig:exp08-ftir
:alt: A laser beam totally internally reflects off the hypotenuse of a right-angle prism, except where a long-radius plano-convex lens is pressed against it, where light instead tunnels across the thin air gap.

Frustrated total internal reflection. Away from the contact point the reflected beam is bright; near it, light tunnels across the air gap $r(x)$ and the reflected spot goes dark.
```

## Procedure

### Part A — Establishing total internal reflection

1. Send the expanded beam into the prism so that it strikes the hypotenuse at
   $45°$ internally, and confirm that essentially all of it emerges from the
   reflected port and none from the hypotenuse.
2. Measure the residual transmitted intensity with nothing in contact. This is
   $I_{\text{stray}}$ and it sets the floor of your dynamic range. Reduce it —
   baffles, a black card, a darkened bench — because your decade of decay is
   only as long as the floor allows.

**[ ] Checkpoint 1.** Show the instructor the reflected
and transmitted powers, and your measured stray floor as a fraction of $I_0$.
You want at least three decades.

### Part B — Newton's rings, for the geometry

3. Illuminate the contact region in reflection with expanded laser light and
   photograph the ring pattern.
4. Measure the ring radii $r_m$. Dark rings satisfy $r_m^2 = m\lambda R$, so a
   fit of $r_m^2$ against $m$ has slope $\lambda R$ and gives $R$ directly.
   Use *your* $R$ in the analysis, not the catalogue value.

### Part C — The transmission curve

5. Bring the lens into contact under gentle, reproducible pressure.
6. Image the transmitted light through the hypotenuse. You should see a bright
   central spot fading rapidly outward — this is tunneling made visible, and
   its radius is set by $1/\kappa$, not by any aperture.
7. Take a series of exposures spanning the dynamic range: short exposures for
   the bright centre, long ones for the tail, with the exposure times recorded
   so that you can splice them onto a common scale. Take a dark frame for each
   exposure time.
8. Repeat the whole set at a second, higher clamping pressure. The contact
   region flattens under load, which changes the effective $R$; comparing the
   two data sets bounds that systematic.

### Part D — The numerical companion

9. Solve the one-dimensional time-independent Schrödinger equation for a
   rectangular barrier numerically (see Analysis), and compare the resulting
   $T(L)$ with [](#eq-ftir-T) and with your measured $I(d)$ curve on a common
   normalized axis.

## Analysis

### From image to transmission curve

Convert pixel radius to physical radius with a stage micrometer or a ruled
scale imaged at the same magnification — do not trust the microscope's
nominal magnification. Then radially average about the contact point, convert
$r$ to $d$ with [](#eq-ftir-gap), and fit.

```python
import numpy as np
from scipy.optimize import curve_fit

d  = r**2 / (2 * R)                         # metres
model = lambda d, I0, kappa, floor: I0 * np.exp(-2 * kappa * d) + floor

# Fit in log space only with correct weights; better, fit directly:
popt, pcov = curve_fit(model, d, I, p0=[I.max(), 4e6, I.min()],
                       sigma=sI, absolute_sigma=True)
kappa, skappa = popt[1], np.sqrt(pcov[1, 1])
print(f"kappa = {kappa:.3g} +/- {skappa:.2g} 1/m")
print(f"decay length 1/(2 kappa) = {1/(2*kappa)*1e9:.0f} nm")
```

Compare $\kappa$ with the prediction of [](#eq-ftir-kappa), propagating the
uncertainties in $n$, $\theta$, and $\lambda$. Note that $\kappa$ is quite
sensitive to $\theta$ near the critical angle — evaluate
$d\kappa/d\theta$ and state how well you would need to know $\theta$ for a 5%
measurement of $\kappa$.

### The numerical Schrödinger solution

Solve by transfer matrix, or by direct diagonalization of the discretized
Hamiltonian. The transfer-matrix version is short:

```python
import numpy as np

hbar = 1.054571817e-34
me   = 9.1093837015e-31
eV   = 1.602176634e-19

def transmission(E_eV, V0_eV, L_nm):
    E, V0, L = E_eV*eV, V0_eV*eV, L_nm*1e-9
    k  = np.sqrt(2*me*E) / hbar
    if E < V0:
        kap = np.sqrt(2*me*(V0 - E)) / hbar
        return 1.0 / (1 + (V0**2 * np.sinh(kap*L)**2) / (4*E*(V0 - E)))
    kk = np.sqrt(2*me*(E - V0)) / hbar
    return 1.0 / (1 + (V0**2 * np.sin(kk*L)**2) / (4*E*(V0 - E)))
```

Plot $T$ against $L$ for $E < V_0$ on a logarithmic axis and confirm that the
slope is $-2\kappa_q$. Then plot $T$ against $E$ through and above $V_0$: the
resonances above the barrier, where $T$ returns to exactly 1 at certain
energies, are a genuinely non-classical feature and are worth a sentence in
the report.

Overlay your *measured* optical curve, normalized, on the computed quantum
curve with the axes scaled by the respective $\kappa$. They should lie on top
of one another — which is the point of the whole experiment.

## Post-lab questions

:::{exercise}
:label: q-ftir-05

Report your measured $\kappa$ with uncertainty and compare with
[](#eq-ftir-kappa) in units of $\sigma$. If it disagrees, is your measured
decay too fast or too slow, and what would each of the following do:
a nonzero gap at contact, a flattened contact under load, stray light?
:::

:::{exercise}
:label: q-ftir-06

Over how many decades of intensity did your fit hold? What set the limit —
saturation at the bright end or the stray floor at the dim end? What would you
change first?
:::

:::{exercise}
:label: q-ftir-07

Using [](#eq-ftir-T) with $V_0 - E = 4\ \text{eV}$, compute the factor by
which the tunneling current changes when an STM tip is moved
$0.10\ \text{nm}$ closer. Explain how this gives an instrument with
picometre vertical resolution, and why it does *not* give the same lateral
resolution.
:::

:::{exercise}
:label: q-ftir-08

Alpha decay is tunneling through the Coulomb barrier. Half-lives among alpha
emitters range over more than twenty orders of magnitude while the alpha
energies range over only a factor of about two. Explain qualitatively how
[](#eq-ftir-T) accounts for this, and name the empirical relation it leads to.
(You will meet it again in Week 13.)
:::

:::{exercise}
:label: q-ftir-09

The optical and quantum problems have the same equation but different boundary
conditions and different conserved quantities. Name one physical feature of
the quantum problem that has *no* analogue in the optical experiment.
:::

## Going further

- **Microwave version.** Two paraffin-wax or acrylic prisms and a $3\ \text{cm}$
  microwave source make the same measurement at a gap scale of centimetres,
  where the gap can be set with a ruler. It is far easier to do quantitatively
  and much less visually striking. If a microwave kit is available, doing both
  and comparing the extracted $\kappa$ values in units of $\lambda$ is an
  excellent full-report topic.
- **Polarization dependence.** $\kappa$ is the same for both polarizations but
  the coupling prefactor is not. Measuring the $s$- and $p$-polarized
  transmission separately tests the part of the theory that
  [](#eq-ftir-transmission) leaves out.
- **Angle dependence.** Mount the prism on a rotation stage and measure
  $\kappa$ as a function of $\theta$ from just above $\theta_c$ to $60°$.
  Fitting the whole $\kappa(\theta)$ curve to [](#eq-ftir-kappa) gives the
  refractive index of the prism as a fitted parameter.

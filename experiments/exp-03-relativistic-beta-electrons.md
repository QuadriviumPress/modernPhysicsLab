---
title: Relativistic Electrons from Beta Decay
short_title: 3. Relativistic Beta Electrons
label: exp-beta-electrons
numbering:
  enumerator: "3.%s"
---

# Experiment 3 — Relativistic Electrons from Beta Decay

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 3, *Relativistic Dynamics*
**Apparatus** Geiger–Müller counter, $^{90}$Sr/$^{90}$Y beta source, aluminium absorber set
**You will measure** the beta endpoint energy from an absorption curve, and the speed it implies
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure an absorption curve and extract a maximum range by extrapolation.
- Convert a range in aluminium into a maximum kinetic energy using an
  empirical range–energy relation.
- Compute $v/c$ for that energy both relativistically and classically, and
  explain why the classical answer is not merely inaccurate but impossible.
- Handle counting data correctly: Poisson uncertainties, background
  subtraction, and dead time.

## Textbook connection

Read §3.1–3.4. This experiment supplies the number that makes relativistic
dynamics unavoidable in a first course. A beta particle from $^{90}$Y carries
up to $2.28\ \text{MeV}$ of kinetic energy — more than four times its own rest
energy — and the classical expression $T = \tfrac12 mv^2$ returns a speed of
about $3c$ for it. Nothing else on the bench makes the failure of Newtonian
mechanics so blunt.

## Theory

### The beta spectrum and its endpoint

Beta decay is a three-body process: the nucleus emits an electron *and* an
antineutrino, which share the available energy. The electron therefore emerges
with a *continuous* spectrum of energies from zero up to a maximum
$T_{\max} = Q$, the endpoint, reached in the rare case that the neutrino takes
essentially nothing. It was precisely this continuous spectrum — apparently
violating energy conservation — that led Pauli to postulate the neutrino in
1930, so the shape you are measuring around today has some history in it.

The source is a $^{90}$Sr/$^{90}$Y pair in secular equilibrium:

$$
^{90}\text{Sr} \xrightarrow{\ \beta^-,\ 28.8\ \text{y}\ } {}^{90}\text{Y}
\xrightarrow{\ \beta^-,\ 64\ \text{h}\ } {}^{90}\text{Zr\ (stable)} ,
$$

with endpoints $0.546\ \text{MeV}$ and $2.28\ \text{MeV}$ respectively. The
high-energy $^{90}$Y component is the one whose range you will measure,
because it is the only part of the beam that survives the thickest absorbers.

### Absorption and range

Beta particles lose energy continuously by ionization and, at these energies,
significantly by bremsstrahlung as well. Empirically, the counting rate behind
an absorber of *mass thickness* $x$ (in $\text{mg/cm}^2$: the density times
the physical thickness) falls close to exponentially,

$$
R(x) = R_0\, e^{-\mu_m x} + R_{\text{bg}} ,
$$ (eq-beta-exp)

over the first part of the curve, and then bends over and flattens into a
residual bremsstrahlung tail plus background. The **maximum range** $R_m$ is
the mass thickness at which the beta contribution disappears into that floor.

Mass thickness is used rather than physical thickness because energy loss per
unit mass is nearly the same in all light materials — so a range quoted in
$\text{mg/cm}^2$ is roughly transferable between absorber materials, which
physical millimetres are not.

### From range to energy

Two standard empirical relations connect the maximum range in aluminium to the
endpoint energy. **Feather's rule**, valid for $T_{\max} > 0.8\ \text{MeV}$:

$$
R_m\ [\text{g/cm}^2] = 0.542\, T_{\max}\ [\text{MeV}] - 0.133 ,
$$ (eq-feather)

and the **Katz–Penfold relation**, valid over $0.01$–$3\ \text{MeV}$:

$$
R_m\ [\text{mg/cm}^2] = 412\, T_{\max}^{\,n}, \qquad
n = 1.265 - 0.0954\,\ln T_{\max}\ [\text{MeV}] .
$$ (eq-katz-penfold)

Katz–Penfold is implicit in $T_{\max}$ and must be inverted numerically; doing
so is one of the analysis steps. Report both, and comment on the difference —
these are fits to data, not laws, and they disagree by a few percent, which is
itself an honest systematic uncertainty on your energy.

### The relativistic payoff

Given $T_{\max}$, the total energy is $E = T_{\max} + m_ec^2$ with
$m_ec^2 = 0.511\ \text{MeV}$, so

$$
\gamma = 1 + \frac{T_{\max}}{m_ec^2},
\qquad
\frac{v}{c} = \sqrt{1 - \frac{1}{\gamma^{2}}},
\qquad
pc = \sqrt{E^2 - (m_ec^2)^2}.
$$ (eq-beta-kinematics)

The classical prediction, for comparison, is

$$
\left(\frac{v}{c}\right)_{\text{classical}} = \sqrt{\frac{2T_{\max}}{m_ec^2}} .
$$ (eq-beta-classical)

## Pre-lab

:::{exercise}
:label: q-beta-01

Evaluate [](#eq-beta-kinematics) and [](#eq-beta-classical) for
$T_{\max} = 2.28\ \text{MeV}$. Report $\gamma$, the relativistic $v/c$, the
momentum $pc$ in MeV, and the classical $v/c$. Comment on the last one.
:::

:::{exercise}
:label: q-beta-02

Use [](#eq-feather) to predict the maximum range of $^{90}$Y betas in
aluminium, in $\text{g/cm}^2$, and convert it to a physical thickness in
millimetres ($\rho_{\text{Al}} = 2.70\ \text{g/cm}^3$). Does the absorber set
on the bench go thick enough?
:::

:::{exercise}
:label: q-beta-03

A detector records $N$ counts in time $t$. The uncertainty on $N$ is
$\sqrt{N}$. Show that the *relative* uncertainty on the rate is
$1/\sqrt{N}$, and find the number of counts needed for a 1% measurement. If
the rate behind a thick absorber is $2\ \text{s}^{-1}$, how long must you
count for 1%?
:::

:::{exercise}
:label: q-beta-04

Why is the *maximum* range, rather than a half-value thickness, the quantity
related to the endpoint energy? Sketch the expected shape of $\log R$ against
$x$ and mark where the endpoint information lives.
:::

## Apparatus

- GM tube with a thin end window ($\lesssim 2\ \text{mg/cm}^2$ mica) on a
  shelf stand, with counter/timer and high-voltage supply
- Sealed $^{90}$Sr/$^{90}$Y source, $\sim1\ \mu\text{Ci}$
- Aluminium absorber set, roughly $5$ to $1200\ \text{mg/cm}^2$
- Micrometer and balance, to verify the labelled mass thicknesses
- Source tongs; the source log sheet

:::{danger}
Sealed beta source. Sign it in and out, handle with tongs, keep it in the
shielded holder except while counting, and wash your hands when you leave.
Read [](#lab-safety).
:::

## Procedure

### Part A — The plateau and the operating voltage

1. With the source on the second shelf, ramp the GM high voltage upward in
   $25\ \text{V}$ steps from below the starting voltage, counting for
   $30\ \text{s}$ at each step. Plot rate against voltage as you go.
2. Identify the plateau — the flat region where the rate is nearly independent
   of voltage — and set the operating voltage about $75$–$100\ \text{V}$ above
   the plateau knee.

**[ ] Checkpoint 1.** Show the instructor your plateau
plot and your chosen operating voltage. A tube run above the plateau goes into
continuous discharge and will be destroyed.

:::{warning}
Never leave the supply above the plateau while you go and think about it. If
the count rate starts climbing steeply with voltage, come back down at once.
:::

### Part B — Background

3. Return the source to its shielded storage. Count the background for at
   least $10\ \text{minutes}$ in a single run and record $N_{\text{bg}}$ and
   the live time. You will subtract this rate from everything.
4. Note the counts, not just the rate; you need $N$ to get the Poisson
   uncertainty.

### Part C — The absorption curve

5. Place the source on a fixed shelf and *do not move it again* — the
   source–detector distance must be identical for every point, or the inverse
   square law will masquerade as absorption.
6. Count with no absorber. Choose a counting time long enough to accumulate at
   least $10\,000$ counts.
7. Add absorbers one at a time, working upward in mass thickness. Use at least
   **fifteen** absorber values, spaced so that the points are roughly evenly
   distributed in $\log(\text{rate})$ — that means fine steps at first and
   coarser ones later.
8. **Increase the counting time as the rate falls**, so that every point
   carries a comparable *relative* uncertainty. This is the single most
   important procedural habit in this experiment. A point at
   $1200\ \text{mg/cm}^2$ counted for $30\ \text{s}$ contributes nothing but
   noise to the extrapolation that determines your answer.
9. Continue past the point where the rate stops falling, and take at least
   four points on the flat tail. That tail is what defines the background-plus-
   bremsstrahlung floor, and the extrapolation to it is your measurement.
10. Verify two or three of the absorbers' labelled mass thicknesses by
    weighing them and measuring their area. Foil labels are sometimes optimistic.

## Analysis

### Rates and their uncertainties

For each point, the net rate and its uncertainty are

$$
R = \frac{N}{t} - \frac{N_{\text{bg}}}{t_{\text{bg}}},
\qquad
\sigma_R = \sqrt{\frac{N}{t^2} + \frac{N_{\text{bg}}}{t_{\text{bg}}^2}} .
$$

Correct for dead time if the no-absorber rate exceeds a few hundred per
second: with dead time $\tau_d \approx 100\ \mu\text{s}$ for a typical GM tube,
the true rate is $R_{\text{true}} = R_{\text{obs}}/(1 - R_{\text{obs}}\tau_d)$.
State whether the correction mattered.

### Finding the range

```python
import numpy as np
from scipy.optimize import curve_fit

x     = np.array([...])      # mass thickness, mg/cm^2 (absorber + window + air)
R     = np.array([...])      # net rate, 1/s
sR    = np.array([...])      # Poisson uncertainty on the net rate

# Fit the falling part only: exponential plus a constant floor.
def model(x, R0, mu, floor):
    return R0 * np.exp(-mu * x) + floor

popt, pcov = curve_fit(model, x, R, p0=[R[0], 3e-3, R[-1]],
                       sigma=sR, absolute_sigma=True)
R0, mu, floor = popt
```

The maximum range is where the beta term drops below the floor's own
uncertainty. A defensible operational definition, and the one to use here: the
mass thickness at which the fitted exponential term equals the standard
uncertainty of the measured floor,

$$
R_0 e^{-\mu R_m} = \sigma_{\text{floor}}
\qquad\Longrightarrow\qquad
R_m = \frac{1}{\mu}\,\ln\!\frac{R_0}{\sigma_{\text{floor}}} .
$$

Propagate $\sigma_{R_m}$ from $\sigma_\mu$, $\sigma_{R_0}$, and
$\sigma_{\text{floor}}$ using the full covariance matrix — $R_0$ and $\mu$ are
strongly correlated in an exponential fit, and ignoring that will make your
uncertainty badly wrong. See [](#uncertainty).

:::{important} Do not forget the absorbers you did not add
The total mass thickness between source and detector includes the GM tube's
mica window ($\sim2\ \text{mg/cm}^2$, from the tube's data sheet), the air gap
($1.2\ \text{mg/cm}^2$ per centimetre at room conditions), and any source
cover. For a $3\ \text{cm}$ gap that is another $\sim6\ \text{mg/cm}^2$. It is
a small correction to $R_m$ but it is a *known* one, so make it and say so.
:::

### Energy and speed

Invert both range–energy relations:

```python
from scipy.optimize import brentq

Rm_g = Rm / 1000.0                                   # g/cm^2

T_feather = (Rm_g + 0.133) / 0.542                   # MeV

def kp(T):                                            # Katz-Penfold, implicit
    n = 1.265 - 0.0954 * np.log(T)
    return 412 * T**n - Rm                            # Rm in mg/cm^2

T_kp = brentq(kp, 0.05, 3.0)

mec2  = 0.51099895                                    # MeV
gamma = 1 + T_kp / mec2
beta  = np.sqrt(1 - 1/gamma**2)
pc    = np.sqrt((T_kp + mec2)**2 - mec2**2)
beta_classical = np.sqrt(2 * T_kp / mec2)
```

Report $T_{\max}$ from both relations, take their spread as a systematic
uncertainty, and combine it with the statistical uncertainty from $R_m$.

## Post-lab questions

:::{exercise}
:label: q-beta-05

Quote $T_{\max}$ with its total uncertainty and compare with the accepted
$^{90}$Y endpoint of $2.280\ \text{MeV}$ in units of $\sigma$. Which
contribution dominated your uncertainty — the statistics of the tail, or the
disagreement between the two range–energy relations?
:::

:::{exercise}
:label: q-beta-06

Report the relativistic $v/c$ and the classical $v/c$. The classical value
exceeds 1. Explain what has gone wrong with the classical calculation in terms
of the definition of kinetic energy, not merely by asserting that nothing can
exceed $c$.
:::

:::{exercise}
:label: q-beta-07

Compute the momentum $pc$ of the endpoint electron, and compare it with the
classical $pc = \sqrt{2m_ec^2 T}$. Which of the two — energy or momentum —
does the classical formula get less badly wrong at this energy, and why?
:::

:::{exercise}
:label: q-beta-08

Your absorption curve is not a single clean exponential. Identify on your plot
(a) the region dominated by $^{90}$Sr betas, (b) the region dominated by
$^{90}$Y betas, and (c) the bremsstrahlung tail. Explain why the tail is
present at all, given that the betas have been stopped.
:::

:::{exercise}
:label: q-beta-09

Suppose you had used the *half*-thickness of the absorption curve, together
with a calibration made on a $^{204}$Tl source ($T_{\max} = 0.763\ \text{MeV}$),
to infer the energy instead. What assumption would that method make that the
range method does not? Under what circumstances would it be the better choice?
:::

## Going further

- **Two sources, one calibration.** Measure the ranges of $^{204}$Tl
  ($0.763\ \text{MeV}$) and $^{90}$Sr/$^{90}$Y ($0.546$ and
  $2.28\ \text{MeV}$) and fit your own range–energy relation. Three points
  will not settle the exponent, but comparing your fit with Katz–Penfold is a
  real exercise in what an empirical relation is.
- **Absorber material dependence.** Repeat a few points using plastic or
  copper absorbers of the same *mass* thickness. The near-coincidence of the
  curves is the justification for using mass thickness at all — and the
  deviation for copper is a direct look at the $Z^2$ dependence of
  bremsstrahlung.
- **The Kurie plot.** With a scintillator and a multichannel analyser instead
  of a GM tube, the full beta spectrum can be recorded and linearized into a
  Kurie plot, whose intercept gives the endpoint directly and whose shape near
  the endpoint is sensitive to the neutrino mass. This is how the endpoint is
  really measured, and how the tightest laboratory limits on $m_\nu$ are set.

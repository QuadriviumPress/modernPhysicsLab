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
**Apparatus** Geiger–Müller counter, $^{90}$Sr/$^{90}$Y beta source, aluminum absorber set
**You will estimate** the $^{90}$Y beta endpoint energy from an absorption curve, if the absorber set spans the terminal region and floor, and calculate the speed it implies
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure an absorption curve and estimate a practical range from its terminal
  region, while recognizing when the available absorber thickness is insufficient.
- Convert a range in aluminum into a maximum kinetic energy using an
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

After several $^{90}$Y half-lives, an older sealed $^{90}$Sr source contains
$^{90}$Sr/$^{90}$Y near secular equilibrium:

$$
^{90}\text{Sr} \xrightarrow{\ \beta^-,\ 28.91\ \text{y}\ } {}^{90}\text{Y}
\xrightarrow{\ \beta^-,\ 64.05\ \text{h}\ } {}^{90}\text{Zr\ (stable)} ,
$$

with endpoints $0.546\ \text{MeV}$ and $2.28\ \text{MeV}$ respectively. The
high-energy $^{90}$Y component is the one whose range you will measure,
because it is the only beta component that survives the thicker absorbers.
See the evaluated [strontium-90](https://www.nndc.bnl.gov/nudat3/getdecaydataset.jsp?dsid=90sr+bM+decay+%2828.91+y%29&nucleus=90Y)
and [yttrium-90](https://www.nndc.bnl.gov/nudat3/getdecaydataset.jsp?dsid=90y+bM+decay+%2864.05+h%29&nucleus=90ZR)
decay data.

### Absorption and range

Beta particles lose energy mainly through collisions and can also produce
bremsstrahlung photons. The counting rate behind an absorber of *mass
thickness* $x$ (in $\text{mg/cm}^2$: density times physical thickness) falls
as the electron spectrum is filtered. A single exponential is a rough
description of part of that curve, not a law for the mixed source:

$$
R(x) = R_0\, e^{-\mu_m x} + R_{\text{bg}} ,
$$ (eq-beta-exp)

At large thickness, the measured rate may approach a floor from background
and source-related photons. The practical, or *extrapolated*, range $R_m$ is
estimated from the terminal electron-dominated decline and its intersection
with that floor on a **linear rate axis**. It is not the thickness at which
every electron track ends, and a threshold chosen from counting noise does
not define it. See the [Katz–Penfold range study](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.24.28)
and the [University of Texas at Arlington absorption procedure](https://cdn.web.uta.edu/-/media/project/website/science/physics/documents/degree-programs/physics-lab/nuclear-lab/lab-absorption-of-beta-particles.ashx?revision=c984b7a8-6329-425c-9c91-bcfff216de47).

Mass thickness is used rather than physical thickness because energy loss per
unit mass is nearly the same in all light materials — so a range quoted in
$\text{mg/cm}^2$ is roughly transferable between absorber materials, which
physical millimeters are not.

```{figure} ../images/exp03-absorption-curve-concept.svg
:label: fig:exp03-absorption-curve
:alt: Left, a semilog plot shows a rapid fall in beta transmission and a flat background-plus-photon floor. Right, a linear-scale view of the terminal region fits its declining count rate and marks the intersection with the measured floor as practical range R_m.

Read the full curve on a log rate axis to identify the components. Estimate
$R_m$ from the terminal electron-dominated decline on a linear rate axis,
extrapolated to a floor measured with thicker absorbers. If the floor or the
terminal decline is absent, the plot does not support an endpoint estimate.
```

### From range to energy

Two standard empirical relations connect the maximum range in aluminum to the
endpoint energy. **Feather's rule**, valid for $T_{\max} > 0.8\ \text{MeV}$:

$$
\frac{R_m}{\text{g/cm}^2} = 0.542\,\frac{T_{\max}}{\text{MeV}} - 0.133 ,
$$ (eq-feather)

and the **Katz–Penfold relation**, used here below $2.5\ \text{MeV}$:

$$
\frac{R_m}{\text{mg/cm}^2} = 412\left(\frac{T_{\max}}{\text{MeV}}\right)^{n}, \qquad
n = 1.265 - 0.0954\,\ln\!\left(\frac{T_{\max}}{\text{MeV}}\right) .
$$ (eq-katz-penfold)

Katz–Penfold is implicit in $T_{\max}$ and must be inverted numerically; doing
so is one of the analysis steps. These are empirical calibrations, not exact
laws. Near $2.28\ \text{MeV}$, their predicted ranges differ by less than 1%,
so their agreement does not remove uncertainty from the practical-range
method or the source geometry. Discuss those effects separately.

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
aluminum, in $\text{g/cm}^2$, and convert it to a physical thickness in
millimeters ($\rho_{\text{Al}} = 2.70\ \text{g/cm}^3$). Does the absorber set
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
related to the endpoint energy? Sketch the full curve on a log rate axis and
the terminal region on a linear rate axis. Mark where the endpoint
information lives.
:::

## Apparatus

- GM tube with a thin end window ($\lesssim 2\ \text{mg/cm}^2$ mica) on a
  shelf stand, with counter/timer and high-voltage supply
- Institution-approved sealed $^{90}$Sr/$^{90}$Y source; record the actual
  activity and source identification from the local inventory
- Aluminum absorber set spanning a few $\text{mg/cm}^2$ to at least
  $1.5\ \text{g/cm}^2$, with several settings beyond the predicted
  $^{90}$Y range near $1.1\ \text{g/cm}^2$. If the set ends near the predicted
  range, plan to report only a lower bound or a provisional estimate.
- Micrometer and balance, to verify the labeled mass thicknesses
- Approved source holder or handling tools; the source log sheet

:::{danger}
Sealed beta source and a high-voltage GM supply. Follow the instructor's
approved source sign-out, handling, storage, and voltage procedures. Keep
the source in its designated holder except during authorized measurements;
power down before changing detector connections. Read [](#lab-safety).
:::

```{figure} ../images/exp03-beta-shelf-schematic.svg
:label: fig:exp03-beta-shelf
:alt: A sealed beta source sits on the lowest shelf of a stand, emitting electrons through an interchangeable aluminum absorber stack toward a Geiger–Müller tube connected to a counter and timer.

The fixed source-absorber-tube geometry. Swapping absorber thicknesses and reading the transmitted count rate through each maps the range of the beta electrons in aluminum.
```

## Procedure

### Before you count

- Match the source, absorber shelf, and GM-tube order to
  [](#fig:exp03-beta-shelf). Record the shelf number and source-to-window
  distance; the sketch does not specify those dimensions for your apparatus.
- Inspect the thin detector window without touching it. Confirm that the source
  holder, absorber tray, and detector cannot shift when foils are exchanged.
- List every absorber in increasing areal density and record its labeled
  value before starting. Keep the foils in that order so that a thickness is
  never inferred from appearance.
- Prepare separate tables for the plateau, background, and absorption scan.
  Every counting row must contain raw counts, live time, high voltage,
  absorber identity, and geometry notes—not only a displayed count rate.
- Estimate counting times in advance: choose them so useful absorption points
  have roughly similar fractional Poisson uncertainty. Ask the instructor to
  handle or relocate any source not explicitly assigned to students.

### Part A — The plateau and the operating voltage

1. Use the instructor-approved voltage range and source shelf. If students
   are authorized to measure the plateau, follow the tube's procedure for
   voltage steps and count duration, and plot rate against voltage as you go.
   Otherwise, record the approved operating voltage and skip the scan.
2. Identify a stable plateau if a scan is performed. Use the operating
   voltage approved for this specific tube; do not infer a universal offset
   above the knee.

**[ ] Checkpoint 1.** Show the instructor your plateau
plot or the approved operating setting before taking source data. Do not
increase voltage beyond the specified operating range.

:::{warning}
If the count rate climbs steeply as voltage rises, stop the scan and return to
the approved setting with the instructor. Do not leave the supply at an
unverified voltage.
:::

### Part B — Background

3. Return the source to its shielded storage. Count the background for at
   least $10\ \text{minutes}$ in a single run and record $N_{\text{bg}}$ and
   the live time. Use this rate to calculate net source rates; the terminal
   range fit below uses gross rates so the shared background estimate does
   not introduce correlations.
4. Note the counts, not just the rate; you need $N$ to get the Poisson
   uncertainty.

### Part C — The absorption curve

5. Place the source on the assigned fixed shelf and *do not move it again* —
   a changed source–detector geometry changes detection efficiency and can
   masquerade as absorption. The near-field geometry does not generally obey
   a simple inverse-square law.
6. Count with no absorber. Aim for about $10\,000$ counts if the detector is
   within its validated count-rate range; otherwise follow the instructor's
   lower-rate geometry or timing plan.
7. Add absorbers in increasing mass thickness. Use roughly 10–15 values,
   placing more points near the predicted $^{90}$Y endpoint than in the
   rapidly falling low-thickness region. Record the *total* stack thickness
   for every setting.
8. **Increase counting time as the rate falls**, especially in the terminal
   region. Estimate the time budget before beginning: at $2\ \text{s}^{-1}$,
   100 counts take 50 s but a 1% Poisson measurement takes 5,000 s. The
   latter is not a reasonable target for every point in a three-hour period.
9. If the absorber set extends beyond the terminal fall, take at least four
   thick-absorber points to characterize the floor. If the measured rate is
   still falling at the thickest available setting, record the limitation;
   do not extrapolate an unobserved floor into a claimed endpoint.
10. Verify two or three of the absorbers' labeled mass thicknesses by
    weighing them and measuring their area. Foil labels are sometimes optimistic.

## Analysis

### Rates and their uncertainties

For each point, the net rate and its uncertainty, before any dead-time
correction, are

$$
R = \frac{N}{t} - \frac{N_{\text{bg}}}{t_{\text{bg}}},
\qquad
\sigma_R = \sqrt{\frac{N}{t^2} + \frac{N_{\text{bg}}}{t_{\text{bg}}^2}} .
$$

The same background estimate appears in every net rate, so those net values
are correlated. Plot them to see the source contribution, but fit the
independent *gross* rates $N/t$ in the terminal and floor regions below. A
negative net rate is possible after background subtraction and is not a
negative physical activity.

Check dead-time losses at the largest gross rate using the instrument's
measured or specified dead time. For a **nonparalyzable** model, the correction
is $R_{\text{true}}=R_{\text{obs}}/(1-R_{\text{obs}}\tau_d)$ when
$R_{\text{obs}}\tau_d<1$. It is not a universal GM-tube law or a substitute
for operating below the instrument's rated count rate. Near the endpoint,
where the rate is low, dead time should have little effect; document that
check. See the [IAEA detector-model discussion](https://nucleus.iaea.org/sites/connect/RRIHpublic/CompendiumDB/Shared%20Documents/Czech%20Republic%20CTU/Protocols%20in%20PDF/Czech_Rep_VR1_Reactor_Neutron_detection_Laboratory_protocol.pdf).

### Finding the range

First plot gross count rate against aluminum mass thickness on both log and
linear rate axes. The log view shows the full fall; the linear view reveals
the terminal region and the measured floor. Select a contiguous terminal
region dominated by the $^{90}$Y component, after the low-energy $^{90}$Sr
component has largely disappeared, and a separate set of thick-absorber
points whose rates are consistent with a constant floor. Do **not** fit the
steep initial semilog line and call its intersection with an arbitrary noise
threshold a physical range.

Fit a straight line to the terminal *gross* rates and take its intersection
with the independently measured floor. In the example below, choose the three
thickness boundaries from your plot; keep the terminal and floor selections
disjoint.

```python
import numpy as np
from scipy.optimize import curve_fit

x = np.array([...], dtype=float)       # aluminum mg/cm^2, one value per run
N = np.array([...], dtype=float)       # gross counts
t = np.array([...], dtype=float)       # live time in seconds

x_fit_start, x_fit_end, x_floor_start = ... , ... , ...
terminal = (x >= x_fit_start) & (x <= x_fit_end)
tail = x >= x_floor_start
assert terminal.sum() >= 3 and tail.sum() >= 4
assert not np.any(terminal & tail)
assert np.all(N[terminal | tail] > 0)   # use a Poisson fit for zero-count bins

rate = N / t
srate = np.sqrt(N) / t
w = 1 / srate[tail]**2
floor = np.sum(w * rate[tail]) / np.sum(w)
sfloor = np.sqrt(1 / np.sum(w))

def terminal_line(x, a, b):
    return a + b * x

(a, b), cov = curve_fit(terminal_line, x[terminal], rate[terminal],
                        sigma=srate[terminal], absolute_sigma=True)
assert b < 0
Rm = (floor - a) / b             # aluminum thickness, mg/cm^2
g = np.array([-1 / b, -(floor - a) / b**2])
sRm = np.sqrt(g @ cov @ g + (sfloor / b)**2)
print(f"practical range = {Rm:.0f} +/- {sRm:.0f} mg/cm^2")
```

The covariance term in `sRm` matters because fitted slope and intercept are
correlated. This statistical error is only one part of the range uncertainty.
Vary the terminal fit window and the choice of floor points, inspect the
residuals, and include the resulting model sensitivity. If the floor is not
observed or the terminal segment is not approximately linear, report a lower
bound or an unresolved endpoint instead of a precise energy.

:::{important} Do not forget the absorbers you did not add
The path between source and detector can also include a source cover, air,
and the GM tube's window. Record their actual materials and dimensions. A
$3\ \text{cm}$ air gap alone has about $3.6\ \text{mg/cm}^2$ of mass thickness
at ordinary room conditions, small against a $\sim1100\ \text{mg/cm}^2$ beta
range. Mass thicknesses of different materials are not automatically
equivalent stopping thicknesses; estimate any correction with an appropriate
material model and include its uncertainty rather than adding guessed values.
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

T_kp = brentq(kp, 0.8, 2.5)             # stay within the energy range used here

mec2  = 0.51099895                                    # MeV
gamma = 1 + T_kp / mec2
beta  = np.sqrt(1 - 1/gamma**2)
pc    = np.sqrt((T_kp + mec2)**2 - mec2**2)
beta_classical = np.sqrt(2 * T_kp / mec2)
```

Report $T_{\max}$ from both relations and propagate the uncertainty in $R_m$
by recomputing each energy at $R_m \pm \sigma_{R_m}$. Their difference is a
useful model comparison, but it is not a complete estimate of calibration or
fit-window uncertainty. If the numerical root is not bracketed in the stated
energy range, do not extrapolate this calibration without justification. If
the range was only bounded, invert that bound and report the energy as a
bound too.

## Post-lab questions

:::{exercise}
:label: q-beta-05

Quote $T_{\max}$ with its counting uncertainty and a separate estimate of
the sensitivity to your terminal-fit and floor selections. Compare with the
evaluated $^{90}$Y endpoint of about $2.28\ \text{MeV}$. If you can justify a
combined uncertainty, express the difference in units of that uncertainty;
otherwise state which calibration and geometry effects remain unquantified.
Did the two range–energy relations differ enough to resolve those effects?
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

Your absorption curve is not a single clean exponential. Identify where
low-energy $^{90}$Sr betas cease to contribute substantially and where the
terminal $^{90}$Y decline is most visible. Does the thick-absorber rate reach
a constant floor? Explain why a rate above the separately measured background
could remain after the betas have been stopped, and why the curve alone cannot
prove that all those counts are bremsstrahlung photons.
:::

:::{exercise}
:label: q-beta-09

Suppose you had used the *half*-thickness of the absorption curve, together
with a calibration made on a $^{204}$Tl source ($T_{\max} = 0.763\ \text{MeV}$),
to infer the energy instead. What assumption would that method make that the
range method does not? Under what circumstances would it be the better choice?
:::

## Going further

- **Several sources, one calibration.** If approved sources with distinct
  known beta endpoints are available, measure a practical range for each
  with a common geometry and fit an empirical range–energy relation. A mixed
  $^{90}$Sr/$^{90}$Y source does not automatically give two separately
  measurable practical ranges. Compare your calibration with Katz–Penfold.
- **Absorber material dependence.** Repeat a few points using plastic or
  copper absorbers of the same *mass* thickness. Compare their curves without
  assuming equal stopping power per unit mass, especially for copper. A
  changed thick-absorber floor may reflect photon production or detector
  response; it does not by itself measure a simple $Z^2$ law.
- **The Kurie plot.** With a scintillator and a multichannel analyzer instead
  of a GM tube, an energy spectrum can be recorded and analyzed with a Kurie
  plot, subject to detector resolution and calibration. Precision neutrino-mass
  experiments require much finer control of the spectrum near an endpoint
  than this teaching apparatus provides.

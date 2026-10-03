---
title: A Cosmic-Ray Muon Telescope
short_title: 14. Cosmic-Ray Muons
label: exp-muon-telescope
numbering:
  enumerator: "14.%s"
---

# Experiment 14 — A Cosmic-Ray Muon Telescope

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 14, *Elementary Particles and the Standard Model*
**Apparatus** Two Geiger–Müller tubes, microcontroller coincidence unit, absorbers, protractor mount
**You will measure** the coincidence rate of penetrating cosmic-ray particles, and its angular dependence if enough counts can be collected
**Report** **Full report** — this is one of the three
:::

## Objectives

By the end of this experiment you should be able to:

- Build and validate a coincidence detector, and distinguish true coincidences
  from accidentals.
- Estimate a vertical muon intensity only if detector efficiency and
  non-muon coincidences can be independently constrained.
- Compare corrected angular rates with a finite-acceptance
  $\cos^n\theta$ model when the counts support a fit.
- Calculate survival for a stated muon energy and production altitude,
  while distinguishing that model from what a one-altitude rate measures.

## Textbook connection

Read §14.1–14.4, and §2.5 on time dilation. The muon is a second-generation
charged lepton with the same electric charge and spin as the electron. Its
discovery prompted the question "Who ordered that?", attributed to
I. I. Rabi. It is also an accessible relativistic
particle in existence. Muons from upper-atmosphere showers can reach sea
level because their laboratory-frame lifetimes are dilated.

This experiment closes the course by using the relativity of Weeks 1–3 to
explain the particle physics of Chapter 14, with a detector you build.

## Theory

### Where muons come from

Primary cosmic rays — mostly protons and other nuclei — strike nuclei in
the upper atmosphere and produce showers containing pions. Charged
pions decay,

$$
\pi^+ \to \mu^+ + \nu_\mu,
\qquad
\pi^- \to \mu^- + \bar\nu_\mu ,
$$

and many resulting muons penetrate the remaining atmosphere. They are
charged and ionize matter, but their much larger mass than the electron's
greatly reduces radiative energy loss at a few GeV. A typical sea-level
muon has energy around
$4\ \text{GeV}$; the muon's rest energy is $105.66\ \text{MeV}$, so a typical
Lorentz factor is of order $\gamma \approx 40$, and lower-energy muons at
$\gamma \approx 20$ are abundant.

### Why they should not get here

The muon's proper mean lifetime is $\tau_0 = 2.197\ \mu\text{s}$. The length
scale $c\tau_0$ is

$$
c\tau_0 = 659\ \text{m}
$$

but it is not a distance traveled in the muon's rest frame. For a
hypothetical muon produced $15\ \text{km}$ above the detector, a
calculation that omits time dilation and sets $\beta\approx1$ gives
$15000/659 = 22.8$ lifetimes and a survival
probability of

$$
e^{-22.8} \approx 1.2\times10^{-10} .
$$

This is a model comparison, not a prediction of the observed flux:
production occurs over a range of altitudes and energies. The familiar
roughly one muon per square centimeter per minute is a flux integrated
over arrival directions, not an intensity per steradian.

### Why they do

In the laboratory frame the muon's lifetime is dilated to $\gamma\tau_0$, so
its mean decay length at fixed speed is $\gamma\beta c\tau_0$. For
$\gamma = 20$ this is approximately $13.2\ \text{km}$, and survival
from the assumed $15\ \text{km}$ becomes
$e^{-15/13.2} \approx 0.32$ — a factor of about $2.5\times10^{9}$ larger.

In the muon's frame the distance between the chosen production and detection
events is $15\ \text{km}/\gamma = 750\ \text{m}$ in this constant-speed
model. It crosses in about $0.75\ \text{km}/(\beta c)$, close to one
proper mean lifetime. The two descriptions are the same
physics in different coordinates, and being able to give both is one of the
things this course is for.

```{figure} ../images/exp14-time-dilation-concept.svg
:label: fig:exp14-time-dilation
:alt: For a hypothetical 15 km production path and muon Lorentz factor 20, the lab-frame 13.2 km mean decay length is compared with the 0.66 km length scale obtained by omitting dilation. In the muon's frame the 15 km path contracts to 0.75 km, compared with the 0.66 km scale c times proper mean lifetime.

The same illustrative 15 km path in two frames, for $\gamma=20$ and
approximately constant speed. The bars compare mean decay lengths with
distance; they do not represent measured production heights or energies.
```

### The angular distribution

Muons arriving from a zenith angle $\theta$ must traverse a longer slant path
through the atmosphere, roughly $\propto \sec\theta$, and so are more likely to
decay or be absorbed. For a restricted zenith and energy range, a useful
empirical approximation is

$$
I(\theta) = I_0\cos^{n}\theta, \qquad n \approx 2 ,
$$ (eq-muon-angular)

with representative near-vertical intensity of order
$0.5\ \text{cm}^{-2}\text{min}^{-1}\text{sr}^{-1}$ at sea level.
The normalization and exponent depend on energy threshold, altitude,
and angular range; the $\cos^2\theta$ approximation is not reliable
near the horizon. The central bench result is a validated coincidence
rate. An exponent needs much longer runs.

### Coincidence and accidentals

A single GM tube counts local radioactivity and electronic noise as well as
muons. Requiring two aligned tubes to fire within a short window selects
penetrating-particle candidates. Some correlated shower secondaries can
also fire both, so coincidence alone does not identify every event as
a muon.

For a symmetric timestamp cut $|t_1-t_2|\le\tau_{\text{coinc}}$, the
rate of **accidental** coincidences from two independent stationary singles
streams of rates $R_1$ and $R_2$ is approximately

$$
R_{\text{acc}} = 2\,\tau_{\text{coinc}}\,R_1 R_2 .
$$ (eq-accidentals)

For $R_1 = R_2 = 0.5\ \text{s}^{-1}$ and $\tau_{\text{coinc}} = 1\ \mu\text{s}$
this is $5\times10^{-7}\ \text{s}^{-1}$, or about one event in 23 days.
A short laboratory run cannot measure that tiny rate directly. Use the
measured singles rates, an offset-timestamp control, and a timing-window
scan to test the estimate and report an upper limit if no accidentals appear.

### Geometric acceptance

For two ideal parallel planar detectors of area $A$ separated by
$d \gg \sqrt{A}$, the solid angle subtended is approximately
$\Omega \approx A/d^2$, and the near-vertical coincidence rate is

$$
R \approx \epsilon_1\epsilon_2 I_0\, A\, \Omega .
$$ (eq-muon-rate)

For $A = 10\ \text{cm}^2$, $d = 10\ \text{cm}$, and
$I_0=0.5\ \text{cm}^{-2}\text{min}^{-1}\text{sr}^{-1}$,
$\Omega\approx0.1\ \text{sr}$ and the ideal rate is only
$0.5\ \text{min}^{-1}$ before efficiency losses. A 30-minute run then
expects about 15 ideal counts, or 26% counting uncertainty. The finite
geometry needs an acceptance calculation, and cylindrical GM tubes
cannot simply use their external cross section as $A$.

## Pre-lab

:::{exercise}
:label: q-muon-01

Compute $c\tau_0$ for the muon. Then compute the survival probability from
$15\ \text{km}$ with and without time dilation for $\gamma = 20$, and report
the ratio.
:::

:::{exercise}
:label: q-muon-02

A muon has total energy $4.0\ \text{GeV}$. Compute $\gamma$, $\beta$, and
$1-\beta$. How many significant figures do you need to write $\beta$ usefully?
:::

:::{exercise}
:label: q-muon-03

Use [](#eq-muon-rate) for the illustrative planar geometry, then estimate
how active tube shape and unknown efficiency might lower the actual rate.
How many counts give 10% Poisson uncertainty, and how long would those
counts take at the illustrative $0.5\ \text{min}^{-1}$ rate? Plan what a
three-hour session can establish.
:::

:::{exercise}
:label: q-muon-04

Evaluate [](#eq-accidentals) for assumed singles rates of
$0.5\ \text{s}^{-1}$ each and a symmetric $1\ \mu\text{s}$ half-window.
How many accidental counts would you expect in three hours? In the lab,
repeat the estimate with the selected timing window.
:::

## Apparatus

- Two larger-area GM tubes with matched high voltage and accessible pulse
  outputs, mounted rigidly one above the other with adjustable separation
- Microcontroller coincidence unit with manufacturer-approved, isolated
  low-voltage pulse outputs and characterized timing inputs. **Never
  connect a raw GM high-voltage pulse to a GPIO pin.**
- Rotating mount with an angle scale, or a rigid frame that can be set at
  measured zenith angles
- Optional absorber placed **between** tubes for a penetration control
- A data logger able to record long runs under the institution's unattended
  equipment procedure

:::{danger}
GM supplies may operate at several hundred volts. Power down and follow
the discharge procedure before changing connections. Use only the
approved isolated pulse interface; a resistor or clamp alone is not a
high-voltage isolation barrier. Do not modify the interface circuit.
See [](#lab-safety).
:::

```{figure} ../images/exp14-muon-telescope-schematic.svg
:label: fig:exp14-telescope
:alt: Two Geiger–Müller tubes and an optional absorber between them are fixed to a frame tilted from vertical by a zenith angle theta. Penetrating-particle tracks pass through both tubes, whose isolated low-voltage outputs feed a coincidence unit.

The two-tube coincidence telescope. Charged particles traversing both
active volumes can trigger a count; the optional absorber tests penetration.
Rotate the complete rigid frame to set its zenith angle $\theta$.
```

## Procedure

### Before you build the telescope

- Match the stacked-tube geometry, angle definition, adjustable separation,
  and coincidence electronics to [](#fig:exp14-telescope). Determine the
  active dimensions, projected shape, and center-to-center separation on
  the real instrument; the drawing is not to scale.
- Label the tubes and electronic channels permanently. Record plateau voltage,
  threshold, pulse polarity, pulse width, cable length, and firmware version
  for each channel before combining them.
- Check timestamp resolution, dropped pulses, and clock stability. Choose
  run names recording angle, separation, coincidence window, and start
  time; write metadata even for controls.
- Level the rotation axis, define $0°$ with a plumb line or inclinometer, and
  mark the tube centers. At each angle confirm that the two active areas remain
  aligned rather than merely reading the scale.
- Make a run plan: singles, displaced-geometry control, timestamp-offset
  control, window scan, and a vertical baseline. Add angles only after a
  short rate test shows that they can accumulate useful counts.

### Part A — Build and validate the coincidence unit

1. Set both tubes to their plateau operating voltages, individually, as in
   [](#exp-beta-electrons).
2. Configure the approved unit to timestamp pulses on both channels and
   count a pair when $|t_1-t_2|\le\tau_{\text{coinc}}$. Save both singles
   streams, pair time differences, and live duration, or save enough data
   to reconstruct them. Prevent one pair from being counted twice.
3. Record the singles rate of each tube separately, over at least 10 minutes.

**[ ] Checkpoint 1.** Show the instructor your singles
rates and one minute of coincidence output.

### Part B — Prove that the coincidences are real

Three controls test different failure modes:

4. **Displace the tubes** so their direct overlap is removed while the
   electronics and environment stay fixed. Record the residual coincidence
   rate or its Poisson upper limit; correlated shower particles may remain.
5. **Offset one timestamp stream** by much more than the timing window,
   wrapping within a long run if needed. Count offset matches at many shifts
   and compare their average with the independent-singles prediction.
6. **Scan the symmetric half-window** across the measured pair-time peak.
   Choose a width that contains the stable prompt peak while limiting
   accidentals. The prompt efficiency need not be flat below the timing
   jitter. Plot counts versus window width with Poisson intervals.

**[ ] Checkpoint 2.** Present the controls and chosen window before
starting long runs. If the rate is too low to measure a control directly,
show its upper limit and the corresponding live time.

### Part C — The angular distribution

7. With the telescope vertical ($\theta = 0$), make a baseline run and
   estimate the live time needed for the planned uncertainty. At the
   illustrative ideal rate, 30 minutes gives only about 15 counts.
8. If time permits, rotate the **whole frame** to $30°$, $45°$, and $60°$;
   give each angle enough exposure to provide a useful count or Poisson
   upper limit. Record actual live time and angle. Treat $75°$ as an
   extension: rates are very low and the simple $\cos^2\theta$ model
   may fail there.
9. Return to $0°$ for a second baseline of comparable precision if
   possible. A rate difference may signal drift or changing environmental
   conditions and needs investigation.
10. Determine the active-area geometry and separation. For an absolute
    intensity, use an independently calibrated **muon** reference detector
    or a suitable third-detector efficiency measurement, and estimate
    correlated non-muon coincidences. A gamma check source or an
    unqualified tube data-sheet value does not give muon efficiency.
    Otherwise report the background-corrected coincidence rate and
    relative angular trend.

:::{tip} Use the week, not just the period
This experiment is limited by counting statistics. If the institution
approves unattended operation, schedule longer runs at each planned angle.
At $0.5$ ideal count per minute, about 200 minutes gives 100 counts
(10% Poisson uncertainty) at one angle; 3% requires roughly 1,100 counts,
or 37 hours before efficiency losses.
:::

### Part D (optional) — Penetration control

11. With the frame vertical, place the approved absorber **between** the
    tubes and compare the coincidence rate with a no-absorber run of
    comparable duration. Keep geometry fixed and include accidental and
    background intervals.
12. A modest absorber may suppress soft charged secondaries while
    transmitting most GeV muons. It does not measure a muon momentum
    spectrum or identify every surviving coincidence as a muon.

## Analysis

### Flux

For the narrow-angle, ideal planar approximation, a vertical measurement
would give

$$
I_0 \approx
\frac{R(0)-R_{\text{acc}}-R_{\text{corr}}}
{\epsilon_1\epsilon_2\, A\,\Omega},
\qquad \Omega \approx \frac{A}{d^2} ,
$$

where $R_{\text{corr}}$ is a separately estimated correlated non-muon
coincidence rate. With only two GM tubes, $\epsilon_1\epsilon_2$ and
$R_{\text{corr}}$ are not determined by the singles and coincidence rates.
Report an absolute intensity only when those quantities have independent
support. The planar formula also needs a finite-geometry check.

For two planar rectangles of active width $w_x$, height $w_y$, and
separation $d$, this Monte Carlo estimates a vertical geometric factor
for a direction-independent intensity:

```python
import numpy as np
rng = np.random.default_rng(0)

n = 2_000_000
wx, wy, d = ..., ..., ...              # measured active dimensions, cm
A = wx * wy
x0 = rng.uniform(-wx/2, wx/2, n)
y0 = rng.uniform(-wy/2, wy/2, n)
u = rng.random(n)                       # cos(angle to telescope axis)
phi = rng.uniform(0, 2*np.pi, n)
shift = d * np.sqrt(1-u*u) / u
hit = ((np.abs(x0 + shift*np.cos(phi)) <= wx/2) &
       (np.abs(y0 + shift*np.sin(phi)) <= wy/2))
G0 = 2*np.pi*A*np.mean(u*hit)           # cm^2 sr
G_vertical_cos2 = 2*np.pi*A*np.mean(u**3*hit)  # for I ~ cos^2(zenith)
sG0 = 2*np.pi*A*np.std(u*hit, ddof=1)/np.sqrt(n)
sG_vertical_cos2 = 2*np.pi*A*np.std(u**3*hit, ddof=1)/np.sqrt(n)
```

The factor $u$ is the projected-area factor. The sampled directions are
uniform in solid angle, with $u$ uniform from 0 to 1; sampling
$u^{1/3}$ would instead bake a $\cos^2$ intensity into the sample.
Report both geometric factors and their Monte Carlo uncertainties;
compare $G_0$ with $A^2/d^2$. The $\cos^2$ weighting changes the
vertical count prediction for a finite field of view.
For a real cylindrical GM tube, use its active volume and directional
efficiency in a refined model. The difference between approximate and
refined acceptances is a correction, not automatically an uncertainty.

If qualified, compare your vertical intensity with a reference for the
same energy threshold and altitude; do not compare it with the
all-direction flux of about $1\ \text{cm}^{-2}\text{min}^{-1}$.

### The angular exponent

Fit **raw counts** with a Poisson model using each angle's live time.
For a narrow telescope, model its corrected rate as
$R(\theta)\approx\epsilon_1\epsilon_2 I_0 G_0\cos^n\theta+
R_{\text{acc}}+R_{\text{corr}}$.
For a broad acceptance, integrate $\cos^n\zeta$ over all directions that
can cross both detectors after the entire frame rotates; $\zeta$ is the
track's zenith angle, which differs from the frame angle for off-axis
tracks. The telescope's local geometric factor remains fixed when the
whole rigid frame rotates, but the sky intensity across its field of view
does not. Quote $n$ only if several angles have enough counts to constrain
it; otherwise show intervals or upper limits and state the angular trend.

### Time dilation

The one-altitude coincidence rate cannot determine a Lorentz factor or a
survival fraction because the production rate, height distribution, and
energy spectrum are unmeasured. As a **model exercise**, suppose a muon
starts at $h=15\ \text{km}$ with constant speed and ask what
$\gamma\beta$ gives a specified survival probability $p$:

$$
\gamma\beta = \frac{h}{c\tau_0\ln(1/p)}.
$$

For $p=0.01$, convert this to $\gamma$ using
$\gamma=\sqrt{1+(\gamma\beta)^2}$, then compare with a muon of
$4\ \text{GeV}$ **total** energy. This is a conditional threshold from
chosen assumptions, not a lower bound extracted from your telescope data.

## Post-lab questions

:::{exercise}
:label: q-muon-05

Report the corrected vertical coincidence rate with its count interval.
If you have independent muon efficiency and non-muon background estimates,
also report vertical intensity and compare it with an appropriate reference.
Which uncertainty component dominates?
:::

:::{exercise}
:label: q-muon-06

If the angular data constrain $n$, report it with uncertainty and compare
with 2 over the fitted angular range. Otherwise report rate intervals or
upper limits. Explain physically why the sea-level rate usually falls
with zenith angle.
:::

:::{exercise}
:label: q-muon-07

Present the three Part B controls with counts, live times, or upper limits.
Show the measured prompt time-difference distribution and compare the
offset-timestamp accidentals with [](#eq-accidentals).
:::

:::{exercise}
:label: q-muon-08

For the stated 15 km model and 1% survival threshold, report the required
$\gamma$ and corresponding total muon energy. Explain why it is not a
bound measured by this telescope. Give the equivalent lab-frame
time-dilation and muon-frame length-contraction calculations.
:::

:::{exercise}
:label: q-muon-09

The muon is a second-generation charged lepton. Using the Standard Model
table in Chapter 14, state which fundamental interactions it participates
in and which it does not. Explain why a muon of a few GeV loses much less
energy to bremsstrahlung in the atmosphere than an electron of the same
energy; both carry electric charge.
:::

:::{exercise}
:label: q-muon-10

Rossi and Hall measured the muon flux at two altitudes in 1941 and compared
the attenuation with the muon lifetime. Explain why measuring at *two*
altitudes is a much stronger test of time dilation than measuring at one, and
describe the energy threshold, detector calibration, atmospheric
production, and exposure controls needed for a modern version.
:::

## Going further

- **Two-altitude measurement.** With a sufficiently large, calibrated
  telescope, compare rates at widely separated heights while matching
  zenith acceptance and energy threshold. Model additional atmospheric
  production and energy loss before interpreting the ratio as survival.
  A 100 m height difference changes the survival factor of a
  $\gamma=40$ muon by only about 0.4%, before these other effects.
- **Penetration study.** Compare well-measured rates with and without an
  absorber between the detectors. A modest thickness can help identify
  a soft component, but it does not yield a GeV muon momentum spectrum.
- **Stopped-muon lifetime project.** Use a separate detector with a
  stopping target, fast scintillation readout, and a decay-electron
  trigger. Measure timing response and accidental delayed pairs before
  fitting a lifetime. A GM tube's recovery time and this two-tube layout
  cannot reliably resolve a 2.2 $\mu\text{s}$ stopped-muon decay.

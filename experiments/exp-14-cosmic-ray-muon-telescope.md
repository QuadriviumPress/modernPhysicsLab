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
**You will measure** the sea-level muon flux, its $\cos^2\theta$ angular distribution, and the time-dilation factor needed to explain it
**Report** **Full report** — this is one of the three
:::

## Objectives

By the end of this experiment you should be able to:

- Build and validate a coincidence detector, and distinguish true coincidences
  from accidentals.
- Estimate the absolute vertical flux of cosmic-ray muons at sea level, using
  a measured detector efficiency and geometric acceptance.
- Measure the angular distribution of that flux and fit it to $\cos^n\theta$.
- Show quantitatively that muons could not reach the ground without
  relativistic time dilation, and extract the Lorentz factor required.

## Textbook connection

Read §14.1–14.4, and §2.5 on time dilation. The muon is a second-generation
charged lepton — an electron in every respect but mass — and it was the first
particle discovered that nobody had asked for. ("Who ordered that?" is
attributed to I. I. Rabi.) It is also the most accessible relativistic
particle in existence: several of them pass through your hand every second,
and they are here only because of time dilation.

This experiment closes the course by using the relativity of Weeks 1–3 to
explain the particle physics of Chapter 14, with a detector you build.

## Theory

### Where muons come from

Primary cosmic rays — mostly protons at GeV to TeV energies — strike nuclei in
the upper atmosphere at altitudes around $15\ \text{km}$ and produce showers
of pions. Charged pions decay,

$$
\pi^\pm \to \mu^\pm + \nu_\mu\ (\bar\nu_\mu) ,
$$

and the muons, being weakly interacting and only minimally ionizing, penetrate
the remaining atmosphere. A typical sea-level muon has energy around
$4\ \text{GeV}$; the muon's rest energy is $105.66\ \text{MeV}$, so a typical
Lorentz factor is of order $\gamma \approx 40$, and lower-energy muons at
$\gamma \approx 20$ are abundant.

### Why they should not get here

The muon's proper lifetime is $\tau_0 = 2.197\ \mu\text{s}$. Travelling at
essentially $c$, a muon covers

$$
c\tau_0 = 659\ \text{m}
$$

in one lifetime *as measured in its own frame*. From $15\ \text{km}$, a
non-relativistic accounting gives $15000/659 = 22.8$ lifetimes, and a survival
probability of

$$
e^{-22.8} \approx 1.2\times10^{-10} .
$$

Essentially none should arrive. In fact roughly one muon per square centimetre
per minute arrives at sea level.

### Why they do

In the laboratory frame the muon's lifetime is dilated to $\gamma\tau_0$, so
its decay length is $\gamma\beta c\tau_0$. For $\gamma = 20$ this is
$13.2\ \text{km}$, and the survival probability from $15\ \text{km}$ becomes
$e^{-15/13.2} \approx 0.32$ — a factor of $2.7\times10^{9}$ larger.

Seen from the muon's own frame the explanation is length contraction: the
atmosphere is only $15\ \text{km}/\gamma = 750\ \text{m}$ thick, which it
crosses comfortably in about one lifetime. The two descriptions are the same
physics in different coordinates, and being able to give both is one of the
things this course is for.

```{figure} ../images/exp14-time-dilation-concept.svg
:label: fig:exp14-time-dilation
:alt: Left, in the lab frame the atmosphere is 15 km while the muon decay length grows from 0.66 km without dilation to 13.2 km with it. Right, in the muon's own frame the atmosphere is contracted to 0.75 km, almost matching the undilated proper decay length of 0.66 km.

The same numbers, both ways. Left: without dilation the decay length is far too short to matter; with it, the decay length nearly spans the atmosphere. Right: in the muon's frame it is the atmosphere, not the muon's lifetime, that shrinks — down to almost exactly one proper decay length.
```

### The angular distribution

Muons arriving from a zenith angle $\theta$ must traverse a longer slant path
through the atmosphere, roughly $\propto \sec\theta$, and so are more likely to
decay or be absorbed. The empirical result at sea level is

$$
I(\theta) = I_0\cos^{n}\theta, \qquad n \approx 2 ,
$$ (eq-muon-angular)

with $I_0 \approx 1\ \text{cm}^{-2}\text{min}^{-1}\text{sr}^{-1}$ for vertical
muons above about $1\ \text{GeV}$. Measuring $n$ is the central quantitative
result of this experiment.

### Coincidence and accidentals

A single GM tube counts local radioactivity and electronic noise as well as
muons. Requiring two tubes, one above the other, to fire within a short
window $\tau_{\text{coinc}}$ selects particles that passed through both — a
*telescope* whose axis you can point.

The rate of **accidental** coincidences from two uncorrelated singles rates
$R_1$ and $R_2$ is

$$
R_{\text{acc}} = 2\,\tau_{\text{coinc}}\,R_1 R_2 .
$$ (eq-accidentals)

For $R_1 = R_2 = 0.5\ \text{s}^{-1}$ and $\tau_{\text{coinc}} = 1\ \mu\text{s}$
this is $5\times10^{-7}\ \text{s}^{-1}$ — utterly negligible against an
expected true rate of order one per minute. You will verify this experimentally
rather than trusting the arithmetic.

### Geometric acceptance

For two detectors of area $A$ separated by a distance $d \gg \sqrt{A}$, the
solid angle subtended is approximately $\Omega \approx A/d^2$, and the expected
coincidence rate is

$$
R \approx I_0\, A\, \Omega .
$$ (eq-muon-rate)

For $A = 10\ \text{cm}^2$ and $d = 10\ \text{cm}$, $\Omega = 0.1\ \text{sr}$
and $R \approx 1\ \text{min}^{-1}$. That is a *slow* experiment, and the
counting-statistics discipline of Week 13 is what makes it possible.

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

Using [](#eq-muon-rate) with the actual dimensions of the GM tubes on the
bench, estimate your coincidence rate in counts per minute, and hence the
counting time needed for a 10% measurement. How many angles can you cover in a
three-hour period? Plan the run before you arrive.
:::

:::{exercise}
:label: q-muon-04

Evaluate [](#eq-accidentals) with the tubes' measured background singles rates
and a $1\ \mu\text{s}$ window. Express the accidental rate as a fraction of
your expected true rate.
:::

## Apparatus

- Two larger-area GM tubes with matched high voltage and accessible pulse
  outputs, mounted rigidly one above the other with adjustable separation
- Microcontroller (Arduino, Raspberry Pi Pico) with pulse-shaping input
  circuitry for each tube: a limiting resistor, a clamp diode pair, and a
  comparator or Schmitt input. **The tube's raw pulse must not reach a GPIO
  pin directly.**
- Rotating mount with an angle scale, or a rigid frame that can be set at
  measured zenith angles
- Lead absorber sheets (for the range/energy extension)
- Long counting times: the setup should be able to run unattended overnight

:::{danger}
GM supplies at $400$–$900\ \text{V}$. Power down before touching the tubes or
the wiring. The microcontroller side must be optically or resistively isolated
from the high-voltage side; do not modify the interface circuit. See
[](#lab-safety).
:::

```{figure} ../images/exp14-muon-telescope-schematic.svg
:label: fig:exp14-telescope
:alt: Two Geiger-Mueller tubes are mounted horizontally one above the other on a rigid, rotatable frame with adjustable separation; muon tracks pass through both tubes at an adjustable zenith angle, and both tubes feed a coincidence microcontroller, with optional lead absorbers below.

The two-tube coincidence telescope. Only muons crossing both tubes' overlap volume trigger a coincidence count; rotating the frame to a zenith angle $\theta$ maps out the $\cos^2\theta$ angular distribution.
```

## Procedure

### Before you build the telescope

- Match the stacked-tube geometry, angle definition, adjustable separation,
  and coincidence electronics to [](#fig:exp14-telescope). Measure active
  dimensions and centre-to-centre separation on the real instrument; the
  drawing is intentionally not to scale.
- Label the tubes and electronic channels permanently. Record plateau voltage,
  threshold, pulse polarity, pulse width, cable length, and firmware version
  for each channel before combining them.
- Synchronize the acquisition computer clock and choose a run-naming scheme
  containing angle, separation, coincidence window, and start time. Write a
  metadata line even for control runs.
- Level the rotation axis, define $0°$ with a plumb line or inclinometer, and
  mark the tube centres. At each angle confirm that the two active areas remain
  aligned rather than merely reading the scale.
- Make a run plan before collecting data: singles, side-by-side control,
  coincidence-window scan, source control, every angle, and a final return to
  $0°$. Estimate durations from a short rate test so low-angle and high-angle
  points reach useful statistical precision.

### Part A — Build and validate the coincidence unit

1. Set both tubes to their plateau operating voltages, individually, as in
   [](#exp-beta-electrons).
2. Program the microcontroller to timestamp pulses on both channels and to
   report a coincidence when they fall within a window $\tau_{\text{coinc}}$.
   Have it print a CSV line per coincidence, and a running singles rate. Print
   the timestamps too — you will want them for Part D.
3. Record the singles rate of each tube separately, over at least 10 minutes.

**[ ] Checkpoint 1.** Show the instructor your singles
rates and one minute of coincidence output.

### Part B — Prove that the coincidences are real

Three controls, all essential, and all quick:

4. **Separate the tubes** so that they are side by side rather than one above
   the other, with no common line of sight. The coincidence rate should fall
   nearly to the accidental rate.
5. **Vary the coincidence window** from $\sim0.5\ \mu\text{s}$ to
   $\sim100\ \mu\text{s}$. The true rate should be flat; the accidental rate
   should rise linearly with $\tau_{\text{coinc}}$, exactly as
   [](#eq-accidentals) predicts. Plot the two contributions.
6. **Add a radioactive source** beside one tube. Its singles rate rises
   sharply; the coincidence rate should barely move.

**[ ] Checkpoint 2.** Present all three controls before
starting the long runs. This is the part of the experiment that turns a number
into evidence, and it is graded accordingly.

### Part C — The angular distribution

7. With the tubes vertical ($\theta = 0$), count for at least $30\ \text{min}$.
8. Rotate to $\theta = 30°, 45°, 60°, 75°$, counting at each for as long as the
   period allows — longer at large $\theta$, where the rate is lowest. With
   small-area tubes, these runs must be overnight or the angular fit should be
   reported as qualitative only.
9. Return to $\theta = 0$ at the end and re-count for 15 minutes. A change
   indicates drift, which must be included in the systematic budget.
10. Measure the tube active areas and their separation carefully, and determine
    the single-tube detection efficiency with a calibrated reference or a
    documented manufacturer value. The absolute flux depends on these factors,
    not just the raw coincidence count.

:::{tip} Use the week, not just the period
This experiment is limited by counting statistics, and the apparatus needs no
supervision. Leave it running at $\theta = 0$ overnight, and arrange with the
instructor to swap the angle daily. A week of unattended running turns a 15%
measurement into a 3% one for no additional effort.
:::

### Part D (optional) — Muon lifetime by delayed coincidence

11. Some muons stop in an absorber between the tubes and decay there, giving a
    second pulse microseconds later. Program the microcontroller to record the
    interval between a stopping signal and any subsequent pulse, and histogram
    the intervals. The exponential decay constant is the muon lifetime.
12. This is a low-rate measurement — the stopping fraction is small — and is
    realistically an overnight or week-long run. It is, however, a direct
    measurement of a fundamental particle lifetime with parts from a drawer.

## Analysis

### Flux

Correct each measured coincidence rate for accidentals, then convert to an
absolute intensity using your measured geometry:

$$
I(\theta) = \frac{R(\theta) - R_{\text{acc}}}{A\,\Omega} ,
\qquad \Omega \approx \frac{A}{d^2} .
$$

The $\Omega \approx A/d^2$ approximation is crude for the geometry you
actually have. A better acceptance comes from a short Monte Carlo:

```python
import numpy as np
rng = np.random.default_rng(0)

# Throw isotropic-in-cos^2 tracks and count those hitting both rectangles.
n = 2_000_000
# sample cos^2 zenith distribution on the upper hemisphere
u   = rng.random(n)
cth = u ** (1/3)                       # inverse CDF for I ~ cos^2 theta on dOmega
sth = np.sqrt(1 - cth**2)
phi = rng.uniform(0, 2*np.pi, n)
# ... propagate a straight line through both detector rectangles and count hits
```

Report the acceptance from both methods and use the difference as a systematic
uncertainty. Doing the Monte Carlo is worth substantial credit; it is how a
real detector acceptance is computed.

Compare your vertical intensity with the accepted
$\approx1\ \text{cm}^{-2}\text{min}^{-1}\text{sr}^{-1}$.

### The angular exponent

```python
from scipy.optimize import curve_fit
import numpy as np

theta = np.radians(np.array([0, 30, 45, 60, 75]))
I     = np.array([...])
sI    = np.array([...])

popt, pcov = curve_fit(lambda t, I0, n: I0 * np.cos(t)**n,
                       theta, I, p0=[1.0, 2.0],
                       sigma=sI, absolute_sigma=True)
```

Report $n$ with its uncertainty and compare with 2. Note that the acceptance
$\Omega$ itself changes with $\theta$ for a real detector pair only if the
geometry changes — if you rotate the whole rigid assembly, it does not, which
is why the assembly must be rigid.

### Time dilation

From your measured sea-level flux and an assumed production altitude of
$15\ \text{km}$, find the Lorentz factor required for the observed survival
fraction. You will need an estimate of the production rate, which you do not
have — so instead invert the question and answer the one your data can
support:

> Given the observed flux and the known production altitude, what is the
> *minimum* $\gamma$ consistent with muons surviving the trip with probability
> at least $10^{-2}$?

Solve $e^{-h/(\gamma\beta c\tau_0)} \ge 10^{-2}$ for $\gamma$, and compare with
$\gamma$ for a $4\ \text{GeV}$ muon. State clearly what your data do and do not
establish. A bound honestly derived is a result; an unbounded claim is not.

## Post-lab questions

:::{exercise}
:label: q-muon-05

Report your vertical muon intensity with its uncertainty, and compare with the
accepted value. Which contributed more to the uncertainty: counting statistics
or the acceptance calculation?
:::

:::{exercise}
:label: q-muon-06

Report the fitted exponent $n$ with uncertainty. Is it consistent with 2?
Explain physically why the flux falls with zenith angle at all.
:::

:::{exercise}
:label: q-muon-07

Present your three validation controls from Part B with numbers, and state
what each rules out. In particular, give the measured dependence of the
accidental rate on $\tau_{\text{coinc}}$ and compare with
[](#eq-accidentals).
:::

:::{exercise}
:label: q-muon-08

State your lower bound on $\gamma$ and the corresponding muon energy. Then
give both explanations of the muon's survival — time dilation in the
laboratory frame, length contraction in the muon frame — and show explicitly
that they give the same numerical answer.
:::

:::{exercise}
:label: q-muon-09

The muon is a lepton of the second generation. Using the Standard Model table
in Chapter 14, state which interactions it participates in and which it does
not, and explain how that accounts for its ability to traverse kilometres of
atmosphere while an electron of the same energy could not.
:::

:::{exercise}
:label: q-muon-10

Rossi and Hall measured the muon flux at two altitudes in 1941 and compared
the attenuation with the muon lifetime. Explain why measuring at *two*
altitudes is a much stronger test of time dilation than measuring at one, and
describe how you would do it with your apparatus given access to a mountain
road.
:::

## Going further

- **Two-altitude measurement.** The Rossi–Hall experiment, done with your own
  telescope: measure the rate at the bottom and the top of the tallest
  accessible building or hill, and compare the attenuation with what
  $\gamma\beta c\tau_0$ predicts. Even a $100\ \text{m}$ height difference
  gives a measurable effect if you count long enough.
- **A momentum spectrum by absorption.** Adding lead between the tubes cuts
  off low-momentum muons, since the range in lead is a known function of
  momentum. Rate versus lead thickness is a crude momentum spectrum, and it
  gives a mean muon energy to compare with the $\gamma$ you bounded.
- **East–west effect.** Slightly more muons arrive from the west than from the
  east, because positive primaries are deflected by the geomagnetic field.
  The asymmetry is a few percent, so it needs a week of running and careful
  attention to systematics — a good senior project, and a measurement of the
  *sign of the charge* of the primary cosmic rays, made from a bench.
- **Muon lifetime.** Complete Part D with a week-long run and fit the decay
  histogram. Getting $2.2\ \mu\text{s}$ out of two Geiger tubes and a
  microcontroller is a fitting way to end the course.

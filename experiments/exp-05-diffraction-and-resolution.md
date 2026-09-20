---
title: Diffraction and the Resolution Limit
short_title: 5. Diffraction and Resolution
label: exp-diffraction
numbering:
  enumerator: "5.%s"
---

# Experiment 5 — Diffraction and the Resolution Limit

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 5, *Diffraction of Light*
**Apparatus** Diode laser, single slits and circular apertures, transmission grating, CD/DVD, camera
**You will measure** slit widths, grating pitch, the track spacing of an optical disc, and a resolution limit
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Fit a single-slit diffraction profile and extract the slit width with an
  uncertainty.
- Use a diffraction grating to measure a wavelength, and explain why a grating
  outperforms a double slit for this purpose.
- Measure a sub-micrometre periodic structure — the track pitch of an optical
  disc — with a laser and a ruler.
- State the Rayleigh criterion, test it experimentally, and explain what sets
  the resolution of a telescope, a microscope, and your own eye.

## Textbook connection

Read §5.1–5.6. The Rayleigh criterion introduced there is the reason
Chapter 7's electron microscope is worth building, and the grating equation is
the instrument that Experiments 10, 11, and 12 all depend on. Treat this week
as calibration for the second half of the course.

## Theory

### The single slit

A slit of width $a$ produces minima where

$$
a\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \ldots
$$ (eq-diff-minima)

(note: $m = 0$ is *not* a minimum — it is the central maximum), and an
intensity profile

$$
I(\theta) = I_0\left[\frac{\sin\beta}{\beta}\right]^{2},
\qquad \beta = \frac{\pi a \sin\theta}{\lambda} .
$$ (eq-diff-single)

The central maximum is twice as wide as the others and contains about 90% of
the transmitted power. Narrowing the slit *widens* the pattern — the inverse
relationship between aperture and angular spread that, translated into
momentum language in Chapter 7, becomes the uncertainty principle.

### The circular aperture

For a circular aperture of diameter $D$ the pattern is the Airy disc, and the
first zero falls at

$$
\sin\theta_1 = 1.22\,\frac{\lambda}{D} .
$$ (eq-diff-airy)

The $1.22$ is the first zero of the Bessel function $J_1$ divided by $\pi$; it
is not $1$, and the difference matters when you compare a measured Airy radius
with a slit-based estimate.

### The Rayleigh criterion

Two incoherent point sources are said to be *just resolved* when the first
zero of one Airy pattern falls on the central maximum of the other:

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D} .
$$ (eq-diff-rayleigh)

This is a convention, not a law of nature — with enough signal-to-noise and a
known point-spread function you can do better, which is the entire basis of
super-resolution microscopy. But it is the right order of magnitude, and it
tells you that resolution is set by the *aperture*, which is why telescopes
are large and why electron microscopes exist.

### The grating

$N$ equally spaced slits of pitch $d$ give maxima at

$$
d\sin\theta = m\lambda ,
$$ (eq-diff-grating)

the same condition as two slits — but the maxima are *far narrower*, with
angular width $\propto 1/N$. That sharpening, not the position of the maxima,
is what makes a grating a spectroscopic instrument. Its resolving power is

$$
\frac{\lambda}{\Delta\lambda} = mN ,
$$ (eq-diff-resolving)

so a $1000\ \text{lines/mm}$ grating with a $5\ \text{mm}$ illuminated width
resolves, in first order, $\lambda/\Delta\lambda = 5000$ — about $0.13\ \text{nm}$
at $650\ \text{nm}$. That number is what you will be relying on in Week 10.

### Optical discs as gratings

The data tracks of a CD or DVD form a reflection grating. Nominal pitches are
$1.6\ \mu\text{m}$ for CD, $0.74\ \mu\text{m}$ for DVD, and $0.32\ \mu\text{m}$
for Blu-ray. For a DVD, $\lambda/d = 650/740 = 0.88$, so first order appears
at $62°$ — a large angle where the small-angle approximation fails completely
and you must measure the actual angle. For Blu-ray at $650\ \text{nm}$,
$\lambda/d > 1$ and *no* first order exists, which is itself a measurement
worth making.

## Pre-lab

:::{exercise}
:label: q-diff-01

For $\lambda = 650\ \text{nm}$ and $a = 0.08\ \text{mm}$, find the angular
position of the first minimum and the width of the central maximum on a screen
at $L = 2.0\ \text{m}$.
:::

:::{exercise}
:label: q-diff-02

Compute the first-order diffraction angle for a $600\ \text{lines/mm}$ grating
at $650\ \text{nm}$. Is the small-angle approximation valid? What is the
largest order you will be able to see at all?
:::

:::{exercise}
:label: q-diff-03

Predict the first-order angle for a CD ($d = 1.6\ \mu\text{m}$) and a DVD
($d = 0.74\ \mu\text{m}$) at $650\ \text{nm}$. Sketch the geometry you will
need to measure those angles, and say what you will measure with what.
:::

:::{exercise}
:label: q-diff-04

The dark-adapted human pupil is about $6\ \text{mm}$ across. Using
[](#eq-diff-rayleigh) at $550\ \text{nm}$, find the smallest angle your eye can
resolve, and convert it to the separation of two headlights just resolvable at
$1\ \text{km}$. Compare with the actual separation of car headlights and
comment.
:::

## Apparatus

- Diode laser, $\lambda \approx 650\ \text{nm}$ (with the uncertainty you
  established in [](#exp-michelson))
- Single slits of several widths; circular apertures; the "unknown" slide
- Transmission grating, $\sim300$–$1000\ \text{lines/mm}$
- CD, DVD, and if available a Blu-ray disc, with the reflective layer exposed
  or used in reflection
- Rotation stage or a large protractor and a metre stick, for large angles
- Camera or scanning photodiode; screen
- Two pinholes on a card with a lamp behind, for the resolution test; variable
  iris

:::{danger}
Class 2 laser, plus specular reflection from the discs. A CD sends beams in
several directions at once. Establish where every order goes before powering
up, and never work with your eye at beam height. See [](#lab-safety).
:::

## Procedure

### Part A — Single slit

1. Set $L \approx 2\ \text{m}$ and illuminate a slit of known width.
2. Record the positions of as many minima as you can see on both sides of the
   centre — at least $m = \pm1$ through $\pm4$. Measuring $m = +4$ to $m = -4$
   and halving is far better than measuring $m = \pm1$ alone.
3. Take a quantitative profile with the camera or the scanning photodiode, as
   in [](#exp-interference). Watch for saturation.
4. Repeat with two more slit widths, and with the unknown.

**[ ] Checkpoint 1.** Confirm with the instructor that
your widest and narrowest slits give patterns of the expected *relative*
widths. If narrowing the slit does not widen the pattern, you are looking at
the beam profile, not diffraction.

### Part B — Circular aperture and the Airy disc

5. Replace the slit with a circular aperture. Photograph the Airy pattern with
   a long enough exposure to see the first ring, and a short enough one to
   keep the centre unsaturated — take both and combine.
6. Measure the radius of the first dark ring, and extract $D$ from
   [](#eq-diff-airy). Compare with a direct measurement of the aperture under
   a travelling microscope if one is available.

### Part C — The grating

7. Mount the grating on the rotation stage with the beam at normal incidence.
   Confirm normal incidence by checking that the $m = +1$ and $m = -1$ angles
   are equal — if they are not, the grating is tilted and every angle is
   biased.
8. Measure $\theta_m$ for every visible order, on both sides.
9. Using the manufacturer's line density, compute $\lambda$; or, using the
   $\lambda$ from Experiment 1, compute the line density. Do both and see
   whether the manufacturer is honest.

### Part D — Optical discs

10. Mount the CD in reflection at normal incidence and measure the first-order
    angle with the rotation stage or by triangulating the diffracted spot's
    position on a wall at a measured distance.
11. Repeat for the DVD. Note that the angle is large: **do not use the
    small-angle approximation**, and measure the geometry carefully enough
    that you know $\theta$ to a degree or better.
12. If a Blu-ray disc is available, look for a first order and record its
    absence. Then state the bound this places on its track pitch.

### Part E — Resolution

13. Set up two closely spaced pinholes, back-illuminated, several metres away.
14. View them through a variable iris. Close the iris until the two merge into
    one, and record the iris diameter at that point.
15. Repeat three times, and have your partner do it independently — this is a
    perceptual threshold and it varies between observers by more than you
    expect. That spread *is* your uncertainty.

## Analysis

### Slit width from minima

The minima positions satisfy $y_m = mL\lambda/a$ in the small-angle limit, but
do not use small angles if you do not have to. Fit

$$
\sin\theta_m = \frac{y_m}{\sqrt{y_m^2 + L^2}} = \frac{m\lambda}{a}
$$

as a straight line through the origin in $m$; the slope is $\lambda/a$.

```python
import numpy as np
from scipy.optimize import curve_fit

m  = np.array([-4, -3, -2, -1, 1, 2, 3, 4])
y  = np.array([...])            # minima positions relative to centre, metres
sy = np.array([...])
sin_th  = y / np.sqrt(y**2 + L**2)
ssin_th = sy * L**2 / (y**2 + L**2)**1.5      # propagate through the geometry

popt, pcov = curve_fit(lambda m, s: s * m, m, sin_th,
                       sigma=ssin_th, absolute_sigma=True)
a  = lam / popt[0]
sa = a * np.sqrt((np.sqrt(pcov[0,0])/popt[0])**2 + (slam/lam)**2)
```

Then fit the full profile with [](#eq-diff-single) and compare the two values
of $a$. They should agree; if the profile fit gives a systematically smaller
$a$, suspect saturation.

### Grating and discs

For each order, $d = m\lambda/\sin\theta_m$. Take the weighted mean over
orders, and check for a trend with $m$ — a drift indicates the grating was not
at normal incidence.

### Resolution

Compare your measured threshold iris diameter with the prediction from
[](#eq-diff-rayleigh), using the measured pinhole separation and distance.
Report the ratio measured/predicted, with its uncertainty, and discuss whether
a ratio different from 1 is a failure of the criterion or a statement about
human vision.

## Post-lab questions

:::{exercise}
:label: q-diff-05

Report the unknown slit width from both methods with uncertainties. Are they
consistent? Which method would you use if you had only twenty minutes?
:::

:::{exercise}
:label: q-diff-06

Report the CD and DVD track pitches with uncertainties and compare with the
standards ($1.60\ \mu\text{m}$ and $0.740\ \mu\text{m}$). Given that the two
formats use the same disc size, use your two pitches to estimate the ratio of
their storage capacities, and compare with the actual $700\ \text{MB}$ versus
$4.7\ \text{GB}$.
:::

:::{exercise}
:label: q-diff-07

Using [](#eq-diff-resolving), compute the resolving power of your grating in
first order for the illuminated width you actually used. Could it separate the
sodium D lines at $589.0$ and $589.6\ \text{nm}$? This is the instrument you
will use in Week 11 — the answer determines whether that experiment works.
:::

:::{exercise}
:label: q-diff-08

An optical microscope using $550\ \text{nm}$ light and an oil-immersion
objective of numerical aperture $1.4$ resolves about $\lambda/(2\,\text{NA})$.
Compute it. Then compute the de Broglie wavelength of a $100\ \text{keV}$
electron (you will meet this formula in Week 7) and comment on why electron
microscopes exist.
:::

:::{exercise}
:label: q-diff-09

If you looked for a Blu-ray first order and did not find one, state the
inequality this places on the track pitch, and compare with the standard's
$0.32\ \mu\text{m}$. If you *did* find one, explain what you actually saw.
:::

## Going further

- **Babinet's principle.** Replace the slit with a wire of the same width. The
  diffraction patterns are identical away from the centre — a result that
  surprises everyone the first time and follows in one line from linearity of
  the wave equation. Measuring a wire diameter this way is a genuinely useful
  technique.
- **Measure a hair, a spider silk, or a fibre.** Same principle, and it
  connects directly to the air-wedge measurement of Week 4. Two independent
  measurements of the same hair make a nice paragraph in a report.
- **Poisson's bright spot.** Put an opaque circular obstacle in an expanded
  clean beam and look at the centre of its shadow. The bright spot there was
  advanced in 1818 as a *reductio ad absurdum* against Fresnel's wave theory,
  and then observed. It requires a clean beam and a good circular edge, and it
  is worth the trouble.

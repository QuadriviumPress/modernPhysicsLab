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
**You will measure** slit widths, grating pitch or wavelength, optical-disc track spacing, and a visual resolution threshold
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
- State the Rayleigh criterion, compare it with a visual threshold, and
  explain what also limits a telescope, a microscope, and your own eye.

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

The $1.22$ is the first positive zero of $J_1$ divided by $\pi$, for an
ideal, uniformly illuminated circular aperture. It differs from the
single-slit result, so use the right aperture model when inferring $D$.

### The Rayleigh criterion

Two incoherent point sources are said to be *just resolved* when the first
zero of one Airy pattern falls on the central maximum of the other:

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D} .
$$ (eq-diff-rayleigh)

This is a convention for two equally bright, incoherent point sources in an
ideal circular-aperture image. Contrast, noise, aberrations, detector sampling,
and the source itself affect a real threshold. A known point-spread function
can support more precise localization under suitable conditions, but the
Rayleigh angle remains a useful diffraction scale. Electron microscopes gain
from much shorter electron wavelengths, while their lenses impose other
limits.

```{figure} ../images/exp05-rayleigh-criterion-concept.svg
:label: fig:exp05-rayleigh
:alt: Two circular-aperture Airy point-spread profiles separated by one first-zero radius overlap; their sum has a central dip about 26.5 percent below the peaks.

Just resolved under the Rayleigh convention. Each source alone (dashed) has an Airy profile; separated by $\theta_{\min}$, their summed intensity (solid) has a central dip about 26.5% below the peaks. The figure is a one-dimensional cross section of the circular pattern.
```

### The grating

$N$ equally spaced slits of pitch $d$ give maxima at

$$
d\sin\theta = m\lambda ,
$$ (eq-diff-grating)

the same condition as two slits — but the maxima are *far narrower*, with
angular width $\propto 1/N$. That sharpening, not the position of the maxima,
is what makes a grating a spectroscopic instrument. Its resolving power is

$$
\left(\frac{\lambda}{\Delta\lambda}\right)_{\mathrm{grating}} = mN ,
$$ (eq-diff-resolving)

so an ideal $1000\ \text{lines/mm}$ grating with a *measured* $5\ \text{mm}$
illuminated width has $N=5000$ and a first-order grating limit of
$\Delta\lambda\approx0.13\ \text{nm}$ at $650\ \text{nm}$. A narrow laser beam
may illuminate fewer grooves, and a spectrometer's entrance slit, optics,
alignment, and detector can make its actual resolution worse. See the
[Feynman grating derivation](https://www.feynmanlectures.caltech.edu/I_30.html)
and this [spectrograph laboratory guide](https://courses.washington.edu/phys331/concave_grating/concave_grating.pdf).

### Optical discs as gratings

The data tracks of a CD or DVD form a reflection grating. Nominal pitches are
$1.6\ \mu\text{m}$ for CD, $0.74\ \mu\text{m}$ for DVD, and $0.32\ \mu\text{m}$
for Blu-ray. For a DVD, $\lambda/d = 650/740 = 0.88$, so first order appears
at $62°$ — a large angle where the small-angle approximation fails completely
and you must measure the actual angle. For Blu-ray at $650\ \text{nm}$,
$\lambda/d > 1$ and no first order can propagate **in air at normal
incidence** in the simple grating model. Failure to see an order alone is not
proof of this inequality: weak efficiency, disc cover layers, alignment, and
limited angular coverage can also hide one. The nominal pitches are tabulated
in this [Stony Brook optical-disc teaching project](https://www.stonybrook.edu/laser/_carolina/project/).

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
- Transmission grating, $\sim300$–$1000\ \text{lines/mm}$ (use a genuine
  transmission grating; a reflective grating requires a different geometry)
- CD, DVD, and optionally a Blu-ray disc, mounted for a separately aligned
  **reflection** measurement; do not peel or cut discs
- Rotation stage or a large protractor and a meter stick, for large angles
- Camera or scanning photodiode; screen
- Two small, measured pinholes on a card with a diffuse lamp behind, for the
  visual threshold comparison; a calibrated variable iris or aperture set

:::{danger}
Confirm the laser's actual class and use the institution's approved controls.
Discs create specular reflection and several diffracted beams on the incident
side. Put beam blocks where those paths can go before powering up; never put
an eye in the beam plane. Do not cut or peel discs. See [](#lab-safety).
:::

```{figure} ../images/exp05-diffraction-bench-schematic.svg
:label: fig:exp05-bench
:alt: A laser beam crosses a transmission slit, aperture, or grating on a mount, and diffracted light fans out to a screen or detector on the far side.

The transmission-diffraction bench for the slit, aperture, and grating. Measure large angles with a rotating detector or protractor. Optical discs require a separate reflection layout, with the diffracted orders detected on the **incident** side.
```

## Procedure

### Before you take diffraction data

- Use [](#fig:exp05-bench) to plan the transmission measurements. Record the
  slit, aperture, or grating installed for each file. Draw and separately
  align the disc reflection layout before collecting disc data.
- Align the rail with no sample present and mark the zero-order beam position.
  Recheck that mark after every sample change; a shifted zero biases all
  measured angles and radii.
- Copy the nominal slit widths, aperture diameters, and grating line density
  into a table, but keep them labeled “nominal” until compared with your
  measured values.
- Record a dark frame and a spatial calibration at the screen plane. For
  profiles, lock the camera settings or record the photodiode gain and step
  size so intensities can be compared.
- For every pattern, save the overview and the quantitative positions or
  profile used in your analysis. Note which orders or minima are visible
  before changing the apparatus; do not infer unseen orders from a diagram.

### Part A — Single slit

1. Set $L \approx 2\ \text{m}$ and illuminate a slit of known width.
2. Record the positions of visible minima on both sides of the center, through
   $m=\pm4$ if the field and dynamic range permit. The separation of the
   $m=+4$ and $m=-4$ minima spans **eight orders**; divide by eight in the
   small-angle limit, or fit the exact-angle relation below.
3. Take a quantitative profile with the camera or the scanning photodiode, as
   in [](#exp-interference). Watch for saturation.
4. Repeat with two more slit widths, and with the unknown.

**[ ] Checkpoint 1.** Confirm with the instructor that
your widest and narrowest slits give patterns of the expected *relative*
   widths. If narrowing the slit does not widen the pattern, check alignment,
   source illumination, detector field, and whether you located the minima.

### Part B — Circular aperture and the Airy disc

5. Replace the slit with a circular aperture. Photograph the Airy pattern with
   a long enough exposure to see the first dark ring and with a shorter
   exposure to keep the center unsaturated. Use each image for the feature it
   resolves; retain its exposure and scale rather than merging intensities
   without a calibrated response.
6. Measure the radius of the first dark ring, and extract $D$ from
   [](#eq-diff-airy). Compare with a direct measurement of the aperture under
   a traveling microscope if one is available.

### Part C — The grating

7. Mount the grating on the rotation stage with the beam at normal incidence.
   Check the grating normal using the reflected zero order or the mount's
   reference, then compare the $m=+1$ and $m=-1$ angles as a symmetry check.
   A mismatch can indicate tilt or an angle-zero error.
8. Measure $\theta_m$ for every visible order, on both sides.
9. Using the specified line density, compute $\lambda$; then use the
   independently measured $\lambda$ from Experiment 1 to infer line density.
   Compare with uncertainties, including the specification's tolerance if
   given.

### Part D — Optical discs

10. Mount the CD in reflection near normal incidence. Block the specular
    return beam and locate first orders on the **incident** side using a
    rotating detector or screen. Measure signed angles from the reflected
    zero-order direction, or measure spot position and screen distance and
    compute $\theta=\arctan(y/L)$. Check $+1/-1$ symmetry before using the
    normal-incidence formula.
11. Repeat for the DVD. Note that the angle is large: **do not use the
    small-angle approximation**, and measure the geometry carefully enough
    that you know $\theta$ to a degree or better.
12. If a Blu-ray disc is available, scan the accessible incident-side angles
    for a first order and record the angular coverage and detection limit.
    An absent spot is consistent with $d<\lambda$ at normal incidence but
    alone does not establish a pitch bound.

### Part E — Resolution

13. Set up two small pinholes with measured separation and diameter,
    back-illuminated by a diffuse lamp at measured distance. Avoid a coherent
    laser source, which would produce a different two-source pattern.
14. View them through a calibrated variable iris near the eye. Record the
    iris diameter at which they merge while keeping ambient light and viewing
    distance fixed. Note the actual eye pupil and pinhole sizes as practical
    limitations.
15. Repeat with both observers. Report trial-to-trial and observer variation,
    plus iris calibration and geometry uncertainty; a visual threshold is not
    a direct measurement of the ideal Rayleigh boundary.

## Analysis

### Slit width from minima

The minima positions satisfy $y_m = mL\lambda/a$ in the small-angle limit, but
do not use small angles if you do not have to. Fit

$$
\sin\theta_m = \frac{y_m}{\sqrt{y_m^2 + L^2}} = \frac{m\lambda}{a}
$$

as a straight line in signed order $m$; its slope is $\lambda/a$. Allow a
small intercept to diagnose a mislocated pattern center.

```python
import numpy as np
from scipy.optimize import curve_fit

m  = np.array([-4, -3, -2, -1, 1, 2, 3, 4])
y  = np.array([...])            # minima positions relative to center, meters
sy = np.array([...])
sin_th  = y / np.sqrt(y**2 + L**2)
ssin_th = sy * L**2 / (y**2 + L**2)**1.5      # independent position errors

popt, pcov = curve_fit(lambda m, b, s: b + s*m, m, sin_th,
                       sigma=ssin_th, absolute_sigma=True)
slope = popt[1]
a  = lam / slope
sa = a * np.sqrt((np.sqrt(pcov[1,1])/slope)**2 + (slam/lam)**2)
```

Here `y`, `sy`, `L`, `lam`, and `slam` are your measured positions, their
standard uncertainties, screen distance, wavelength, and wavelength
uncertainty in SI units. Refit at plausible $L$ and center-position limits
to include their **shared** systematic effects; do not put one common $L$
error into every independent `sigma` entry. Inspect the intercept and
residuals. Use `absolute_sigma=True` only for defensible absolute standard
uncertainties. Then fit the full profile with [](#eq-diff-single) if the
detector response is linear enough, and compare the two values of $a$ with
their shared wavelength and distance errors. Saturation or camera processing
can distort an intensity fit.

### Grating and discs

For a near-normal transmission grating, fit signed $\sin\theta_m$ against
signed $m$ with an intercept; its slope is $\lambda/d$. A nonzero intercept
or differing $+m/-m$ estimates may indicate angle-zero or incidence error.
Common wavelength and angle calibrations correlate the inferred pitches, so
do not treat all orders as independent measurements when quoting uncertainty.
For discs, use the reflected zero-order direction and the separately drawn
reflection geometry. The same simple $d\sin\theta=m\lambda$ form applies
only after normal incidence and an appropriate diffraction order have been
established.

### Resolution

Compare your measured threshold iris diameter with the prediction from
[](#eq-diff-rayleigh), using the measured pinhole separation and distance.
Report the ratio measured/predicted with the uncertainties you can support.
Discuss pinhole size, eye optics, pupil diameter, brightness, and observer
judgment before interpreting disagreement with the ideal criterion.

## Post-lab questions

:::{exercise}
:label: q-diff-05

Report the unknown slit width from both methods with uncertainties. Are they
consistent? Which method would you use if you had only twenty minutes?
:::

:::{exercise}
:label: q-diff-06

Report the CD and DVD track pitches with uncertainties and compare with the
nominal pitches ($1.60\ \mu\text{m}$ and $0.740\ \mu\text{m}$). Assuming equal
usable area and equal bit length *along* the track, what capacity ratio
would the measured track pitches alone predict? Compare with about
$700\ \text{MB}$ versus $4.7\ \text{GB}$ for common single-layer formats.
What additional design differences does the comparison reveal? See this
[Yale teaching note](https://volga.eng.yale.edu/teaching-resources/cds-and-dvds/methods-and-materials).
:::

:::{exercise}
:label: q-diff-07

Using [](#eq-diff-resolving), compute the *grating-only* resolving-power limit
in first order for the illuminated width you actually used. Is that limit
sufficient to separate the sodium D lines at $589.0$ and $589.6\ \text{nm}$?
Why could the complete Week 11 spectrometer still fail to separate them?
:::

:::{exercise}
:label: q-diff-08

An optical microscope using $550\ \text{nm}$ light and an oil-immersion
objective of numerical aperture $1.4$ resolves about $\lambda/(2\,\text{NA})$.
Compute it. Then compute the de Broglie wavelength of a $100\ \text{keV}$
electron with **relativistic** momentum,
$pc=\sqrt{T(T+2m_ec^2)}$ and $\lambda=h/p$ (you will meet this in Week 7).
Explain why the much shorter wavelength helps electron microscopy while
electron-lens aberrations and the specimen still limit real resolution.
:::

:::{exercise}
:label: q-diff-09

For a normal-incidence grating in air, what inequality on track pitch would
make a first order impossible at $650\ \text{nm}$? Compare it with the nominal
Blu-ray pitch of $0.32\ \mu\text{m}$. If you saw no spot, explain why absence
alone cannot establish that inequality. If you saw a spot, list other
possible structures, reflections, or alignment effects to check.
:::

## Going further

- **Babinet's principle.** Replace the slit with a wire of the same width. The
  diffraction patterns are identical away from the center — a result that
  surprises everyone the first time and follows in one line from linearity of
  the wave equation. Measuring a wire diameter this way is a genuinely useful
  technique.
- **Measure a hair, a spider silk, or a fiber.** Same principle, and it
  connects directly to the air-wedge measurement of Week 4. Two independent
  measurements of the same hair make a nice paragraph in a report.
- **Poisson's bright spot.** Put an opaque circular obstacle in an expanded
  clean beam and look at the center of its shadow. The bright spot there was
  advanced in 1818 as a *reductio ad absurdum* against Fresnel's wave theory,
  and then observed. It requires a clean beam and a good circular edge, and it
  is worth the trouble.

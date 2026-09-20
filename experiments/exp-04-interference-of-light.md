---
title: Interference of Light
short_title: 4. Interference of Light
label: exp-interference
numbering:
  enumerator: "4.%s"
---

# Experiment 4 — Interference of Light

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 4, *Interference of Light*
**Apparatus** Diode laser, multiple-slit set, camera or scanning photodiode, glass slides
**You will measure** slit separations from fringe spacing, and the thickness of a human hair from an air wedge
**Report** **Full report** — this is one of the three
:::

## Objectives

By the end of this experiment you should be able to:

- Predict and verify the fringe spacing of a two-slit interference pattern.
- Fit a full two-slit intensity model, including the single-slit envelope, to
  a measured profile, and separate the roles of slit separation and slit width.
- Measure a sub-100-micrometre thickness by counting interference fringes in
  an air wedge.
- Explain why interference requires coherence, and demonstrate the
  consequences of losing it.

## Textbook connection

Read §4.2–4.6. Chapter 4 develops the wave picture of light in the form that
Chapters 6 and 7 will then have to be reconciled with. Everything you see this
afternoon is unambiguously wave behaviour, and it will be worth remembering
in Week 7 that the *same* apparatus, run one photon at a time, produces the
*same* pattern.

## Theory

### Two slits

Two narrow slits separated by $d$, illuminated coherently, produce maxima
where the path difference is a whole number of wavelengths:

$$
d\sin\theta = m\lambda, \qquad m = 0, \pm1, \pm2,\ldots
$$ (eq-int-maxima)

On a screen at distance $L \gg d$, with the small-angle approximation
$\sin\theta \approx \tan\theta = y/L$, the maxima fall at $y_m = m\lambda L/d$
and are evenly spaced by

$$
\Delta y = \frac{\lambda L}{d}.
$$ (eq-int-spacing)

This is the working equation. Notice that it inverts nicely: measuring
$\Delta y$, $L$, and $\lambda$ gives $d$ — you are using light to measure a
distance far too small to read off with a ruler, which is the same trick as
Experiment 1 in different clothing.

### Two slits of finite width

Real slits have a width $a$, and each one diffracts. The intensity is the
two-slit interference pattern *modulated* by the single-slit envelope:

$$
I(\theta) = I_0
\underbrace{\left[\frac{\sin(\pi a \sin\theta/\lambda)}{\pi a \sin\theta/\lambda}\right]^{2}}_{\text{single-slit envelope}}
\underbrace{\cos^{2}\!\left(\frac{\pi d \sin\theta}{\lambda}\right)}_{\text{two-slit interference}} .
$$ (eq-int-full)

The envelope has its first zero at $\sin\theta = \lambda/a$, and interference
maxima that fall there are **missing orders**. Counting how many interference
fringes fit inside the central envelope gives $d/a$ directly, without
measuring any distance at all:

$$
\frac{d}{a} = \text{(number of interference maxima in the central envelope} + 1)/2 .
$$

A pattern with, say, nine fringes across the central lobe has $d/a = 5$.
Checking this by eye before you fit anything is the fastest sanity check
available in this experiment.

### The air wedge

Press two flat glass slides together and slip a thin object — a hair, a strip
of foil — between them at one end. The air gap grows linearly along the
slides, and light reflected from the bottom of the top slide interferes with
light reflected from the top of the bottom slide. Because the second
reflection is off a medium of *higher* index, it acquires a $\pi$ phase shift,
so **dark** fringes occur where the gap $t$ satisfies

$$
2t = m\lambda .
$$ (eq-wedge)

Successive dark fringes are therefore separated by a gap change of
$\lambda/2$. If the wedge has length $\ell$ from the contact line to the
spacer, and $N$ dark fringes are counted over that length, the spacer
thickness is

$$
T = \frac{N\lambda}{2} .
$$ (eq-wedge-thickness)

A human hair is $50$–$100\ \mu\text{m}$ thick, so expect $N$ of order $200$ —
count over a measured sub-length and scale.

## Pre-lab

:::{exercise}
:label: q-int-01

For $\lambda = 650\ \text{nm}$, $d = 0.25\ \text{mm}$, and $L = 2.00\ \text{m}$,
compute the fringe spacing $\Delta y$. Is it comfortably resolvable by eye? By
a camera sensor with $3\ \mu\text{m}$ pixels placed at $L = 2.00\ \text{m}$
with no lens?
:::

:::{exercise}
:label: q-int-02

A double slit has $d = 0.25\ \text{mm}$ and $a = 0.04\ \text{mm}$. How many
interference maxima lie within the central diffraction envelope? Which orders
are missing? Sketch the expected pattern.
:::

:::{exercise}
:label: q-int-03

Using [](#eq-wedge-thickness), how many dark fringes would you expect across
an air wedge made with a $70\ \mu\text{m}$ hair at $\lambda = 650\ \text{nm}$?
If the wedge is $4\ \text{cm}$ long, what is the fringe spacing in millimetres?
Can you count them by eye, and if not, what would you do?
:::

:::{exercise}
:label: q-int-04

Two independent laser pointers illuminate the two slits, one each. Will you
see interference fringes? Explain in terms of coherence, and state what would
have to be true of the two lasers for fringes to appear.
:::

## Apparatus

- Diode laser module, $\lambda \approx 650\ \text{nm}$ (use the value you
  measured in [](#exp-michelson) if the same source, with its uncertainty)
- Slit set with several $(a, d)$ combinations, and at least one "unknown"
- Optical rail or metre stick, screen, and a mount for the camera
- Camera: a machine-vision USB camera with the lens removed, or a phone with
  manual exposure. A photodiode on a translation stage also works and is
  better calibrated.
- Two microscope slides, binder clips, a human hair, aluminium foil
- Diffusing screen; tape measure

:::{danger}
Class 2 laser. Never look into the beam or its reflection from a slide. Glass
slides are excellent unintended beamsplitters — know where every reflection
goes before you power up. See [](#lab-safety).
:::

## Procedure

### Part A — Verifying the fringe-spacing law

1. Mount the laser, slit holder, and screen on the rail. Set $L \approx 2\ \text{m}$.
   Expand the beam slightly if needed so it illuminates both slits evenly.
2. Choose a slit pair of known $d$. Photograph the pattern, and also mark the
   positions of ten fringe maxima on a paper screen with a pencil, measuring
   across the *outermost* pair rather than adjacent ones — measuring across
   ten spacings and dividing by ten reduces the position uncertainty tenfold.
3. Repeat for **at least five values of $L$** from about $0.8\ \text{m}$ to
   the longest the bench allows.
4. Repeat for **at least three values of $d$** at fixed $L$.

**[ ] Checkpoint 1.** Before taking the full set, verify
that your first $\Delta y$ agrees with your pre-lab prediction to about 10%.
If it does not, the usual causes are a mis-measured $L$ (measure from the
*slit*, not from the laser) or the wrong slit pair in the beam.

### Part B — The full intensity profile

5. Choose the slit pair with the clearest envelope structure. Record a
   quantitative intensity profile:
   - **With a camera:** remove the lens so the sensor sits directly in the
     pattern, lock the exposure, disable HDR and any "scene optimization",
     and shoot RAW if you can. Take a dark frame with the beam blocked.
   - **With a photodiode:** mount it behind a narrow ($\lesssim 0.1\ \text{mm}$)
     slit on a translation stage and scan in steps small compared with
     $\Delta y$, logging position and voltage.
6. Verify that you are not saturating: the central maximum must be below the
   sensor's full scale. If it is clipped, the fit will return nonsense for $a$.
7. Count the interference maxima within the central envelope and identify the
   missing orders by eye. Write the number in your notebook before you fit.

### Part C — The unknown slit

8. Insert the unknown slit pair and record a profile under the same
   conditions. You will report $d$ and $a$ for it with uncertainties.

### Part D — The air wedge

9. Clean two slides. Lay a single hair across one end, place the second slide
   on top, and clamp gently at both ends.
10. Illuminate at near-normal incidence with expanded laser light (or with a
    sodium lamp, which gives beautiful fringes in white-light-free
    monochromatic contrast) and view the reflected pattern on a screen, or
    photograph it directly through a beamsplitter.
11. Measure the distance $\ell$ from the contact line to the hair, and count
    fringes over a measured sub-length. Photograph the pattern and count in
    software rather than by eye.
12. Measure the hair with a micrometer as an independent check.

### Part E — Coherence

13. Replace the laser with a white LED behind a narrow single slit
    (a spatial filter). Fringes should reappear, coloured. Now widen that
    slit progressively and watch the visibility collapse.
14. Record the slit width at which fringes become undetectable. This is a
    direct measurement of the spatial coherence condition.

## Analysis

### Fringe spacing

Fit $\Delta y$ against $L$ at fixed $d$; the slope is $\lambda/d$. Then fit
$\Delta y$ against $1/d$ at fixed $L$; the slope is $\lambda L$. Two
independent routes to the same physics, and disagreement between them is
informative.

### The full profile

Convert pixel index to angle using the pixel pitch and $L$, subtract the dark
frame, and fit [](#eq-int-full) with $a$, $d$, $I_0$, and a centre offset free.

```python
import numpy as np
from scipy.optimize import curve_fit

def two_slit(y, I0, a, d, y0, bg):
    """y in metres on the screen; small-angle sin(theta) ~ (y - y0)/L."""
    s     = (y - y0) / L                       # L defined outside, in metres
    alpha = np.pi * a * s / lam
    delta = np.pi * d * s / lam
    env   = np.sinc(alpha / np.pi) ** 2        # np.sinc(x) = sin(pi x)/(pi x)
    return I0 * env * np.cos(delta) ** 2 + bg

p0 = [prof.max(), 40e-6, 250e-6, y[np.argmax(prof)], prof.min()]
popt, pcov = curve_fit(two_slit, y, prof, p0=p0, sigma=sprof,
                       absolute_sigma=True)
```

:::{warning} `np.sinc` is normalized
NumPy defines `np.sinc(x) = sin(pi x)/(pi x)`, not `sin(x)/x`. Passing an
argument that already contains $\pi$ without dividing it back out is the most
common bug in this fit, and it produces a plausible-looking curve with a slit
width wrong by a factor of $\pi$.
:::

The starting guess matters here: a nonlinear fit to an oscillatory model will
happily settle into a local minimum one fringe over. Seed $d$ from the fringe
spacing you measured in Part A, and $a$ from your envelope count, and check
that the fitted values are near the seeds rather than far from them.

Propagate to $d$ and $a$ from the covariance matrix, and include the
uncertainty in $\lambda$ and $L$ — both enter multiplicatively.

### The wedge

$T = N\lambda/2$, scaled from your counted sub-length to the full length
$\ell$. Propagate from the fringe count, the two lengths, and $\lambda$.
Compare with the micrometer reading, in units of $\sigma$.

## Post-lab questions

:::{exercise}
:label: q-int-05

Report $d$ and $a$ for the unknown slit with uncertainties, and compare with
the manufacturer's specification. Which of the two is better determined by
your data, and why?
:::

:::{exercise}
:label: q-int-06

Your two routes to $\lambda/d$ — varying $L$ and varying $d$ — give two
answers. Are they consistent? If not, name a systematic that would affect one
but not the other.
:::

:::{exercise}
:label: q-int-07

Plot your residuals from the two-slit fit. Real data almost always show
systematic structure here. Identify at least one physical effect not in
[](#eq-int-full) that could produce it — candidates include finite source
size, a slit that is not perfectly rectangular, sensor nonlinearity, and
stray light.
:::

:::{exercise}
:label: q-int-08

From Part E, estimate the source size $w$ at which fringes vanished, and
compare with the spatial-coherence condition $w\,d/(\lambda D) \approx 1$,
where $D$ is the source–slit distance. What does this say about why a laser
works so much better here than a lamp?
:::

:::{exercise}
:label: q-int-09

The hair thickness from fringe counting and from the micrometer should agree.
If yours do not, which do you trust more, and why? Note that the micrometer
compresses the hair and the wedge does not.
:::

:::{exercise}
:label: q-int-10

*Looking ahead.* In Week 7 you will see an interference pattern built up one
particle at a time. Before you do: write down what [](#eq-int-full) predicts
for the *probability distribution* of a single photon's arrival position, and
what it does not predict.
:::

## Going further

- **White-light fringes.** With a broadband source and a compensated
  interferometer, fringes appear only within a coherence length of zero path
  difference — a few micrometres. Finding them is fiddly and is the standard
  technique for locating zero-order in an interferometer, used in optical
  coherence tomography.
- **Newton's rings.** A plano-convex lens on a flat gives circular fringes
  whose radii go as $\sqrt{m}$; fitting them gives the lens's radius of
  curvature to a fraction of a percent from a photograph.
- **Lloyd's mirror.** A single slit and a grazing-incidence mirror produce
  two-source interference from *one* source, with the mirror image acting as
  the second slit — and the fringe at the mirror surface is dark, not bright,
  which is a direct measurement of the $\pi$ phase shift on reflection.

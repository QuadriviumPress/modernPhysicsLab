---
title: The Quantum Eraser and Complementarity
short_title: 7. The Quantum Eraser
label: exp-quantum-eraser
numbering:
  enumerator: "7.%s"
---

# Experiment 7 — The Quantum Eraser and Complementarity

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 7, *Wave Properties of Particles*
**Apparatus** Thorlabs EDU-QE1 quantum eraser kit (double slit, polarizers, 532 nm laser), camera
**You will measure** fringe visibility as a function of which-path information, and test $V^2 + D^2 \le 1$
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Demonstrate that marking the path of light through a double slit destroys
  the interference pattern, and that erasing the mark restores it.
- Measure fringe visibility quantitatively from an intensity profile.
- Test the complementarity relation $V^2 + D^2 \le 1$ between fringe
  visibility and path distinguishability.
- State precisely what this experiment does and does not establish about the
  quantum nature of light — a distinction that a great many popular accounts
  get wrong.

## Textbook connection

Read §7.1–7.5. Chapter 7 argues that particles have wave properties; this
experiment approaches complementarity from the other side, showing that a wave
loses its interference exactly when it acquires the particle property of
having taken a definite path. The electron-diffraction apparatus this
laboratory formerly used is no longer serviceable, so the de Broglie
wavelength is treated computationally in the analysis while the
complementarity physics is done on the optical bench.

## Theory

### Which-path information destroys interference

Put orthogonal linear polarizers over the two slits of a double slit —
horizontal over slit 1, vertical over slit 2. The two emerging fields are now
orthogonally polarized, and orthogonal polarizations do not interfere: the
cross term in $|E_1 + E_2|^2$ contains $\hat{e}_1 \cdot \hat{e}_2 = 0$. The
fringes vanish, leaving the sum of the two single-slit patterns.

The physical statement is stronger than the algebra. The polarization now
*carries the information* about which slit the light passed through. If a
measurement could in principle determine the path — whether or not anyone
performs it — interference is impossible.

### Erasing the mark

Now place a third polarizer, at $45°$, *after* the slits. It projects both
beams onto the same polarization state, and the which-path information is
irretrievably destroyed: a photon transmitted through the $45°$ analyzer could
have come from either slit with equal amplitude. The fringes return.

Rotate the analyzer to $-45°$ and the fringes return again, but *shifted by
half a period* — bright where they were dark. This is the crucial control.
Adding the two erased patterns reproduces the no-fringe pattern exactly, so
nothing has been created; the erasure has *sorted* the photons into two
complementary subsets, each of which shows interference.

### Visibility and distinguishability

Define the fringe visibility from the intensity profile:

$$
V = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} .
$$ (eq-qe-visibility)

Define the path distinguishability $D$ as the probability of correctly
identifying the path in an optimal measurement, rescaled so that $D = 0$ for a
pure guess and $D = 1$ for certainty. For the polarization marking, an
analyzer at angle $\theta$ to slit 1's polarizer gives

$$
D = \left|\cos^2\theta - \sin^2\theta\right| = |\cos 2\theta| ,
\qquad
V = \left|\sin 2\theta\right| ,
$$ (eq-qe-DV)

so that

$$
V^2 + D^2 = 1 .
$$ (eq-qe-complementarity)

This is the quantitative statement of complementarity, due to Greenberger,
Yasin, Englert, and others. It is not a binary "either wave or particle": you
can have partial which-path information and partial visibility, and the
trade-off is a smooth curve you can measure point by point.

:::{important} What this experiment does and does not show
The laser in this kit emits an intense classical beam, and every result you
will see today is reproduced exactly by classical electromagnetism with
polarized waves. **This experiment does not demonstrate quantum mechanics.**

What it demonstrates is *complementarity*, which is a statement about
information and interference that holds identically in the classical wave
theory and in the quantum theory. The step to quantum mechanics is the
observation — established with attenuated sources and single-photon detectors
— that the same pattern builds up dot by dot when the intensity is turned down
so far that only one photon is in the apparatus at a time.

Say this explicitly in your report. A report that claims to have observed
single-photon interference with a 1 mW laser will lose the credit it would
have earned by getting this right.
:::

## Pre-lab

:::{exercise}
:label: q-qe-01

Two waves of equal amplitude $E_0$ and orthogonal polarizations arrive at a
point. Write the total intensity and show explicitly that the interference
cross term vanishes. Now pass both through a polarizer at $45°$ and repeat.
:::

:::{exercise}
:label: q-qe-02

Evaluate [](#eq-qe-DV) for $\theta = 0°, 15°, 30°, 45°, 60°, 75°, 90°$ and
tabulate $V$, $D$, and $V^2 + D^2$. Sketch $V$ against $D$ and mark the unit
circle.
:::

:::{exercise}
:label: q-qe-03

The EDU-QE1 uses $\lambda = 532\ \text{nm}$. For a slit separation of
$d = 0.25\ \text{mm}$ and a screen at $L = 1.5\ \text{m}$, what is the fringe
spacing? How many pixels is that on a sensor with $3\ \mu\text{m}$ pixels?
:::

:::{exercise}
:label: q-qe-04

Compute the de Broglie wavelength of (a) an electron accelerated through
$50\ \text{V}$, (b) a $100\ \text{eV}$ electron, (c) a thermal neutron at
$300\ \text{K}$, and (d) a $C_{60}$ molecule ($720\ \text{u}$) moving at
$200\ \text{m/s}$. For each, name a diffraction grating whose spacing would be
comparable — a crystal lattice, a nanofabricated grating, or nothing that
exists.
:::

## Apparatus

- Thorlabs EDU-QE1 quantum eraser kit: $532\ \text{nm}$ laser, double slit,
  slit polarizers, rotatable analyzer, mounts, breadboard
- Camera (lens removed) or scanning photodiode with a narrow entrance slit
- Rotation mount with a scale readable to $1°$ or better
- Neutral-density filters
- Beam block, screen

:::{danger}
The EDU-QE1 laser is Class 3R at $532\ \text{nm}$ — green, where the eye is
most sensitive, and above the power at which the blink reflex protects you.
Wear the eyewear supplied with the kit whenever the beam is unenclosed. Keep
your head above beam height, remove watches and rings, and switch the source
off before moving any optic. See [](#lab-safety).
:::

```{figure} ../images/exp07-quantum-eraser-schematic.svg
:label: fig:exp07-eraser
:alt: A 532 nm laser illuminates a double slit with a horizontal polarizer on one slit and a vertical polarizer on the other; the beams pass through a rotatable analyzer before reaching a camera.

The quantum-eraser bench. Orthogonal polarizers on the two slits tag which-path information; rotating the analyzer to 45 degrees erases that tag and the fringes return.
```

## Procedure

### Part A — The baseline pattern

1. Assemble the kit per its manual: laser, beam expander, double slit,
   screen/camera. Do **not** install the slit polarizers yet.
2. Record a clean interference pattern. Check for saturation and add an ND
   filter if needed — the visibility measurement is destroyed by clipping,
   because a clipped maximum makes $V$ artificially small.
3. Measure the fringe spacing and confirm it matches your pre-lab prediction.
   Record the baseline visibility.

**[ ] Checkpoint 1.** Show the instructor an unsaturated
profile with $V > 0.7$. A poor baseline visibility means the slits are
unevenly illuminated or the beam is not sufficiently expanded, and everything
downstream will inherit the problem.

### Part B — Marking the path

4. Install the orthogonal polarizers over the two slits. The fringes should
   collapse into a smooth two-slit envelope with no oscillation.
5. Record a profile. Measure the residual visibility — it will not be exactly
   zero, and the value is a measurement of how well the polarizers are aligned
   and how good their extinction ratio is.
6. Verify with a hand-held polarizer that light from the two slits really is
   orthogonally polarized: rotating it should extinguish one slit and then the
   other.

### Part C — Erasing

7. Install the analyzer after the slits and set it to $+45°$. Record the
   profile: fringes should return.
8. Set it to $-45°$ and record again. The fringes should be shifted by half a
   period.
9. **The essential control:** add your two profiles from steps 7 and 8 point by
   point and compare with the unpolarized profile from step 5. They should
   agree to within noise. Do this in the room, before you take Part D.

**[ ] Checkpoint 2.** Show the instructor the two erased
profiles and their sum.

### Part D — The complementarity curve

10. Rotate the analyzer through at least twelve angles from $0°$ to $90°$ and
    record a profile at each. Use equal exposure at every angle, and record the
    angle to the precision of the mount.
11. At each angle, you will extract $V$ from the profile and compute $D$ from
    [](#eq-qe-DV). Plot $V$ against $D$.

### Part E (optional) — Interaction-free measurement

12. If the EDU-BT1 Elitzur–Vaidman bomb-tester kit is available, set up its
    Mach–Zehnder interferometer, balance it so that one output port is dark,
    and then block one arm. Light appears at the previously dark port *because*
    the arm is blocked — an object has been detected by photons that did not
    interact with it. Record the output-port intensities with the arm open and
    blocked, and compute the detection efficiency.

## Analysis

### Extracting visibility

Do not read $I_{\max}$ and $I_{\min}$ off the plot by eye; fit.

```python
import numpy as np
from scipy.optimize import curve_fit

def fringes(y, I0, V, k, phi, y0, w):
    """Two-slit fringes under a Gaussian envelope, with visibility V."""
    env = np.exp(-((y - y0) / w) ** 2)
    return I0 * env * (1 + V * np.cos(k * y + phi))

popt, pcov = curve_fit(fringes, y, prof, p0=[...], sigma=sprof,
                       absolute_sigma=True)
V, sV = popt[1], np.sqrt(pcov[1, 1])
```

Fitting $V$ as an explicit parameter is much more robust than differencing two
noisy extrema, and it hands you the uncertainty directly. Keep $k$ fixed to
the value from Part A across all angles — the fringe spacing does not change
when you rotate the analyzer, and letting it float invites the fit to chase
noise.

### The complementarity test

For each analyzer angle $\theta$, compute $D = |\cos 2\theta|$ with its
uncertainty from the angle reading, and plot $V$ against $D$ with error bars on
both axes. Overlay the unit circle $V^2 + D^2 = 1$.

Then compute $V^2 + D^2$ for each point and test whether it is consistent with
1, or with a value slightly below 1. It will come out below — the polarizers
have finite extinction, the slits are unevenly illuminated, and the baseline
visibility was not 1 to begin with. **Correct for the baseline** by dividing
your measured $V$ by the Part A visibility, and report both the raw and
corrected versions.

### The de Broglie calculation

Complete the pre-lab calculation properly, using the relativistic relation
where it matters:

$$
\lambda = \frac{h}{p}, \qquad
pc = \sqrt{T^2 + 2Tm c^2} .
$$

For a $50\ \text{eV}$ electron the relativistic correction is negligible; for
a $100\ \text{keV}$ electron in a microscope it is not. Report both the
non-relativistic and relativistic wavelengths at $100\ \text{keV}$ and quote
the fractional difference.

## Post-lab questions

:::{exercise}
:label: q-qe-05

Report your measured $V$ at $\theta = 0°$, $45°$, and $90°$ with
uncertainties, and compare with [](#eq-qe-DV).
:::

:::{exercise}
:label: q-qe-06

Does your $V$-versus-$D$ curve lie on or inside the unit circle? Explain why
it *cannot* lie outside, and name the specific imperfections in your apparatus
that push it inside.
:::

:::{exercise}
:label: q-qe-07

Your two erased patterns at $\pm45°$ sum to the unmarked pattern. Explain
carefully why this rules out the interpretation that the $45°$ polarizer
"creates" the interference.
:::

:::{exercise}
:label: q-qe-08

A student claims this experiment shows that "the observer's knowledge changes
the physics". Give a more careful statement of what determines whether fringes
appear, and identify precisely what is wrong with the student's version.
:::

:::{exercise}
:label: q-qe-09

Describe what would have to change in this apparatus to make it a genuine
single-photon experiment, and estimate the source intensity needed so that on
average fewer than one photon is in the $1\ \text{m}$ apparatus at a time.
:::

:::{exercise}
:label: q-qe-10

Report your de Broglie wavelengths from [](#q-qe-04). Explain why electron
diffraction was demonstrated with a nickel crystal in 1927 but $C_{60}$
diffraction had to wait until 1999.
:::

## Going further

- **Delayed choice.** Move the erasing polarizer far downstream, so that the
  decision to erase is made after the light has passed the slits. Nothing
  changes — which is the point, and is the experimental content of Wheeler's
  delayed-choice argument.
- **Quantum key distribution.** The EDU-QCRY1 kit implements a BB84 analogue
  with polarization states. It uses the same physics you have just measured —
  that measuring in the wrong basis destroys information — turned into a
  protocol whose security rests on it.
- **A real single-photon source.** With an attenuated source, a
  photon-counting module, and a long integration, the pattern can be built up
  count by count. This is the experiment that closes the gap identified in the
  Theory section above, and it is a good senior-project scope.

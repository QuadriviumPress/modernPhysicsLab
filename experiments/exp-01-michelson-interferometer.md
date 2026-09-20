---
title: The Michelson Interferometer and the Ether Null Result
short_title: 1. Michelson Interferometer
label: exp-michelson
numbering:
  enumerator: "1.%s"
---

# Experiment 1 — The Michelson Interferometer and the Ether Null Result

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 1, *The Need for Relativity*
**Apparatus** Michelson interferometer (bench instrument or Thorlabs EDU-MINT1), HeNe or 632 nm diode laser
**You will measure** the laser wavelength to $\sim0.1\%$, and set an upper bound on the ether drift speed
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Align a Michelson interferometer and explain the function of each optic in it.
- Relate a counted number of fringe transitions to a mirror displacement, and
  use the relation to measure an optical wavelength.
- Estimate the smallest fringe shift your apparatus can detect, and convert
  that limit into an upper bound on a hypothetical ether drift speed.
- Explain why the null result of the Michelson–Morley experiment could not be
  explained away by any of the obvious loopholes.

## Textbook connection

Read §1.3–1.5 of Chapter 1 before the period. The interferometer you will
align is the same instrument, in miniature, that Michelson and Morley floated
on a bed of mercury in 1887. The difference between what they were trying to
detect and what you can detect on a laboratory bench in three hours is itself
worth understanding, and is the subject of the analysis below.

## Theory

### Fringes from a path difference

A Michelson interferometer splits a beam in two at a beamsplitter, sends the
halves down two perpendicular arms of lengths $L_1$ and $L_2$, and recombines
them. Each beam traverses its arm twice, so the optical path difference is

$$
\Delta = 2(L_1 - L_2).
$$ (eq-mich-path)

Constructive interference at the output occurs when $\Delta = m\lambda$ for
integer $m$. Translating one mirror by a distance $d$ changes $\Delta$ by
$2d$, and the number of bright fringes $N$ that sweep past a fixed point in
the output pattern is

$$
N = \frac{2d}{\lambda}
\qquad\Longleftrightarrow\qquad
\lambda = \frac{2d}{N}.
$$ (eq-mich-lambda)

This is the entire measurement. Its beauty is that it converts a wavelength —
a sub-micrometre quantity you cannot rule off — into a *count*, which has no
calibration uncertainty at all, and a *mirror displacement*, which you can
measure with a micrometer. The factor of two is the most commonly dropped
quantity in this experiment; it is there because light traverses the arm both
ways.

### Why the fringes are circles

With a slightly diverging beam and mirrors that are accurately perpendicular,
rays leaving the source at angle $\theta$ to the axis acquire path difference
$\Delta = 2d\cos\theta$, so the interference condition depends only on
$\theta$: the pattern is a set of concentric circles, and translating the
mirror makes them swallow into, or boil out of, the centre. If the mirrors are
*not* quite perpendicular, the fringes become straight and parallel — still
usable, and in fact easier to count. Either pattern obeys
[](#eq-mich-lambda) at the centre of the field.

### What Michelson and Morley were looking for

If light propagated in a medium at rest in some absolute frame, and the Earth
moved through that medium at speed $v$, the round-trip times along the two
arms would differ. To first order in $(v/c)^2$, the fringe shift on rotating
the apparatus by $90°$ is

$$
\Delta N = \frac{2L}{\lambda}\left(\frac{v}{c}\right)^{2},
$$ (eq-mich-shift)

where $L$ is the arm length (taken equal for both arms). The quadratic
dependence on $v/c$ is what makes the experiment hard: for the Earth's orbital
speed $v = 30\ \text{km/s}$, $(v/c)^2 = 10^{-8}$, so even a metre of arm
length buys only a few hundredths of a fringe.

Michelson and Morley beat this by folding the beam through multiple
reflections to reach an effective $L = 11\ \text{m}$, and by floating the whole
apparatus on mercury so it could be rotated continuously while being watched.
They expected a shift of about $0.4$ fringes and saw, at most, about
one-fortieth of that. You will not repeat their sensitivity. You will
*quantify* how far short of it you fall, which is the honest version of the
experiment and teaches more than a rigged one would.

## Pre-lab

Answer in your notebook before you arrive.

:::{exercise}
:label: q-mich-01

The mirror is translated by $d = 0.100\ \text{mm}$ and $N$ fringes are
counted. Estimate $N$ for a $633\ \text{nm}$ laser. Is that a number you can
count by eye in a reasonable time? What $d$ would give you a count you could
manage in about two minutes at roughly two fringes per second?
:::

:::{exercise}
:label: q-mich-02

The micrometer on the interferometer reads to $10\ \mu\text{m}$ with a
vernier or fine scale you can interpolate to about $1\ \mu\text{m}$. Using
[](#eq-mich-lambda), find the relative uncertainty in $\lambda$ contributed by
the displacement reading for $d = 0.1\ \text{mm}$ and for $d = 1.0\ \text{mm}$.
Which term dominates your final result, and what does that tell you about how
far to translate the mirror?
:::

:::{exercise}
:label: q-mich-03

Take your apparatus to have $L = 0.30\ \text{m}$ arms and suppose you can
detect a shift of $0.2$ fringes. Using [](#eq-mich-shift), what is the
smallest ether drift speed $v$ you could detect? Compare it with the Earth's
orbital speed. Write down, in one sentence, what you therefore expect this
experiment to be able to conclude.
:::

:::{exercise}
:label: q-mich-04

A student proposes that the null result is explained by the Earth "dragging"
the ether along with it, so that the ether is at rest relative to the
laboratory. Name one astronomical observation that this hypothesis contradicts.
(Chapter 1 discusses it.)
:::

## Apparatus

- Michelson interferometer with micrometer-driven movable mirror — a bench
  instrument, or the Thorlabs EDU-MINT1 kit built on a breadboard
- HeNe laser ($632.816\ \text{nm}$ in air) or a $\sim650\ \text{nm}$ diode
  laser module
- Short-focal-length diverging lens ($f \approx -25\ \text{mm}$) to expand the beam
- Viewing screen or white card; optional photodiode + oscilloscope for
  automated counting
- Beam blocks; laser safety eyewear if the source exceeds Class 2
- Tally counter (or the counter app on a phone)

:::{danger}
Class 2/3R laser. Keep your eye out of the beam plane, remove watches and
rings, terminate every beam on a block, and switch the source off before
moving an optic. See [](#lab-safety).
:::

```{figure} ../images/exp01-michelson-schematic.svg
:label: fig:exp01-michelson
:alt: A laser beam is split at a beamsplitter into two arms, one to a fixed mirror and one to a micrometer-driven movable mirror, recombining to form circular fringes on a screen.

The Michelson interferometer. The beamsplitter sends light down two perpendicular arms; translating the movable mirror by $d$ sweeps $N = 2d/\lambda$ fringes past a point on the screen.
```

## Procedure

### Part A — Alignment

1. With the beam-expanding lens **removed**, send the raw laser beam into the
   beamsplitter. You should see two spots on the screen: one from each arm.
2. Adjust the tilt screws on the fixed mirror until the two spots coincide.
   Work on the *dimmer* of the two spots so you can tell which is which.
3. When the spots overlap, faint interference fringes should flicker into
   existence. If they do not, the two path lengths differ by more than the
   coherence length of the source — for a diode laser this can be under a
   millimetre, so equalize the arms with a ruler first.
4. Insert the diverging lens between the laser and the beamsplitter. The
   fringes should expand into a circular bullseye filling the screen.
5. Fine-tune the fixed-mirror tilt until the bullseye is centred and its
   centre is as large and slow-moving as you can make it.

**[ ] Checkpoint 1.** Show the instructor a stable
circular fringe pattern. Do not proceed with a pattern that drifts on its own
faster than about one fringe per ten seconds — find the source (usually
someone leaning on the table, an air current from a vent, or an unlocked
mount) and fix it.

### Part B — Measuring the wavelength

6. Record the micrometer reading. Establish which way you must turn to *always
   approach from the same direction*: reversing direction introduces backlash
   of several micrometres, and this is the largest systematic error in the
   experiment.
7. Choose a reference feature at the centre of the pattern. Translate the
   mirror slowly and steadily, counting fringe transitions with the tally
   counter. Have your partner call out at every $50$ counts so you can catch a
   miscount.
8. Stop at $N = 200$ (or the count you chose in [](#q-mich-01)) and record the
   final micrometer reading.
9. **Repeat this five times.** Two of the five runs should be taken in the
   opposite direction of travel, so that you can see the backlash directly.
10. Estimate, and write in your notebook *now*, the uncertainty you assign to
    a single micrometer reading and to a single fringe count.

**[ ] Checkpoint 2.** Compute $\lambda$ from your first
run before you take the other four. If it is not within about 10% of
$633\ \text{nm}$, you have a factor-of-two problem or a micrometer scale
problem, and it is much cheaper to find it now.

### Part C — Bounding the ether drift

11. Measure both arm lengths from the beamsplitter face to each mirror, with
    an uncertainty.
12. With the pattern stable, determine the smallest fringe shift you can
    reliably *detect*. Do this operationally rather than by guessing: have
    your partner translate the mirror by a small unknown amount, half the time
    by nothing at all, and see how small a real shift you can still call
    correctly. Ten trials is enough to establish the threshold to a factor of
    two.
13. If the instrument can be rotated on the bench (the EDU-MINT1 breadboard
    can be turned; a heavy bench interferometer usually cannot), rotate it
    through $90°$ and watch the pattern. Record any shift you see, and its
    uncertainty. Expect this to be dominated by mechanical flexure, not by
    physics — say so in the report.

## Analysis

### Wavelength

For each run, $\lambda_i = 2d_i/N_i$. Propagate the uncertainty in $d$ and, if
you think a miscount is plausible, in $N$:

$$
\left(\frac{\sigma_\lambda}{\lambda}\right)^2 =
\left(\frac{\sigma_d}{d}\right)^2 + \left(\frac{\sigma_N}{N}\right)^2 .
$$

Take the weighted mean of the five runs, and compare its scatter with the
uncertainty you propagated. If the scatter is much larger, the backlash or a
systematic miscount is the reason.

A better estimator uses all your data at once: plot $d$ against $N$ for all
runs and fit a straight line through the origin, whose slope is $\lambda/2$.

```python
import numpy as np
from scipy.optimize import curve_fit

N  = np.array([200, 200, 200, 400, 400])          # fringe counts
d  = np.array([...])                              # displacements, metres
sd = np.array([...])                              # uncertainty on each d, metres

line = lambda n, half_lambda: half_lambda * n     # forced through the origin
popt, pcov = curve_fit(line, N, d, sigma=sd, absolute_sigma=True)

lam, slam = 2 * popt[0], 2 * np.sqrt(pcov[0, 0])
print(f"lambda = {lam*1e9:.1f} +/- {slam*1e9:.1f} nm")
```

:::{tip} Why force the fit through the origin?
Zero fringes counted must mean zero displacement. Letting the intercept float
lets it absorb a real systematic — the backlash — instead of exposing it. Fit
both ways: a nonzero intercept that is several $\sigma$ from zero is a
*measurement of your backlash*, and belongs in the discussion.
:::

### The ether bound

Rearrange [](#eq-mich-shift) for the speed corresponding to your detection
threshold $\Delta N_{\min}$:

$$
v_{\max} = c\,\sqrt{\frac{\lambda\,\Delta N_{\min}}{2L}} .
$$

Quote it in km/s and as a fraction of $c$, with an uncertainty propagated from
$\Delta N_{\min}$ and $L$. Compare it with the Earth's orbital speed of
$29.8\ \text{km/s}$ and with Michelson and Morley's own bound.

## Post-lab questions

:::{exercise}
:label: q-mich-05

Compare your $\lambda$ with the accepted value ($632.816\ \text{nm}$ in air
for a HeNe; use the manufacturer's specification for a diode laser, which is
typically only guaranteed to a few nanometres). Quote the discrepancy in units
of the combined uncertainty. Is it consistent?
:::

:::{exercise}
:label: q-mich-06

Which term dominated $\sigma_\lambda$: the displacement or the count? Given a
week and no budget, what one change would you make to improve the result, and
by roughly what factor?
:::

:::{exercise}
:label: q-mich-07

Your upper bound on $v$ is almost certainly larger than the Earth's orbital
speed, which means this apparatus *cannot* rule out the ether. Explain
precisely what Michelson and Morley did differently, and by what factor each
change improved the sensitivity. Given [](#eq-mich-shift), what arm length
would your apparatus need to reach their sensitivity?
:::

:::{exercise}
:label: q-mich-08

A fringe drifts past when someone walks near the table. Estimate the change in
optical path length that corresponds to one fringe. Compare it with the
thermal expansion of a $30\ \text{cm}$ aluminium arm for a $0.1\ \text{K}$
temperature change ($\alpha_{\text{Al}} = 23\times10^{-6}\ \text{K}^{-1}$).
What does this tell you about the real difficulty of the 1887 experiment?
:::

:::{exercise}
:label: q-mich-09

The Lorentz–FitzGerald contraction hypothesis proposed that objects moving
through the ether contract by exactly the factor needed to null the fringe
shift. This reproduces the Michelson–Morley result exactly. On what grounds
did physicists nonetheless find it unsatisfactory, and what did Einstein's
1905 paper offer instead? Two or three sentences.
:::

## Going further

- **Automate the count.** Put a photodiode at the centre of the pattern, feed
  it to an oscilloscope or a microcontroller ADC, and drive the mirror with a
  stepper. Counting zero crossings in software removes the human miscount
  entirely and lets you translate ten times as far. This is the same technique
  that turns an interferometer into a displacement metrology instrument good
  to nanometres.
- **Measure the refractive index of air.** Put an evacuable cell of length
  $\ell$ in one arm and count fringes as it is pumped down:
  $n - 1 = N\lambda/(2\ell)$. Expect $n - 1 \approx 2.7\times10^{-4}$ at
  laboratory pressure — a tiny number measured to three digits with a bicycle
  pump and a fringe count.
- **Measure the sodium doublet.** With a sodium lamp instead of a laser, the
  fringe visibility collapses and revives as the two D lines drift in and out
  of phase. The mirror displacement between successive collapses gives the
  splitting $\Delta\lambda = \lambda^2/(2\Delta d)$ — a $0.6\ \text{nm}$
  splitting measured with a micrometer, and a preview of
  [](#exp-quantum-defect).

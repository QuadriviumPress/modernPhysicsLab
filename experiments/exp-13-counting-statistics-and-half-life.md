---
title: Counting Statistics, Half-Life, and Gamma Attenuation
short_title: 13. Counting Statistics and Half-Life
label: exp-counting-statistics
numbering:
  enumerator: "13.%s"
---

# Experiment 13 — Counting Statistics, Half-Life, and Gamma Attenuation

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 13, *Nuclear Physics*
**Apparatus** Geiger–Müller counter, $^{137}$Cs/$^{137m}$Ba isotope generator, lead and aluminium absorbers
**You will measure** the Poisson character of radioactive decay, the half-life of $^{137m}$Ba, and a gamma attenuation coefficient
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Show that radioactive counting obeys Poisson statistics, and use $\sqrt{N}$
  correctly as an uncertainty.
- Distinguish the Poisson and Gaussian regimes and know when each applies.
- Measure a short half-life from a decay curve with a properly weighted fit.
- Measure a linear attenuation coefficient for $662\ \text{keV}$ gamma rays
  and identify the dominant interaction mechanism.

## Textbook connection

Read §13.3–13.6. This experiment is the practical foundation for everything in
nuclear and particle physics: essentially every measurement in the field is a
counting measurement, and its uncertainty is set by the statistics of a random
process rather than by the precision of an instrument. It is also where the
`sqrt(N)` you have been using since Week 3 is finally justified.

## Theory

### Why decay is Poisson

Each nucleus in a sample has the same probability $\lambda\,dt$ of decaying in
any short interval $dt$, independently of its age and of every other nucleus.
For a large number of nuclei each with a small probability of decaying, the
number $N$ observed in a fixed interval follows the **Poisson distribution**

$$
P(N;\mu) = \frac{\mu^N e^{-\mu}}{N!} ,
$$ (eq-poisson)

whose mean and *variance* are both $\mu$. Hence the standard deviation is
$\sqrt{\mu}$, and a single measurement $N$ estimates its own uncertainty as
$\sqrt{N}$. This is why counting for longer helps: the relative uncertainty is
$\sqrt{N}/N = 1/\sqrt{N}$, so a 1% measurement needs $10^4$ counts and a 0.1%
measurement needs $10^6$.

For $\mu \gtrsim 20$ the Poisson distribution is well approximated by a
Gaussian of mean $\mu$ and standard deviation $\sqrt{\mu}$. Below that it is
visibly asymmetric, and for small $\mu$ the difference matters: at $N = 0$ the
estimator $\sqrt{N} = 0$ is plainly wrong, and one must use a proper
confidence interval instead. You will observe both regimes today.

```{figure} ../images/exp13-poisson-gaussian-concept.svg
:label: fig:exp13-poisson-gaussian
:alt: Two bar charts of the Poisson distribution, one for mu equals 3 showing a visibly skewed shape that departs from the overlaid Gaussian curve, and one for mu equals 30 where the Poisson bars and the Gaussian curve are nearly indistinguishable.

The same law, two regimes. At $\mu=3$ the Poisson distribution is visibly skewed and the Gaussian approximation is poor near $N=0$; at $\mu=30$ the two are nearly indistinguishable, which is why $\sqrt{N}$ works so well once the counts are large.
```

### Decay law

$$
N(t) = N_0 e^{-\lambda t}, \qquad
T_{1/2} = \frac{\ln 2}{\lambda} .
$$ (eq-decay)

The measured *count rate* is proportional to the activity $\lambda N(t)$, so
the rate obeys the same exponential.

### The isotope generator

$^{137}$Cs ($T_{1/2} = 30.08\ \text{y}$) beta-decays to an excited state of
$^{137}$Ba, which de-excites by emitting a $661.7\ \text{keV}$ gamma with
$T_{1/2} = 2.552\ \text{min}$. Because the metastable barium is chemically
distinct from caesium, it can be eluted from an ion-exchange column with a
saline solution, giving a nearly pure short-lived sample. Ten minutes of
counting spans four half-lives, and the parent stays behind on the column.

### Gamma attenuation

A narrow beam of monoenergetic gammas through an absorber of thickness $x$
follows

$$
I(x) = I_0 e^{-\mu x} ,
\qquad
x_{1/2} = \frac{\ln 2}{\mu} ,
$$ (eq-attenuation)

where $\mu$ is the linear attenuation coefficient. Unlike the beta absorption
of Week 3, this is genuinely exponential, because a gamma is removed from the
beam in a single event rather than losing energy gradually.

At $662\ \text{keV}$ the dominant mechanism in light materials is **Compton
scattering**, which scales roughly with electron density and therefore with
$Z/A$ — nearly constant across the periodic table. In lead, the higher-$Z$
photoelectric contribution is also significant. The NIST mass attenuation
coefficients at $662\ \text{keV}$ are about $0.111\ \text{cm}^2/\text{g}$ for
lead and $0.0745\ \text{cm}^2/\text{g}$ for aluminium, giving narrow-beam
half-value layers of roughly $5.5\ \text{mm}$ and $34\ \text{mm}$
respectively. Look these up yourself in XCOM rather than taking them from
here.

:::{warning} Broad beam and buildup
[](#eq-attenuation) assumes a *narrow* beam: any photon that scatters is
counted as removed. In a real geometry, scattered photons can still reach the
detector, so the measured attenuation is weaker than the true $\mu$ and the
apparent half-value layer is larger. Collimating the beam reduces this
**buildup**; quantifying how much your geometry suffers from it is one of the
questions below.
:::

## Pre-lab

:::{exercise}
:label: q-count-01

Evaluate [](#eq-poisson) for $\mu = 3$ and $N = 0,1,\ldots,8$, and for
$\mu = 30$ and $N = 20,\ldots,40$. Plot both and comment on the symmetry.
:::

:::{exercise}
:label: q-count-02

How many counts are needed for a relative uncertainty of 5%? 1%? 0.1%? If
your source gives $200\ \text{s}^{-1}$, how long for each?
:::

:::{exercise}
:label: q-count-03

$^{137m}$Ba has $T_{1/2} = 2.552\ \text{min}$. If you start with a rate of
$1500\ \text{s}^{-1}$ above background, what is the rate after 5, 10, and
15 minutes? If the background is $0.5\ \text{s}^{-1}$, at what time does the
sample rate fall to the background rate? How long should you therefore plan to
count?
:::

:::{exercise}
:label: q-count-04

A GM tube has a dead time of $\tau_d = 100\ \mu\text{s}$. At an observed rate
of $500\ \text{s}^{-1}$, what fraction of counts is lost? At
$2000\ \text{s}^{-1}$? At what observed rate does the correction exceed 10%,
and what does that imply for the early part of your decay curve?
:::

## Apparatus

- GM tube, counter/timer with programmable repeat runs, and HV supply
- $^{137}$Cs/$^{137m}$Ba isotope generator, eluting solution, planchets,
  gloves, tray
- Long-lived check source ($^{137}$Cs or $^{60}$Co sealed button) for the
  attenuation measurement
- Lead sheets ($1$–$10\ \text{mm}$) and the available aluminium absorber set
- Collimator, if available
- Stopwatch; the source log

:::{danger}
The eluate is **unsealed** activity. Gloves, work over a tray, do not touch the
planchet face, and dispose of it as directed. It is essentially gone within
half an hour, but it is loose while you have it. Sealed sources are handled
with tongs and returned to shielded storage. See [](#lab-safety).
:::

```{figure} ../images/exp13-counting-schematic.svg
:label: fig:exp13-counting
:alt: Panel (a), a GM tube mounted directly above an eluted barium-137m planchet on a fixed shelf, feeding a counter and timer. Panel (b), a sealed check source facing a GM tube through an interchangeable stack of lead absorber sheets.

Two fixed geometries. (a) The short-lived $^{137m}$Ba planchet counted at close, unchanging range for the half-life run. (b) A long-lived check source counted through increasing lead thickness for the attenuation run.
```

## Procedure

### Part A — The statistics of counting

1. Set the operating voltage from the plateau, as in [](#exp-beta-electrons).
2. Place a long-lived source so that you get an average of about **3 counts**
   per one-second interval. Take **at least 300** one-second runs. Use the
   counter's repeat mode; do not do this with a stopwatch.
3. Move the source (or increase the interval) so that you get an average of
   about **30 counts** per interval. Take another 300 runs.
4. Take 300 runs of pure background at the same interval.

**[ ] Checkpoint 1.** Show the instructor your two mean
counts and confirm they are near 3 and 30 before committing to the full runs.

### Part B — Half-life of $^{137m}$Ba

5. Set the counter to take, say, 60 consecutive $10\ \text{s}$ runs and to
   record each — you want a time series, not a total.
6. Elute the generator onto a planchet, put it under the detector at a fixed
   geometry, and start counting. **Record the elution time.**
7. Let the run continue for at least $15\ \text{minutes}$ — about six
   half-lives, over which the rate falls by a factor of about $60$.

   Note that this does **not** bring you down to background: a sample starting
   at $1500\ \text{s}^{-1}$ is still at roughly $25\ \text{s}^{-1}$ after
   15 minutes, and would need about half an hour to reach a
   $0.5\ \text{s}^{-1}$ background. So the background term in your fit is
   *not* determined by your own decay curve. Measure it separately, before
   elution and again after the run, and hold it fixed in the fit rather than
   letting it float — a floating floor that the data cannot constrain will
   absorb real signal and bias $T_{1/2}$ upward.
8. Do not move the sample or the detector during the run.
9. If time allows, elute a second sample and repeat. Two independent decay
   curves is a much better basis for a claimed uncertainty than one.

### Part C — Gamma attenuation

10. Replace the eluate with the sealed $^{137}$Cs source at a fixed geometry,
    collimated if possible.
11. Measure the rate through lead absorbers of at least eight thicknesses,
    spanning zero to about four half-value layers. Increase the counting time
    as the rate falls, aiming for a comparable relative uncertainty at every
    point.
12. Repeat with aluminium over the full thickness supplied. This set does not
    provide four aluminium half-value layers at 662 keV, so report the
    measured range and fit a mass attenuation coefficient only over that
    range; do not claim a four-HVL comparison.
13. Measure the background with the source removed and the absorbers in place.

## Analysis

### Testing the Poisson hypothesis

```python
import numpy as np
from scipy.stats import poisson, chisquare

counts = np.array([...])                 # 300 one-second counts
mu     = counts.mean()
var    = counts.var(ddof=1)
print(f"mean = {mu:.3f},  variance = {var:.3f},  ratio = {var/mu:.3f}")

# Compare the observed histogram with Poisson AND with a Gaussian of the same mean.
k    = np.arange(0, counts.max() + 1)
obs  = np.bincount(counts, minlength=k.size)
exp  = poisson.pmf(k, mu) * counts.size
```

For a Poisson process the variance-to-mean ratio should be 1. Report it with
an uncertainty — for $n$ samples, the ratio has a standard deviation of
approximately $\sqrt{2/(n-1)}$ — and perform a chi-square goodness-of-fit test
against both the Poisson and Gaussian expectations, binning so that every bin
has an expectation of at least 5.

For the $\mu \approx 3$ data set the Poisson distribution should fit and the
Gaussian should not. For $\mu \approx 30$ both should fit. **Showing this
difference is the point of Part A**, so present both comparisons on the same
figure.

### The half-life

```python
import numpy as np
from scipy.optimize import curve_fit

t  = np.array([...])           # mid-interval times, seconds since elution
N  = np.array([...])           # counts in each interval
sN = np.sqrt(N)                # Poisson; use a proper interval where N is small

bg = bg_measured                          # counts per interval, measured separately
model = lambda t, N0, lam: N0 * np.exp(-lam * t) + bg
popt, pcov = curve_fit(model, t, N, p0=[N[0], np.log(2)/153.1],
                       sigma=sN, absolute_sigma=True)
lam, slam = popt[1], np.sqrt(pcov[1, 1])
T12  = np.log(2) / lam
sT12 = T12 * slam / lam
```

Three points of technique that separate a good analysis from a poor one:

1. **Fit the exponential directly**, with the background held at its
   independently measured value. Do not take logarithms and fit a line unless
   you transform the uncertainties too — see [](#uncertainty). This experiment
   is the canonical case where the shortcut biases the answer.
2. **Use the mid-point of each counting interval** as $t$, not its start. Over
   a $10\ \text{s}$ interval with a $153\ \text{s}$ half-life this is a 3%
   effect on the early points.
3. **Apply the dead-time correction** to the early, high-rate points, and
   check whether it moves $T_{1/2}$. If it does, quote the corrected value and
   report the size of the shift.

Plot the residuals. A curved residual pattern at early times is the signature
of an uncorrected dead time; one at late times means the background floor is
wrong.

### Attenuation

Fit $R(x) = R_0e^{-\mu x} + R_{\text{bg}}$ for each material, and convert to a
half-value layer and to a mass attenuation coefficient $\mu/\rho$. Compare
$\mu/\rho$ for lead and aluminium: if Compton scattering dominates, the two
mass attenuation coefficients should be much closer to each other than the two
linear coefficients are.

## Post-lab questions

:::{exercise}
:label: q-count-05

Report the variance-to-mean ratio for both data sets, with uncertainties. Are
they consistent with 1? Report the chi-square results for the Poisson and
Gaussian fits at $\mu \approx 3$ and state which distribution is required.
:::

:::{exercise}
:label: q-count-06

In your low-count data set, how many intervals had $N = 0$? What does the
naive uncertainty $\sqrt{N}$ give for those, and why is it wrong? Look up the
Poisson upper confidence limit for zero observed counts and state it.
:::

:::{exercise}
:label: q-count-07

Report $T_{1/2}$ with its uncertainty and compare with $2.552\ \text{min}$ in
units of $\sigma$. State the size of the dead-time correction and of the
mid-interval correction, and whether each mattered.
:::

:::{exercise}
:label: q-count-08

Report $\mu$ and $\mu/\rho$ for lead and aluminium. Compare the two $\mu/\rho$
values and use the comparison to argue which interaction mechanism dominates
at $662\ \text{keV}$. Look up the NIST XCOM values and compare.
:::

:::{exercise}
:label: q-count-09

Was your geometry narrow-beam or broad-beam? Estimate the size of the buildup
effect from the sign and size of your discrepancy with the tabulated $\mu$,
and describe the measurement you would make to test the explanation.
:::

:::{exercise}
:label: q-count-10

A colleague reports a count of $10\,000 \pm 100$ from a $60\ \text{s}$ run and
says the uncertainty comes from "instrument precision". Explain what is
actually setting that uncertainty, and what would and would not reduce it.
:::

## Going further

- **The interval distribution.** The times *between* successive counts in a
  Poisson process follow an exponential distribution. Logging individual event
  timestamps with a microcontroller and histogramming the intervals shows this
  directly, and the deficit of very short intervals is a clean, independent
  measurement of the detector's dead time.
- **Two-source dead-time measurement.** Count source A, source B, and both
  together. Because $R_{A+B} < R_A + R_B$ when counts are lost, the deficit
  gives $\tau_d$ without any assumption about the counter's electronics.
- **Gamma spectroscopy.** A scintillator and a multichannel analyser resolve
  the $662\ \text{keV}$ photopeak from the Compton continuum and edge, letting
  you verify the Compton formula from Chapter 6 with the same source. Compute
  the expected Compton edge at $478\ \text{keV}$ and look for it.

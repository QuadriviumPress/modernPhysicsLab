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
**Apparatus** Geiger–Müller counter, $^{137}$Cs/$^{137m}$Ba isotope generator, lead and aluminum absorbers
**You will measure** the Poisson character of radioactive decay, the half-life of $^{137m}$Ba, and a gamma attenuation coefficient
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Test whether repeated counts are consistent with a Poisson model, and
  state when $\sqrt{N}$ is a useful uncertainty estimate.
- Distinguish the Poisson and Gaussian regimes and know when each applies.
- Measure a short half-life from interval counts with a Poisson fit.
- Estimate a gamma attenuation coefficient and compare the result with
  a narrow-beam reference after checking the measurement geometry.

## Textbook connection

Read §13.3–13.6. This experiment is the practical foundation for everything in
nuclear and particle physics: essentially every measurement in the field is a
counting measurement. Its uncertainty includes random counts, background
subtraction, dead time, geometry, and calibration. This experiment explains
when the `sqrt(N)` approximation used since Week 3 is appropriate.

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
$\sqrt{\mu}$. For sufficiently many counts, a single observation $N$ gives
the approximate standard uncertainty $\sqrt{N}$. In an ideal gross count
with negligible background and dead time, the relative uncertainty is then
$1/\sqrt{N}$: 1% needs about $10^4$ counts and 0.1% needs $10^6$.
Subtracting an independently measured background adds its counting variance.

For $\mu \gtrsim 20$ the Poisson distribution is well approximated by a
Gaussian of mean $\mu$ and standard deviation $\sqrt{\mu}$. Below that it is
visibly asymmetric, and for small $\mu$ the difference matters: at $N = 0$ the
estimator $\sqrt{N} = 0$ is plainly wrong, and one must use a proper
confidence interval instead. You will observe both regimes today.

```{figure} ../images/exp13-poisson-gaussian-concept.svg
:label: fig:exp13-poisson-gaussian
:alt: Two plots of Poisson count probabilities as bars with an overlaid continuous Gaussian density, one for mean 3 showing skew and a mismatch near zero, and one for mean 30 showing close shapes.

The same law, two regimes. At $\mu=3$ the Poisson distribution is visibly skewed
and the Gaussian density is poor near $N=0$; at $\mu=30$ their shapes are close.
The bars show probabilities and the line is a continuous density.
```

### Decay law

$$
N(t) = N_0 e^{-\lambda t}, \qquad
T_{1/2} = \frac{\ln 2}{\lambda} .
$$ (eq-decay)

The measured *count rate* is proportional to the activity $\lambda N(t)$, so
the rate obeys the same exponential.

### The isotope generator

$^{137}$Cs ($T_{1/2} \approx 30.08\ \text{y}$) feeds metastable
$^{137m}$Ba, which has $T_{1/2} \approx 2.552\ \text{min}$ and emits a
$661.7\ \text{keV}$ gamma in its de-excitation. A licensed generator can
retain the caesium while barium is eluted under its approved procedure.
Do not assume perfect parent retention: the instructor checks for
long-lived $^{137}$Cs breakthrough and controls the eluate and waste.

### Gamma attenuation

A narrow beam of monoenergetic gammas through an absorber of thickness $x$
follows

$$
I(x) = I_0 e^{-\mu x} ,
\qquad
x_{1/2} = \frac{\ln 2}{\mu} ,
$$ (eq-attenuation)

where $\mu$ is the linear attenuation coefficient. Each interaction removes
a primary gamma from the unscattered beam, producing an exponential
primary transmission. A GM counter has no energy resolution and can also
count scattered photons that reach it.

At $662\ \text{keV}$ the dominant mechanism in light materials is **Compton
scattering**, which scales roughly with electron density and therefore with
$Z/A$ — nearly constant across the periodic table. In lead, the higher-$Z$
photoelectric contribution is also significant. The NIST mass attenuation
coefficients at $662\ \text{keV}$ are about $0.11\ \text{cm}^2/\text{g}$ for
lead and $0.0745\ \text{cm}^2/\text{g}$ for aluminum, giving narrow-beam
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

Assume a nonparalyzable GM dead time $\tau_d = 100\ \mu\text{s}$, for which
the true rate is $r=m/(1-m\tau_d)$ at observed rate $m$. What fraction of
events is lost at observed rates of $500$ and $2000\ \text{s}^{-1}$?
At what observed rate does the lost fraction exceed 10%? What early
rate would limit it to 1%?
:::

## Apparatus

- GM tube, counter/timer with programmable repeat runs, and HV supply
- $^{137}$Cs/$^{137m}$Ba isotope generator, eluting solution, planchets,
  gloves, tray
- Sealed $^{137}$Cs check source for the 662 keV attenuation measurement
- Lead sheets ($1$–$10\ \text{mm}$) and the available aluminum absorber set
- Collimator, if available
- Stopwatch; the source log

:::{danger}
The eluate is **unsealed** activity. Use a generator only under the
institution's approved procedure, with the specified gloves, tray,
contamination checks, and waste controls. Its short daughter half-life
does not establish that eluate or waste is safe to discard: parent
breakthrough must be assessed. Handle sealed sources with the approved
holder or tools and return them to designated storage. See [](#lab-safety).
:::

```{figure} ../images/exp13-counting-schematic.svg
:label: fig:exp13-counting
:alt: Panel (a), a GM tube mounted directly above an eluted barium-137m planchet on a fixed shelf, feeding a counter and timer. Panel (b), a sealed caesium-137 source facing a GM tube through an interchangeable stack of lead absorber sheets.

Two fixed geometries. (a) The short-lived $^{137m}$Ba planchet counted at close, unchanging range for the half-life run. (b) A long-lived check source counted through increasing lead thickness for the attenuation run.
```

## Procedure

### Before you start the timed runs

- Identify the two independent geometries in [](#fig:exp13-counting): the
  generator eluate directly beneath the GM tube for half-life and the sealed
  source–absorber–tube line for attenuation. Record dimensions for each and do
  not transfer distances from the schematic.
- Verify the counter clock and repeat mode with ten short test intervals. Make
  sure it stores each interval separately, including its start and end times
  and whether the duration is wall time or corrected live time.
- Prepare three machine-readable tables: repeated counts, decay time series,
  and attenuation. Include raw counts, start time, live time, source,
  absorber, geometry, high voltage, and run ID in every applicable row.
- Measure background in the geometry used for each part. Record raw background
  counts and duration; do not enter a pre-subtracted rate into the primary
  data file. Background is part of the fitted count model.
- Plan source handling before elution, including who starts the counter and who
  records the elution time. Rehearse once without activity so the first decay
  point is not lost to confusion.

### Part A — The statistics of counting

1. Set the operating voltage from the plateau, as in [](#exp-beta-electrons).
2. Place a long-lived source so that you get an average of about **3 counts**
   per one-second interval, including background. Take **at least 300**
   one-second runs. Use the
   counter's repeat mode; do not do this with a stopwatch.
3. Move the source (or increase the interval) so that you get an average of
   about **30 counts** per interval. Take another 300 runs.
4. Take 300 runs of pure background at the same interval. Check that the
   mean does not drift during either series; a changing rate is not a
   single stationary Poisson process.

**[ ] Checkpoint 1.** Show the instructor your two mean
counts and confirm they are near 3 and 30 before committing to the full runs.

### Part B — Half-life of $^{137m}$Ba

5. Set the counter to take at least 90 consecutive $10\ \text{s}$ runs,
   recording every interval. Aim for an early observed rate below about
   $100\ \text{s}^{-1}$ if the nonparalyzable dead time is
   $100\ \mu\text{s}$; this limits the lost-count fraction to about 1%.
   Verify the actual detector dead time and adjust the approved source
   geometry before elution.
6. Elute the generator onto a planchet, put it under the detector at a fixed
   geometry, and start counting. **Record the elution time.**
7. Let the run continue for at least $15\ \text{minutes}$ — about six
   half-lives, over which the rate falls by a factor of about $60$.

   This may not reach background: a hypothetical sample starting at
   $1500\ \text{s}^{-1}$ remains near $25\ \text{s}^{-1}$ after 15 minutes
   and needs about 30 minutes to approach a $0.5\ \text{s}^{-1}$ background.
   Measure background before elution and after the run. Fit it jointly with
   the decay data and background count, so its finite precision is included.
   Investigate any apparent persistent activity as possible breakthrough.
8. Do not move the sample or the detector during the run.
9. If time allows, elute a second sample and repeat. Two independent decay
   curves is a much better basis for a claimed uncertainty than one.

### Part C — Gamma attenuation

10. Remove and control the eluate as directed, then use a sealed $^{137}$Cs
    source at a fixed geometry. Record source, absorber, and detector
    apertures and separations; collimate if the approved setup allows it.
11. Measure lead at several thicknesses spanning as much of the available
    transmission range as practical. Increase counting time as the rate
    falls, aiming for comparable uncertainty in net rates. Record each
    sheet's thickness and the stack order.
12. Repeat with aluminum over the thickness available. Report the actual
    number of half-value layers covered rather than assuming the kit spans
    four.
13. Measure background with the source removed in the same detector and
    absorber geometry, including a check near each end of the series.

## Analysis

### Testing the Poisson hypothesis

```python
import numpy as np
from scipy.stats import poisson, norm

counts = np.array([...])                 # 300 equal-duration gross counts
mu     = counts.mean()
var    = counts.var(ddof=1)
print(f"mean = {mu:.3f},  variance = {var:.3f},  ratio = {var/mu:.3f}")

# Include every observation and a model tail in the last bin.
kmax = max(counts.max(), int(poisson.ppf(0.9999, mu)))
k    = np.arange(kmax + 1)
obs  = np.bincount(counts, minlength=k.size)
exp_p = counts.size * poisson.pmf(k, mu)
exp_p[-1] = counts.size * poisson.sf(kmax - 1, mu)

# Continuity-corrected Gaussian probabilities for integer-count bins.
exp_g = counts.size * (norm.cdf(k + 0.5, mu, np.sqrt(mu))
                       - norm.cdf(k - 0.5, mu, np.sqrt(mu)))
exp_g[0] = counts.size * norm.cdf(0.5, mu, np.sqrt(mu))
exp_g[-1] = counts.size * norm.sf(kmax - 0.5, mu, np.sqrt(mu))
```

For a Poisson process the variance-to-mean ratio should be 1. Report it with
an uncertainty — for $n$ samples, the ratio has a standard deviation of
approximately $\sqrt{2/(n-1)}$ under the stationary Poisson model. Combine
adjacent tail bins until each model's expected count is at least about 5,
then compute $\chi^2=\sum(O-E)^2/E$. With $b$ final bins and one mean
estimated from the data, use approximately $b-2$ degrees of freedom.
Document the bins; the Gaussian approximation includes its negative tail
in the zero-count bin.

At $\mu \approx 3$ the Gaussian approximation has a visibly different shape;
300 trials may or may not reject it at a chosen significance level. At
$\mu \approx 30$ the two models are close. Present both comparisons with
the observed histogram, and interpret a non-rejection as limited evidence,
not proof that a model is exact.

### The half-life

```python
import numpy as np
from scipy.optimize import minimize
from scipy.special import xlogy

t0 = np.array([...])       # interval starts, seconds since elution
t1 = np.array([...])       # interval ends, seconds since elution
N = np.array([...])        # raw gross counts in those intervals
B, TB = ..., ...           # separate background count and duration (s)
dt = t1 - t0

def expected(logpars):
    r0, lam, bg = np.exp(logpars)  # source rate at elution, decay, background
    signal = r0 * np.exp(-lam * t0) * (-np.expm1(-lam * dt)) / lam
    return signal + bg * dt, bg

def nll(logpars):
    mean, bg = expected(logpars)
    return np.sum(mean - xlogy(N, mean)) + bg * TB - xlogy(B, bg * TB)

guess = np.log([max(N[0] / dt[0], 0.1), np.log(2) / 153.12,
                max(B / TB, 0.001)])
fit = minimize(nll, guess)
if not fit.success:
    raise RuntimeError(fit.message)
lam = np.exp(fit.x[1])
T12 = np.log(2) / lam
```

The fit uses the expected count integrated over each real interval and
includes the separate background measurement in the same likelihood.
Obtain a half-life interval by profiling the likelihood or by simulating
new count series and background counts from the fitted model and refitting.
Check the following:

1. **Keep the raw counts.** Subtracting background before a Poisson fit or
   weighting each point by $1/\sqrt{N}$ fails at small $N$.
2. **Keep real time stamps.** For equal interval widths, replacing each
   integral by a midpoint value changes the fitted amplitude, not the
   exponential slope. For a 10 s interval at this half-life the integrated
   value differs from the midpoint approximation by only about 0.009%.
   Irregular or missed intervals still need their actual bounds.
3. **Check dead time.** At low rates the Poisson model above is suitable.
   If the measured early dead-time loss is material, incorporate a
   calibrated detector model or repeat at greater source–detector distance;
   a naive correction to counts does not preserve Poisson uncertainties.

Plot count residuals against time. Early or late patterns can suggest dead
time, geometry changes, background error, or parent breakthrough; investigate
with controls rather than assigning a cause from the shape alone.

### Attenuation

Fit gross interval counts with a source term proportional to
$e^{-\mu x}$ plus measured background, using a Poisson likelihood and each
point's acquisition time. Check dead time at the thinnest absorber and
propagate thickness and density uncertainty when calculating
$x_{1/2}=\ln 2/\mu$ and $\mu/\rho$. Compare the material values with
NIST XCOM at the same energy. If the detector accepts scattered photons,
label the fitted value an **effective** attenuation coefficient; agreement
or disagreement alone cannot establish an interaction mechanism.

## Post-lab questions

:::{exercise}
:label: q-count-05

Report the variance-to-mean ratio for both data sets, with uncertainties. Are
they consistent with 1? Report the chi-square results for the Poisson and
Gaussian comparisons at $\mu \approx 3$, including the binning and degrees
of freedom. Does the data distinguish them at your chosen threshold?
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
units of $\sigma$ if the relevant uncertainties are well estimated. State
the dead-time loss at the earliest rate and the effect of using interval
bounds rather than midpoints.
:::

:::{exercise}
:label: q-count-08

Report $\mu$ and $\mu/\rho$ for lead and aluminum. Compare the two $\mu/\rho$
values with NIST XCOM at $662\ \text{keV}$. Which interaction channels does
XCOM predict for each material, and can your GM measurements separate them?
:::

:::{exercise}
:label: q-count-09

Was your geometry narrow-beam or broad-beam? Estimate the size of the buildup
effect only if you have a geometry comparison or another independent
constraint. What change in collimation or detector position would test it?
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
  can estimate $\tau_d$ after background and geometry corrections, under an
  explicit paralyzable or nonparalyzable detector model.
- **Gamma spectroscopy.** A scintillator and a multichannel analyzer resolve
  the $662\ \text{keV}$ photopeak from the Compton continuum and edge, letting
  you verify the Compton formula from Chapter 6 with the same source. Compute
  the expected Compton edge at $478\ \text{keV}$ and look for it.

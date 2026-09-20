---
title: Uncertainty and Curve Fitting
short_title: Uncertainty
label: uncertainty
---

# Uncertainty and Curve Fitting

Every experiment in this manual ends in a number with an uncertainty. This
section is the reference for how that uncertainty is obtained. Read it once
now, and come back to it in Weeks 3, 6, and 13, where it does the most work.

## What an uncertainty means

A result quoted as $x = 633.4 \pm 0.8\ \text{nm}$ is a claim about a
probability distribution: the experimenter believes the true value lies within
one $\sigma$ of the quoted value about 68% of the time, and within two $\sigma$
about 95% of the time. It is not a bound, not a guarantee, and not a worst
case.

Two kinds of uncertainty contribute.

**Type A (statistical)** uncertainties are estimated from the scatter of
repeated measurements. They fall as $1/\sqrt{N}$ and are reduced by taking
more data.

**Type B (systematic)** uncertainties are estimated from everything else: the
calibration of the instrument, the resolution of the scale, a temperature
coefficient, a geometric offset. They do *not* fall with $N$, which is why an
experiment eventually stops improving no matter how long you run it. Deciding
when you have hit that floor is a large part of experimental judgement.

### Estimating a Type A uncertainty

For $N$ repeated measurements $x_i$ of the same quantity, the sample standard
deviation

$$
s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2}
$$

estimates the spread of a *single* reading, and the standard error of the mean

$$
\sigma_{\bar{x}} = \frac{s}{\sqrt{N}}
$$

is the uncertainty of the average. The distinction matters: $s$ describes the
apparatus, $\sigma_{\bar{x}}$ describes your knowledge of the mean. Report the
second, but look at the first — if $s$ is much larger than the instrument's
resolution, something is fluctuating and it is worth knowing what.

### Estimating a Type B uncertainty

Common cases:

:::{list-table}
:header-rows: 1

* - Source
  - Standard uncertainty
* - Digital display, last digit $d$
  - $d/\sqrt{12} \approx 0.29\,d$ (uniform over the last digit)
* - Analogue scale, division $D$
  - $\approx D/4$ if you can interpolate to a quarter division
* - Manufacturer's spec "$\pm a$" with no distribution stated
  - $a/\sqrt{3}$ (uniform over $\pm a$)
* - Manufacturer's spec "$\pm a$ at 95% confidence"
  - $a/2$
* - A quantity you can bound between $x_-$ and $x_+$ and know nothing else
  - $(x_+ - x_-)/\sqrt{12}$
:::

Combine independent Type A and Type B contributions in quadrature:
$\sigma^2 = \sigma_A^2 + \sigma_{B,1}^2 + \sigma_{B,2}^2 + \cdots$.

## Propagating uncertainty

For a result $f(x, y, \ldots)$ computed from independently measured
quantities,

$$
\sigma_f^2 = \left(\frac{\partial f}{\partial x}\right)^2\sigma_x^2
           + \left(\frac{\partial f}{\partial y}\right)^2\sigma_y^2 + \cdots
$$

Two shortcuts cover most cases in this manual:

- **Sums and differences**: $f = x \pm y \Rightarrow \sigma_f^2 = \sigma_x^2 + \sigma_y^2$.
  *Absolute* uncertainties add in quadrature.
- **Products and powers**: $f = A\,x^a y^b \Rightarrow
  \left(\sigma_f/f\right)^2 = a^2(\sigma_x/x)^2 + b^2(\sigma_y/y)^2$.
  *Relative* uncertainties add in quadrature, weighted by the exponents.

:::{warning} The difference trap
The product rule fails badly for a difference of two nearly equal numbers.
If $x = 10.00 \pm 0.02$ and $y = 9.95 \pm 0.02$, then $x - y = 0.05 \pm 0.03$
— a 0.2% measurement of each has produced a 57% measurement of the difference.
Several experiments here (the Michelson mirror displacement, the Compton shift,
the LED turn-on voltage) are exactly this kind of measurement, and the way to
beat it is always to arrange for the difference to be large: translate the
mirror further, use a longer baseline, span a wider range of wavelengths.
:::

If the derivatives are unpleasant, propagate numerically — perturb each input
by its uncertainty, recompute, and add the changes in quadrature. Three lines
of Python, no calculus, and it handles correlations badly in exactly the same
way the formula above does.

## Fitting a model to data

Most experiments here reduce to: *fit a model $y = f(x; \theta)$ to data and
report the parameters $\theta$ with their uncertainties.* The parameter is the
physics; the fit is bookkeeping.

### Weighted least squares

Given data $(x_i, y_i)$ with uncertainties $\sigma_i$ on $y$, choose the
parameters that minimize

$$
\chi^2(\theta) = \sum_{i=1}^{N}
  \frac{\left[y_i - f(x_i;\theta)\right]^2}{\sigma_i^2}.
$$

Each residual is measured in units of its own uncertainty, so a point you know
well pulls the fit harder than one you do not. This is why **you must supply
the $\sigma_i$**: an unweighted fit silently assumes every point is equally
good, which is almost never true when a signal spans decades — as in every
exponential decay in this manual.

### Reading the fit

Three numbers come out, and all three matter.

**The parameters** $\hat\theta$ — the physics.

**Their uncertainties**, the square roots of the diagonal of the covariance
matrix, $\sigma_{\theta_j} = \sqrt{C_{jj}}$.

**The reduced chi-square**, $\chi^2_\nu = \chi^2_{\min}/\nu$ with
$\nu = N - p$ degrees of freedom for $p$ fitted parameters. It is a
self-consistency check on your uncertainty estimates:

- $\chi^2_\nu \approx 1$: the model describes the data to within the quoted
  uncertainties. Good.
- $\chi^2_\nu \gg 1$: either the model is wrong or the uncertainties are
  underestimated. Look at the residuals — *structure* in the residuals means
  the model is wrong; uniform excess scatter means the errors are too small.
- $\chi^2_\nu \ll 1$: the uncertainties are overestimated. Common when
  students assign a whole scale division to a reading they could interpolate.

Always plot the residuals $(y_i - f(x_i;\hat\theta))/\sigma_i$ against $x_i$.
A fit is judged by its residuals, not by how good the curve looks on top of
the data.

### Correlation between parameters

The off-diagonal elements of $C$ are not decoration. In a straight-line fit
$y = mx + b$ over data far from the origin, $m$ and $b$ are strongly
anticorrelated, and quoting their independent uncertainties overstates how
well you know $f(x)$ at any particular $x$. When a derived quantity depends on
more than one fitted parameter — as in Experiment 6, where $h$ comes from a
slope and the work function from an intercept — propagate with the full
covariance matrix:

$$
\sigma_g^2 = \sum_{j}\sum_{k}
  \frac{\partial g}{\partial \theta_j}\frac{\partial g}{\partial \theta_k} C_{jk}.
$$

### Linearize with care

It is tempting to fit an exponential $N(t) = N_0 e^{-\lambda t}$ by taking
logarithms and fitting a straight line. This is legitimate *only if you
transform the uncertainties too*: if $N$ has uncertainty $\sigma_N$, then
$\ln N$ has uncertainty $\sigma_N/N$, so the late-time points — which have
small absolute uncertainty but large relative uncertainty — must be
down-weighted. An unweighted fit to $\ln N$ gives systematically wrong decay
constants, and this is the single most common error in the reports from this
course. Prefer fitting the exponential directly; if you linearize, weight
correctly and say in the report that you did.

For Poisson-distributed counts $N$, the uncertainty is $\sqrt{N}$ — see
[](#exp-counting-statistics) for why, and for the case $N = 0$, where
$\sqrt{N}$ is not usable.

## Comparing to an accepted value

Quote the discrepancy in units of the combined uncertainty:

$$
t = \frac{\left|x_{\text{meas}} - x_{\text{acc}}\right|}
         {\sqrt{\sigma_{\text{meas}}^2 + \sigma_{\text{acc}}^2}}.
$$

Interpret it as a $z$-score: $t < 2$ is agreement, $2 < t < 3$ is a mild
tension worth a sentence, $t > 3$ needs an explanation. Never use percent
difference alone — a 3% discrepancy is excellent for the muon flux and
catastrophic for the Rydberg constant, and only the uncertainty tells you
which situation you are in.

## Worked template

```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def model(x, m, b):
    """Replace with the physics. x, m, b are floats or arrays."""
    return m * x + b

x  = np.array([...])          # independent variable
y  = np.array([...])          # measured values
sy = np.array([...])          # 1-sigma uncertainty on each y  (never omit)

p0 = [1.0, 0.0]               # a starting guess that is roughly right matters
                              # more for nonlinear models than students expect

popt, pcov = curve_fit(model, x, y, p0=p0, sigma=sy, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))

resid = (y - model(x, *popt)) / sy
chi2  = np.sum(resid**2)
nu    = len(x) - len(popt)

for name, val, err in zip(["m", "b"], popt, perr):
    print(f"{name} = {val:.6g} +/- {err:.2g}")
print(f"chi2/nu = {chi2/nu:.2f}  (nu = {nu})")

fig, (ax, axr) = plt.subplots(
    2, 1, sharex=True, height_ratios=[3, 1], figsize=(6, 5)
)
xs = np.linspace(x.min(), x.max(), 400)
ax.errorbar(x, y, yerr=sy, fmt="o", capsize=3, label="data")
ax.plot(xs, model(xs, *popt), "-", label="fit")
ax.set_ylabel("y  [unit]")
ax.legend()

axr.axhline(0, lw=0.8)
axr.errorbar(x, resid, yerr=1, fmt="o", capsize=3)
axr.set_xlabel("x  [unit]")
axr.set_ylabel(r"residual / $\sigma$")
fig.tight_layout()
```

:::{important} `absolute_sigma=True`
Without it, `curve_fit` treats your `sigma` array as *relative* weights and
rescales the covariance matrix so that $\chi^2_\nu = 1$ by construction. That
throws away the information you worked to obtain, and makes the reduced
chi-square check meaningless. Set it to `True` whenever your `sigma` values
are real, physical uncertainties — which, in this course, they always are.
:::

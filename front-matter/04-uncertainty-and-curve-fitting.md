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

A result quoted as $x = 633.4 \pm 0.8\ \text{nm}$ needs a stated meaning for
the $0.8\ \text{nm}$. In this manual, an uncertainty written as $\sigma$ is a
*standard uncertainty*, comparable to one standard deviation. If the
uncertainty model is approximately normal, an interval of one $\sigma$ covers
about 68% of that distribution, and two $\sigma$ about 95%. These are model
based coverage statements, not guarantees or worst-case bounds. State a
different coverage factor when you report an expanded uncertainty.

Two methods are used to evaluate uncertainty components.

**Type A** components are evaluated statistically, often from repeated
measurements. For independent readings under stable conditions, the standard
uncertainty of their *mean* falls as $1/\sqrt{N}$. The scatter of individual
readings does not fall merely because you collect more of them.

**Type B** components are evaluated by other information, such as an
instrument specification, calibration certificate, scale resolution, or a
bound on a geometric offset. Type A and Type B describe *how a component was
evaluated*, not whether its effect is random or systematic. A shared
calibration offset, for example, is not reduced by repeating readings with
the same instrument. Decide which effects are shared before assuming that
more measurements will improve the result. See [NIST TN 1297, §§2–4](https://www.nist.gov/pml/nist-technical-note-1297).

### Estimating a Type A uncertainty

For $N \ge 2$ repeated measurements $x_i$ of the same quantity, the sample standard
deviation

$$
s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2}
$$

estimates the spread of a *single* reading, and the standard error of the mean

$$
\sigma_{\bar{x}} = \frac{s}{\sqrt{N}}
$$

is the standard uncertainty of the average *if the readings are independent
and the conditions stable*. The distinction matters: $s$ estimates the spread
of individual readings, while $\sigma_{\bar{x}}$ describes the precision of
their mean. Report the second when the mean is your result, but look at the
first — if $s$ is much larger than the instrument's resolution, something is
fluctuating and it is worth knowing what. Neither expression includes a
shared calibration error.

### Estimating a Type B uncertainty

Common cases:

:::{list-table}
:header-rows: 1

* - Source
  - Standard uncertainty
* - Digital display, step size $d$
  - $d/\sqrt{12} \approx 0.29\,d$ if rounding is the only effect and the
    unknown position within a step is modeled as uniform
* - Analog scale, division $D$
  - Estimate the reading limit from the actual scale and viewing conditions;
    do not assign a quarter division automatically
* - Manufacturer's spec "$\pm a$" as a bound, with no distribution stated
  - $a/\sqrt{3}$ if a uniform distribution over $\pm a$ is a reasonable
    model; record that assumption
* - Manufacturer's spec "$\pm a$ at 95% confidence"
  - Approximately $a/2$ if the specification uses a normal model; check its
    stated coverage factor when available
* - A quantity you can bound between $x_-$ and $x_+$ and know nothing else
  - $(x_+ - x_-)/\sqrt{12}$ if a uniform distribution over that interval is
    a reasonable model
:::

Combine *independent* Type A and Type B contributions in quadrature:
$\sigma^2 = \sigma_A^2 + \sigma_{B,1}^2 + \sigma_{B,2}^2 + \cdots$.
If components share a source, include their covariance instead.

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
The Michelson mirror displacement from two endpoint readings and the voltage
span between differently colored LEDs have this structure. When the
procedure permits, increase the measured mirror travel or wavelength span;
also check that added range does not introduce a larger systematic error.
:::

If the derivatives are unpleasant, estimate them numerically by perturbing
each input and recomputing the result. Add the resulting contributions in
quadrature only for independent inputs; retain covariance terms when inputs
are correlated. For a strongly nonlinear function or large uncertainties,
check the linear approximation with a simulation of the input distributions.

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
well pulls the fit harder than one you do not. Supply the $\sigma_i$ when you
have defensible uncertainty estimates; an unweighted fit treats the points
as having equal variance. Counts with widely different magnitudes, for
example, generally do not meet that assumption. This formula also assumes
independent $y_i$ errors and negligible uncertainty in $x_i$; revisit the fit
method if either assumption fails.

### Reading the fit

Three numbers come out, and all three matter.

**The parameters** $\hat\theta$ — the physics.

**Their estimated uncertainties**, the square roots of the diagonal of the
covariance matrix, $\sigma_{\theta_j} = \sqrt{C_{jj}}$, provided the fit model
and uncertainty assumptions are reasonable.

**The reduced chi-square**, $\chi^2_\nu = \chi^2_{\min}/\nu$ with
$\nu = N - p$ degrees of freedom for $p$ fitted parameters. It is a
self-consistency check on your uncertainty estimates:

- $\chi^2_\nu \approx 1$: the residual scatter is broadly compatible with the
  quoted uncertainties and model.
- $\chi^2_\nu \gg 1$: either the model is wrong or the uncertainties are
  underestimated; correlated points or outliers can also raise it. Look at
  the residuals for structure and check the uncertainty model.
- $\chi^2_\nu \ll 1$: the uncertainties may be overestimated, the data may be
  correlated, or the model may be too flexible.

For small $\nu$, this ratio fluctuates substantially even under a good model;
do not treat these descriptions as fixed pass/fail thresholds.

Always plot the residuals $(y_i - f(x_i;\hat\theta))/\sigma_i$ against $x_i$.
A fit is judged by its residuals, not by how good the curve looks on top of
the data.

### Correlation between parameters

The off-diagonal elements of $C$ are not decoration. In a straight-line fit
$y = mx + b$ over data far from the origin, $m$ and $b$ are strongly
anticorrelated, and ignoring that correlation can misstate how well you know
$f(x)$ at a particular $x$. When a derived quantity depends on
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
constants. Prefer fitting the exponential directly; if you linearize, weight
correctly and say in the report that you did. At low counts, the log transform
also distorts the error distribution, so a count-based likelihood may be more
appropriate.

For Poisson-distributed counts $N$, the uncertainty is $\sqrt{N}$ — see
[](#exp-counting-statistics) for why, and for the case $N = 0$, where
$\sqrt{N}$ is not usable.

## Comparing to an accepted value

Quote the discrepancy in units of the combined uncertainty:

$$
t = \frac{\left|x_{\text{meas}} - x_{\text{acc}}\right|}
         {\sqrt{\sigma_{\text{meas}}^2 + \sigma_{\text{acc}}^2}}.
$$

Treat $t$ as a standardized discrepancy when the two estimates are
independent, their quoted uncertainties are comparable standard
uncertainties, and a normal approximation is reasonable. A value near or
above 2 invites a closer look; a large value warrants investigation of the
model and uncertainty budget. It does not identify the cause by itself. If
the accepted-value uncertainty is negligible, say so and omit that term.
Never use percent
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
rescales the **parameter covariance** by the observed reduced chi-square.
The fit residuals and the reduced chi-square you calculate from the supplied
`sigma` do not change. Set it to `True` when the supplied values are
independently estimated standard uncertainties, so the returned parameter
uncertainties reflect their absolute scale. See the [SciPy `curve_fit`
documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html).
:::

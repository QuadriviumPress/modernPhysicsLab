---
title: The Speed of Light
short_title: 2. The Speed of Light
label: exp-speed-of-light
numbering:
  enumerator: "2.%s"
---

# Experiment 2 — The Speed of Light

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 2, *Special Relativity*
**Apparatus** Pulsed laser diode or fast LED, two photodiodes, ≥100 MHz oscilloscope, folded optical path
**You will measure** $c$ by time of flight, to $\sim1$–$3\%$
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure a nanosecond time interval with an oscilloscope, and state what
  limits the measurement.
- Extract a propagation speed from the *slope* of delay versus distance, and
  explain why this is better than dividing a single delay into a single
  distance.
- Distinguish the instrumental delays that cancel in a slope from those that
  do not.
- Explain what it means for $c$ to be a defined constant, and what is
  therefore actually being measured here.

## Textbook connection

Read §2.1–2.3. Einstein's second postulate makes $c$ the same in every
inertial frame; since 1983 the metre has been *defined* so that
$c = 299\,792\,458\ \text{m/s}$ exactly. You are therefore not measuring a
constant of nature this afternoon — you are calibrating your metre stick
against your oscilloscope. That is a slightly deflating way to put it, and it
is worth being clear-eyed about, because it is exactly the kind of
definitional shift that Chapter 2 argues relativity forced on physics.

## Theory

### Time of flight

Light emitted at time $t_0$ and detected after travelling a distance $L$
arrives at

$$
t = t_0 + \frac{L}{c} + \tau,
$$ (eq-sol-tof)

where $\tau$ lumps together every fixed delay in the system: the LED's turn-on
lag, the photodiode's response time, the amplifier, and the electrical length
of the cables. $\tau$ is of order tens of nanoseconds — comparable to or
larger than the flight time you are trying to measure — and you have no
reliable way to compute it.

The way out is not to measure $\tau$ but to *eliminate* it. Take the delay
$\Delta t$ at two or more path lengths $L$. Since $\tau$ does not depend on
$L$,

$$
\Delta t(L) = \frac{L}{c} + \tau
\qquad\Longrightarrow\qquad
\frac{d(\Delta t)}{dL} = \frac{1}{c}.
$$ (eq-sol-slope)

Fit a straight line to $\Delta t$ against $L$; the slope gives $c$ and the
intercept gives $\tau$, which you get for free and which is a useful check
that nothing is drifting.

This is a general and important technique: **when an unknown offset
contaminates a measurement, vary the quantity of interest and fit a slope.**
It reappears in Experiments 6, 8, and 13.

### What limits you

An oscilloscope of analogue bandwidth $B$ has a 10–90% rise time of about

$$
t_r \approx \frac{0.35}{B},
$$ (eq-sol-risetime)

so a $100\ \text{MHz}$ instrument smears every edge over roughly
$3.5\ \text{ns}$ — about a metre of light travel. This does *not* mean you
cannot do better than a metre. A smeared edge can still be *located* to a
fraction of its rise time, because averaging many acquisitions beats down the
noise on the edge and the scope interpolates between samples. In practice,
with 128-fold averaging and a stable trigger, locating an edge to $\sim0.2$–$0.5\ \text{ns}$
is achievable, which over a $10\ \text{m}$ path length change is a 1–2%
measurement of $c$.

The other contributors are: the sampling interval (use the fastest time base
that still shows both edges), trigger jitter (trigger on the *reference*
channel, which is bright and fast), and — the one students usually forget —
the unequal electrical lengths of the two BNC cables. Signal travels in RG-58
at about $0.66c$, so a $30\ \text{cm}$ cable mismatch is $1.5\ \text{ns}$,
which is a systematic error of the same size as your entire statistical
uncertainty. Measure the cables, or better, swap them and see if the answer
moves.

## Pre-lab

:::{exercise}
:label: q-sol-01

How long does light take to travel $1.00\ \text{m}$? $10.0\ \text{m}$? Express
both in nanoseconds. If your scope's fastest useful time base is
$5\ \text{ns/div}$ with ten divisions across the screen, what is the longest
path difference you can display on one screen without scrolling?
:::

:::{exercise}
:label: q-sol-02

Using [](#eq-sol-risetime), find the rise time of a $100\ \text{MHz}$ scope and
of a $200\ \text{MHz}$ scope. If two independent elements each contribute a
rise time, the total is $t_r = \sqrt{t_{r,1}^2 + t_{r,2}^2}$. Given a
photodiode with $t_r = 2\ \text{ns}$ and a $100\ \text{MHz}$ scope, what total
rise time do you expect to see on the screen?
:::

:::{exercise}
:label: q-sol-03

You will fit $\Delta t = L/c + \tau$ over path lengths from $2\ \text{m}$ to
$12\ \text{m}$. If each $\Delta t$ carries an uncertainty of $0.4\ \text{ns}$
and each $L$ an uncertainty of $5\ \text{mm}$, estimate the relative
uncertainty you expect in the fitted $c$. (A rough estimate is enough: compare
the timing uncertainty to the total spread in $\Delta t$ across your range.)
:::

:::{exercise}
:label: q-sol-04

Since 1983 the speed of light has been fixed by definition. Explain in two or
three sentences what quantity your measurement is therefore actually
determining, and why the experiment is still worth doing.
:::

## Apparatus

- Fast pulsed source: a laser diode module driven by a $\sim1\ \text{MHz}$
  square wave with a fast edge, or a red/IR LED driven hard by a MOSFET
  gate-driver. A microcontroller GPIO pin alone is too slow; use the driver.
- Function generator or microcontroller producing the drive pulse
- Two photodiodes with fast amplifiers (BPW34 or similar with a transimpedance
  stage; the kit boards on the bench are prewired)
- Oscilloscope, $\ge 100\ \text{MHz}$, with averaging
- Two front-surface mirrors on adjustable mounts, to fold the path
- Tape measure ($\pm 2\ \text{mm}$) and a target card
- Two BNC cables of *measured*, ideally equal, length

:::{danger}
If the source is a laser diode rather than an LED, the folded beam crosses the
room at head height. Mark the path, keep the room clear, and terminate the
beam on a block. See [](#lab-safety).
:::

## Procedure

### Part A — Setting up the two channels

1. Mount the source. Split a small fraction of its output onto the
   **reference** photodiode a few centimetres away — a glass slide at $45°$ is
   enough. This channel defines $t_0$ and removes any drift in the source's
   turn-on time.
2. Send the main beam across the room, fold it with the two mirrors, and bring
   it back onto the **signal** photodiode. Start with the shortest workable
   path, about $2\ \text{m}$ total.
3. Trigger the scope on the reference channel. Set both channels to the same
   vertical scale and DC coupling.
4. Turn on averaging (128 acquisitions is a good starting point) and watch the
   edges sharpen.

**[ ] Checkpoint 1.** Show the instructor two clean,
averaged edges with a stable trigger. If the signal edge is noisy, the beam is
not centred on the detector — walk the mirrors, do not turn up the gain.

### Part B — The delay measurement

5. Define your timing criterion *before* taking data and use it unchanged for
   every measurement. The 50%-amplitude crossing of the rising edge is a good
   choice; the peak is a bad one, because the two pulses have different shapes.
   Most scopes will do this automatically with a delay or "phase" measurement
   between channels.
6. Record $\Delta t$ and its scatter over several acquisitions.
7. Measure the total optical path $L$ from the source, via both mirrors, to
   the signal detector. Measure it with a tape, along the beam, and record the
   uncertainty. Do not forget the short leg from the beamsplitter to the
   reference detector — it enters $\tau$, so it must not change between runs.
8. Move one mirror to lengthen the path by roughly $1\ \text{m}$, realign onto
   the detector, and repeat. **Collect at least eight path lengths spanning as
   large a range as the room allows.**

:::{warning}
Every time you move a mirror you must re-centre the beam on the detector. A
beam that lands on the edge of the photodiode produces a smaller, slower pulse
whose 50% crossing is *later* — a systematic error that grows with path
length, which is exactly where it does the most damage. Re-peak the signal
amplitude after every move.
:::

### Part C — Controls

9. **Swap the two BNC cables** and repeat one measurement. Any shift is twice
   the cable-length mismatch; correct for it or fold it into the systematic
   uncertainty.
10. **Block the main beam** and confirm the signal channel goes flat. If it
    does not, you are picking up electrical crosstalk from the drive pulse,
    not light, and the whole measurement is invalid. Fix it with shielding or
    by moving the drive electronics.
11. If time allows, repeat one path length with the averaging turned off, to
    see what averaging bought you.

## Analysis

Fit $\Delta t = L/c + \tau$ with both parameters free.

```python
import numpy as np
from scipy.optimize import curve_fit

L   = np.array([...])          # total optical path, metres
sL  = np.array([...])          # uncertainty, metres
dt  = np.array([...])          # measured delay, seconds
sdt = np.array([...])          # uncertainty, seconds

model = lambda L, inv_c, tau: inv_c * L + tau
p0    = [1 / 3e8, 0.0]
popt, pcov = curve_fit(model, L, dt, p0=p0, sigma=sdt, absolute_sigma=True)

inv_c, tau = popt
s_inv_c    = np.sqrt(pcov[0, 0])
c, sc      = 1 / inv_c, s_inv_c / inv_c**2      # note the 1/x propagation
print(f"c   = {c:.4g} +/- {sc:.2g} m/s")
print(f"tau = {tau*1e9:.2f} ns")

resid = (dt - model(L, *popt)) / sdt
print(f"chi2/nu = {np.sum(resid**2) / (len(L) - 2):.2f}")
```

Note the propagation in the fourth-to-last line: the fit parameter is $1/c$,
so $\sigma_c = \sigma_{1/c}/(1/c)^2$. Fitting $1/c$ rather than $c$ keeps the
model linear, which makes the fit robust and the covariance matrix meaningful.

Because $L$ also carries uncertainty, check whether it matters: the effective
uncertainty on $\Delta t$ from a position error is $\sigma_L/c$. For
$\sigma_L = 5\ \text{mm}$ this is $17\ \text{ps}$, far below your timing
uncertainty — so position error is negligible here, and you should say so
rather than silently ignoring it.

Plot the residuals. A *curved* residual pattern means something depends on
path length that should not — almost always the beam-centring problem in the
warning above.

## Post-lab questions

:::{exercise}
:label: q-sol-05

Quote your $c$ with its uncertainty and compare it with the defined value in
units of $\sigma$. If your result disagrees, is the disagreement in the slope
or would it also show up as a bad $\chi^2_\nu$? What does each case imply?
:::

:::{exercise}
:label: q-sol-06

Your fitted $\tau$ has a physical meaning. Estimate independently what it
should be from the cable lengths ($v \approx 0.66c$ in RG-58) and the
photodiode rise times, and compare. Does your fit's intercept make sense?
:::

:::{exercise}
:label: q-sol-07

Suppose you had made a single measurement at $L = 12\ \text{m}$ and computed
$c = L/\Delta t$, ignoring $\tau$. Using your fitted $\tau$, how far off would
that answer have been, and in which direction? This is the point of the whole
slope method — state it in one sentence.
:::

:::{exercise}
:label: q-sol-08

Rømer inferred a finite speed of light in 1676 from the timing of Jupiter's
moon Io, using a baseline of the Earth's orbital diameter rather than a
laboratory. His result was about 25% low. Given that his *timing* was good to
minutes on a delay of about 16 minutes, what was almost certainly the limiting
error, and how does that compare with your own limiting error?
:::

:::{exercise}
:label: q-sol-09

Special relativity asserts that you would obtain the same $c$ if the source
were moving toward you at $0.5c$. Nothing in this experiment tests that.
Describe, qualitatively, an experiment that does — and note what kind of
source you would need.
:::

## Going further

- **Propagation speed in coaxial cable.** Send the same pulse down a long
  spool of RG-58 and measure the delay per metre. You should get
  $v \approx 0.66c$, and $v = c/\sqrt{\varepsilon_r}$ then gives you the
  dielectric constant of polyethylene. Same apparatus, one extra cable, ten
  minutes.
- **Speed of light in a medium.** Put a $1\ \text{m}$ tube of water in the
  beam path and measure the extra delay. Expect $n = 1.33$, so a
  $1.1\ \text{ns}$ shift — right at the edge of what you can resolve, which
  makes it a good exercise in whether you believe your own error bars.
- **Rømer's method, from your desk.** Public ephemerides give the eclipse
  times of Io over a year. Fitting the residual against Earth–Jupiter distance
  reproduces the 1676 measurement in an afternoon of Python and no apparatus
  at all.

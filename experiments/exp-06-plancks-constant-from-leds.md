---
title: Planck's Constant from Light-Emitting Diodes
short_title: 6. Planck's Constant from LEDs
label: exp-planck-leds
numbering:
  enumerator: "6.%s"
---

# Experiment 6 — Planck's Constant from Light-Emitting Diodes

:::{admonition} At a glance
:class: seealso

**Accompanies** Chapter 6, *Particle Properties of Waves*
**Apparatus** Set of LEDs spanning the visible, spectrometer kit, microcontroller or bench supply, tungsten lamp
**You will measure** $h$ to $\sim10\%$, and the Stefan–Boltzmann exponent
**Report** Short
:::

## Objectives

By the end of this experiment you should be able to:

- Measure an LED's turn-on voltage by extrapolating its $I$–$V$ curve, and
  explain why extrapolation is necessary.
- Measure an LED's emission spectrum and use its peak rather than its nominal
  colour.
- Extract Planck's constant from the slope of turn-on voltage against inverse
  wavelength, and identify honestly the systematic that limits the result.
- Determine the exponent in the Stefan–Boltzmann law from a tungsten lamp
  operated over a wide range of temperature.

## Textbook connection

Read §6.1–6.3. Chapter 6 introduces $h$ through blackbody radiation and the
photoelectric effect. The photoelectric apparatus that this laboratory used
for many years is no longer serviceable, and this experiment replaces it with
two measurements that between them make the same point: light comes in quanta
of energy $hf$, and the classical picture of thermal radiation fails without
that assumption.

An LED is, in a real sense, a photoelectric effect run backwards. In the
photoelectric effect a photon of energy $hf$ liberates an electron against a
work function; in an LED an electron falls across a band gap and emits a
photon of energy $hf \approx E_g$. Both experiments measure the same constant
by relating a voltage to a frequency.

## Theory

### The LED as a quantum energy converter

An electron crossing the junction of a forward-biased LED falls through an
energy gap $E_g$ and can emit a single photon:

$$
eV \approx E_g = hf = \frac{hc}{\lambda} .
$$ (eq-led-basic)

Below a threshold voltage $V_{\text{on}} \approx E_g/e$ the diode carries
almost no current and emits no light; above it, current rises very steeply.
Measuring $V_{\text{on}}$ for LEDs of several colours and plotting against
$1/\lambda$ should give a straight line of slope $hc/e$:

$$
V_{\text{on}} = \frac{hc}{e}\cdot\frac{1}{\lambda} + V_{\text{offset}} .
$$ (eq-led-fit)

### Why this is honest but imperfect

[](#eq-led-basic) is an approximation, and a report that does not say so is
incomplete. Three effects matter:

**Thermal tail.** The diode current is $I = I_s\left(e^{eV/nk_BT} - 1\right)$,
which is never exactly zero. There is no true threshold; $V_{\text{on}}$ is
whatever your extrapolation procedure says it is, so the procedure must be
stated and used identically for every LED. At room temperature $k_BT/e = 26\ \text{mV}$,
which sets the scale of the ambiguity.

**Series resistance.** At high current the measured voltage includes $IR_s$
across the bulk semiconductor and the leads, bending the $I$–$V$ curve. This
is why you extrapolate the *linear* high-current region back to $I = 0$ rather
than reading a voltage at some arbitrary current.

**The gap is not the photon energy.** Carriers are thermally distributed
within the bands, so emission peaks slightly *below* $E_g$ and the emitted
spectrum has a width of order $k_BT$. Different LED chemistries — AlGaInP for
red and amber, InGaN for green, blue, and white — have different band
structures and different amounts of this offset.

The consequence: expect a result for $h$ within roughly 10–20% of the accepted
value, with a nonzero intercept in [](#eq-led-fit). **The intercept is the
interesting part of the experiment**, because it is where all of the above
physics lives, and a report that reports the slope and ignores the intercept
has missed it.

### The Stefan–Boltzmann law

A tungsten filament at temperature $T$ radiates

$$
P = \varepsilon\sigma A\left(T^4 - T_{\text{amb}}^4\right) \approx \varepsilon\sigma A\,T^4
$$ (eq-sb-law)

for $T \gg T_{\text{amb}}$, which for a filament above $1000\ \text{K}$ is an
excellent approximation. You cannot easily measure $\varepsilon$ or $A$, but
you can measure the *exponent*, by measuring the electrical power dissipated
(which in steady state equals the radiated power, once conduction down the
leads is negligible) and the temperature.

You get the temperature from the filament's own resistance. For tungsten, over
$300$–$3000\ \text{K}$,

$$
\frac{R(T)}{R_0} \approx \left(\frac{T}{T_0}\right)^{1.20},
\qquad T_0 = 300\ \text{K},
$$ (eq-tungsten)

which reproduces the tabulated resistivity to about 5% across that range. So

$$
P = kT^{n} \quad\Longrightarrow\quad \ln P = n\ln T + \ln k ,
$$ (eq-sb-fit)

and a straight-line fit gives $n$, which should come out near 4.

## Pre-lab

:::{exercise}
:label: q-planck-01

Convert: what photon energy in eV corresponds to $\lambda = 470\ \text{nm}$
(blue), $525\ \text{nm}$ (green), $590\ \text{nm}$ (amber), and $630\ \text{nm}$
(red)? Use $hc = 1240\ \text{eV}\cdot\text{nm}$. What turn-on voltages does
[](#eq-led-basic) predict?
:::

:::{exercise}
:label: q-planck-02

Sketch the expected plot of $V_{\text{on}}$ against $1/\lambda$ for those four
LEDs, and mark the slope you would need in order to recover the accepted $h$.
Give the slope in $\text{V}\cdot\text{nm}$.
:::

:::{exercise}
:label: q-planck-03

The diode equation gives $I = I_s(e^{eV/nk_BT}-1)$ with ideality factor
$n \approx 2$ for an LED. By what factor does the current change for a
$100\ \text{mV}$ increase in $V$ at room temperature? Use this to explain why
"the voltage at which the LED first visibly glows" is a bad definition of
$V_{\text{on}}$ — and estimate how much it would depend on how dark the room is.
:::

:::{exercise}
:label: q-planck-04

A lamp filament at $2500\ \text{K}$ has resistance $R$. Using
[](#eq-tungsten), what is $R/R_0$? If the cold resistance is $0.9\ \Omega$,
what current flows at $6\ \text{V}$, and what current flows at the instant the
lamp is switched on? (This is why filament lamps fail at switch-on.)
:::

## Apparatus

- At least five LEDs spanning the visible and near infrared: e.g. $\sim940$,
  $630$, $590$, $525$, $470$, $405\ \text{nm}$. **Do not use a white LED** —
  it is a blue LED plus a phosphor and its spectrum is meaningless here.
- Variable DC supply $0$–$5\ \text{V}$, or a microcontroller DAC/PWM with an
  RC filter
- Two digital multimeters, or a microcontroller with two ADC channels and a
  known current-sense resistor
- $100\ \Omega$ series resistor
- Thorlabs EDU-SPEA1/SPEB1 spectrometer kit, or a compact USB spectrometer
- Small tungsten filament lamp (a $6\ \text{V}$ automotive or torch bulb) with
  a clear envelope
- Bench supply capable of $0$–$8\ \text{V}$ at $2\ \text{A}$, with a four-wire
  or separate voltage-sense connection at the lamp terminals

:::{danger}
The filament reaches over $2500\ \text{K}$ and the envelope stays hot for
minutes. Use the ceramic tile. Do not exceed the lamp's rated voltage.
Violet and near-UV LEDs at $405\ \text{nm}$ are bright and should not be
viewed directly.
:::

```{figure} ../images/exp06-led-planck-schematic.svg
:label: fig:exp06-planck
:alt: Panel (a), an LED forward-biased through a series resistor with an ammeter and a voltmeter reading its turn-on voltage. Panel (b), a tungsten lamp shining through a slit and grating spectrometer onto a linear detector array.

Two independent routes to $h$. (a) The LED turn-on voltage, read from a simple current-limited circuit. (b) The tungsten filament's continuum spectrum, resolved by the spectrometer kit.
```

## Procedure

### Part A — Emission spectra

1. Drive each LED at a modest current ($\sim5\ \text{mA}$) and record its
   emission spectrum with the spectrometer kit. Take a dark spectrum first and
   subtract it.
2. For each LED, find the peak wavelength $\lambda_p$ and the full width at
   half maximum. Record both — the FWHM is a direct measurement of the thermal
   energy spread and you will use it in the discussion.
3. Compare $\lambda_p$ with the nominal colour printed on the bag. They can
   differ by $10$–$20\ \text{nm}$, which is a 2–4% systematic on $h$ if you
   use the nominal value. **Use your measured peak.**

**[ ] Checkpoint 1.** Show the instructor your spectra
with the peaks marked. A spectrum with a flat top is saturated; reduce the
integration time and retake it.

### Part B — Turn-on voltages

4. Wire the LED in series with the $100\ \Omega$ resistor across the supply.
   Measure the voltage **across the LED alone** (not across the pair) and the
   current through the resistor.
5. Sweep the supply upward and record $(V, I)$ pairs — at least 25 points,
   concentrated where the current is rising steeply. Go up to about
   $15\ \text{mA}$ and no higher.
6. **Use the same current range for every LED.** The extrapolation is only
   comparable across LEDs if the procedure is identical.
7. Repeat for all LEDs.

:::{tip} Automate it
A microcontroller can sweep a DAC or filtered PWM output, read the two
voltages, and print CSV, giving 200 points in ten seconds and letting you
repeat the whole sweep five times per LED for a real statistical uncertainty.
This is a better use of the period than turning a knob.
:::

### Part C — The tungsten lamp

8. Measure the cold resistance $R_0$ of the lamp with a four-wire ohmmeter, or
   from a low-current $(V,I)$ measurement at a current small enough not to
   heat the filament. Record the ambient temperature.
9. Increase the lamp voltage in steps up to the rated value, recording $V$ and
   $I$ at each step. **Wait for thermal equilibrium** — ten seconds or so — at
   each point, and sense the voltage at the lamp terminals, not at the supply,
   or the lead resistance will corrupt $R$.
10. Take at least fifteen points, and take them over as wide a range as the
    lamp tolerates, since you are fitting an exponent.

## Analysis

### Turn-on voltage by extrapolation

For each LED, fit a straight line to the steep, nearly linear high-current
portion of the $I$–$V$ curve and extrapolate to $I = 0$.

```python
import numpy as np
from scipy.optimize import curve_fit

# Select the linear region reproducibly: use the same current window for all.
sel = (I > 5e-3) & (I < 15e-3)
line = lambda V, m, b: m * V + b
popt, pcov = curve_fit(line, V[sel], I[sel], sigma=sI[sel], absolute_sigma=True)
m, b   = popt
V_on   = -b / m
# full covariance propagation: V_on depends on both parameters
J      = np.array([b / m**2, -1 / m])
sV_on  = np.sqrt(J @ pcov @ J)
```

State your current window in the report. Then repeat the whole analysis with a
*different* window (say $8$–$20\ \text{mA}$) and quote the change in $h$ as a
systematic uncertainty. This is the honest way to handle a procedure-dependent
definition, and it is worth more credit than pretending the ambiguity is not
there.

### Planck's constant

```python
inv_lam  = 1 / lam_peak                       # 1/m
popt, pcov = curve_fit(lambda x, s, c: s * x + c, inv_lam, V_on,
                       sigma=sV_on, absolute_sigma=True)
slope, offset = popt
e = 1.602176634e-19
c_light = 299792458.0
h  = slope * e / c_light
sh = np.sqrt(pcov[0, 0]) * e / c_light
```

Report $h$, its statistical uncertainty, its systematic uncertainty from the
window choice, and the intercept with its uncertainty.

### Stefan–Boltzmann

```python
R  = V / I
T  = 300.0 * (R / R0) ** (1 / 1.20)
P  = V * I
fit = np.polyfit(np.log(T), np.log(P), 1)     # start here, then do it properly
```

The `polyfit` line is a starting point only: do the fit with proper weights,
propagating $\sigma_V$ and $\sigma_I$ into $\sigma_P/P$ and $\sigma_T/T$, and
report $\chi^2_\nu$. Note that $T$ carries uncertainty too, so strictly this
is an errors-in-both-variables problem; the honest minimum is to check whether
$\sigma_T/T$ contributes comparably to $\sigma_P/P$ and say so.

Exclude the lowest-temperature points from the fit and see whether $n$ moves.
It usually rises toward 4, because at low filament temperature conduction down
the leads carries a larger fraction of the power and is not $\propto T^4$.
That trend is a real physical finding and belongs in the discussion.

## Post-lab questions

:::{exercise}
:label: q-planck-05

Report $h$ with statistical and systematic uncertainties, and compare with
$6.62607015\times10^{-34}\ \text{J}\cdot\text{s}$ in units of $\sigma$. If the
disagreement exceeds your uncertainty, is your result high or low, and does
the sign match what the theory section predicts?
:::

:::{exercise}
:label: q-planck-06

Your fitted intercept in [](#eq-led-fit) should not be zero. Report it in
volts and interpret it: what physical effects does it absorb, and what sign
would each of them produce?
:::

:::{exercise}
:label: q-planck-07

You measured the FWHM of each LED's emission spectrum. Convert one of them
into an energy width in eV and compare with $k_BT$ at room temperature
($0.0257\ \text{eV}$). Comment on the agreement, and on what a much broader
line would imply.
:::

:::{exercise}
:label: q-planck-08

Report the Stefan–Boltzmann exponent $n$ with its uncertainty. If it differs
from 4, name the two most likely causes and say which direction each pushes
$n$. Would a filament in vacuum, in an evacuated envelope, behave differently
from one in an inert fill gas?
:::

:::{exercise}
:label: q-planck-09

Use Wien's displacement law with your highest filament temperature to find the
peak emission wavelength. In what part of the spectrum does an incandescent
lamp put most of its power? Compute the fraction of the total radiated power
falling in the visible ($400$–$700\ \text{nm}$) by integrating Planck's law
numerically, and comment on incandescent lamps as lighting.
:::

:::{exercise}
:label: q-planck-10

Explain, in three or four sentences, how this measurement is and is not a
substitute for a photoelectric-effect measurement of $h$. What does the
photoelectric experiment establish that the LED experiment does not?
:::

## Going further

- **Temperature dependence of $V_{\text{on}}$.** Cool an LED in an ice bath
  and repeat. The band gap and the thermal tail both shift, and the turn-on
  voltage moves by a few millivolts per kelvin. Measuring $dV_{\text{on}}/dT$
  turns the LED into a thermometer, and it is how many cryogenic diode
  thermometers work.
- **Numerically integrate Planck's law.** Compute the visible fraction of a
  blackbody's output as a function of $T$, find the temperature that maximizes
  it, and compare with the melting point of tungsten ($3695\ \text{K}$). This
  is the entire engineering argument for the incandescent lamp's replacement.
- **The infrared LED.** A $940\ \text{nm}$ LED extends your $1/\lambda$ range
  by a useful amount, and because it lies furthest from the visible LEDs it
  carries a great deal of leverage on the fitted slope. Measuring its spectrum
  requires a spectrometer that reaches into the near infrared — check the
  kit's range before you trust the peak.

---
title: "Instructor Notes — Experiment 13: Counting Statistics and Half-Life"
short_title: 13. Counting Statistics (instructor)
label: inst-exp-13
---

# Instructor Notes — Experiment 13

## Prep (45 min, plus source paperwork)

- Check the $^{137}$Cs/$^{137m}$Ba generator's elution performance a day
  ahead. Columns degrade; a weak elution ruins the half-life measurement and
  there is no recovering the period.
- Make up fresh eluting solution, and lay out planchets, gloves, tray, and
  the disposal container.
- Confirm the counters can do programmed repeat runs and log them. Doing 300
  one-second runs by stopwatch is not feasible; if the counters cannot repeat,
  use a microcontroller with a pulse input instead.
- Look up and post the GM tube's dead time from its data sheet.
- Verify the lead and aluminium absorber sets and their thicknesses.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| GM counter with repeat/log mode | ✓ | Essential for Part A |
| $^{137}$Cs/$^{137m}$Ba isotope generator | ✓ | Check the column annually |
| Eluting solution, planchets | consumable | |
| Sealed $^{137}$Cs button source | ✓ | For Part C |
| Lead sheets 1–10 mm, Al absorbers | ✓ | |
| Collimator | build | Improves the narrow-beam approximation a lot |

## Expected results

**Part A.** Variance-to-mean ratio consistent with 1. For $n = 300$ samples
the ratio's standard deviation is $\sqrt{2/299} = 0.082$, so a ratio of
$0.95$–$1.05$ is unremarkable and $1.3$ is not. At $\mu \approx 3$ the Poisson
fit should pass and the Gaussian fail; at $\mu \approx 30$ both should pass.
That contrast is the whole point of taking two data sets.

**Part B.** $^{137m}$Ba: $T_{1/2} = 2.552\ \text{min} = 153.1\ \text{s}$,
$\lambda = 4.527\times10^{-3}\ \text{s}^{-1}$, $E_\gamma = 661.7\ \text{keV}$.

From a starting rate of $1500\ \text{s}^{-1}$: $386\ \text{s}^{-1}$ at 5 min,
$99\ \text{s}^{-1}$ at 10 min, $25.5\ \text{s}^{-1}$ at 15 min. It reaches a
$0.5\ \text{s}^{-1}$ background only at about **29.5 min**, so a 15-minute run
does *not* determine the floor — hold the background fixed at its separately
measured value. Groups that float it will get $T_{1/2}$ biased high.

Dead time at $100\ \mu\text{s}$: $4.8\%$ loss at $500\ \text{s}^{-1}$,
$16.7\%$ at $2000\ \text{s}^{-1}$; the correction exceeds $10\%$ above about
$1100\ \text{s}^{-1}$. It therefore matters for the first minute or two of the
decay curve and nowhere else — which is exactly where the fit has the most
leverage.

Typical student result: $2.5$–$2.7\ \text{min}$. Groups that skip the
mid-interval correction come in about $3\%$ high on $\lambda$.

**Part C.** NIST mass attenuation at $662\ \text{keV}$: lead
$\approx0.111\ \text{cm}^2/\text{g}$ ($\rho = 11.35$, HVL $5.5\ \text{mm}$);
aluminium $\approx0.0745\ \text{cm}^2/\text{g}$ ($\rho = 2.70$, HVL
$34\ \text{mm}$). The *linear* coefficients differ by a factor of $6.3$; the
*mass* coefficients by only $1.5$ — that near-equality is the Compton
signature and is question 8's target.

Uncollimated geometries typically measure an HVL $20$–$40\%$ too large because
of buildup. Expect this and reward groups that diagnose it correctly.

Compton edge for $662\ \text{keV}$: $478\ \text{keV}$ (for the going-further
section).

## Where groups get stuck

1. **Fixed counting time across the decay curve or the absorption curve.**
   Same lesson as Week 3; some groups still need it twice.
2. **Floating the background in the half-life fit.** Covered above; watch for
   it in the code.
3. **Using interval start times instead of midpoints.** A $3\%$ bias.
4. **$\sqrt{N}$ at $N = 0$.** Question 6 exists for this. The standard answer
   is the $68\%$ one-sided Poisson upper limit of about $1.15$ counts (or
   $3.0$ at $95\%$).
5. **Missing the elution time**, so $t = 0$ is unknown. It only shifts $N_0$,
   not $\lambda$ — a good thing to have them realize rather than panic about.

## Grading notes

- Both distributions must be compared at $\mu \approx 3$, on one figure. A
  report showing only the Poisson comparison has skipped the experiment's
  actual question.
- The dead-time and midpoint corrections should each be quantified, with a
  statement of whether they mattered.
- Question 9 (buildup) requires a *sign* — the measured $\mu$ is too small —
  and a proposed test (better collimation, or varying the source–detector
  distance).

## Safety

The eluate is unsealed activity. Gloves, tray, no touching the planchet face,
disposal as directed. It is essentially gone in half an hour, but supervise
the elution itself.

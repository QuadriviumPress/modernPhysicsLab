---
title: "Instructor Notes — Experiment 8: Tunneling by FTIR"
short_title: 8. FTIR Tunneling (instructor)
label: inst-exp-08
---

# Instructor Notes — Experiment 8

**This is the most technically demanding experiment in the manual.** The
optical measurement is genuinely difficult — sub-micrometre gaps, three
decades of dynamic range, and a dust-sensitive contact. The computational Part
D is designed to stand alone, so a group whose optics fail still has a report
to write. Say this to them at the start so they do not panic.

If a microwave kit ($\sim3\ \text{cm}$, paraffin or acrylic prisms) can be
borrowed, running the microwave version instead — or alongside — is
substantially easier and arguably better physics teaching. Consider it.

## Prep (1.5 h)

- Select a plano-convex lens with the longest available $R$ ($1000\ \text{mm}$
  or more). Short-$R$ lenses compress the whole interesting region into a
  quarter of a millimetre.
- Clean prism and lens with lens tissue and isopropanol immediately before the
  period, and again between groups. **Dust is the dominant failure mode.**
- Build a gentle, reproducible clamp — a spring-loaded mount is far better
  than a screw, which students overtighten and which flattens the contact.
- Set up baffles to get the stray floor below $10^{-3}$ of $I_0$. Without
  three decades the exponential fit has nothing to work with.
- Calibrate the USB microscope against a stage micrometer and tape the scale
  factor to it.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Right-angle prism, N-BK7 | ✓ | |
| Plano-convex lens R ≥ 1000 mm | ? | ~$40 |
| USB microscope, calibrated | ? | ~$60 |
| Spring clamp mount | build | |
| 650 nm laser + expander | ✓ | |
| Lens tissue, isopropanol | consumable | |

## Expected results

- $\theta_c = 41.14°$ for $n = 1.52$.
- At $\theta = 45°$, $\lambda = 650\ \text{nm}$: $\kappa = 3.81\times10^{6}\ \text{m}^{-1}$,
  amplitude decay length $1/\kappa = 263\ \text{nm}$, intensity decay length
  $1/2\kappa = 131\ \text{nm}$.
- With $R = 1000\ \text{mm}$: gaps of $100$, $250$, $500$, $1000\ \text{nm}$
  at radii $0.447$, $0.707$, $1.000$, $1.414\ \text{mm}$. Three decades of
  intensity span about $900\ \text{nm}$ of gap.
- Typical fitted $\kappa$: within $10$–$30\%$ of prediction, usually
  reading *too small* (too slow a decay) because of a residual gap at contact
  and stray light. Both push the same way; question 5 asks them to work this
  out.
- Quantum companion, $E = 1\ \text{eV}$, $V_0 = 5\ \text{eV}$:
  $\kappa_q = 1.02\times10^{10}\ \text{m}^{-1}$; $T = 0.303$, $0.042$,
  $9.1\times10^{-5}$ at $L = 0.1$, $0.2$, $0.5\ \text{nm}$. The factor per
  $0.1\ \text{nm}$ is $\approx0.13$, i.e. nearly an order of magnitude — the
  STM answer.

## Where groups get stuck

1. **Dust at the contact point.** Symptom: the transmission does not saturate
   at small $r$. Clean and re-contact; do not let them fit around it.
2. **Overtightening.** Flattens the contact and invalidates
   $d = r^2/2R$ near the centre. The two-pressure comparison in step 8 is
   there to expose this — make sure they do it.
3. **Uncalibrated magnification.** They trust the microscope's label. Insist
   on the stage micrometer.
4. **Fitting in log space unweighted.** Standard error; see the front matter.
5. **Running out of period.** Prioritize Parts A, C, D; Part B (Newton's
   rings for $R$) can use the catalogue value if time is short, with the
   uncertainty inflated accordingly.

## Grading notes

- The correspondence table (question 4) should be exact and term-by-term.
- Question 9 — a feature of the quantum problem with no optical analogue — is
  the discriminating question. Good answers: probability interpretation and
  normalization of $\psi$; particle number conservation versus energy flux;
  the fact that a single quantum either tunnels or does not, whereas the
  optical field always splits.
- The Part D above-barrier resonances ($T = 1$ at certain $E > V_0$) are worth
  a sentence and few students volunteer it.

## Safety

Class 2 laser with multiple prism reflections. Standard.

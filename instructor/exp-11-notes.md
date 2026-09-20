---
title: "Instructor Notes — Experiment 11: Alkali Spectra"
short_title: 11. Alkali Spectra (instructor)
label: inst-exp-11
---

# Instructor Notes — Experiment 11

This is the replacement for the retired Moseley/X-ray experiment. Both measure
screening of the nuclear charge; this one does it from the valence side.
Question 10 makes the connection explicit and is worth teaching from.

## Prep (30 min)

- **Turn the sodium lamps on well before the period.** A cold Na lamp emits
  mostly from the neon starter gas and looks red-orange; it takes 10–15
  minutes to come up. Groups that measure a cold lamp get nothing.
- Have students pull their NIST ASD tables in the pre-lab, and check them at
  the door. A group without the table will spend the period guessing at
  assignments.
- Verify each spectrometer can resolve the mercury yellow doublet
  ($576.96$/$579.07\ \text{nm}$, $\Delta\lambda = 2.11\ \text{nm}$) before the
  period. This is Checkpoint 1 and it is a genuine gate — an instrument that
  fails it will not resolve the D lines.
- Put out ND filters. The D lines will saturate anything set correctly for
  the weaker series members.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Sodium lamp or Na spectral tube | ✓ | Long warm-up |
| Mercury, helium lamps | ✓ | |
| High-resolution grating spectrometer | ✓ | |
| ND filters | ✓ | |
| Potassium / lithium lamps | ? | Optional Part D |

## Expected results

- Sodium D: $588.995$ and $589.592\ \text{nm}$;
  $\Delta\lambda = 0.597\ \text{nm}$, $\Delta\tilde\nu = 17.19\ \text{cm}^{-1}$,
  $\Delta E = 2.13\ \text{meV}$. Required resolving power: $987$.
- Quantum defects (accepted): $\delta_{3s} = 1.373$, $\delta_{3p} = 0.883$,
  $\delta_{3d} = 0.010$.
- Sensitivity check for question 1: with $\delta_p = 0.883$ fixed,
  $\delta_s = 1.373 \to 589.3\ \text{nm}$; $1.35 \to 632.0\ \text{nm}$;
  $1.30 \to 741.5\ \text{nm}$. A change of $0.02$ in the defect moves the line
  by $40\ \text{nm}$. Students are usually startled by this, which is the
  point — quantum defects must be known to three decimals to be useful.
- Ionization energy from $n=3$, $\delta_s = 1.373$: $5.140\ \text{eV}$
  (accepted $5.139\ \text{eV}$). Treating sodium as hydrogenic with $n=3$
  gives $1.512\ \text{eV}$ — a factor of 3.4 out, which is question 2's point.
- $Z_{\text{eff}} = n/(n-\delta)$: $1.844$ for $3s$, $1.417$ for $3p$,
  $1.003$ for $3d$. The $3d$ result being essentially 1 is the striking one.
- Potassium principal doublet: $766.49$/$769.90\ \text{nm}$,
  $57.8\ \text{cm}^{-1}$ — a factor of $3.4$ above sodium's $17.2$. A naive
  $Z_{\text{eff}}^4$ scaling with $Z_{\text{eff}}\propto Z$ would predict far
  more; question 9 is about why the rule is crude.
- Typical student defects: $\delta_s$ and $\delta_p$ to $\pm0.02$ if they
  measure at least two series; $\delta_d$ poorly constrained.

## Where groups get stuck

1. **Cold sodium lamp.** Address it before the period, not during.
2. **Only measuring the D lines.** The D lines alone constrain only the
   *combination* $\delta_s - \delta_p$; a second series member is required to
   separate them. Make sure they find at least two more lines, and make sure
   the report acknowledges the degeneracy if they did not.
3. **Saturating on the D lines.** ND filters.
4. **Forced assignments.** Encourage "unassigned" over a wrong assignment;
   grade it that way.
5. **Propagating the doublet splitting as a product rather than a
   difference.** The relative uncertainty on $\Delta\lambda$ is much worse
   than on either line; see the difference trap in the front matter.

## Grading notes

- The physical explanation of $\delta_s > \delta_p > \delta_d$ (penetration
  versus the centrifugal barrier) is the core conceptual content.
- Look for the covariance discussion: which parameters are individually
  determined and which only in combination.
- Question 8 connects back to Experiment 9's symmetry argument — reward
  students who make the link explicitly.

## Safety

Kilovolt supplies, hot lamps. Sodium lamps stay hot a long time.

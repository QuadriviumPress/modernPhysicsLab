---
title: "Instructor Notes — Experiment 4: Interference of Light"
short_title: 4. Interference (instructor)
label: inst-exp-04
---

# Instructor Notes — Experiment 4

**Full-report week.** Budget grading time accordingly, and remind students in
Week 3 that the report is due in two weeks, not one.

## Prep (45 min)

- Label the "unknown" slit slides and keep a private key. Rotate which slide
  is unknown between sections.
- If using phone cameras, walk through disabling HDR, auto-exposure, and
  "scene optimization" once, at the board. Otherwise half the class returns
  with tone-mapped images and unusable intensity data.
- Clean a stock of microscope slides and put out fresh hairs, foil strips, and
  binder clips for Part D.
- Verify the machine-vision cameras' pixel pitch and write it on each.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| 650 nm diode module | ✓ | |
| Multiple-slit slide set | ✓ | Cornell/Pasco style |
| Optical rail, 2 m | ✓ | |
| USB machine-vision camera, lens removed | ? | ~$150; much better than phones |
| Microscope slides, binder clips | consumable | |
| Micrometer | ✓ | For the hair cross-check |

## Expected results

- $d = 0.25\ \text{mm}$, $L = 2.00\ \text{m}$, $\lambda = 650\ \text{nm}$:
  $\Delta y = 5.2\ \text{mm}$. Easily visible and easily measured.
- $d/a = 250/40 = 6.25$ for a typical pair, so about 11–12 interference
  maxima in the central envelope, with orders $\pm6$ suppressed near the
  envelope zero. Encourage counting before fitting.
- Air wedge with a $70\ \mu\text{m}$ hair: $N \approx 215$ dark fringes over
  the wedge length. At $\ell = 4\ \text{cm}$ that is $0.19\ \text{mm}$
  spacing — too fine to count by eye, which is why they photograph and count
  in software. Some groups will discover this the hard way; that is fine.
- Hair diameters: $50$–$100\ \mu\text{m}$; the micrometer typically reads
  $5$–$15\%$ *lower* because it compresses. This discrepancy is a feature —
  question 9 is about it.
- Fitted $a$ and $d$ typically within $5\%$ and $2\%$ of nominal
  respectively; $d$ is always better determined.

## Where groups get stuck

1. **Saturated images.** Ruins the visibility and the envelope fit. Check
   histograms at Checkpoint 1.
2. **`np.sinc` normalization.** Produces $a$ wrong by $\pi$. The warning is in
   the handout; expect to repeat it verbally.
3. **Nonlinear fit settling one fringe over.** Seeding from Part A fixes it.
4. **Measuring $L$ from the laser instead of the slit.** A $10\ \text{cm}$
   error at $L = 2\ \text{m}$ is a 5% bias in $d$.
5. **Part E (coherence) skipped for time.** Acceptable if Parts A–D are
   complete; note it in the grade rather than penalizing heavily.

## Grading notes

Full-report criteria apply. Specifically look for:

- Both routes to $\lambda/d$ (varying $L$ and varying $d$) done and compared.
- Residuals from the two-slit fit shown, with a physical explanation attempted
  for their structure. Real data always show structure here.
- The hair measured two ways, with the discrepancy discussed rather than
  averaged away.
- Question 10 (looking ahead to Week 7) answered thoughtfully — it is worth
  reading these before you teach Week 7.

## Safety

Glass slides are unintended beamsplitters. Have groups map the reflections
from the wedge assembly before powering up.

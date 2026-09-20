---
title: "Instructor Notes — Experiment 14: Cosmic-Ray Muon Telescope"
short_title: 14. Muon Telescope (instructor)
label: inst-exp-14
---

# Instructor Notes — Experiment 14

**Full-report week, and the one experiment that cannot be done in a single
period.** Plan for it from Week 12.

## Prep (4 h the first year, 30 min thereafter)

- **Build the coincidence unit once and keep it.** Two GM tubes, each pulse
  taken through a limiting resistor and a clamp into a comparator or Schmitt
  input on a microcontroller, which timestamps edges and prints CSV. Test it
  on the bench with a signal generator before it ever sees a tube.
- Mount the tubes rigidly in a frame that can be set to measured zenith
  angles *without changing their separation*. This rigidity is what makes the
  acceptance angle-independent, and a floppy frame invalidates the whole
  angular measurement.
- Measure and record each tube's active area and the separation. These are the
  only quantities the absolute flux depends on, so measure them well.
- **Start the apparatus running in Week 12.** Set it vertical and let it
  accumulate. Arrange a rota for changing the zenith angle daily. A period's
  worth of counting gives $\sim15\%$; a week gives $\sim3\%$.

## Bill of materials

| Item | Have | Note |
|---|---|---|
| Two GM tubes, matched HV | ✓ | Pancake tubes if available — larger area |
| Microcontroller + interface board | build | ~$20; the interface is the work |
| Rigid rotating frame with angle scale | build | ~$40 |
| Lead sheets | ✓ | For the momentum-spectrum extension |
| Long-run logging (laptop or SD card) | ✓ | |

## Expected results

- $c\tau_0 = 659\ \text{m}$ for the muon ($\tau_0 = 2.197\ \mu\text{s}$).
- From $15\ \text{km}$: $22.8$ lifetimes, survival $1.3\times10^{-10}$ without
  dilation.
- At $\gamma = 20$: decay length $13.2\ \text{km}$, survival $0.32$ — a factor
  of $2.5\times10^{9}$ improvement. This ratio is the headline number.
- A $4\ \text{GeV}$ muon: $\gamma = 37.9$, $\beta = 0.999651$,
  $1-\beta = 3.5\times10^{-4}$.
- Geometry: $A = 10\ \text{cm}^2$, $d = 10\ \text{cm}$ gives
  $\Omega \approx 0.10\ \text{sr}$ and a coincidence rate of about
  $1\ \text{min}^{-1}$. So $100$ minutes for $10\%$ statistics at one angle —
  hence the multi-day plan.
- Accidentals with $R_1 = R_2 = 0.5\ \text{s}^{-1}$ and
  $\tau_{\text{coinc}} = 1\ \mu\text{s}$: $5\times10^{-7}\ \text{s}^{-1}
  = 3\times10^{-5}\ \text{min}^{-1}$ — utterly negligible, by about four
  orders of magnitude. Part B step 5 should show the accidental rate rising
  linearly with the window while the true rate stays flat.
- Fitted exponent: $n = 1.8$–$2.4$ is a good result with a week of data;
  a single period will typically give $n = 2 \pm 1$, which is honest and
  should be graded as such.
- Vertical intensity: accepted
  $\approx1\ \text{cm}^{-2}\text{min}^{-1}\text{sr}^{-1}$. Student results
  within a factor of $1.5$ are good; the acceptance calculation, not the
  counting, is usually the limiting uncertainty.
- **Minimum $\gamma$ bound:** solving
  $e^{-h/(\gamma\beta c\tau_0)} \ge 10^{-2}$ for $h = 15\ \text{km}$ gives
  $\gamma \ge 5.05$, i.e. $E \ge 0.53\ \text{GeV}$. This is a weak bound — but
  it is a bound $\gg 1$, obtained from their own data, and that is a real
  result. Do not let students overstate it, and do not let them dismiss it.

## Where groups get stuck

1. **Impatience with the count rate.** Manage expectations in Week 12. The
   arithmetic in pre-lab question 3 is meant to do this for you.
2. **Skipping the Part B controls.** These are what turn coincidence counts
   into evidence. Make them a hard checkpoint.
3. **Trusting $\Omega = A/d^2$.** It is crude for realistic geometries. The
   Monte Carlo is where the credit is; help groups that stall on it.
4. **A non-rigid frame.** Changes the acceptance with angle and destroys the
   $\cos^n\theta$ fit. Check before the long runs start.
5. **Feeding a raw GM pulse into a GPIO pin.** Destroys the pin, and the
   student learns nothing except that microcontrollers are fragile. The
   interface board exists for this; do not let them bypass it.

## Grading notes

Full-report criteria, plus:

- The three validation controls must appear with numbers, not as assertions.
- Both frames of the time-dilation explanation (dilated lifetime in the lab
  frame, contracted atmosphere in the muon frame) must be given and shown to
  agree numerically. This is question 8 and it is the course's closing idea.
- Reward the Monte Carlo acceptance heavily; it is how real detector
  acceptances are computed and few undergraduates ever do one.
- Question 9 (why a muon traverses kilometres of atmosphere and an electron
  cannot): the answer is that the muon is $207$ times heavier, so
  bremsstrahlung — which scales as $1/m^2$ — is suppressed by a factor of
  $\sim4\times10^{4}$, leaving ionization as its only significant loss. It
  also does not feel the strong interaction, unlike the pions that produced
  it.

## Safety

GM supplies at several hundred volts. The interface board must be left
intact; check it before each long run. Otherwise this is the safest experiment
in the manual — the apparatus can run unattended for a week.

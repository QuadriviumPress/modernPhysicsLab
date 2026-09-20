---
title: Laboratory Safety
short_title: Safety
label: lab-safety
---

# Laboratory Safety

Read this before Week 1. You will sign a sheet saying that you have.

Three classes of hazard appear in this manual: laser light, ionizing
radiation, and electrical or thermal hazards from bench instruments. None of
them is exotic, and all of them are managed by a small number of habits.

## Lasers

Experiments 1, 4, 5, 7, and 8 use lasers. Most are Class 2 (visible,
$\le 1\ \text{mW}$, blink-reflex protection); the Thorlabs quantum kits use a
Class 3R source (up to $5\ \text{mW}$), for which the blink reflex is **not**
adequate protection.

:::{danger} Laser rules
1. **Never place your eye at beam height.** Almost every laser eye injury in a
   teaching laboratory happens when someone bends down to look along the beam.
   Work standing, or raise the bench, but keep your head above the beam plane.
2. **Remove watches, rings, and badges** before reaching over the table.
   Specular reflection from jewelry is the second most common mechanism.
3. **Terminate the beam.** Every beam path ends on a beam block or a diffusing
   card, not on a wall, a window, or a neighbouring group's bench.
4. **Beam off while you reconfigure.** Block or switch off the source before
   moving a mirror, inserting an optic, or changing a mount.
5. **Never aim a beam out of the laboratory**, and keep the door closed while
   a Class 3R source is on.
6. **Report any suspected exposure immediately**, even if you feel fine. An
   afterimage that persists more than a few minutes is a reason to be seen.
:::

Safety eyewear rated for the source wavelength is available for the Class 3R
experiments and is required whenever the beam is unenclosed.

## Radioactive sources

Experiments 3 and 13 use sealed check sources — typically $^{90}$Sr
($\beta$), $^{137}$Cs ($\beta,\gamma$), $^{60}$Co ($\gamma$), and a
$^{137}$Cs/$^{137m}$Ba isotope generator. Their activities are of order
$1\ \mu\text{Ci}$ ($37\ \text{kBq}$) to a few $\mu$Ci: small enough that the
dose from a full laboratory period at working distance is a small fraction of
a day's natural background, and large enough that carelessness is still worth
avoiding.

:::{danger} Source rules
1. **Sources are signed out and signed back in.** A source that leaves the
   laboratory is a reportable incident.
2. **Handle sealed sources with the tongs or by the plastic holder**, never by
   the active face, and never with bare fingers on the window.
3. **Distance is free protection.** Dose rate falls as $1/r^2$; doubling your
   distance quarters your dose. Keep sources on the bench and yourself an
   arm's length back except when placing them.
4. **Time is the other free variable.** Do not leave a source out of its
   shielded storage while you are analyzing data.
5. **Never eat, drink, or apply cosmetics in the laboratory**, and wash your
   hands when you leave. The one real hazard from a sealed source is a
   compromised seal, which turns an external-dose problem into an ingestion
   problem.
6. **The $^{137m}$Ba eluate is an unsealed liquid.** Wear gloves, work over a
   tray, and dispose of the planchet as directed. Its $2.55\ \text{min}$
   half-life means it is essentially gone within half an hour, but it is
   genuinely loose activity until then.
:::

If a source is dropped, damaged, or cannot be found, stop work and tell the
instructor. Do not search for it yourself with a survey meter unless asked to.

## Electrical and thermal

- **The tungsten lamp in Experiment 6 reaches temperatures above
  $2500\ \text{K}$.** Its envelope will burn you for several minutes after
  power-off. Let it cool on a ceramic tile.
- **High-voltage supplies for GM tubes** run at $400$–$900\ \text{V}$ at very
  low current. The current is too small to be dangerous but the startle
  reflex is not: power down before connecting or disconnecting the tube.
- **Do not float an oscilloscope ground.** The BNC shield on a mains-powered
  scope is earthed. Connecting it to a point that is not at earth potential
  makes a short circuit through the instrument. If you need a differential
  measurement, use two channels and subtract.
- **Microcontroller boards are $3.3\ \text{V}$ or $5\ \text{V}$ logic.**
  Feeding a $12\ \text{V}$ signal or a GM tube's raw pulse into a GPIO pin
  destroys the pin. Every circuit in this manual that touches a high-voltage
  domain includes a limiting resistor and a clamp; do not remove them.

## Chemical

Experiment 12 uses ethanol or isopropanol as a solvent for the fluorophore
(fluorescein, rhodamine, quinine from tonic water, or a chlorophyll extract).
These are flammable and are kept away from the hot lamp. Quinine and
fluorescein at the concentrations used are not acutely toxic, but they are not
food. Gloves, and the same no-eating rule as above.

## What to do if

:::{list-table}
:header-rows: 1

* - Situation
  - Action
* - Suspected laser eye exposure
  - Stop, tell the instructor, do not resume work. Seek medical review if any
    visual symptom persists.
* - Dropped or damaged radioactive source
  - Stop, keep everyone back, tell the instructor. Do not pick it up.
* - Burn from the lamp or a soldering iron
  - Cool under running water for at least ten minutes. Report it.
* - Smell of burning from an instrument
  - Switch off at the bench, unplug, tell the instructor.
* - Chemical spill
  - Contain with the absorbent pad in the spill kit; ventilate; report.
:::

The first-aid kit is by the door; the eyewash and the fire extinguisher are in
the corridor alcove. Know where they are before you need them.

---
title: Laboratory Safety
short_title: Safety
label: lab-safety
---

# Laboratory Safety

Read this before Week 1 and follow your institution's approved laboratory
procedures. The instructor must identify the actual equipment, source
activities, safety contacts, and emergency equipment before work begins.

The experiments may involve laser light, ionizing radiation, electrical or
thermal hazards, and flammable solvents. The controls below supplement the
site's training and written procedures; they do not replace them.

## Lasers

Experiments 1, 4, 5, 7, and 8 use lasers; Experiment 2 may use a pulsed
laser diode. Confirm each source's class and
wavelength from its label before use. A Class 2 visible laser can injure an
eye during prolonged direct viewing; direct viewing of a Class 3R beam or a
specular reflection can be hazardous. Do not rely on the blink or aversion
response as a working control. See [OSHA's laser hazard guide](https://www.osha.gov/laser-hazards/hazards).

:::{danger} Laser rules
1. **Keep your eyes out of the beam plane.** Do not bend down to look along a
   beam path or view it through an optical instrument.
2. **Remove reflective jewelry and badges** before working over the beam path.
   Check for other shiny surfaces that could produce a specular reflection.
3. **Terminate the beam.** Every beam path ends on an approved beam stop,
   not on a wall, a window, or a neighboring group's bench.
4. **Beam off while you reconfigure.** Block or switch off the source before
   moving a mirror, inserting an optic, or changing a mount.
5. **Never aim a beam out of the laboratory**, and keep the door closed while
   a Class 3R source is on.
6. **Report any suspected eye exposure immediately.** Stop work and follow
   the institution's procedure for prompt medical evaluation; do not wait for
   an afterimage or other symptom.
:::

Use protective eyewear when the site's laser safety assessment requires it.
It must be rated for the laser's wavelength and optical density; ordinary
safety glasses are not a substitute. Beam enclosure, beam stops, and safe
alignment procedures remain essential even when eyewear is worn.

## Radioactive sources

Experiments 3 and 13 may use sealed check sources such as $^{90}$Sr,
$^{137}$Cs, or $^{60}$Co. A $^{137}$Cs/$^{137m}$Ba generator, if used, produces
*unsealed* radioactive material and needs a separate approved procedure.
Source activity, shielding, handling, monitoring, and disposal depend on the
actual equipment and the institution's authorization. Do not infer a safe
dose from the examples in this manual. The [NRC's radiation protection guide](https://www.nrc.gov/facilities-safety/radiation-protection/how-the-nrc-protects-you/minimize-your-exposure)
explains the principles of time, distance, shielding, and containment.

:::{danger} Source rules
1. **Account for every source.** Follow the instructor's sign-out, storage,
   and return procedure. Report a missing source immediately.
2. **Handle sources only as trained.** Use the holder or tools specified for
   the approved source, and never touch its active window.
3. **Increase distance and use the specified shielding.** Exposure generally
   decreases with distance; an exact inverse-square calculation is not valid
   for every source geometry or near-field setup.
4. **Minimize time outside storage.** Return a source to its designated
   shielded container when the measurement is complete.
5. **Never eat, drink, or apply cosmetics in the laboratory.** Wash your
   hands when you leave. A damaged sealed source may present contamination
   as well as external-exposure hazards.
6. **Treat any $^{137m}$Ba eluate as unsealed radioactive material.** Only
   use it under the institution's approved procedure, with the required
   containment, contamination checks, and waste controls. Its short
   half-life does not by itself establish that the tray or waste is safe to
   handle or discard.
:::

If a source is dropped, damaged, or cannot be found, stop work, keep others
away, and notify the instructor and radiation safety contact. Do not touch
the source or improvise a search or cleanup.

## Electrical and thermal

- **The tungsten lamp in Experiment 6 becomes a burn hazard.** Its envelope
  can remain hot after power-off. Let it cool on a heat-resistant mat or tile
  before handling it, and use the lamp's rated electrical limits.
- **High-voltage supplies for GM tubes** may operate at hundreds of volts.
  Do not assume a supply is safe because its nominal output current is low.
  Power down and follow the instrument's discharge procedure before changing
  connections; do not touch exposed conductors.
- **Do not float an oscilloscope ground.** The BNC shield on a conventional
  mains-powered bench scope is earthed. Connecting a probe's ground lead to a
  live point can create a short circuit and shock hazard. For a floating
  measurement, use an appropriately rated differential probe or isolated
  input instrument under the instructor's direction; see [Tektronix's
  floating-measurement guide](https://www.tek.com/en/datasheet/floating-measurements-selection-guide).
- **Microcontroller inputs have specified voltage limits.** Verify the
  board's ratings and the interface circuit before connecting an external
  signal. Never feed a GM tube's raw high-voltage pulse into a GPIO pin.

## Chemical

Experiment 12 uses ethanol or isopropanol as a solvent for the fluorophore
(fluorescein, rhodamine, quinine from tonic water, or a chlorophyll extract).
These solvents are flammable: keep them away from the hot lamp and ignition
sources. Follow the safety data sheet and local ventilation, glove, storage,
and waste procedures for the actual solvent and dye. No food or drink belongs
on the bench.

## What to do if

:::{list-table}
:header-rows: 1

* - Situation
  - Action
* - Suspected laser eye exposure
  - Stop, tell the instructor, and follow the site's procedure for prompt
    medical evaluation even if no symptom is apparent.
* - Dropped or damaged radioactive source
  - Stop, keep others back, notify the instructor and radiation safety contact.
    Do not pick it up.
* - Burn from the lamp or a soldering iron
  - Move away from the heat source. Cool the burn under cool running water
    for 20 minutes; do not use ice. Report it and seek medical advice as
    directed by the site. See [NHS burn first aid](https://www.nhs.uk/conditions/burns-and-scalds/).
* - Smell of burning from an instrument
  - Switch off at the bench, unplug, tell the instructor.
* - Chemical spill
  - Stop work, keep others away, and tell the instructor. Follow the site's
    spill procedure; do not clean up an unknown or radioactive spill yourself.
:::

Before the first experiment, locate the actual first-aid kit, eyewash,
fire extinguisher, exits, and emergency contact instructions in your lab.

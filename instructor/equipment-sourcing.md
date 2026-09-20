---
title: "Equipment Sourcing"
short_title: Equipment Sourcing
label: inst-equipment-sourcing
---

# Equipment Sourcing

A purchasing-oriented bill of materials, one table per experiment, to
accompany the terse "Have / Note" tables in each `instructor/exp-NN-notes.md`.
Where those files assume a department already owns most of the gear, this
file is written for someone placing an actual order.

**Sourcing rule.** Thorlabs and PASCO scientific are used wherever they carry
the item; a third-party supplier is named only when neither does (bare
electronics, chemicals, an oscilloscope, a discharge tube PASCO doesn't
stock). Prices below were checked against thorlabs.com and pasco.com on
2026-09-20 and are **approximations that will drift** — treat every number as
a starting point for a quote, not a purchase order. Most Thorlabs catalog
items (including educational kits) and PASCO apparatus now publish web
pricing directly; a few third-party or spare-part lines remain quote-only.
All PASCO prices are before PASCO's current 5% tariff surcharge.

:::{important} Two things to check before ordering
1. **The GM tube/counter named implicitly throughout this manual
   (PASCO SN-7927A) is discontinued.** PASCO's listed replacement is the
   **PS-3238 Wireless Geiger Counter** — but it is a closed Bluetooth/USB unit
   with no raw pulse output, unlike the SN-7927A. It's a fine substitute for
   Experiments 3 and 13, which only need a logged count rate (via SPARKvue or
   PASCO Capstone). It is **not** a substitute for Experiment 14's
   coincidence telescope, which needs a per-tube TTL pulse to feed external
   pulse-shaping electronics — see that section below for the actual fix.
2. **`EDU-SPEA1` and `EDU-SPEB1`**, named in the Exp 6/10/11/12 apparatus
   text, were discontinued by Thorlabs in 2020. The current equivalent is the
   single **`EDU-SPEB2`** kit (grating + prism spectrometer in one kit); this
   document sources that instead. Worth a one-line update to the experiment
   text itself at some point, but that's outside this file's scope.
:::

## Experiment 1 — The Michelson Interferometer and the Ether Null Result

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Michelson interferometer educational kit | Thorlabs | EDU-MINT1/M (metric) or EDU-MINT2 (imperial) | **$3,285.58** (imperial) | Breadboard, micrometer-driven mirror stage, beamsplitter, mounts |
| HeNe laser head, ~5 mW, with power supply | Thorlabs | HNL050LB (-EC for 100–240 VAC) | **$2,005.45** | 632.8 nm polarized; preferred over the diode module for coherence length |
| 650 nm diode laser module (backup) | Thorlabs | CPS635R (round beam, 1.2 mW) | **$114.39** | Shorter coherence length — text calls this the cheap backup |
| f ≈ −9 to −25 mm diverging lens | Thorlabs | N-BK7/N-SF11 plano-concave, e.g. LD2568-A | **$44.81** (LD2568-A, f = −9 mm) | Pick focal length to suit the kit's beam diameter |
| Beam block / viewing screen | Thorlabs | LB1 beam block + VRC2 viewing card | **$62.92** (LB1) + **$100.63** (VRC2) | LB1 replaces the older informal "BB1 beam block" wording |
| Laser safety eyewear | Thorlabs | LG9 / LG10 (match source OD rating) | **$244.33** each | Required per `front-matter/02-laboratory-safety.md` |
| Tally counter | Generic (office/lab supply) | — | ~$5 each, buy 4 | Neither Thorlabs nor PASCO stocks these; they get lost |

## Experiment 2 — The Speed of Light

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Fast pulsed laser diode / driven LED | Thorlabs | CPS635F module, driven through a MOSFET gate driver | **$129.65** | Do not drive from a bare GPIO pin |
| Fast amplified photodiode ×2 | Thorlabs | PDA36A2 switchable-gain Si detector | **$400.01** each (×2) | 350–1100 nm, up to 12 MHz — matches the BPW34-class sensor the text calls for |
| Front-surface mirror + kinematic mount ×2 | Thorlabs | BB1-E02 mirror + KM100 mount | **$86.91** + **$44.78** each (×2) | |
| Oscilloscope, ≥100 MHz, with averaging | Rigol or Siglent | DS1104Z-S / SDS1104X-E | ~$500–650 | Not a Thorlabs or PASCO product line |
| Function generator | Rigol or Siglent, or PASCO 850 Universal Interface | DG822 / UI-5000 | ~$400 (Rigol) or $1,199 (PASCO, shared, see below) | |
| Matched-length BNC cables ×2 | Digi-Key or Pasternack | — | ~$10–20 each | |
| Tape measure | Generic | — | ~$10 | |

## Experiment 3 — Relativistic Electrons from Beta Decay

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| GM counter with counter/timer | PASCO | PS-3238 Wireless Geiger Counter | $265 | Replaces discontinued SN-7927A; needs SPARKvue/Capstone — fine here, unlike Exp 14 |
| Sealed ⁹⁰Sr/⁹⁰Y source, ~1 µCi | PASCO | SN-9796 | $68 | US NRC license-exempt sealed disk; confirm local rules outside the US |
| Aluminium absorber set | PASCO | SN-8111 (Qty. 20) | **$339** | 4 lead / 2 plastic / 10 Al / 2 polyethylene / 2 Al-foil, 5–7200 mg/cm² |
| Source tongs | PASCO or Spectrum Techniques | — | ~$20–40 | |
| Micrometer + balance | Generic lab supply | — | ~$30–80 (micrometer) if buying new | Likely already on hand |

## Experiment 4 — Interference of Light

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| 650 nm diode laser | Thorlabs | CPS635R | **$114.39** | Shared with Exp 1/5/7/8 |
| Optics bench + double-slit / multi-slit sets | PASCO | OS-8515D Basic Optics System | $599 | Includes 4 double-slits, multi-slit disk, variable double-slit (0.125–0.75 mm) |
| USB machine-vision camera (lens removed) | Generic (Amazon/Edmund Optics) | e.g. ELP board camera | ~$30–50 | Or a phone on manual exposure |
| Microscope slides, binder clips, human hair, foil | Generic lab supply | — | Consumables, ~$10–20 | |

## Experiment 5 — Diffraction and the Resolution Limit

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Single-slit / circular-aperture set | PASCO | OS-8515D (included Single-Slit Disk) | Shared with Exp 4 | |
| Precision diffraction slits | PASCO | OS-8453 | $275 | |
| Transmission grating, ~300–1000 l/mm | Thorlabs | GR25-0605 (600/mm, 500 nm blaze) | **$137.27** | Reflective ruled grating; transmission alternatives also fine |
| CD / DVD / Blu-ray disc | Generic | — | Scrap media | |
| Rotation stage | Thorlabs | RP01/M manual rotation mount | **$119.18** (RP01) | |
| Camera / scanning photodiode | Shared with Exp 4 / PDA36A2 | | | |

## Experiment 6 — Planck's Constant from Light-Emitting Diodes

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| LEDs: 405, 470, 525, 590, 630, 940 nm | Digi-Key or Adafruit | assorted THT 5 mm LEDs | ~$1–3 each, buy 10 of each | **Do not substitute a white LED** |
| Variable DC supply 0–5 V, or microcontroller DAC/PWM | Rigol bench supply, or Arduino/Pico + RC filter | — | ~$150–300 (bench) / ~$25 (microcontroller) | |
| Two digital multimeters | Fluke or Extech | 115 / EX330 | ~$100–150 each | Or microcontroller ADC + current-sense resistor |
| 100 Ω series resistor | Digi-Key | — | <$1 | |
| Spectrometer kit | Thorlabs | **EDU-SPEB2** (successor to discontinued EDU-SPEA1/SPEB1) | **$2,246.39** | Confirm near-IR range reaches 940 nm before trusting that LED's peak |
| 6 V clear-envelope filament lamp | Generic (automotive) | #1156 bulb or torch bulb | ~$5 | Consumable — reorder yearly |
| Bench supply, 0–8 V / 2 A, 4-wire sense | Rigol DP832 or Siglent SPD3303X | — | ~$350–500 | |

## Experiment 7 — The Quantum Eraser and Complementarity

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Quantum eraser demonstration kit | Thorlabs | EDU-QE1 (imperial) / EDU-QE1/M (metric) | **$2,284.11** (confirmed, imperial) | 532 nm laser, double slit, slit polarizers, rotatable analyzer, mounts, breadboard — complete kit |
| USB camera / scanning photodiode | Shared with Exp 4/5 | | | |
| Neutral-density filter kit | Thorlabs | NDC-25C-4 or NEK01 | **$402.93** (NDC-25C-4) / **$678.85** (NEK01) | Shared with Exp 8/11; NEK01S square set is $992.56 if preferred |

## Experiment 8 — Tunneling by Frustrated Total Internal Reflection

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Right-angle N-BK7 prism (n ≈ 1.52) | Thorlabs | PS912 (40 mm uncoated) or PS608 (20 mm UVFS) | **$118.52** (PS912) / **$96.62** (PS608) | Prefer N-BK7 PS912 for the n ≈ 1.52 the text assumes |
| Long plano-convex lens, f ≈ 200–500 mm | Thorlabs | LA1708-A (f = 200 mm) or LA1461-A (f = 250 mm) | ~$35–40 (LA1708-A class) | LA17xx-A series; longer f also available |
| Adjustable clamp / spring-loaded mount | Thorlabs | PM4 prism mount or spring clamp | **$28.60** | |
| 650 nm diode laser + beam expander | Thorlabs | CPS635R + **GBE02-A** (successor to BE02M-A) | **$114.39** + **$512.24** | GBE02-A is 2× Galilean, AR 400–650 nm |
| USB microscope or macro camera, or photodiode on translation stage | Generic (Dino-Lite) or Thorlabs PDA36A2 + MT1 stage | — | ~$70–100 (microscope) | |
| Neutral-density filters | Shared with Exp 7/11 | | | |
| Lens tissue, isopropanol | Thorlabs | MC-5 lens tissue | **$12.48** | Consumable |

## Experiment 9 — Eigenmodes, Degeneracy, and Nodal Patterns

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Rigid rectangular cavity (plywood/acrylic box) | Fabricated locally (hardware store / TAP Plastics) | — | ~$20–60 materials | Not a catalog item |
| Small full-range speaker + amplifier | Adafruit or generic | — | ~$20–40 | |
| Electret microphone + preamp | Adafruit | MAX9814 mic amp module | ~$8 | Into sound card or microcontroller ADC |
| Function generator / swept-sine source | PASCO | 850 Universal Interface (UI-5000) | $1,199 | Doubles as DAQ; shared with Exp 2. A standalone Rigol DG822 (~$400) is cheaper if the 850 isn't already owned |
| Chladni plates kit | PASCO | WA-9607 | $125 | Includes 24×24 cm square plate, round plate, sand, shaker |
| Mechanical wave driver | PASCO | **WA-9855** (replaces discontinued WA-9753 / SF-9324) | **$155** | Required to drive the Chladni plate; banana cords SE-9751 ($23) also needed |
| Fine sand / salt | Included with WA-9607, or generic craft supply | — | ~$5 if buying separately | |
| Thermometer | Generic lab supply | — | ~$10–25 | |

## Experiment 10 — The Balmer Series and the Rydberg Constant

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Spectral tube power supply and mount | PASCO | SE-9460 | $229 | Do not energize a tube for more than ~1 min at a time |
| Hydrogen spectral tube | PASCO | SE-9461 | $40 | Ages quickly at full current — reorder yearly per `instructor/README.md` |
| Mercury spectral tube (calibration) | PASCO | SE-9466 | **$40** | Shared with Exp 11 |
| Helium spectral tube (calibration) | PASCO | SE-9462 | **$40** | Shared with Exp 11 |
| Spectrometer | Thorlabs | EDU-SPEB2 | **$2,246.39** | Shared across Exp 6/10/11/12 |
| Thermometer / barometer (optional) | Generic lab supply | — | ~$15–40 | For the air-index correction |

## Experiment 11 — Alkali Spectra, Screening, and the Quantum Defect

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Sodium discharge lamp (with housing / PSU) | **Not carried by PASCO or Thorlabs** — 3B Scientific 1003159 (Na low-pressure lamp + housing) | 1003159 / U21829-230 | **~$1,160** | Flagged gap: PASCO's spectral-tube line (SE-9461…9468) does not include sodium. Bare Na tube alone is cheaper (~$283–688) if a ballast/housing is already owned |
| Mercury / helium calibration tubes | PASCO | SE-9466 / SE-9462 | Shared with Exp 10 ($40 each) | |
| Grating spectrometer | Thorlabs | EDU-SPEB2 | Shared with Exp 10/12 ($2,246.39) | Best resolving power the manual assumes |
| Neutral-density filters | Shared with Exp 7/8 | | | |
| Potassium or lithium lamps (optional extension) | 3B Scientific or Edmund Scientific | — | ~$600–900 (lamp) + ballast | Same spectral-lamp product family as Na; confirm ballast compatibility |

## Experiment 12 — Molecular Fluorescence, the Stokes Shift, and Franck–Condon

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Spectrometer kit, fiber input | Thorlabs | EDU-SPEB2 | **$2,246.39** | |
| Cuvette holder, SMA905 fiber adapter | Thorlabs | CVH100/M | **$490** (confirmed) | Add CVH100-COL SMA-to-SM1 adapter ($88) if a different collimating lens is needed |
| Broadband white LED or tungsten source | Thorlabs | SLS201L/M stabilized tungsten-halogen | **$1,283.79** | Or a Digi-Key white LED for a cheaper start |
| Excitation LEDs: 405, 470 nm, 365 nm UV | Thorlabs (405 nm: M405L4) or Digi-Key | M405L4 | **$274.16** (M405L4) / ~$2 each (Digi-Key THT) | 365 nm UV needed specifically for quinine sulfate; M405L4 needs a current driver (LEDD1B class) |
| Long-pass filter | Thorlabs | FEL0450 or similar colored-glass longpass | ~$115 | 450 nm cut-on |
| 1 cm cuvettes, volumetric glassware, micropipettes | Fisher Scientific | — | ~$5–50 per cuvette depending on material | Quartz for UV work, PMMA otherwise |
| Fluorophores: fluorescein (dilute NaOH), quinine sulfate (0.1 M H₂SO₄), tonic water, rhodamine 6G, chlorophyll/spinach/acetone | Sigma-Aldrich or Fisher Scientific (tonic water/spinach: grocery store) | — | ~$30–80 per reagent bottle | Consumables — reorder yearly per `instructor/README.md` |

## Experiment 13 — Counting Statistics, Half-Life, and Gamma Attenuation

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| GM counter, repeat/log mode | PASCO | PS-3238 | $265 | SPARKvue/Capstone provides the programmable repeat-run logging the text calls for |
| Cs-137/Ba-137m isotope generator kit | PASCO | SN-7995 | **$339** (confirmed) | Includes generator, eluting solution, syringe, 5 planchets |
| Extra eluting solution / planchets | United Nuclear or Spectrum Techniques (PASCO spares by quote) | — | ~$29 (250 mL eluting) / ~$69 (100 planchets) | Consumable — reorder yearly |
| Long-lived check source, Cs-137, 5 µCi | PASCO | SN-9795 | $125 | US license-exempt sealed disk |
| Lead sheets / aluminium absorbers | PASCO | SN-8111 | **$339** | Shared with Exp 3 |
| Collimator | Fabricated (lead pipe or brass stock) | — | ~$15–40 materials | Improves the narrow-beam approximation substantially |

## Experiment 14 — A Cosmic-Ray Muon Telescope

| Item | Supplier | Part # | Approx. price | Notes |
|---|---|---|---|---|
| Two GM tubes with an accessible raw pulse output | LND Inc. (bare tube) or a complete kit with a TTL pulse pin (e.g. an SBM-20-based "Mightyohm"-style Geiger kit) | LND712 (bare tube) | ~$50–80/tube (bare) or ~$30–50/unit (complete kit) + a custom HV supply for the bare-tube route | **PASCO's PS-3238 will not work here** — it's a closed Bluetooth/USB unit with no exposed per-tube pulse for the coincidence circuit |
| Microcontroller | Adafruit or SparkFun | Arduino Uno R4, or Raspberry Pi Pico | ~$20–28 | |
| Per-tube pulse-shaping components (limiting resistor, clamp diode pair, comparator) | Digi-Key or Mouser | e.g. LM339 comparator, 1N4148 diodes | <$5 per channel | |
| Lead absorber sheets | PASCO | SN-8111 | Shared with Exp 3/13 ($339) | |
| Rotating mount / rigid frame at measured zenith angles | Fabricated locally | — | ~$30–80 materials | Long unattended counting periods — see `instructor/README.md`'s "Long-running experiments" note |

## Shared across multiple experiments

Buying one of each of these covers several weeks and avoids duplicate orders:

| Item | Used in | Supplier | Part # | Approx. price |
|---|---|---|---|---|
| Oscilloscope, ≥100 MHz | Exp 2 (required); useful in Exp 9 | Rigol / Siglent | DS1104Z-S / SDS1104X-E | ~$500–650 |
| Function generator / PASCO 850 interface | Exp 2, 9 | PASCO | UI-5000 | $1,199 |
| Digital multimeters | Exp 2, 6 | Fluke / Extech | 115 / EX330 | ~$100–150 each |
| Microcontroller (Arduino/Pico) | Exp 6, 9, 14 | Adafruit / SparkFun | — | ~$20–28 each |
| Neutral-density filter kit | Exp 7, 8, 11 | Thorlabs | NDC-25C-4 | **$402.93** |
| Laser safety eyewear | Exp 1, 2, 4, 5, 7, 8 | Thorlabs | LG9 / LG10 | **$244.33** each |
| Spectrometer kit | Exp 6, 10, 11, 12 | Thorlabs | EDU-SPEB2 | **$2,246.39** |
| Lead / aluminium absorber set | Exp 3, 13, 14 | PASCO | SN-8111 | **$339** |

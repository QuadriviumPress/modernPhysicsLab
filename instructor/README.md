# Instructor Notes

One file per experiment. **Not built into the student site or PDF** —
`instructor/**` is listed under `exclude:` in `myst.yml`. Build these
deliberately:

```bash
myst build instructor/*.md --pdf
```

`equipment-sourcing.md` is the exception: a single purchasing-oriented bill
of materials covering all fourteen experiments, with Thorlabs/PASCO catalog
numbers and prices, for actually placing an order.

Each experiment file follows the same structure:

- **Prep** — what must be done before the period, and how long it takes
- **Bill of materials** — with rough costs where the item is not already owned
- **Expected results** — the numbers a competent group should obtain
- **Where groups get stuck** — ranked by how often it happens
- **Grading notes** — what to look for, and the common report failures
- **Safety** — the specific control, beyond the general rules

## Semester-level notes

**Retired apparatus.** The electron diffraction tube, the Franck–Hertz
apparatus, the Millikan oil-drop bench, and the X-ray diffractometer are not
used. Their physics is covered as follows:

| Retired experiment | Where the physics now lives |
|---|---|
| Photoelectric effect (PASCO EX-5549A) | Exp 6, LED turn-on voltage |
| Electron diffraction tube | Exp 7 (complementarity) + computational de Broglie |
| Franck–Hertz | Exp 10/11 (quantized atomic levels, spectroscopically) |
| Millikan oil drop | Not replaced; see the note below |
| X-ray Bragg / Moseley | Exp 11, screening via the quantum defect |

*On Millikan:* the charge quantization result is not currently covered by any
experiment. If it matters to you, the cheapest route back is a
shot-noise measurement of $e$ with a photodiode and a low-noise amplifier —
$e = \sigma_I^2/(2 I \Delta f)$ — which is a real measurement of the electron
charge with no oil, no atomizer, and no eyestrain. It would fit Week 6.

**Long-running experiments.** Experiment 14 is statistics-limited and should
be left running between periods. Set the telescope up in a corner of the
laboratory in Week 12 and have groups change the zenith angle daily. The same
applies to the optional muon-lifetime extension, which needs a week.

**Consumables to reorder each year.** Hydrogen discharge tubes (they age
quickly at full current), the $^{137}$Cs/$^{137m}$Ba generator's eluting
solution, fluorescein and quinine sulfate, planchets, gloves, and sand for the
Chladni plates.

**Sources.** $^{90}$Sr/$^{90}$Y ($\sim1\ \mu$Ci), $^{137}$Cs sealed button,
$^{204}$Tl if the range–energy extension in Exp 3 is used, and the
$^{137}$Cs/$^{137m}$Ba isotope generator. Check the licence conditions and the
inventory log before Week 3.

**Pacing.** Weeks 4, 10, and 14 are the full-report weeks and are the three
most substantial experiments. Weeks 8 and 9 are the two most likely to need
rescoping if the semester runs short; both have a computational component that
stands alone if the hardware fails.

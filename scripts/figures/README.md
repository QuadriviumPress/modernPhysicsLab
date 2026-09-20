# Figure generation

Apparatus schematics for each experiment are generated with matplotlib and
written as SVG into [`../../images/`](../../images/). The rendered SVGs are
**committed**, because the GitHub Pages workflow runs `myst build --html`
only — there is no Python available at build time. These are static
apparatus diagrams; unlike the textbook, the lab manual has no
`{animation}` figures.

## Regenerating

```bash
python3 -m pip install -r requirements-figures.txt
python3 scripts/figures/exp01_figure.py   # Michelson interferometer
python3 scripts/figures/exp02_figure.py   # time-of-flight speed of light
python3 scripts/figures/exp03_figure.py   # beta-decay shelf stand
python3 scripts/figures/exp04_figure.py   # interference bench
python3 scripts/figures/exp05_figure.py   # diffraction bench
python3 scripts/figures/exp06_figure.py   # LED I-V circuit + tungsten spectrometer
python3 scripts/figures/exp07_figure.py   # quantum eraser
python3 scripts/figures/exp08_figure.py   # frustrated total internal reflection
python3 scripts/figures/exp09_figure.py   # rectangular cavity + Chladni plate
python3 scripts/figures/exp10_figure.py   # Balmer series spectrometer
python3 scripts/figures/exp11_figure.py   # sodium D-line spectrometer (reuses exp10's layout)
python3 scripts/figures/exp12_figure.py   # fluorescence / absorption
python3 scripts/figures/exp13_figure.py   # half-life + gamma attenuation
python3 scripts/figures/exp14_figure.py   # muon telescope
```

Each script prints the file it writes. Commit the regenerated SVGs along with
any change to the scripts, so the site and the source stay in step.

## Layout

| File | Contents |
|---|---|
| `labstyle.py` | Shared rcParams, palette, `save()`, and reusable apparatus glyphs (mirrors, beamsplitters, lenses, prisms, GM tubes, absorber stacks, rotation stages, …) |
| `exp01_figure.py` | Michelson interferometer: beamsplitter, fixed and movable mirrors, circular-fringe screen |
| `exp02_figure.py` | Pulsed source split into a short reference path and a folded long path via two mirrors, into a fast oscilloscope |
| `exp03_figure.py` | Sealed beta source on a shelf stand, removable aluminium absorber stack, end-window GM tube |
| `exp04_figure.py` | Laser, slit set, and camera on a common optical rail |
| `exp05_figure.py` | Laser, sample on a rotation mount, diffracted orders to a screen or rotating detector |
| `exp06_figure.py` | (a) LED forward-bias I-V circuit; (b) tungsten lamp through a slit/grating spectrometer |
| `exp07_figure.py` | Double slit with orthogonal polarizers, rotatable analyzer, camera |
| `exp08_figure.py` | Right-angle prism, long-radius lens pressed on the hypotenuse, reflected/tunneled beams |
| `exp09_figure.py` | (a) corner-driven rectangular acoustic cavity; (b) Chladni plate with sand |
| `exp10_figure.py` | Discharge tube, entrance slit, collimating lens, grating on a vernier turntable, Balmer lines |
| `exp11_figure.py` | Same spectrometer as Experiment 10, sodium lamp and D-line doublet (imports `exp10_figure.spectrometer_layout`) |
| `exp12_figure.py` | (a) 90-degree excitation/emission geometry with a long-pass filter; (b) in-line absorption |
| `exp13_figure.py` | (a) planchet directly under a GM tube; (b) check source through a lead absorber stack |
| `exp14_figure.py` | Two GM tubes on a rotatable frame with adjustable separation and zenith angle, coincidence electronics |

## Conventions

- **SVG only.** Every figure here is a line-art apparatus schematic; none of
  the export-format concerns that force PNG/ICO in the textbook's
  `brand_assets.py` or `simulation_placeholder.py` apply.
- **Palette** matches the *Modern Physics* textbook figures (blue `#1769aa`,
  red `#b33a3a`, green `#2e7d5b`, purple `#6a4c93`, orange `#d97706`), so a
  reader moving between the two books sees the same visual language.
- **White background**, set explicitly, so figures read the same in either
  site theme.
- **`svg.fonttype: "path"`** so text renders identically without depending on
  the viewer's fonts.
- These are schematic, not to-scale ray diagrams: angles and proportions are
  chosen for legibility, not for optical accuracy.

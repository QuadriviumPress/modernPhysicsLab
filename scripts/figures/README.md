# Figure generation

Apparatus schematics and theory concept figures for each experiment are
generated with matplotlib and written as SVG into
[`../../images/`](../../images/). The rendered SVGs are **committed**,
because the GitHub Pages workflow runs `myst build --html` only — there is
no Python available at build time. These are static diagrams; unlike the
textbook, the lab manual has no `{animation}` figures.

Each experiment script produces **two** figures: the apparatus/bench
schematic (used in the Apparatus section) and a theory concept figure (used
in the Theory section, illustrating the physics idea rather than the bench
layout).

## Regenerating

```bash
python3 -m pip install -r requirements-figures.txt
python3 scripts/figures/exp01_figure.py   # Michelson interferometer + fringe geometry
python3 scripts/figures/exp02_figure.py   # time-of-flight speed of light + slope-fit trick
python3 scripts/figures/exp03_figure.py   # beta-decay shelf stand + absorption-curve shape
python3 scripts/figures/exp04_figure.py   # interference bench + envelope-modulated fringes
python3 scripts/figures/exp05_figure.py   # diffraction bench + Rayleigh criterion
python3 scripts/figures/exp06_figure.py   # LED I-V circuit + tungsten spectrometer + V_on vs 1/lambda fit
python3 scripts/figures/exp07_figure.py   # quantum eraser + V,D complementarity
python3 scripts/figures/exp08_figure.py   # frustrated total internal reflection + quantum barrier
python3 scripts/figures/exp09_figure.py   # rectangular cavity + Chladni plate + mode counting
python3 scripts/figures/exp10_figure.py   # Balmer series spectrometer + hydrogen energy levels
python3 scripts/figures/exp11_figure.py   # sodium D-line spectrometer (reuses exp10's layout) + quantum defect
python3 scripts/figures/exp12_figure.py   # fluorescence / absorption + Franck-Condon diagram
python3 scripts/figures/exp13_figure.py   # half-life + gamma attenuation + Poisson vs Gaussian
python3 scripts/figures/exp14_figure.py   # muon telescope + time dilation / length contraction
```

Each script prints the files it writes. Commit the regenerated SVGs along
with any change to the scripts, so the site and the source stay in step.

## Layout

| File | Apparatus schematic | Theory concept figure |
|---|---|---|
| `labstyle.py` | Shared rcParams, palette, `save()`, and reusable apparatus glyphs (mirrors, beamsplitters, lenses, prisms, GM tubes, absorber stacks, rotation stages, …) | — |
| `exp01_figure.py` | Michelson interferometer: beamsplitter, fixed and movable mirrors, circular-fringe screen | Unfolded-mirror ray geometry ($\Delta = 2d\cos\theta$) and fringe order vs. angle |
| `exp02_figure.py` | Pulsed source split into a short reference path and a folded long path via two mirrors, into a fast oscilloscope | Delay vs. path-length slope fit: slope $=1/c$, intercept $=\tau$ |
| `exp03_figure.py` | Sealed beta source on a shelf stand, removable aluminium absorber stack, end-window GM tube | Absorption-curve shape: exponential region, bremsstrahlung tail, extrapolated range $R_m$ |
| `exp04_figure.py` | Laser, slit set, and camera on a common optical rail | Two-slit fringes modulated by the single-slit envelope, with a missing order |
| `exp05_figure.py` | Laser, sample on a rotation mount, diffracted orders to a screen or rotating detector | Rayleigh criterion: two point-spread functions just resolved |
| `exp06_figure.py` | (a) LED forward-bias I-V circuit; (b) tungsten lamp through a slit/grating spectrometer | $V_{\rm on}$ vs. $1/\lambda$ fit: slope $=hc/e$, nonzero intercept |
| `exp07_figure.py` | Double slit with orthogonal polarizers, rotatable analyzer, camera | Visibility/distinguishability vs. analyzer angle, and the $V$–$D$ unit circle |
| `exp08_figure.py` | Right-angle prism, long-radius lens pressed on the hypotenuse, reflected/tunneled beams | Rectangular quantum barrier: oscillating, decaying, oscillating wavefunction |
| `exp09_figure.py` | (a) corner-driven rectangular acoustic cavity; (b) Chladni plate with sand | Mode counting: lattice points inside a constant-frequency quarter circle |
| `exp10_figure.py` | Discharge tube, entrance slit, collimating lens, grating on a vernier turntable, Balmer lines | Hydrogen energy levels with the Balmer series (and one Lyman/Paschen line) marked |
| `exp11_figure.py` | Same spectrometer as Experiment 10, sodium lamp and D-line doublet (imports `exp10_figure.spectrometer_layout`) | Hydrogenic vs. quantum-defect-shifted $s,p,d,f$ levels for $n=3,4$ |
| `exp12_figure.py` | (a) 90-degree excitation/emission geometry with a long-pass filter; (b) in-line absorption | Franck-Condon potential curves: absorption, relaxation, emission, Stokes shift |
| `exp13_figure.py` | (a) planchet directly under a GM tube; (b) check source through a lead absorber stack | Poisson PMF vs. matching Gaussian, at small and large $\mu$ |
| `exp14_figure.py` | Two GM tubes on a rotatable frame with adjustable separation and zenith angle, coincidence electronics | Time dilation (lab frame) and length contraction (muon frame), side by side |

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

# MyST editorial review

Started 2026-09-30. Scope: the 21 student-facing pages in `myst.yml`.
Instructor notes are intentionally outside the table of contents. Count a
page as reviewed only after reading the entire page and checking substantive
claims. The schedule has now been checked against all 14 experiments.

## Page status

| Page | Status | Notes |
| --- | --- | --- |
| `index.md` | Reviewed 2026-09-30 | Matched all 14 schedule claims to the revised experiments, including the conditional beta endpoint, effective gamma attenuation, and muon angular trend. Corrected the blanket covariance-matrix statement to include count-likelihood intervals and bounds. |
| `front-matter/01-how-to-use-this-manual.md` | Reviewed 2026-09-30 | Matched short and full report deadlines to the rubric; allowed for long counting runs. |
| `front-matter/02-laboratory-safety.md` | Reviewed 2026-09-30 | Replaced unsupported hazard and dose assurances with equipment-specific controls and institutional procedures; corrected laser, source, oscilloscope, chemical, and emergency guidance. Experiment 6 follow-up removed an unconditional filament-temperature claim. Recheck consistency with each experiment's safety section during its review. |
| `front-matter/03-the-laboratory-notebook.md` | Reviewed 2026-09-30 | Qualified the standardized-discrepancy example and linked to the uncertainty chapter. |
| `front-matter/04-uncertainty-and-curve-fitting.md` | Reviewed 2026-09-30 | Corrected Type A/B definitions, conditions on averaging and quadrature, instrument-specification assumptions, fit diagnostics, and `curve_fit` covariance scaling. Experiment 6 follow-up replaced an invalid LED/Compton difference example with the actual LED voltage span. |
| `front-matter/05-python-toolkit.md` | Reviewed 2026-09-30 | Fixed significant-figure formatting, package setup, fitting advice, file-flush claim, and camera-linearity caveat. |
| `front-matter/06-grading-rubric.md` | Reviewed 2026-09-30 | Restricted axis and error-bar requirements to data plots so diagrams and photographs remain valid figures. |
| `experiments/exp-01-michelson-interferometer.md` | Reviewed 2026-09-30 | Replaced the unsupported 0.1% precision and “ether bound” claims with a percent-level wavelength measurement and a conditional sensitivity calculation. Corrected backlash procedure, fit interpretation, laser control, and vacuum-pump extension. Inspected both figures. |
| `experiments/exp-02-speed-of-light.md` | Reviewed 2026-09-30 | Distinguished air group speed from defined vacuum $c$, fixed the role of common source and fixed cable delays, revised safety and controls, and corrected the single-delay formula printed in the apparatus schematic. Inspected both figures. |
| `experiments/exp-03-relativistic-beta-electrons.md` | Reviewed 2026-09-30 | Replaced a count-time-dependent “range” from a semilog noise threshold with a practical-range fit to the terminal gross-rate decline and an independently measured floor. Corrected the absorber coverage, conditional endpoint claim, uncertainty and dead-time guidance, post-lab questions, and misleading extension claims. Regenerated and inspected the concept figure; inspected the apparatus figure. |
| `experiments/exp-04-interference-of-light.md` | Reviewed 2026-09-30 | Corrected the missing-order rule for noninteger $d/a$, the 10-maxima/10-spacings error, camera geometry and calibration, air-wedge imaging and fringe-interval counting, coherence-source assumptions, fitting guidance, and laser/slide controls. Corrected the index's “film thickness” claim and mislabeled apparatus SVG/source. Inspected both figures. |
| `experiments/exp-05-diffraction-and-resolution.md` | Reviewed 2026-09-30 | Replaced the sinc-squared Rayleigh illustration with an Airy profile and corrected its dip from 19% to 26.5%. Separated transmission and optical-disc reflection geometries, removed the unsupported Blu-ray pitch bound from an absent spot, qualified ideal grating resolving power and the subjective iris test, and corrected order counting, fitting uncertainty, capacity, and electron-wavelength questions. Inspected both revised figures. |
| `experiments/exp-06-plancks-constant-from-leds.md` | Reviewed 2026-09-30 | Recast LED extrapolation as a procedure-dependent voltage proxy and lamp $VI$ fit as an effective exponent. Corrected spectral-response, current-limit, fit-window, covariance, and cold-resistance guidance; removed the 10% schedule promise and unsupported intercept/FWHM claims. Rebuilt and inspected both figures, including a lamp electrical circuit in place of an unused spectrometer path. |
| `experiments/exp-07-quantum-eraser.md` | Reviewed 2026-09-30 | Distinguished the EDU-QE1 Mach–Zehnder hardware from the separate double-slit add-on, corrected the supplied laser class, added 45° input preparation and adequate detector field of view, and reframed the result as a classical-wave analog. Replaced angle-derived $D$ and baseline-divided $V$ with independent one-slit powers and a measured-envelope visibility fit. Corrected the orthogonal-analyzer sum, $C_{60}$ diffraction premise, photon-counting scope, and delayed-choice extension. Rebuilt and inspected both figures. |
| `experiments/exp-08-tunneling-by-ftir.md` | Reviewed 2026-09-30 | Limited optical exponential fitting to the thick-gap tail and distinguished it from contact saturation; added incident-beam uniformity, dark/floor, gap-geometry, pressure, and separate Newton-ring controls. Corrected the above-barrier transmission denominator and $E=V_0$ limit, replaced the false exact-curve overlay and nonclassical-resonance claim, and used the exact quantum formula where the thick-barrier approximation fails. Rebuilt the physically reversed prism-ray schematic and clarified the barrier concept figure. Updated the index promise. |
| `experiments/exp-09-eigenmodes-in-two-dimensions.md` | Reviewed 2026-09-30 | Changed the cavity to a square cross section so a specified mode pair can split under a sealed partition. Replaced the unidentifiable four-parameter sound-speed/length fit with a speed fit using independently measured lengths. Corrected the density-of-states surface-term example and log-slope, separated mode count from distinct detected peaks, and distinguished Chladni bending nodes from acoustic and quantum modes. Revised the plate drive, Zeeman and hydrogen analogies, linewidth claim, index promise, and both figures. |
| `experiments/exp-10-balmer-series-and-rydberg.md` | Reviewed 2026-09-30 | Distinguished observed Balmer centers from the leading-order reduced-mass model and `R_H` from `R_\infty`. Removed unsupported precision promises, fixed Hg/He calibration span and held-out checks, distinguished reflective from normal-incidence transmission geometry, and propagated correlated calibration uncertainty. Corrected lamp handling, weak Hδ treatment, air conversion, mass-ratio claim, Doppler-width question, and deuterium extension. Rebuilt and inspected both figures and revised the index promise. |
| `experiments/exp-11-alkali-spectra-quantum-defect.md` | Reviewed 2026-09-30 | Replaced a fit to mostly unavailable lines with level reconstruction from the visible D, 615 nm, and 568 nm lines plus an independent ionization limit. Distinguished measured 5s/3p/4d defects from the reference 3s defect and from a literal screened charge. Corrected D-line labels and spin–orbit claims, the unsupported kit-resolution promise, mercury resolution check, weak-line targets, near-IR potassium extension, and the index claim. Removed the impossible n=3 f level from the concept figure and rebuilt the reflective apparatus figure. |
| `experiments/exp-12-molecular-fluorescence.md` | Reviewed 2026-09-30 | Corrected the distinction between absorbance and emission density on a wavenumber axis, the Stokes/mirror and vibronic-spacing inferences, instrument and blank requirements, dye concentration conditions, UV controls, fit uncertainty, and optional quantum-yield/lifetime claims. Rebuilt and inspected both figures. |
| `experiments/exp-13-counting-statistics-and-half-life.md` | Reviewed 2026-09-30 | Replaced the ten-minute/15-minute timing conflict and low-count weighted least squares with interval-integrated Poisson likelihood including separate background counts. Corrected midpoint and dead-time effects, source controls, Gaussian goodness-of-fit expectations, GM attenuation limits, and figure source label. Rebuilt and inspected both figures. |
| `experiments/exp-14-cosmic-ray-muon-telescope.md` | Reviewed 2026-09-30 | Separated vertical per-steradian intensity from all-angle flux; corrected the ideal rate and achievable counting precision. Recast the one-altitude survival argument as a conditional model, revised coincidence/acceptance and angular analyses, removed an infeasible two-GM-tube lifetime measurement, and moved the absorber between tilted tubes in the rebuilt schematic. Inspected both figures. |

## Sources used for substantive corrections

- [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297), especially its [classification of Type A and Type B components](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty), [Type B models](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-4-type-b-evaluation-standard-uncertainty), and [coverage factors](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-6-expanded-uncertainty).
- [SciPy's `curve_fit` reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) specifies how `absolute_sigma` scales the returned parameter covariance.
- [OSHA's laser hazard classes](https://www.osha.gov/laser-hazards/hazards) describe Class 2 and 3R viewing risks; the [NRC's exposure guide](https://www.nrc.gov/facilities-safety/radiation-protection/how-the-nrc-protects-you/minimize-your-exposure) covers time, distance, shielding, and containment.
- [Tektronix's floating-measurement guide](https://www.tek.com/en/datasheet/floating-measurements-selection-guide) recommends rated differential probes or isolated inputs for floating signals. [NHS burn first aid](https://www.nhs.uk/conditions/burns-and-scalds/) gives the cool-running-water guidance.
- The [1887 Michelson–Morley paper](https://ajsonline.org/article/62505-on-the-relative-motion-of-the-earth-and-the-luminiferous-ether) supplies the historical shift scale. [NIST's HeNe metrology note](https://www.nist.gov/publications/uncalibrated-helium-neon-lasers-length-metrology) distinguishes laser wavelength and uncertainty.
- The [BIPM metre definition](https://www.bipm.org/en/si-base-units/metre) and its [practical realization guide](https://www.bipm.org/documents/20126/41489670/SI-App2-metre.pdf/0e011055-9736-d293-5e56-b8b1b267fd68?download=true&version=1.7) distinguish vacuum $c$ from propagation through air. [Tektronix's oscilloscope guidance](https://www.tek.com/en/support/faqs/how-bandwidth-related-rise-time-oscilloscopes) gives the approximate bandwidth–rise-time relation; its [RG-58 data](https://download.tek.com/datasheet/RSA600A-Datasheet-EN-US-37W-60397-12.pdf) uses a 0.66 velocity factor. [NASA's Rømer account](https://pwg.gsfc.nasa.gov/stargaze/Sun4Adop1.htm) describes the eclipse-timing method.
- The [Katz–Penfold range study](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.24.28) and [UTA beta-absorption procedure](https://cdn.web.uta.edu/-/media/project/website/science/physics/documents/degree-programs/physics-lab/nuclear-lab/lab-absorption-of-beta-particles.ashx?revision=c984b7a8-6329-425c-9c91-bcfff216de47) support a practical range from the terminal decline on linear count-rate axes, not a floor defined by counting uncertainty. [NNDC strontium-90](https://www.nndc.bnl.gov/nudat3/getdecaydataset.jsp?dsid=90sr+bM+decay+%2828.91+y%29&nucleus=90Y) and [yttrium-90](https://www.nndc.bnl.gov/nudat3/getdecaydataset.jsp?dsid=90y+bM+decay+%2864.05+h%29&nucleus=90ZR) evaluations supply the decay data. The [IAEA detector guide](https://nucleus.iaea.org/sites/connect/RRIHpublic/CompendiumDB/Shared%20Documents/Czech%20Republic%20CTU/Protocols%20in%20PDF/Czech_Rep_VR1_Reactor_Neutron_detection_Laboratory_protocol.pdf) describes the nonparalyzable dead-time model.
- The [University of Central Florida double-slit treatment](https://pressbooks.online.ucf.edu/osuniversityphysics3/chapter/double-slit-diffraction/) and [Cornell optics notes](https://muchomas.lassp.cornell.edu/p214/Notes/Interference/node24.html) explain finite-width envelopes and missing orders. The [air-wedge derivation](https://web.njit.edu/~tyson/MTSE451_LECT2_Pt1_CH35_YF_v2.pdf) relates dark-fringe order difference to gap thickness; the [UT Austin coherence notes](https://farside.ph.utexas.edu/teaching/315/Waveshtml/node92.html) give the source-width scale for two-slit visibility.
- The [Feynman grating derivation](https://www.feynmanlectures.caltech.edu/I_30.html) gives $mN$ for the ideal grating; this [University of Washington spectrograph lab](https://courses.washington.edu/phys331/concave_grating/concave_grating.pdf) explains the additional whole-instrument limitations. [Stony Brook's optical-disc project](https://www.stonybrook.edu/laser/_carolina/project/) gives nominal CD/DVD/Blu-ray pitches, while [Yale's disc teaching note](https://volga.eng.yale.edu/teaching-resources/cds-and-dvds/methods-and-materials) explains that along-track bit size also changes storage density. [University of Utah electron microscopy guidance](https://advanced-microscopy.utah.edu/education/electron-micro/index.html) gives the relativistic 100 keV wavelength and real imaging limitations.
- The [UCSB LED demonstration](https://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/88.10.html) documents method-dependent voltage and $h$ estimates; [Thorlabs' educational spectrometer description](https://punchout.thorlabs.com/newgrouppage9.cfm?objectgroup_id=6930) specifies scanning-detection options and photodiode range. The [William & Mary tungsten table](https://physics.wm.edu/~evmik/classes/manual_for_Experimental_Atomic_Physics/blackbody_new.pdf) supports a several-percent resistance–temperature approximation and notes temperature-dependent emissivity. [NIST's SI constants page](https://www.nist.gov/si-redefinition/meet-constants) gives the exact defining value of $h$.
- [Thorlabs' CPS532-C2 specifications](https://www.thorlabs.com/catalogpages/Obsolete/2015/CPS198.pdf) identify the EDU-QE1 supplied laser as Class 2; the [Thorlabs educational interferometer comparison](https://www.thorlabs.com/catalogpages/obsolete/2018/EDU-MINT1_M.pdf) distinguishes the Mach–Zehnder kit from a double-slit setup. [Englert's duality relation](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.2154) supports the ideal complementarity bound, while [Arndt and colleagues' $C_{60}$ diffraction report](https://www.nature.com/articles/44348) shows that a grating period need not equal the molecule's de Broglie wavelength.
- [MIT's barrier lecture](https://ocw.mit.edu/courses/6-772-compound-semiconductor-devices-spring-2003/cf610e766603218f5e15fe998daf18d4_Lecture6v2.pdf) gives the exact hyperbolic-sine transmission and its thick-barrier behavior. [UT Austin's FTIR derivation](https://farside.ph.utexas.edu/teaching/315/Waveshtml/node60.html) and [Harvard's optical demonstration](https://sciencedemonstrations.fas.harvard.edu/presentations/frustrated-total-internal-reflection) document evanescent coupling through a glass–air–glass gap. [UNSW's Newton's-rings explanation](https://www.animations.physics.unsw.edu.au/jw/light/Newton%27s-rings.html) gives the reflected-light ring-spacing relation.
- [MIT's acoustics chapter](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/50a609ff2cc992401a099bca53801474_MIT6_013S09_chap13.pdf) gives rectangular-cavity resonances and leading geometric mode counting. [University of Toronto's PDE text](https://www.math.toronto.edu/ivrii/PDE-textbook/Chapter13/S13.3.html) identifies Chladni plate modes with a fourth-order bending equation. [MIT's hydrogen discussion](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/4f14d9f9212e020419ee300ccd6fbf5d_G5_u6k9LR3E.pdf) distinguishes rotational degeneracy from the extra Coulomb-specific degeneracy. [Yale's Chladni demonstration](https://yppsweb2.its.yale.edu/physics/demos/demomain.asp?id=3D40.30&task=viewdemo) shows off-center excitation for nonsymmetric patterns.
- [NIST's critical hydrogen compilation](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=842564), Table 10 and its explanation, supplies observed standard-air Balmer wavelengths and describes the fine-structure and line-center limits. [NIST's mercury](https://physics.nist.gov/PhysRefData/Handbook/Tables/mercurytable2.htm) and [helium](https://physics.nist.gov/PhysRefData/Handbook/Tables/heliumtable2.htm) line tables supply the calibration anchors. [NIST's air/vacuum guidance](https://physics.nist.gov/PhysRefData/ASD/Html/lineshelp.html) describes standard-air conversion. [Thorlabs' EDU-SPEB2 description](https://punchout.thorlabs.com/newgrouppage9.cfm?objectgroup_id=6930) specifies reflective gratings and visual-kit components. [NIST's deuterium history](https://www.nist.gov/history/nbsnist-culture-excellence/harold-c-urey-ferdinand-g-brickwedde-and-discovery-deuterium) describes the 1931–32 spectral evidence.
- [NIST's Na I strong-line table](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable2.htm) and [Sansonetti's sodium compilation](https://www.nist.gov/system/files/documents/srd/jpcrd3720081763p.pdf) supply the sodium wavelengths, assignments, and extended energy levels; the [NIST Na I level table](https://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable5_a.htm) gives the 41449.451 cm⁻¹ ionization limit. [NIST's potassium line table](https://physics.nist.gov/PhysRefData/Handbook/Tables/potassiumtable2.htm) locates its principal pair in the near infrared.
- The [IUPAC Stokes-shift definition](https://goldbook.iupac.org/terms/view/S06031), [Kasha rule](https://old.goldbook.iupac.org/html/K/K03370.html), and [Franck–Condon entry](https://old.goldbook.iupac.org/pdf/F02510.pdf) delimit the molecular-spectroscopy interpretations. The [NIST fluorescence instrument guide](https://www.govinfo.gov/content/pkg/GOVPUB-C13-4c1a62e19ef69365ddf6454ba1bee6a8/pdf/GOVPUB-C13-4c1a62e19ef69365ddf6454ba1bee6a8.pdf) supports wavelength-response, inner-filter, quantum-yield, and lifetime controls. [NIST's fluorescein study](https://www.nist.gov/publications/raman-and-ftir-spectroscopies-fluorescein-solutions) describes pH-dependent species, and its [spectrophotometry guide](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication260-81.pdf) addresses stray light.
- [NIST's chi-square goodness-of-fit reference](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35f.htm) explains count-bin and fitted-parameter conditions. Its [lead](https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z82.html) and [aluminum](https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z13.html) attenuation tables bracket the 662 keV comparison; the [NRC's decay-in-storage guidance](https://www.nrc.gov/materials/toolboxes/llrw/decay-in-storage) requires controlled waste handling after short-lived activity decays.
- The [Particle Data Group cosmic-ray flux summary](https://pdg.lbl.gov/2017/html/Condensed_Reviews_Booklet_2016.pdf) distinguishes near-vertical muon intensity from integrated horizontal flux and describes the approximate angular law and mean ground energy. The [PDG muon listing](https://pdg.lbl.gov/2025/listings/rpp2025-list-muon.pdf) supplies mass and proper mean life. [NIST's GM-counter review](https://nvlpubs.nist.gov/nistpubs/Legacy/circ/nbscircular490.pdf) documents coincidence use and timing limits; this [stopped-muon scintillator experiment](https://doi.org/10.1088/1361-6404/ae66bb) shows the separate fast detector and decay-electron trigger required for a lifetime measurement. The [Rossi–Hall 1941 paper](https://supernovae.in2p3.fr/~llg/Enseignements/Agregation/Relativite/biblio/Rossi-et-Hall--1941.pdf) supports the historical two-altitude question.

## Verification and next work

- `npm run verify` passed: book structure, MyST metadata, and 28 experiment
  figures valid. The strict MyST site build passed for all 21 pages. The
  Python significant-figure helper was exercised on representative values
  including the printed `633.4 ± 0.8 nm` example and rounding boundaries.
- After Experiments 1–2, the verifier and strict 21-page site build passed
  again. Arithmetic checks give $63.3\ \mu\text{m}$ of motion for 200 fringes
  at 633 nm and about 2.23% displacement uncertainty from two independent
  $1\ \mu\text{m}$ endpoint readings. For Experiment 2, a 10 m path change
  produces about 33.36 ns of delay; a 30 cm RG-58 mismatch contributes about
  1.52 ns to the fixed channel offset, not the slope.
- After Experiment 3, the verifier and strict 21-page site build passed
  again. At 2.28 MeV, Feather and Katz–Penfold predict 1102.76 and
  1095.32 mg/cm² respectively, a 0.67% difference. A synthetic terminal and
  floor data check returned a practical range of 1090.84 ± 0.84 mg/cm²;
  its small counting error does not include fit-window or detector-model
  uncertainty. The revised SVG was rendered and visually inspected.
- After Experiment 4, the verifier and strict 21-page site build passed.
  At 650 nm, $d=0.25$ mm, and $L=2$ m, the fringe period is 5.20 mm, so a
  6 mm bare sensor sees only 1.15 periods. For the pre-lab $d/a=6.25$, there
  are 13 central integer orders and no exact missing first order. A 70 µm
  hair at 650 nm gives about 215 wedge intervals over 4 cm, spaced about
  0.186 mm. Both figures were rendered and inspected.
- After Experiment 5, the verifier and strict 21-page site build passed.
  A circular-aperture Airy cross section gives a 26.50% Rayleigh dip versus
  18.94% for the old sinc-squared slit surrogate. At 650 nm the CD/DVD
  first-order reflection angles are about 23.97°/61.45° at normal incidence;
  a 0.32 µm Blu-ray pitch has no propagating first order in air. A 100 keV
  electron's relativistic wavelength is 3.70 pm. Both revised figures were
  rendered and inspected.
- After Experiment 6, the verifier and strict 21-page site build passed.
  The revised micrometre-scaled LED slope calculation recovers the SI $h$
  from ideal synthetic data. With the stated $T_0=300$ K model, a 2500 K
  filament has $R/R_0\approx12.74$; an ideal 6 V source would drive 6.67 A
  through a 0.9 Ω cold filament, while a 2 A-limited supply would restrict
  startup. Both figures were rendered and inspected. This is 12 of 21
  student-facing pages reviewed; the index remains provisional.
- After Experiment 7, the verifier and strict 21-page site build passed.
  A synthetic harmonic profile with $V=0.65$ fitted to $V=0.652$.
  For the stated geometry, fringe spacing is 3.192 mm and a 6 mm bare sensor
  spans only 1.88 periods. A $720\ \mathrm{u}$ molecule at 200 m/s has
  $\lambda\approx2.77$ pm, giving a $2.77\times10^{-5}$ rad first-order angle
  for a 100 nm grating. The mean-occupancy-one power for 532 nm light in a
  1 m path is about 0.112 nW. Both revised SVGs were rendered and inspected;
  `git diff --check` passed. This is 13 of 21 student-facing pages reviewed.
- After Experiment 8, the verifier and strict 21-page site build passed.
  For $n=1.52$, $\theta=45°$, and $\lambda=650$ nm, the predicted
  intensity decay length is 131.3 nm. At $E=1$ eV and $V_0=5$ eV, the exact
  quantum $T$ is 0.303 at 0.10 nm and 0.0421 at 0.20 nm; the thick-barrier
  approximation is about 9% high at 0.10 nm. The code was executed below,
  at, and above $V_0$ and gives continuous, physical transmission. A
  synthetic optical tail recovers $\kappa=3.808\times10^6\ \mathrm{m}^{-1}$.
  Both revised SVGs were rendered and inspected. This is 14 of 21
  student-facing pages reviewed; the index remains provisional.
- After Experiment 9, the verifier and strict 21-page site build passed.
  For the revised $30\times20\times20$ cm example at 3 kHz, exact enumeration
  gives 58 acoustic mode triples but only 30 distinct ideal peak
  frequencies; the smooth volume and surface contributions are about 33.63
  and 19.23. A synthetic one-parameter fit recovered $v=343.019$ m/s from
  $343$ m/s input, while scaling $v$ and all lengths together left every
  frequency unchanged numerically. Shortening a 20 cm side by 10% splits
  the $(0,1,0)$ and $(0,0,1)$ fundamentals by 95.28 Hz exactly; the
  first-order prediction is 85.75 Hz. Both revised figures were rendered
  and inspected; `git diff --check` passed. This is 15 of 21
  student-facing pages reviewed, with the index provisional.
- After Experiment 10, the verifier and strict 21-page site build passed.
  The simple reduced-mass model with a constant 1.000277 air index predicts
  656.288, 486.139, 434.053, and 410.180 nm, rather than exactly reproducing
  the observed line centers in the NIST table. A synthetic four-line
  generalized least-squares fit with correlated calibration covariance
  recovered its input `R_H = 10967758` m⁻¹ and a positive fit uncertainty.
  Both revised SVGs were rendered and inspected; `git diff --check` passed.
  This is 16 of 21 student-facing pages reviewed; the index remains
  provisional.
- After Experiment 11, the verifier and strict 21-page site build passed.
  Using NIST standard-air wavelengths, an approximate air-index conversion,
  and the external ionization limit, the revised calculation gives
  $\delta_{3p}\approx0.88286$, $\delta_{5s}\approx1.35265$, and
  $\delta_{4d_{3/2}}\approx0.01227$. The D pair gives 17.20 cm⁻¹ and
  requires grating resolving power of at least about 987; separating the
  two 568.82 nm components would require about 474,000. A synthetic
  correlated-covariance propagation produced finite defect uncertainties.
  Both revised figures were rendered and inspected; `git diff --check`
  passed. This is 17 of 21 student-facing pages reviewed, with the
  index provisional.
- After Experiment 12, the verifier and strict 21-page site build passed.
  The 490/514 nm example gives a 952.91 cm⁻¹ (118.15 meV) Stokes shift;
  the stated molar absorptivity gives 13.16 µM or 4.37 mg/L for A = 1.
  With an illustrative 0.1% stray-light signal, true A = 2 and 3 appear
  as about 1.959 and 2.699. Both revised SVGs were rendered and inspected;
  `git diff --check` passed. This is 18 of 21 student-facing pages
  reviewed; the index remains provisional.
- After Experiment 13, the verifier and strict 21-page site build passed.
  A synthetic 90-bin, 10-second Poisson decay with a separate background
  count returned 152.42 s from a 153.12 s input half-life. Both example
  histogram expectation arrays summed to 300 observations. The integrated
  signal is 0.00854% above its midpoint approximation for a 10-second
  interval at this decay constant; equal-width intervals therefore do not
  shift the fitted slope. Both revised SVGs were rendered and inspected;
  `git diff --check` passed. This is 19 of 21 student-facing pages
  reviewed, with the index provisional.
- After Experiment 14 and the index, the verifier and strict 21-page site
  build passed. The illustrative ideal telescope rate is 0.5/minute, so
  30 minutes gives about 15 counts (26% Poisson uncertainty); 100 ideal
  counts take 200 minutes. The symmetric 1 µs accidental window with
  0.5/s singles on each channel predicts only 0.0054 accidents in three
  hours. For 10 cm² square detectors 10 cm apart, a two-million-track
  simulation gives $G_0=0.927$ cm² sr versus the $1.00$ cm² sr far-field
  approximation, and $G_{\cos^2}=0.899$ cm² sr. The 15 km, 1% survival
  model requires $\gamma\approx5.045$, not a bound extracted from the
  one-altitude telescope. Both revised SVGs were rendered and inspected;
  `git diff --check` passed. All 21 student-facing pages are now
  reviewed.
- Consider a print handout export from the checked source; the existing
  experiment exercises intentionally have no hidden solution dropdown
  because instructor notes are excluded from the student book.

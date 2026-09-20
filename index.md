---
title: Modern Physics Laboratory
short_title: Contents
label: lab-index
---

# Modern Physics Laboratory

Fourteen experiments, one per week, one per chapter of *Modern Physics:
Relativity, Quantum Theory, and the Structure of Matter*. Each experiment is
designed to fit a single three-hour laboratory period, to be built from
apparatus that a small department can keep working without a service contract,
and to be analyzed in Python rather than in a proprietary application.

## The schedule

```{list-table} Weekly experiments and the chapter each accompanies
:header-rows: 1
:label: tbl-schedule

* - Week
  - Experiment
  - Chapter
  - Central measurement
* - 1
  - [Michelson Interferometer and the Ether Null Result](#exp-michelson)
  - 1
  - Laser wavelength to $\sim0.1\%$; an upper bound on ether drift
* - 2
  - [The Speed of Light](#exp-speed-of-light)
  - 2
  - $c$ by time of flight over a few metres
* - 3
  - [Relativistic Electrons from Beta Decay](#exp-beta-electrons)
  - 3
  - $\beta$ endpoint energy; $v/c$ where the classical formula breaks
* - 4
  - [Interference of Light](#exp-interference)
  - 4
  - Slit separation and film thickness from fringe spacing
* - 5
  - [Diffraction and the Resolution Limit](#exp-diffraction)
  - 5
  - Slit width, grating pitch, and the Rayleigh criterion
* - 6
  - [Planck's Constant from Light-Emitting Diodes](#exp-planck-leds)
  - 6
  - $h$ to $\sim10\%$; the Stefan–Boltzmann exponent
* - 7
  - [The Quantum Eraser](#exp-quantum-eraser)
  - 7
  - Fringe visibility versus which-path information
* - 8
  - [Tunneling by Frustrated Total Internal Reflection](#exp-ftir-tunneling)
  - 8
  - Exponential decay of an evanescent wave across a barrier
* - 9
  - [Eigenmodes, Degeneracy, and Nodal Patterns](#exp-eigenmodes)
  - 9
  - A measured eigenvalue spectrum and its degeneracies
* - 10
  - [The Balmer Series and the Rydberg Constant](#exp-balmer)
  - 10
  - $R_\infty$ to $\sim0.5\%$
* - 11
  - [Alkali Spectra and the Quantum Defect](#exp-quantum-defect)
  - 11
  - Quantum defects $\delta_s,\delta_p,\delta_d$ for sodium
* - 12
  - [Molecular Fluorescence and the Stokes Shift](#exp-fluorescence)
  - 12
  - Absorption and emission spectra; Beer–Lambert law
* - 13
  - [Counting Statistics and Half-Life](#exp-counting-statistics)
  - 13
  - Poisson statistics; a half-life and an attenuation coefficient
* - 14
  - [A Cosmic-Ray Muon Telescope](#exp-muon-telescope)
  - 14
  - Muon flux, its $\cos^2\theta$ angular distribution, and time dilation
```

## What every experiment file contains

Each experiment is a single self-contained Markdown file with the same
sections in the same order, so that a student who has done one lab knows where
to look in all the others:

1. **Objectives** — what you should be able to do afterwards.
2. **Textbook connection** — the sections of the chapter this lab tests.
3. **Theory** — the derivation you need, and nothing more.
4. **Pre-lab** — questions to be answered *in your notebook before you arrive*.
   These are collected at the start of the period.
5. **Apparatus** — a checklist of what is on the bench.
6. **Safety** — read it; the laser and source labs are not optional reading.
7. **Procedure** — numbered steps, with instructor checkpoints marked `[ ]`.
8. **Analysis** — what to fit, how, and with what uncertainty model. Python
   scaffolding is provided; the physics is not.
9. **Post-lab questions** — what goes in the discussion section of your report.
10. **Going further** — optional extensions for students who finish early.


**Python instead of point-and-click.** Analysis is done in Jupyter with
`numpy`, `scipy.optimize`, and `matplotlib`. Fits report parameter
uncertainties from the covariance matrix, and every result is quoted as a
value, an uncertainty, and a unit. Old `.cap` and `.cmbl` data files remain
readable by exporting to CSV; see [](#python-toolkit).

**Uncertainty is the through-line.** Nearly every experiment produces a number
that has a known accepted value. The interesting question in each case is not
whether the number is close, but whether the *discrepancy is consistent with
the quoted uncertainty*. That question is worth more of the grade than the
measurement itself, and the [rubric](#lab-rubric) says so.

:::{note} A note on sources and safety
Radioactive sources, Class 2 and Class 3R lasers, and mains-powered heaters
appear in this manual. Every experiment that uses one carries a safety section
naming the specific hazard and the specific control. Read
[](#lab-safety) before Week 1.
:::

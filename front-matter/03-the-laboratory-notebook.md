---
title: The Laboratory Notebook and the Report
short_title: Notebook and Report
label: lab-notebook
---

# The Laboratory Notebook and the Report

These are two different documents with two different purposes, and the most
common mistake is to write one when the other was wanted.

The **notebook** is a contemporaneous record. Its test is: *could someone
repeat this measurement from what is written here, including the mistakes?*

The **report** is an argument. Its test is: *does a reader who was not there
believe the number, and know how much to believe it?*

---

## The notebook

Use a bound notebook with numbered pages — not a spiral pad, not loose sheets,
not a laptop file. Write in ink. When you make a mistake, draw a single line
through it so that it remains legible, and write what was wrong beside it. The
crossed-out entry is often the most useful thing on the page three weeks
later.

### What goes on the page

**Date, partner, experiment, and the instrument's identity.** "Tektronix
TBS1052B, bench 3, serial ...074" is worth writing down; when two groups get
different answers, the instrument is a suspect and you will want to know which
one you had.

**A sketch of the setup, with distances.** Thirty seconds of drawing saves an
hour of reconstruction. Label what you actually measured, with the origin
marked. Photographs supplement the sketch; they do not replace it, because a
photograph does not tell the reader which distance you called $L$.

**Raw readings, in the units the instrument displays.** Do not convert in your
head and record the converted value. If the counter reads $4127$ counts in
$60\ \text{s}$, write "4127 counts, 60 s", not "68.8 s$^{-1}$". Conversions
are recoverable; the raw reading is not.

**The uncertainty of each reading, decided at the time you take it.** Was it
the last-digit resolution of the display? The spread over three repeats? The
width over which you could not tell the fringe had moved? You know this at the
bench and you will be guessing at your desk.

**Tables drawn before they are filled.** A table with a header row and
labelled units, drawn empty, is a plan. A column of numbers written down the
margin is a puzzle.

**What went wrong, and what you did.** "First run: photodiode saturated above
$3\ \text{mm}$ aperture — added ND1 filter, retook from step 4." This sentence
is worth more to your report's discussion section than any of the good data.

**A running conclusion.** Before you leave, write one sentence: what number
did you get, and does it look right? This forces the twenty-minute in-room fit
described in [](#how-to-use).

### What the instructor checks

Notebooks are initialled at the end of every period — a signature that the
work in front of them was done that day — and graded four times a semester
against the [rubric](#lab-rubric). Grading is for completeness and
contemporaneity, not for neatness. A messy, honest, complete notebook scores
above a tidy one written up afterwards, and the difference is usually
detectable.

---

## The report

Reports follow the structure of a short experimental paper. Length: two to
three pages for a short report, five to eight for a full report, in both cases
excluding figures.

### Structure

**Title and abstract.** The abstract is three or four sentences and contains
the number. "We measured the wavelength of a helium–neon laser by counting
interference fringes in a Michelson interferometer as one mirror was
translated, obtaining $\lambda = 633.4 \pm 0.8\ \text{nm}$, consistent with the
accepted $632.816\ \text{nm}$." An abstract that promises the reader will find
a result, without stating it, has failed.

**Introduction** *(full reports only)*. What physical question is at stake and
why the measurement bears on it. Two paragraphs. Cite the textbook chapter and
at least one outside source.

**Theory.** The derivation of the equation you will fit, starting from
something the reader already accepts. Include the equation you actually use,
numbered, with every symbol defined. Do not reproduce the whole chapter.

**Apparatus and method.** Enough that a competent reader could repeat it.
A labelled figure — your sketch, redrawn, or a photograph with annotations —
does most of this work. Give model numbers and the quantities you controlled.

**Results.** The data, reduced. A figure showing the data *with error bars*
and the fitted curve; a table of fitted parameters with their uncertainties.
Every figure has a caption that states what is plotted and what the reader
should notice. Every number has a unit and an uncertainty.

**Discussion.** The part that is actually graded hardest. It must answer:

- Is the discrepancy from the accepted value consistent with the uncertainty?
  Quote the discrepancy in units of the combined uncertainty,
  $t = |x_{\text{meas}} - x_{\text{acc}}| / \sqrt{\sigma_{\text{meas}}^2 + \sigma_{\text{acc}}^2}$.
  A $t$ of $0.4$ means agreement; a $t$ of $6$ means something is wrong and you
  should say what you think it is.
- Which uncertainty dominates, and what would you change to reduce it?
  "Random" and "human error" are not answers. "The dominant term is the
  $\pm 0.5\ \text{mm}$ ruler reading on $L = 2.14\ \text{m}$; a laser
  rangefinder would reduce it tenfold and make the photodiode rise time the
  new limit" is an answer.
- What systematic effects could shift the result *in a particular direction*,
  and did you bound them?

**Conclusion.** One paragraph. The number, its uncertainty, and what it means.

**References.** Any consistent style, used consistently.

### On voice and tense

Write in the past tense for what you did ("the mirror was translated in
$50\ \mu\text{m}$ steps") and the present for what is true ("the fringe
spacing is inversely proportional to the slit separation"). First person
plural is fine and often clearer than the passive. Avoid "the experiment was
a success" — the reader will decide that.

### On figures

A figure that is not referred to in the text should be deleted. Axes are
labelled with quantity and unit. Data are points with error bars; fits are
lines without markers. Do not use a spreadsheet's default styling, do not
connect data points with straight segments, and do not plot a fit outside the
range of the data.

### On significant figures

Round the uncertainty to one significant figure (two if the leading digit is
1), then round the value to the same decimal place.
$\lambda = 633.4 \pm 0.8\ \text{nm}$, never $633.427 \pm 0.8113\ \text{nm}$.
This single habit accounts for a surprising fraction of the difference between
reports that read as competent and reports that do not.

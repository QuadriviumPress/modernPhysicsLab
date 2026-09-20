---
title: Grading Rubric
short_title: Rubric
label: lab-rubric
---

# Grading Rubric

## How the laboratory grade is composed

:::{list-table}
:header-rows: 1

* - Component
  - Weight
  - When
* - Pre-lab questions
  - 10%
  - Collected at the start of each period, 14 times
* - Notebook
  - 20%
  - Initialled weekly; graded in Weeks 3, 6, 10, 14
* - Short reports (11)
  - 35%
  - One week after the period
* - Full reports (3)
  - 25%
  - Weeks 4, 10, 14 — two weeks after the period
* - Participation and technique
  - 10%
  - Continuous
:::

The lowest short-report score is dropped. Full reports are not dropped.

---

## Report rubric

Each report is scored out of 100 against the criteria below. The weighting is
deliberate: **the discussion of uncertainty is worth more than the result.**
A report with a 12% discrepancy that correctly identifies why, and bounds it,
outscores one with a 1% discrepancy and no error analysis.

:::{list-table} Report scoring
:header-rows: 1

* - Criterion
  - Pts
  - What full credit looks like
* - **Abstract**
  - 5
  - Three to four sentences. States the method and the numerical result with
    its uncertainty and unit. A reader learns the answer without reading on.
* - **Theory**
  - 15
  - The working equation is derived or cited to a specific chapter section,
    every symbol is defined, and the assumptions that could fail in this
    apparatus are named. No unnecessary reproduction of the textbook.
* - **Apparatus and method**
  - 10
  - A labelled diagram or annotated photograph. Model numbers, controlled
    quantities, and ranges. A competent reader could repeat the measurement.
* - **Data and figures**
  - 15
  - Every figure has labelled axes with units, a caption stating what to
    notice, data as points *with error bars*, and fits as smooth curves.
    Tables carry units and uncertainties. Nothing is plotted outside the
    data's range.
* - **Analysis**
  - 20
  - The fit is weighted by real uncertainties. Parameter uncertainties come
    from the covariance matrix. $\chi^2_\nu$ is reported and interpreted.
    Residuals are shown or discussed. Propagation to the final quantity is
    correct and shown.
* - **Discussion of uncertainty**
  - 20
  - Type A and Type B contributions are separated and quantified. The
    dominant term is identified, with a concrete statement of what would
    reduce it. Systematic effects are named *with a sign or a bound*.
    The comparison to the accepted value is made in units of $\sigma$, not
    percent alone.
* - **Conclusion and writing**
  - 10
  - One paragraph with the number and what it means. Prose is clear, tenses
    consistent, significant figures correct throughout. References present.
* - **Notebook and code**
  - 5
  - Notebook pages for this experiment are attached or scanned; the Jupyter
    notebook runs top to bottom and produces the numbers in the text.
:::

### Automatic deductions

These are applied on top of the criteria above, because they are habits worth
breaking early:

- **−5** per figure with an unlabelled axis or a missing unit.
- **−5** per result quoted without an uncertainty.
- **−5** for uncertainties quoted to more than two significant figures, or
  values carried to more digits than the uncertainty supports.
- **−10** for an unweighted fit to logarithmically transformed data (see
  [](#uncertainty)).
- **−10** for a discussion whose only named error source is "human error".
- **Up to −100** for data or text that is not your own. Partners share data;
  everything else is individual work. See the course syllabus.

---

## Notebook rubric

Graded four times a semester, 25 points each.

:::{list-table} Notebook scoring
:header-rows: 1

* - Criterion
  - Pts
  - What full credit looks like
* - **Contemporaneity**
  - 6
  - Entries were plainly made at the bench: ink, in order, dated, with
    mistakes struck through and left legible rather than erased or recopied.
* - **Completeness**
  - 6
  - Date, partner, apparatus identity, a labelled sketch with dimensions,
    raw readings in the instrument's own units, and settings.
* - **Uncertainty at the point of measurement**
  - 5
  - Each reading carries the uncertainty you assigned *at the time*, with a
    one-line justification of where it came from.
* - **Narrative of what went wrong**
  - 4
  - Failed attempts, adjustments, and the reasoning behind them are recorded.
    A notebook with no problems in it is either luck or fiction.
* - **Running conclusion**
  - 4
  - A sentence at the end of each period stating the result obtained and
    whether it looked reasonable.
:::

:::{note} On neatness
Neatness is not a criterion. A crossed-out page that shows you caught your own
mistake is worth more than a clean page written up afterwards, and the
difference is usually visible. Write it as it happens.
:::

---

## Pre-lab rubric

Each pre-lab is scored out of 10, collected at the start of the period, and
not accepted late — its purpose is to prepare you for the next three hours,
which it cannot do afterwards.

- **4** — All questions attempted, with work shown.
- **4** — The order-of-magnitude estimate for the headline quantity is correct
  and is the number you will compare your first reading against.
- **2** — A one-sentence statement of what you expect to see, specific enough
  to be wrong.

---

## Participation and technique

Assessed continuously, not by attendance alone:

- Arrives having read the experiment, not having skimmed it.
- Aligns and operates the apparatus rather than watching a partner do it, and
  swaps roles at the halfway point.
- Handles lasers, sources, and instruments according to
  [](#lab-safety) without needing to be reminded.
- Leaves the bench in the state they would want to find it.
- Asks questions that follow an attempt to answer them.

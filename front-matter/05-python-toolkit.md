---
title: The Python Toolkit
short_title: Python Toolkit
label: python-toolkit
---

# The Python Toolkit

Analysis in this course is done in Python. You are not expected to arrive
knowing it; you are expected to leave able to load a CSV, fit a model, and
make a publication-quality figure with error bars.

## Setup

Any of these works. Pick one and stay with it.

**Recommended — a local environment.**

```bash
python -m venv phys320
source phys320/bin/activate        # Windows: phys320\Scripts\activate
pip install numpy scipy matplotlib pandas jupyterlab uncertainties
jupyter lab
```

**Alternative — Google Colab.** No installation; `numpy`, `scipy`,
`matplotlib`, and `pandas` are preinstalled. Add `!pip install uncertainties`
in the first cell. Mount your Drive to keep data with the notebook.

**Alternative — Anaconda.** Everything above already present. Heavier, but
fine.

Two packages beyond the standard scientific stack are worth having:

- [`uncertainties`](https://pythonhosted.org/uncertainties/) — arithmetic on
  numbers that carry an uncertainty, with correlations tracked automatically.
  Turns half a page of propagation algebra into one line.
- [`lmfit`](https://lmfit.github.io/lmfit-py/) — optional, but a real
  improvement over `curve_fit` when a model has bounded or fixed parameters,
  which happens in Experiments 8, 12, and 13.

## The five things you will do every week

### 1. Load data

```python
import numpy as np
import pandas as pd

df = pd.read_csv("week06_led_data.csv")     # header row with units in the name
print(df.head())
V, sV = df["V_on_V"].to_numpy(), df["sigma_V_V"].to_numpy()
```

Keep the raw file exactly as the instrument wrote it, and do the cleaning in
the notebook. A CSV that has been hand-edited in a spreadsheet cannot be
regenerated, and when the fit misbehaves you will want to know whether the
data or the cleaning is at fault.

### 2. Fit

See the template in [](#uncertainty). The two rules that matter:
always pass `sigma=`, and always pass `absolute_sigma=True`.

### 3. Propagate

```python
from uncertainties import ufloat, umath

L  = ufloat(2.143, 0.002)      # m
dt = ufloat(14.3e-9, 0.4e-9)   # s
c  = 2 * L / dt                # round trip
print(f"c = {c:.4g} m/s")      # uncertainty carried through automatically
```

`uncertainties` tracks correlations, so `x - x` is exactly zero with zero
uncertainty, as it should be — something the quadrature formula gets wrong if
applied blindly.

### 4. Plot

```python
import matplotlib.pyplot as plt
plt.rcParams.update({
    "figure.dpi": 130, "font.size": 11,
    "axes.grid": True, "grid.alpha": 0.3,
    "errorbar.capsize": 3,
})
```

Data are markers with error bars; models are lines without markers; axes carry
a quantity and a unit; the caption says what the reader should notice. Save as
PDF or SVG, not PNG, for anything that goes in a report.

### 5. Report the number

```python
def quote(value, err, unit=""):
    """Round err to one significant figure and value to match."""
    from math import floor, log10
    if err == 0:
        return f"{value:g} {unit}"
    d = -int(floor(log10(abs(err))))
    d += 1 if round(err, d) >= 10 ** (-d) * 9.5 else 0   # keep 1 sig fig
    return f"{round(value, d)} ± {round(err, d)} {unit}".strip()

print(quote(633.4271, 0.8113, "nm"))    # -> 633.4 ± 0.8 nm
```

## Reading data out of the instruments

:::{list-table} Getting numbers off the bench and into Python
:header-rows: 1

* - Instrument
  - Export path
  - Notes
* - Tektronix / Rigol oscilloscope
  - USB stick → CSV
  - Two columns, time and volts, with a multi-line header. `pd.read_csv(f, skiprows=N)`; check `N` against the file.
* - Thorlabs spectrometer kit (EDU-SPEA1/SPEB1)
  - Kit software → CSV
  - Wavelength in nm, intensity in counts. Take a dark spectrum and subtract it.
* - GM counter with serial output
  - `pyserial` → text
  - See the logging snippet below.
* - Arduino / Raspberry Pi Pico
  - Serial print → captured text
  - Print CSV lines directly; do not invent a binary format.
* - Phone or webcam image
  - PNG/JPEG → `imageio` or `PIL`
  - Shoot RAW or turn off auto-exposure and HDR, or the intensities are not linear.
* - Legacy PASCO `.cap` files
  - Capstone → *File ▸ Export Data* → CSV
  - Only needed for the archived data in `old/laboratoryHandouts/data/`.
* - Legacy Vernier `.cmbl` files
  - Logger *Pro* → *File ▸ Export As ▸ CSV*
  - Same.
:::

### Logging a serial stream

```python
import serial, time, csv

with serial.Serial("/dev/ttyACM0", 115200, timeout=2) as ser, \
     open("counts.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["t_s", "counts"])
    t0 = time.time()
    while time.time() - t0 < 3600:            # one hour
        line = ser.readline().decode().strip()
        if line:
            w.writerow([round(time.time() - t0, 3), line])
            f.flush()                          # survive a crash at minute 58
```

The `f.flush()` is not optional. A long acquisition that buffers everything in
memory and then dies has produced nothing.

### Images to intensity profiles

Experiments 4 and 5 photograph a fringe pattern and extract a profile.

```python
import numpy as np, imageio.v3 as iio

img = iio.imread("fringes.png").astype(float)
if img.ndim == 3:
    img = img[..., :3].mean(axis=2)          # to greyscale; see the caution below
row  = slice(540, 560)                        # a band through the pattern
prof = img[row, :].mean(axis=0)               # averaging the band kills noise
x_px = np.arange(prof.size)
```

:::{warning} Camera linearity
A JPEG from a phone has had gamma, white balance, and often local tone mapping
applied, none of which is linear in incident intensity. For quantitative
photometry, shoot RAW (or use a machine-vision camera), lock the exposure, and
verify linearity by imaging a target through calibrated neutral-density
filters before you trust an intensity ratio. For measuring fringe *positions*
— which is what Experiments 4 and 5 mostly need — nonlinearity is harmless,
because a monotonic transformation does not move a maximum.
:::

## Notebook hygiene

- **One notebook per experiment**, named for it, kept with the raw data.
- **Restart and run all before you submit.** A notebook whose cells were run
  out of order does not reproduce, and the number in the text may not be the
  number the code now produces.
- **Never hard-code a number you computed elsewhere.** If the fit gives the
  slope, the report's number must come from the fit variable.
- **Comment the physics, not the syntax.** `# lambda from fringe count, Eq. 3`
  is useful; `# fit the data` is not.
- **Submit the notebook with the report.** It is the analysis's raw notebook,
  and it is graded on the same contemporaneity principle.

"""Apparatus schematic for Experiment 11, alkali spectra and the quantum defect.

Reuses the Experiment 10 spectrometer layout with a sodium source and the
D-line doublet in place of the Balmer series.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from exp10_figure import spectrometer_layout
from labstyle import use_style

SODIUM_LINES = [
    (589.6, "D$_2$", "#d97706"),
    (589.0, "D$_1$", "#b8860b"),
]


def sodium_spectrometer():
    spectrometer_layout(
        source_label="sodium\ndischarge\nlamp",
        source_color="#ffb703",
        lines=SODIUM_LINES,
        name="exp11-sodium-spectrometer-schematic",
        extra_note=("Same spectrometer as Experiment 10, at its highest resolving power:\n"
                     "the sodium D lines sit close enough to test the instrument itself."),
    )


if __name__ == "__main__":
    use_style()
    sodium_spectrometer()

"""Apparatus schematic for Experiment 12, molecular fluorescence."""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, grating_lines, label, save, source_dot, use_style,
)


def _cuvette(ax, xy, w=0.34, h=0.55, color="#bfe3c4"):
    x, y = xy
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=color,
                            edgecolor=DARK, lw=1.3, zorder=4))


def fluorescence_panels():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.0))

    # --- (a) fluorescence, excitation at 90 degrees to detection -----------
    ax = axes[0]
    ax.set_aspect("equal")
    ax.axis("off")

    led = (-1.9, 0.0)
    box(ax, led, 0.75, 0.4, "excitation\nLED (405/470)", fontsize=6.8)
    source_dot(ax, (led[0] + 0.45, 0), color="#7b2fd6", ms=7, glow=False)
    beam(ax, (led[0] + 0.55, 0), (-0.2, 0), color="#7b2fd6", lw=1.6)

    cuvette = (0.0, 0.0)
    _cuvette(ax, cuvette)

    beam(ax, (0.0, 0.3), (0.0, 1.3), color="#2ecc71", lw=1.4, alpha=0.85)
    ax.add_patch(Rectangle((-0.14, 1.3), 0.28, 0.16, facecolor="#f4d35e",
                            edgecolor=DARK, lw=1.0, zorder=4))
    label(ax, (0.35, 1.38), "long-pass\nfilter", fontsize=6.6, ha="left")

    spec = (0.0, 2.2)
    box(ax, spec, 1.15, 0.45, "spectrometer\n(fiber input)", fontsize=6.8)
    beam(ax, (0.0, 1.46), (0.0, spec[1] - 0.24), color="#2ecc71", lw=1.4, alpha=0.85)

    label(ax, (0.0, -0.5), "cuvette\n(fluorophore solution)", fontsize=6.8, ha="center")
    label(ax, (-1.05, 0.55), "excitation\n(90$°$ to detection\navoids swamping\nthe weak signal)", fontsize=6.2, color=GRAY, ha="center")

    ax.set_title("(a)  emission (90$°$ geometry)", fontsize=9.3)
    ax.set_xlim(-2.6, 2.0)
    ax.set_ylim(-1.0, 2.9)

    # --- (b) absorption, in-line through the same cuvette -------------------
    ax = axes[1]
    ax.set_aspect("equal")
    ax.axis("off")

    lamp = (-2.0, 0.0)
    box(ax, lamp, 0.8, 0.45, "white LED /\ntungsten lamp", fontsize=6.8)
    source_dot(ax, (lamp[0] + 0.48, 0), color=ORANGE, ms=7, glow=False)
    beam(ax, (lamp[0] + 0.58, 0), (-0.18, 0), color=ORANGE, lw=1.6)

    _cuvette(ax, (0.0, 0.0))
    beam(ax, (0.18, 0), (1.1, 0), color=ORANGE, lw=1.6, alpha=0.85)

    spec2 = (1.9, 0.0)
    box(ax, spec2, 1.1, 0.5, "spectrometer\n(fiber input)", fontsize=6.8)

    label(ax, (0.0, -0.5), "same cuvette,\nin-line", fontsize=6.8, ha="center")
    label(ax, (0.0, 0.9), "reference spectrum with an empty\ncuvette gives the baseline", fontsize=6.6,
          color=GRAY, ha="center")

    ax.set_title("(b)  absorption (in-line)", fontsize=9.3)
    ax.set_xlim(-2.8, 2.7)
    ax.set_ylim(-1.0, 1.6)

    fig.tight_layout()
    save(fig, "exp12-fluorescence-schematic")


if __name__ == "__main__":
    use_style()
    fluorescence_panels()

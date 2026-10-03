"""Figures for Experiment 3, relativistic electrons from beta decay: the
apparatus schematic, and a concept figure for the absorption-curve shape."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    absorber_stack, beam, box, gm_tube, label, new_ax, save, use_style,
)


def beta_shelf_layout():
    fig, ax = new_ax(figsize=(6.6, 5.2))

    shelf_x = -1.6
    src = (shelf_x, -1.5)
    absorber_x = shelf_x + 0.9
    tube = (shelf_x + 2.2, 0.4)

    # shelf stand: a vertical post with numbered shelf slots
    ax.plot([shelf_x, shelf_x], [-1.7, 1.3], color=GRAY, lw=2.2, zorder=1)
    for y in (-1.5, -0.8, -0.1, 0.6):
        ax.plot([shelf_x - 0.12, shelf_x + 0.12], [y, y], color=GRAY, lw=1.6, zorder=1)

    # sealed source on the lowest shelf
    ax.add_patch(Circle((src[0], src[1]), 0.13, facecolor=ORANGE, edgecolor="#7a4a00", lw=1.0, zorder=4))
    label(ax, (src[0] - 0.05, src[1] - 0.32), r"$^{90}$Sr/$^{90}$Y" "\nsource", fontsize=7.5, ha="center")

    # emitted electrons, fanning up toward the tube
    for dy in (-0.15, 0.0, 0.15):
        beam(ax, src, (tube[0] - 0.5, tube[1] + dy), color=RED, lw=1.1, alpha=0.7, arrow=True)
    label(ax, (0.05, -0.75), r"$\beta^-$", color=RED, fontsize=10)

    # removable absorber slot between source and tube
    absorber_stack(ax, (absorber_x, -0.55), n=3, w=0.05, h=0.55, gap=0.05)
    label(ax, (absorber_x, -1.0), "Al absorber\nstack\n(removable)", fontsize=7, ha="center")

    # GM tube on an upper shelf, end window facing down toward the source
    gm_tube(ax, tube, length=1.0, angle_deg=100, color="#cfd8dc")
    label(ax, (tube[0] + 0.65, tube[1] + 0.25), "GM tube,\nthin end window", fontsize=7.5, ha="left")

    box(ax, (tube[0] + 0.3, tube[1] + 1.2), 1.3, 0.55, "counter / timer\n+ HV supply", fontsize=7.5)
    ax.plot([tube[0] + 0.15, tube[0] + 0.15], [tube[1] + 0.55, tube[1] + 0.93],
            color=PURPLE, lw=1.1, ls="--")

    label(ax, (0.3, 2.35),
          "Fixed geometry: swap absorber thicknesses and read the count rate\n"
          "through each one; the range in aluminium sets the endpoint energy.",
          fontsize=8.0, color=DARK, ha="center")

    ax.set_xlim(-2.6, 3.3)
    ax.set_ylim(-2.1, 2.7)
    save(fig, "exp03-beta-shelf-schematic")


def absorption_curve_figure():
    """Illustrative mixed-beta transmission and a linear terminal-range fit.

    The synthetic curve is chosen to show the analysis geometry, not to model
    the exact spectrum or source-detector response of a particular lab.
    """
    fig, (ax, zoom) = plt.subplots(1, 2, figsize=(9.2, 4.0))
    floor = 20.0  # illustrative background plus source-related photons
    x = np.linspace(0, 1600, 800)
    rate = floor + 600 * np.maximum(1 - x / 1100, 0) + 5000 * np.exp(-x / 130)

    ax.semilogy(x, rate, color=RED, lw=2.0)
    ax.axhline(floor, color=GRAY, ls=":", lw=1.0)
    ax.text(170, 1050, "mixed beta\ntransmission", fontsize=8.5, color=DARK)
    ax.text(1130, 28, "measured floor", fontsize=8, color=GRAY)
    ax.set_xlabel(r"Al thickness $x$ (mg/cm$^2$)")
    ax.set_ylabel(r"gross rate (s$^{-1}$, log scale)")
    ax.set_xlim(0, 1600)
    ax.set_ylim(10, 1e4)
    ax.set_title("Full curve", fontsize=10)

    fit_x = np.array([650, 725, 800, 875, 950, 1025], dtype=float)
    fit_rate = floor + 600 * np.maximum(1 - fit_x / 1100, 0) + 5000 * np.exp(-fit_x / 130)
    slope, intercept = np.polyfit(fit_x, fit_rate, 1)
    tail_x = np.array([1200, 1300, 1400, 1500], dtype=float)
    tail_rate = floor + 5000 * np.exp(-tail_x / 130)
    measured_floor = tail_rate.mean()
    practical_range = (measured_floor - intercept) / slope

    zoom.plot(x, rate, color=RED, lw=1.8)
    zoom.plot(fit_x, fit_rate, "o", color=BLUE, ms=4)
    zoom.plot(tail_x, tail_rate, "o", color=PURPLE, ms=4)
    zoom.axhline(measured_floor, color=GRAY, ls=":", lw=1.0)
    fit_line_x = np.linspace(fit_x.min(), practical_range, 100)
    zoom.plot(fit_line_x, intercept + slope * fit_line_x, color=DARK, ls="--", lw=1.2)
    zoom.plot(practical_range, measured_floor, "o", color=PURPLE, ms=6)
    zoom.annotate(r"$R_m$", xy=(practical_range, measured_floor),
                  xytext=(practical_range + 110, 125), fontsize=10, color=PURPLE,
                  arrowprops=dict(arrowstyle="-", color=PURPLE, lw=0.9))
    zoom.text(670, 320, "terminal fit", fontsize=8, color=DARK)
    zoom.text(1250, 43, "floor", fontsize=8, color=GRAY)
    zoom.set_xlabel(r"Al thickness $x$ (mg/cm$^2$)")
    zoom.set_ylabel(r"gross rate (s$^{-1}$, linear scale)")
    zoom.set_xlim(600, 1600)
    zoom.set_ylim(0, 380)
    zoom.set_title("Terminal region", fontsize=10)

    fig.tight_layout()
    save(fig, "exp03-absorption-curve-concept")


if __name__ == "__main__":
    use_style()
    beta_shelf_layout()
    absorption_curve_figure()

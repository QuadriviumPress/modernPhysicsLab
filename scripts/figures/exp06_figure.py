"""Figures for Experiment 6, Planck's constant from LEDs: the apparatus
schematic, and a concept figure for the turn-on-voltage fit."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Wedge

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, grating_lines, label, save, use_style,
)


def _led_icon(ax, xy, color=RED, size=0.22):
    x, y = xy
    ax.add_patch(Wedge((x, y), size, 200, 160 + 360, facecolor=color, edgecolor=DARK, lw=1.0, zorder=4))
    ax.plot([x - size, x - size], [y - size * 0.55, y + size * 0.55], color=DARK, lw=1.4, zorder=4)


def led_and_lamp_panels():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.9))

    # --- (a) LED forward-bias I-V circuit ---------------------------------
    ax = axes[0]
    ax.set_aspect("equal")
    ax.axis("off")

    supply = (-1.7, 0.0)
    box(ax, supply, 0.75, 0.6, "variable\nsupply\n0-5 V", fontsize=6.8)

    # loop: supply -> resistor -> LED -> back to supply, with meters
    ax.plot([-1.3, -0.5], [0.55, 0.55], color=DARK, lw=1.4)
    ax.add_patch(Rectangle((-0.5, 0.42), 0.4, 0.26, facecolor="white", edgecolor=DARK, lw=1.2, zorder=3))
    label(ax, (-0.3, 0.55), r"$100\,\Omega$", fontsize=6.8)
    ax.plot([-0.1, 0.45], [0.55, 0.55], color=DARK, lw=1.4)

    _led_icon(ax, (0.7, 0.55), color=RED)
    label(ax, (0.7, 0.95), "LED\nunder test", fontsize=6.8)
    ax.plot([0.95, 1.35], [0.55, 0.55], color=DARK, lw=1.4)
    ax.plot([1.35, 1.35], [0.55, -0.55], color=DARK, lw=1.4)
    ax.plot([1.35, -1.3], [-0.55, -0.55], color=DARK, lw=1.4)
    ax.plot([-1.3, -1.3], [-0.55, 0.55], color=DARK, lw=1.4)

    ax.add_patch(Circle((0.15, -0.55), 0.16, facecolor="white", edgecolor=BLUE, lw=1.3, zorder=4))
    label(ax, (0.15, -0.55), "A", color=BLUE, fontsize=8, weight="bold")
    label(ax, (0.15, -0.85), "ammeter", color=BLUE, fontsize=6.5)

    ax.add_patch(Circle((0.35, 1.0), 0.16, facecolor="white", edgecolor=PURPLE, lw=1.3, zorder=4))
    label(ax, (0.35, 1.0), "V", color=PURPLE, fontsize=8, weight="bold")
    ax.plot([0.35, 0.55], [0.84, 0.63], color=PURPLE, lw=1.0)
    ax.plot([0.35, 0.85], [0.84, 0.63], color=PURPLE, lw=1.0)
    label(ax, (0.65, 1.25), "voltmeter\nacross LED", color=PURPLE, fontsize=6.5)

    ax.set_title("(a)  LED turn-on voltage", fontsize=9.5)
    ax.set_xlim(-2.3, 2.0)
    ax.set_ylim(-1.2, 1.6)

    # --- (b) tungsten lamp continuum, through the spectrometer -------------
    ax = axes[1]
    ax.set_aspect("equal")
    ax.axis("off")

    lamp = (-1.6, 0.0)
    box(ax, lamp, 0.85, 0.5, "tungsten\nlamp", fontsize=7.2)
    ax.add_patch(Circle((lamp[0] + 0.55, 0), 0.1, facecolor=ORANGE, edgecolor="#7a4a00", lw=0.8, zorder=4))

    beam(ax, (lamp[0] + 0.7, 0), (-0.35, 0), color=ORANGE, lw=1.6)

    spec = (0.6, 0.0)
    ax.plot([0.15, 0.15], [-0.55, 0.55], color=DARK, lw=2.2, zorder=3)
    grating_lines(ax, (0.85, 0), height=0.9, n=9)
    for dy in (-0.55, -0.2, 0.15, 0.5):
        beam(ax, (0.9, 0), (1.8, dy), color=ORANGE, lw=1.0, alpha=0.6)
    label(ax, (0.5, 1.0), "spectrometer\n(slit + grating)", fontsize=7.2)

    ax.add_patch(Rectangle((1.85, -0.7), 0.12, 1.4, facecolor="#eeeeee", edgecolor=DARK, lw=1.0, zorder=3))
    label(ax, (2.35, 0), "linear\ndetector\narray", fontsize=6.8, ha="left")

    ax.set_title("(b)  filament color vs. temperature", fontsize=9.5)
    ax.set_xlim(-2.4, 3.1)
    ax.set_ylim(-1.2, 1.6)

    fig.tight_layout()
    save(fig, "exp06-led-planck-schematic")


def led_fit_figure():
    """V_on against 1/lambda: a straight line of slope hc/e, with a
    nonzero intercept that carries the diode's own physics."""
    fig, ax = plt.subplots(figsize=(6.2, 4.3))

    hc_over_e = 1.23984  # V*um, so that V = hc_over_e * (1/lambda[um]) + V_offset
    V_offset = -0.15
    wavelengths = np.array([940, 630, 590, 525, 470, 405])  # nm
    colors = [DARK, RED, ORANGE, "#8a9a3a", BLUE, PURPLE]
    x = 1000.0 / wavelengths  # 1/lambda, in 1/um
    rng = np.random.default_rng(7)
    V = hc_over_e * x + V_offset + rng.normal(0, 0.035, size=x.size)

    xfit = np.linspace(0, x.max() * 1.15, 100)
    ax.plot(xfit, hc_over_e * xfit + V_offset, color=GRAY, lw=1.6, zorder=2)
    for xi, Vi, c in zip(x, V, colors):
        ax.plot(xi, Vi, "o", color=c, ms=7, zorder=3)
    ax.plot([0], [V_offset], marker="o", mfc="white", mec=PURPLE, mew=1.6, ms=7, zorder=4)

    ax.annotate(r"slope $= hc/e$", xy=(1.6, hc_over_e * 1.6 + V_offset),
                xytext=(0.55, 2.5), fontsize=9.5, color=DARK,
                arrowprops=dict(arrowstyle="-", color=DARK, lw=0.9))
    ax.annotate(r"intercept $V_{\rm offset}$", xy=(0, V_offset),
                xytext=(0.45, V_offset - 0.55), fontsize=9, color=PURPLE,
                arrowprops=dict(arrowstyle="-", color=PURPLE, lw=0.9))

    ax.axhline(0, color=GRAY, lw=0.7, alpha=0.5)
    ax.set_xlabel(r"$1/\lambda$  ($\mu$m$^{-1}$)")
    ax.set_ylabel(r"$V_{\rm on}$ (V)")
    ax.set_xlim(0, x.max() * 1.15)
    ax.set_ylim(V_offset - 0.7, hc_over_e * x.max() * 1.15 + V_offset + 0.3)
    ax.set_title("Turn-on voltage versus inverse wavelength", fontsize=10)

    fig.tight_layout()
    save(fig, "exp06-led-fit-concept")


if __name__ == "__main__":
    use_style()
    led_and_lamp_panels()
    led_fit_figure()

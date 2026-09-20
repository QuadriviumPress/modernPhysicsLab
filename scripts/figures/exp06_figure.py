"""Apparatus schematic for Experiment 6, Planck's constant from LEDs."""

import matplotlib.pyplot as plt
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


if __name__ == "__main__":
    use_style()
    led_and_lamp_panels()

"""Figures for Experiment 9, eigenmodes and nodal patterns: the apparatus
schematic, and a concept figure for mode counting / density of states."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Wedge

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    box, label, mic_icon, save, speaker_icon, use_style,
)


def cavity_and_chladni_panels():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.2))

    # --- (a) rectangular acoustic cavity -----------------------------------
    ax = axes[0]
    ax.set_aspect("equal")
    ax.axis("off")

    w, h = 2.6, 1.6
    ax.add_patch(Rectangle((-w / 2, -h / 2), w, h, facecolor="#f4f6f8", edgecolor=DARK, lw=2.0, zorder=2))
    speaker_icon(ax, (-w / 2 + 0.18, -h / 2 + 0.18), size=0.3, angle_deg=45)
    mic_icon(ax, (w / 2 - 0.18, h / 2 - 0.18), r=0.11)
    label(ax, (-w / 2 + 0.1, -h / 2 - 0.28), "speaker\n(corner-mounted)", fontsize=6.8, ha="left")
    label(ax, (w / 2 - 0.1, h / 2 + 0.35), "microphone\n(opposite corner)", fontsize=6.8, ha="right")

    # a movable partition, sketched as a dashed insertable wall
    ax.plot([0.4, 0.4], [-h / 2, h / 2], color=PURPLE, lw=1.6, ls="--", zorder=3)
    label(ax, (0.62, -h / 2 + 0.18), "movable\npartition", fontsize=6.4, color=PURPLE, ha="left")

    label(ax, (-w / 2 + 0.05, 0.0), "$L_x$", color=GRAY, fontsize=9, ha="left")
    ax.annotate("", xy=(-w / 2, -h / 2 - 0.55), xytext=(w / 2, -h / 2 - 0.55),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    label(ax, (0, -h / 2 - 0.75), "$L_x$", color=GRAY, fontsize=8.5)
    ax.annotate("", xy=(w / 2 + 0.4, -h / 2), xytext=(w / 2 + 0.4, h / 2),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    label(ax, (w / 2 + 0.62, 0), "$L_y$", color=GRAY, fontsize=8.5)

    box(ax, (0, -1.7), 1.5, 0.4, "function generator", fontsize=6.8)
    box(ax, (0, 1.75), 1.5, 0.4, "sound card / ADC", fontsize=6.8)
    ax.plot([-w / 2 + 0.18, -w / 2 + 0.18], [-h / 2 + 0.05, -1.5], color=DARK, lw=0.9, ls=":")
    ax.plot([w / 2 - 0.18, w / 2 - 0.18], [h / 2 - 0.05, 1.55], color=DARK, lw=0.9, ls=":")

    ax.set_title("(a)  rectangular cavity", fontsize=9.5)
    ax.set_xlim(-2.2, 2.6)
    ax.set_ylim(-2.2, 2.3)

    # --- (b) Chladni plate --------------------------------------------------
    ax = axes[1]
    ax.set_aspect("equal")
    ax.axis("off")

    r = 1.1
    ax.add_patch(Circle((0, 0), r, facecolor="#e9edf1", edgecolor=DARK, lw=1.6, zorder=2))
    # a simple two-lobe nodal-line pattern with scattered sand grains
    th = np.linspace(0, 2 * np.pi, 400)
    nodal = r * 0.62 * np.abs(np.cos(2 * (th - np.pi / 4)))
    ax.plot(nodal * np.cos(th), nodal * np.sin(th), color=RED, lw=1.3, zorder=3)
    rng = np.random.default_rng(3)
    n_grains = 220
    ang = rng.uniform(0, 2 * np.pi, n_grains)
    rad = r * np.sqrt(rng.uniform(0, 1, n_grains))
    keep = np.abs(rad - r * 0.62 * np.abs(np.cos(2 * (ang - np.pi / 4)))) < 0.05
    ax.plot(rad[keep] * np.cos(ang[keep]), rad[keep] * np.sin(ang[keep]),
            marker="o", ms=1.6, ls="none", color="#8a6d3b", zorder=4)

    ax.add_patch(Circle((0, 0), 0.07, facecolor=GRAY, edgecolor=DARK, lw=0.8, zorder=5))
    ax.plot([0, 0], [-r - 0.5, -0.07], color=DARK, lw=1.6, zorder=2)
    speaker_icon(ax, (0, -r - 0.75), size=0.35, angle_deg=90)
    label(ax, (0, -r - 1.15), "speaker driver\n(below, on center bolt)", fontsize=6.8)
    label(ax, (0, r + 0.35), "fine sand traces\nthe nodal lines", fontsize=6.8, color=RED)

    ax.set_title("(b)  Chladni plate", fontsize=9.5)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-2.4, 1.9)

    fig.tight_layout()
    save(fig, "exp09-eigenmodes-schematic")


def mode_counting_figure():
    """Mode counting as lattice points inside a quarter circle: the 2D
    analogue of the octant-of-an-ellipsoid argument behind eq-dos."""
    fig, ax = plt.subplots(figsize=(5.6, 5.6))
    ax.set_aspect("equal")

    R = 8.6
    nmax = 12
    nx, ny = np.meshgrid(np.arange(1, nmax + 1), np.arange(1, nmax + 1))
    nx, ny = nx.ravel(), ny.ravel()
    r = np.sqrt(nx**2 + ny**2)
    inside = r <= R

    ax.add_patch(Wedge((0, 0), R, 0, 90, facecolor="#dbe9f5", edgecolor="none", zorder=0))
    ax.plot(nx[~inside], ny[~inside], "o", color="#c9d6e0", ms=5, zorder=2)
    ax.plot(nx[inside], ny[inside], "o", color=BLUE, ms=5, zorder=3)

    arc = np.linspace(0, np.pi / 2, 100)
    ax.plot(R * np.cos(arc), R * np.sin(arc), color=PURPLE, lw=1.8, zorder=1)
    label(ax, (R * np.cos(np.pi / 4) + 0.6, R * np.sin(np.pi / 4) + 0.6),
          r"$n_x^2+n_y^2 = (2Lf/v)^2$", color=PURPLE, fontsize=8.5, ha="left")

    n_inside = int(inside.sum())

    ax.set_xlabel(r"$n_x$")
    ax.set_ylabel(r"$n_y$")
    ax.set_xlim(0, nmax + 0.5)
    ax.set_ylim(0, nmax + 0.5)
    ax.set_title("Counting modes below a frequency $f$", fontsize=10)

    fig.tight_layout()
    fig.text(0.5, -0.02,
              f"{n_inside} lattice points inside the quarter circle — " r"$N(f) \approx \frac{\pi}{4}R^2$ (2D analogue of the octant-of-an-ellipsoid count in the text)",
              fontsize=8.3, color=DARK, ha="center")
    save(fig, "exp09-mode-counting-concept")


if __name__ == "__main__":
    use_style()
    cavity_and_chladni_panels()
    mode_counting_figure()

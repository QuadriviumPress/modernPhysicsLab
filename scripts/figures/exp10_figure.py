"""Figures for Experiment 10, the Balmer series and the Rydberg constant:
the apparatus schematic, and the hydrogen energy-level concept figure."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from labstyle import (
    GRAY, DARK,
    beam, box, grating_lines, label, new_ax, save, use_style,
)

BALMER = [(656, "$H_\\alpha$", "#c0392b"), (486, "$H_\\beta$", "#1769aa"),
          (434, "$H_\\gamma$", "#6a4c93"), (410, "$H_\\delta$", "#4b0082")]


def spectrometer_layout(source_label="hydrogen\ndischarge tube",
                         source_color="#e08fd6",
                         lines=BALMER,
                         name="exp10-balmer-spectrometer-schematic",
                         extra_note=None):
    fig, ax = new_ax(figsize=(8.2, 4.4))

    tube = (-3.3, -1.0)
    box(ax, tube, 1.4, 0.5, source_label, fontsize=7.1)
    ax.add_patch(Rectangle((tube[0] + 0.5, tube[1] - 0.16), 0.1, 0.32,
                            facecolor=source_color, edgecolor="#7a4a6a", lw=0.8, zorder=4))

    slit = (-1.5, -1.0)
    beam(ax, (tube[0] + 0.68, -1.0), (slit[0] - 0.1, -1.0), color=source_color, lw=1.6)
    ax.plot([slit[0], slit[0]], [-1.55, -1.08], color=DARK, lw=2.2, zorder=3)
    ax.plot([slit[0], slit[0]], [-0.92, -0.45], color=DARK, lw=2.2, zorder=3)
    label(ax, (slit[0], -2.05), "adjustable\nentrance slit", fontsize=7.2)

    collimator = (-0.4, -1.0)
    beam(ax, (slit[0] + 0.08, -1.0), (collimator[0] - 0.14, -1.0), color=source_color, lw=1.6)
    from labstyle import lens_biconvex
    lens_biconvex(ax, collimator, height=1.0, thickness=0.12)
    label(ax, (collimator[0], -2.05), "collimating\nlens", fontsize=7.2)

    grating = (1.1, -1.0)
    beam(ax, (collimator[0] + 0.14, -1.0), (grating[0] - 0.05, -1.0), color=source_color, lw=1.6)
    grating_lines(ax, grating, height=1.0, n=11)
    label(ax, (2.2, -0.95), "reflective grating\non mount", fontsize=7.2)

    heights = np.linspace(1.85, 0.25, len(lines))
    for (_, sym, c), yy in zip(lines, heights):
        beam(ax, (grating[0] - 0.05, -1.0), (-1.0, yy), color=c, lw=1.3, alpha=0.85)
        label(ax, (-1.18, yy), sym, color=c, fontsize=8, ha="right")

    label(ax, (-2.75, 0.25), "viewer selects one\nreturned direction", fontsize=7.0, color=GRAY)

    title = ("Reflective-grating path: the separated colors return\n"
             "toward the incident side (angles schematic).")
    if extra_note:
        title = extra_note
    label(ax, (0.35, 2.2), title, fontsize=7.8, color=DARK, ha="center")

    ax.set_xlim(-4.1, 3.25)
    ax.set_ylim(-2.5, 2.55)
    save(fig, name)


def energy_levels_figure():
    """Hydrogen energy levels (schematic spacing, rounded model eV values)
    with the Balmer series marked, and one Lyman and one Paschen line for
    context."""
    fig, ax = plt.subplots(figsize=(6.6, 5.6))

    levels = {1: 0.0, 2: 3.05, 3: 4.55, 4: 5.45, 5: 6.05, 6: 6.5}
    E = {n: -13.6 / n**2 for n in levels}
    continuum_y = 7.4
    xmax = 4.2

    for n, y in levels.items():
        ax.plot([0, xmax], [y, y], color=DARK, lw=1.6, zorder=2)
        label(ax, (-0.18, y), f"$n={n}$", fontsize=8.5, ha="right", va="center")
        label(ax, (xmax + 0.18, y), f"${E[n]:.2f}$ eV", fontsize=7.6, color=GRAY, ha="left", va="center")
    ax.plot([0, xmax], [continuum_y, continuum_y], color=GRAY, lw=1.2, ls="--", zorder=2)
    label(ax, (xmax + 0.18, continuum_y), "0 eV\n(continuum)", fontsize=7.6, color=GRAY, ha="left", va="center")

    balmer_x = {3: 1.0, 4: 1.7, 5: 2.4, 6: 3.1}
    for (wl, tex, color), (n, x) in zip(BALMER, balmer_x.items()):
        ax.annotate("", xy=(x, levels[2] + 0.06), xytext=(x, levels[n] - 0.06),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6))
        label(ax, (x, levels[n] + 0.22), tex, fontsize=8.5, color=color)

    ax.annotate("", xy=(3.8, levels[1] + 0.06), xytext=(3.8, levels[2] - 0.06),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.3, alpha=0.8))
    label(ax, (3.8, (levels[1] + levels[2]) / 2), "Lyman-$\\alpha$\n(UV)", fontsize=7.2, color=GRAY, ha="left")

    ax.annotate("", xy=(0.35, levels[3] + 0.06), xytext=(0.35, levels[4] - 0.06),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.3, alpha=0.8))
    label(ax, (0.35, (levels[3] + levels[4]) / 2), "Paschen-$\\alpha$\n(IR)", fontsize=7.2, color=GRAY, ha="right")

    ax.set_title("Hydrogen energy levels and the Balmer series\n(level spacing schematic; model $E_n$ rounded)", fontsize=9.5)
    ax.set_xlim(-1.3, xmax + 1.3)
    ax.set_ylim(-0.6, continuum_y + 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()
    save(fig, "exp10-energy-levels-concept")


if __name__ == "__main__":
    use_style()
    spectrometer_layout()
    energy_levels_figure()

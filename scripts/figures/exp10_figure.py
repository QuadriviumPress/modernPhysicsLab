"""Figures for Experiment 10, the Balmer series and the Rydberg constant:
the apparatus schematic, and the hydrogen energy-level concept figure."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, grating_lines, label, new_ax, rotation_stage, save, use_style,
)

BALMER = [(656, "$H_\\alpha$", "#c0392b"), (486, "$H_\\beta$", "#1769aa"),
          (434, "$H_\\gamma$", "#6a4c93"), (410, "$H_\\delta$", "#4b0082")]


def spectrometer_layout(source_label="hydrogen\ndischarge tube",
                         source_color="#e08fd6",
                         lines=BALMER,
                         name="exp10-balmer-spectrometer-schematic",
                         extra_note=None):
    fig, ax = new_ax(figsize=(8.2, 4.4))

    tube = (-3.3, 0.0)
    box(ax, tube, 0.9, 0.5, source_label, fontsize=7.4)
    ax.add_patch(Rectangle((tube[0] + 0.5, tube[1] - 0.16), 0.1, 0.32,
                            facecolor=source_color, edgecolor="#7a4a6a", lw=0.8, zorder=4))

    slit = (-1.5, 0.0)
    beam(ax, (tube[0] + 0.68, 0), (slit[0] - 0.1, 0), color=source_color, lw=1.6)
    ax.plot([slit[0], slit[0]], [-0.9, -0.08], color=DARK, lw=2.2, zorder=3)
    ax.plot([slit[0], slit[0]], [0.08, 0.9], color=DARK, lw=2.2, zorder=3)
    label(ax, (slit[0], 1.15), "adjustable\nentrance slit", fontsize=7.2)

    collimator = (-0.4, 0.0)
    beam(ax, (slit[0] + 0.08, 0), (collimator[0] - 0.14, 0), color=source_color, lw=1.6)
    from labstyle import lens_biconvex
    lens_biconvex(ax, collimator, height=1.0, thickness=0.12)
    label(ax, (collimator[0], -1.15), "collimating\nlens", fontsize=7.2)

    grating = (1.1, 0.0)
    beam(ax, (collimator[0] + 0.14, 0), (grating[0] - 0.05, 0), color=source_color, lw=1.6)
    grating_lines(ax, grating, height=1.0, n=11)
    rotation_stage(ax, grating, r=0.75, angle_deg=200, color=GRAY)
    label(ax, (grating[0], 1.35), "grating on a\nvernier turntable", fontsize=7.2)

    if len(lines) <= 2:
        dys = np.linspace(0.85, 0.65, len(lines))
    else:
        dys = np.linspace(1.15, 0.35, len(lines))
    for (wl, sym, c), dy in zip(lines, dys):
        beam(ax, (grating[0] + 0.05, 0), (grating[0] + 1.9, dy), color=c, lw=1.3, alpha=0.85)
        label(ax, (grating[0] + 2.05, dy), sym, color=c, fontsize=8, ha="left")
    beam(ax, (grating[0] + 0.05, 0), (grating[0] + 1.9, 0), color=GRAY, lw=1.0, alpha=0.6)
    label(ax, (grating[0] + 2.05, 0), "$m=0$", color=GRAY, fontsize=7.2, ha="left")

    label(ax, (grating[0] + 0.5, -1.55),
          "detector or eyepiece\nswings on the turntable arm", fontsize=7.0, color=GRAY, ha="center")

    title = ("Collimated light meets the grating; each wavelength diffracts to its own\n"
             "angle, read off the turntable vernier to the Rydberg formula.")
    if extra_note:
        title = extra_note
    label(ax, (0.1, 2.1), title, fontsize=7.8, color=DARK, ha="center")

    ax.set_xlim(-4.1, 4.6)
    ax.set_ylim(-2.0, 2.5)
    save(fig, name)


def energy_levels_figure():
    """Hydrogen energy levels (schematic spacing, true eV values labelled)
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

    ax.set_title("Hydrogen energy levels and the Balmer series\n(level spacing schematic; $E_n$ values are exact)", fontsize=9.5)
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

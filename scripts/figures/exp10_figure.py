"""Apparatus schematic for Experiment 10, the Balmer series and the Rydberg constant."""

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


if __name__ == "__main__":
    use_style()
    spectrometer_layout()

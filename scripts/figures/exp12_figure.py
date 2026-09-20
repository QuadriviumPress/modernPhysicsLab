"""Figures for Experiment 12, molecular fluorescence: the apparatus
schematic, and the Franck-Condon potential-energy-curve concept figure."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from labstyle import (
    BLUE, GRAY, GREEN, ORANGE, PURPLE, RED, DARK,
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


def franck_condon_figure():
    """Ground and excited electronic potential-energy curves, offset in
    bond length, with the vertical absorption/emission transitions,
    vibrational relaxation, and the resulting Stokes shift."""
    fig, ax = plt.subplots(figsize=(6.6, 5.2))

    k, r_g, r_e, E0 = 1.0, 0.0, 1.3, 6.0
    r = np.linspace(-1.6, 3.2, 400)
    Eg = k * (r - r_g) ** 2
    Ee = E0 + k * (r - r_e) ** 2
    ax.plot(r, Eg, color=DARK, lw=2.0, zorder=2)
    ax.plot(r, Ee, color=DARK, lw=2.0, zorder=2)
    label(ax, (r_g - 1.3, 0.3), "$S_0$\n(ground)", fontsize=9, color=DARK, ha="center")
    label(ax, (r_e + 1.4, E0 + 0.3), "$S_1$\n(excited)", fontsize=9, color=DARK, ha="center")

    dv = 0.65
    for well_min, r0, n in ((0.0, r_g, 3), (E0, r_e, 3)):
        for v in range(n):
            Ev = well_min + dv * (v + 0.5)
            half_width = np.sqrt(max(Ev - well_min, 0) / k)
            ax.plot([r0 - half_width, r0 + half_width], [Ev, Ev], color=GRAY, lw=1.0, alpha=0.7, zorder=1)

    Eg_v0 = 0.5 * dv
    Ee_v0 = E0 + 0.5 * dv
    Ee_at_rg = E0 + k * (r_g - r_e) ** 2
    Eg_at_re = k * (r_e - r_g) ** 2

    ax.annotate("", xy=(r_g, Ee_at_rg), xytext=(r_g, Eg_v0),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.0))
    label(ax, (r_g - 0.32, (Eg_v0 + Ee_at_rg) / 2), "absorption", color=BLUE, fontsize=8.5, ha="right")

    ax.annotate("", xy=(r_e, Ee_v0), xytext=(r_g + 0.12, Ee_at_rg - 0.12),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.3, ls=(0, (2, 2))))

    ax.annotate("", xy=(r_e, Eg_at_re), xytext=(r_e, Ee_v0),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.0))
    label(ax, (r_e + 0.32, (Eg_at_re + Ee_v0) / 2), "emission", color=GREEN, fontsize=8.5, ha="left")

    ax.annotate("", xy=(r_g + 0.1, Eg_v0 + 0.1), xytext=(r_e - 0.1, Eg_at_re - 0.1),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.3, ls=(0, (2, 2))))

    ax.annotate("", xy=(4.3, Eg_v0), xytext=(4.3, Ee_at_rg),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.3))
    label(ax, (4.5, (Eg_v0 + Ee_at_rg) / 2), "$h\\nu_{\\rm abs}$", color=BLUE, fontsize=8.5, ha="left")

    ax.annotate("", xy=(5.3, Eg_at_re), xytext=(5.3, Ee_v0),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    label(ax, (5.5, (Eg_at_re + Ee_v0) / 2), "$h\\nu_{\\rm em}$", color=GREEN, fontsize=8.5, ha="left")

    label(ax, (4.9, E0 + 2.1),
          f"Stokes shift $= h\\nu_{{\\rm abs}} - h\\nu_{{\\rm em}}$", color=PURPLE, fontsize=8.2, ha="center")

    ax.set_xlabel("nuclear coordinate (bond length)")
    ax.set_ylabel("energy")
    ax.set_xlim(-2.0, 6.4)
    ax.set_ylim(-0.4, E0 + 2.6)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Franck-Condon: vertical transitions,\nvibrational relaxation, and the Stokes shift", fontsize=10)

    fig.tight_layout()
    save(fig, "exp12-franck-condon-concept")


if __name__ == "__main__":
    use_style()
    fluorescence_panels()
    franck_condon_figure()

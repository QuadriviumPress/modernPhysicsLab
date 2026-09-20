"""Figures for Experiment 5, diffraction and the resolution limit: the
apparatus schematic, and a concept figure for the Rayleigh criterion."""

import matplotlib.pyplot as plt
import numpy as np

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, label, new_ax, save, screen, source_dot, rotation_stage, use_style,
)


def diffraction_bench_layout():
    fig, ax = new_ax(figsize=(7.6, 4.2))

    laser = (-3.1, 0.0)
    sample = (-0.6, 0.0)
    scr = (2.4, 0.0)

    box(ax, laser, 0.8, 0.4, "diode laser\n650 nm", fontsize=7.6)
    source_dot(ax, (laser[0] + 0.48, 0), color=RED, ms=7, glow=False)
    beam(ax, (laser[0] + 0.58, 0), (sample[0] - 0.28, 0), color=RED)

    rotation_stage(ax, sample, r=0.42, angle_deg=35, color=GRAY)
    ax.plot([sample[0], sample[0]], [-0.55, 0.55], color=DARK, lw=3.0, zorder=3)
    label(ax, (sample[0], 1.05), "slit / aperture /\ngrating / CD\n(on rotation mount)", fontsize=7.3)

    # zero order plus a fan of diffracted orders
    beam(ax, (sample[0] + 0.05, 0), (scr[0] - 0.05, 0), color=RED, alpha=0.9)
    for m, dy in zip((1, 2, -1, -2), (0.55, 1.05, -0.55, -1.05)):
        beam(ax, (sample[0] + 0.05, 0), (scr[0] - 0.05, dy), color=RED, lw=1.0, alpha=0.55)
        label(ax, (scr[0] + 0.25, dy), f"$m={m:+d}$", fontsize=6.8, color=GRAY, ha="left")
    label(ax, (scr[0] + 0.25, 0), "$m=0$", fontsize=6.8, color=GRAY, ha="left")

    screen(ax, scr, height=2.6)
    label(ax, (scr[0], -1.85), "screen / camera\n(or rotating detector arm)", fontsize=7.3)

    th = np.radians(20)
    ax.plot([sample[0], sample[0] + 1.1 * np.cos(th)], [0, 1.1 * np.sin(th)],
            color=PURPLE, lw=1.0, ls=":")
    from matplotlib.patches import Arc
    ax.add_patch(Arc((sample[0], 0), 1.4, 1.4, theta1=0, theta2=20, edgecolor=PURPLE, lw=1.1))
    label(ax, (sample[0] + 0.85, 0.22), r"$\theta$", color=PURPLE, fontsize=9)

    label(ax, (-0.2, 2.0),
          "Same rail for every part: swap the sample and, for large angles,\n"
          "replace the screen with a rotation stage or protractor read-out.",
          fontsize=8.0, color=DARK, ha="center")

    ax.set_xlim(-4.1, 3.6)
    ax.set_ylim(-2.3, 2.5)
    save(fig, "exp05-diffraction-bench-schematic")


def rayleigh_criterion_figure():
    """Two point-spread functions separated by exactly the Rayleigh
    criterion: the first zero of one lands on the central peak of the other."""
    fig, ax = plt.subplots(figsize=(6.4, 4.2))

    x = np.linspace(-2.6, 2.6, 1600)
    c1, c2 = -0.5, 0.5  # centres, one first-zero-width apart
    p1 = np.sinc(x - c1) ** 2
    p2 = np.sinc(x - c2) ** 2
    total = p1 + p2

    ax.plot(x, p1, color=BLUE, lw=1.3, ls="--", zorder=2)
    ax.plot(x, p2, color=RED, lw=1.3, ls="--", zorder=2)
    ax.plot(x, total, color=DARK, lw=2.0, zorder=3, label="sum (what you observe)")

    for c, col in ((c1, BLUE), (c2, RED)):
        ax.plot([c, c], [0, 1.0], color=col, lw=0.8, ls=":", zorder=1)
    ax.annotate("", xy=(c1, 1.12), xytext=(c2, 1.12),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.2))
    label(ax, (0, 1.22), r"$\theta_{\min} = 1.22\,\lambda/D$", color=PURPLE, fontsize=9.5)

    dip = total[np.argmin(np.abs(x - 0))]
    ax.annotate("central dip\n(barely resolved)", xy=(0, dip), xytext=(1.15, 0.55),
                fontsize=8.2, color=DARK, ha="left",
                arrowprops=dict(arrowstyle="->", color=DARK, lw=0.9))

    ax.set_xlabel("position on screen (units of the first-zero radius)")
    ax.set_ylabel(r"intensity $I/I_0$")
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(0, 1.35)
    ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    ax.set_title("The Rayleigh criterion: just resolved", fontsize=10)

    fig.tight_layout()
    save(fig, "exp05-rayleigh-criterion-concept")


if __name__ == "__main__":
    use_style()
    diffraction_bench_layout()
    rayleigh_criterion_figure()

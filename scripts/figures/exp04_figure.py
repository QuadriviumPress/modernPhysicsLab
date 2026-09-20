"""Figures for Experiment 4, interference of light: the apparatus schematic,
and a concept figure for the envelope-modulated two-slit pattern."""

import matplotlib.pyplot as plt
import numpy as np

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, label, new_ax, save, screen, source_dot, use_style,
)


def interference_bench_layout():
    fig, ax = new_ax(figsize=(7.6, 3.6))

    laser = (-3.0, 0.0)
    slits = (-0.8, 0.0)
    cam = (2.2, 0.0)

    box(ax, laser, 0.8, 0.4, "diode laser\n650 nm", fontsize=7.6)
    source_dot(ax, (laser[0] + 0.48, 0), color=RED, ms=7, glow=False)
    beam(ax, (laser[0] + 0.58, 0), (slits[0] - 0.12, 0), color=RED)

    # slit set: two narrow gaps in a barrier
    ax.plot([slits[0], slits[0]], [-0.9, -0.12], color=DARK, lw=2.4, zorder=3)
    ax.plot([slits[0], slits[0]], [0.12, 0.9], color=DARK, lw=2.4, zorder=3)
    label(ax, (slits[0], 1.15), "slit set\n$(a, d)$ on a slide", fontsize=7.5)

    # diverging fan of beams toward the camera, with a fringe pattern
    for m in (-2, -1, 0, 1, 2):
        beam(ax, (slits[0] + 0.05, 0.06 * m), (cam[0] - 0.05, 0.42 * m), color=RED, lw=0.9, alpha=0.55)

    screen(ax, cam, height=1.4)
    label(ax, (cam[0], 1.05), "camera / scanning\nphotodiode", fontsize=7.5)

    ax.annotate("", xy=(cam[0], -1.35), xytext=(slits[0], -1.35),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.2))
    label(ax, ((slits[0] + cam[0]) / 2, -1.55), r"$L$ (optical rail)", color=PURPLE, fontsize=8)

    label(ax, (laser[0] - 0.7, 1.15), "unpolarized\nbeam", fontsize=6.8, color=GRAY, ha="left")

    ax.set_xlim(-4.0, 3.1)
    ax.set_ylim(-2.0, 1.7)
    save(fig, "exp04-interference-bench-schematic")


def envelope_fringes_figure():
    """The two-slit pattern as an interference fringe pattern modulated by
    the single-slit diffraction envelope, with a missing order marked."""
    fig, ax = plt.subplots(figsize=(6.6, 4.0))

    d_over_a = 5  # matches the d/a = 5 worked example in the theory text
    x = np.linspace(-12.4, 12.4, 2000)  # x = d*sin(theta)/lambda

    with np.errstate(divide="ignore", invalid="ignore"):
        beta = np.pi * x / d_over_a
        envelope = np.where(np.abs(beta) < 1e-9, 1.0, (np.sin(beta) / beta) ** 2)
    fringes = np.cos(np.pi * x) ** 2
    intensity = envelope * fringes

    ax.plot(x, envelope, color=GRAY, lw=1.3, ls="--", zorder=2, label="single-slit envelope")
    ax.fill_between(x, intensity, color=RED, alpha=0.25, zorder=1)
    ax.plot(x, intensity, color=RED, lw=1.5, zorder=3, label="two-slit pattern")

    for m in (-d_over_a, d_over_a):
        ax.annotate("missing\norder", xy=(m, 0.02), xytext=(m, 0.32),
                    fontsize=8, color=PURPLE, ha="center",
                    arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.0))

    ax.set_xlabel(r"$x = d\sin\theta/\lambda$  (interference order)")
    ax.set_ylabel(r"intensity $I/I_0$")
    ax.set_xlim(-12.4, 12.4)
    ax.set_ylim(0, 1.08)
    ax.legend(loc="upper right", fontsize=8.5)
    ax.set_title(r"$d/a = 5$: every 5th interference order is missing", fontsize=10)

    fig.tight_layout()
    save(fig, "exp04-envelope-fringes-concept")


if __name__ == "__main__":
    use_style()
    interference_bench_layout()
    envelope_fringes_figure()

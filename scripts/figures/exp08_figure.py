"""Figures for Experiment 8, tunneling by frustrated total internal
reflection: the apparatus schematic, and the quantum-barrier concept figure."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon, Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, box, label, new_ax, save, source_dot, use_style,
)


def ftir_layout():
    fig, ax = new_ax(figsize=(7.6, 4.6))

    laser = (-3.0, -0.9)

    # right-angle prism: hypotenuse along the top, horizontal
    prism = np.array([[-1.4, -1.0], [1.4, -1.0], [0.0, 1.0]])
    ax.add_patch(Polygon(prism, closed=True, facecolor="#dbe9f5", edgecolor=BLUE, lw=1.5, zorder=2))
    label(ax, (0.0, -1.35), "right-angle prism ($n\\approx1.52$)", fontsize=7.6)

    # plano-convex lens pressed against the hypotenuse near the apex,
    # drawn as a shallow arc since its radius of curvature is very long
    R = 1.35
    lens_center = (0.0, 1.0 + R)
    ax.add_patch(Arc(lens_center, 2 * R, 2 * R, theta1=254, theta2=286,
                      edgecolor=RED, lw=1.6, zorder=3))
    label(ax, (0.85, 1.55), "plano-convex lens,\nlong radius $R$\n(pressed on the\nhypotenuse)", fontsize=6.8, ha="left")
    ax.annotate("", xy=(0.0, 1.02), xytext=(0.0, 1.55),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2))
    label(ax, (-0.55, 1.45), "air gap\n$r(x)$", color=RED, fontsize=7, ha="right")

    box(ax, laser, 0.85, 0.4, "diode laser\n+ expander", fontsize=7.2)
    source_dot(ax, (laser[0] + 0.5, laser[1]), color=RED, ms=7, glow=False)

    # incident beam toward the prism's left face at the TIR angle
    entry = (-0.75, -0.35)
    beam(ax, (laser[0] + 0.6, laser[1]), entry, color=RED)

    # reflected (TIR, away from contact) and transmitted (tunneled, near contact) beams
    exit_tir = (0.85, -0.35)
    beam(ax, entry, exit_tir, color=RED, alpha=0.9)
    exit_tunnel = (0.0, -1.55)
    beam(ax, (0.0, 0.85), exit_tunnel, color=ORANGE, lw=1.2, ls="--", alpha=0.9)
    label(ax, (0.0, -1.85), "tunneled beam\n(camera / photodiode)", fontsize=6.8, color=ORANGE)

    ax.add_patch(Arc(entry, 0.7, 0.7, theta1=52, theta2=90, edgecolor=GRAY, lw=1.0))
    label(ax, (entry[0] + 0.05, entry[1] + 0.5), r"$\theta > \theta_c$", color=GRAY, fontsize=8, ha="left")

    box(ax, (2.55, -0.35), 0.9, 0.6, "USB\nmicroscope /\ncamera", fontsize=6.8)
    ax.plot([exit_tir[0] + 0.05, 2.15], [exit_tir[1], -0.35], color=GRAY, lw=1.0, ls=":")
    label(ax, (1.05, 0.05), "reflected beam\n(dark spot at contact)", fontsize=6.8, color=RED, ha="left")

    label(ax, (0.0, 2.4),
          "Reflection is total except where the lens nearly touches the prism;\n"
          "there, light tunnels across the gap and the reflected spot goes dark.",
          fontsize=8.0, color=DARK, ha="center")

    ax.set_xlim(-3.9, 3.4)
    ax.set_ylim(-2.3, 2.8)
    save(fig, "exp08-ftir-schematic")


def quantum_barrier_figure():
    """A rectangular potential barrier with E < V0: an oscillating
    wavefunction outside, decaying (not oscillating) inside, and a reduced
    oscillating transmitted wave beyond -- the quantum-side correspondence
    to the optical evanescent wave shown in the apparatus schematic above."""
    fig, ax = plt.subplots(figsize=(7.0, 4.2))

    V0, E, L = 5.0, 1.0, 1.4
    k = 6.0
    T_amp = 0.25
    kappa = -np.log(T_amp) / L
    amp = 0.8

    ax.add_patch(Rectangle((0, 0), L, V0, facecolor="#dbe9f5", edgecolor="none", zorder=0))

    # V(x): a step up to V0 across the barrier, zero outside.
    ax.plot([-1.6, 0, 0, L, L, 1.8 + L], [0, 0, V0, V0, 0, 0], color=DARK, lw=2.0, zorder=2)
    ax.axhline(E, color=GRAY, lw=1.1, ls="--", zorder=1)
    label(ax, (-1.75, E), "$E$", color=GRAY, fontsize=9.5, ha="right")
    label(ax, (L / 2, V0 + 0.35), "$V_0$", color=DARK, fontsize=9.5)

    x1 = np.linspace(-1.6, 0, 250)
    x2 = np.linspace(0, L, 150)
    x3 = np.linspace(L, L + 1.8, 250)
    ax.plot(x1, E + amp * np.cos(k * x1), color=RED, lw=1.6, zorder=3)
    ax.plot(x2, E + amp * np.exp(-kappa * x2), color=RED, lw=1.6, zorder=3)
    ax.plot(x3, E + amp * T_amp * np.cos(k * (x3 - L)), color=RED, lw=1.6, zorder=3)

    label(ax, (-1.1, V0 - 0.15), "incident +\nreflected", fontsize=8.2, color=DARK, ha="center")
    label(ax, (L / 2, -0.55), "barrier:\n$\\psi \\propto e^{-\\kappa_q x}$", fontsize=8.2, color=DARK, ha="center")
    label(ax, (L + 1.1, V0 - 0.15), "transmitted\n(reduced amplitude)", fontsize=8.2, color=DARK, ha="center")

    ax.set_xlabel("$x$")
    ax.set_ylabel("energy  /  $\\psi(x)$ (offset by $E$)")
    ax.set_xlim(-1.6, L + 1.8)
    ax.set_ylim(-1.0, V0 + 0.9)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)

    fig.tight_layout()
    save(fig, "exp08-quantum-barrier-concept")


if __name__ == "__main__":
    use_style()
    ftir_layout()
    quantum_barrier_figure()

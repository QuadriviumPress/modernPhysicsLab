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

    laser = (-3.0, -1.5)

    # Right-angle prism with its hypotenuse horizontal at the top.
    prism = np.array([[-1.4, 1.0], [1.4, 1.0], [0.0, -0.4]])
    ax.add_patch(Polygon(prism, closed=True, facecolor="#dbe9f5", edgecolor=BLUE, lw=1.5, zorder=2))
    label(ax, (0.0, -1.35), "right-angle prism ($n\\approx1.52$)", fontsize=7.6)

    # plano-convex lens pressed against the hypotenuse near the apex,
    # drawn as a shallow arc since its radius of curvature is very long
    R = 1.35
    lens_center = (0.0, 1.0 + R)
    ax.add_patch(Arc(lens_center, 2 * R, 2 * R, theta1=254, theta2=286,
                      edgecolor=RED, lw=1.6, zorder=3))
    label(ax, (0.75, 1.6), "long-radius lens\nabove hypotenuse", fontsize=7, ha="left")
    label(ax, (-0.55, 1.35), "air gap $d(r)$", color=RED, fontsize=7, ha="right")

    box(ax, laser, 0.85, 0.4, "diode laser\n+ expander", fontsize=7.2)
    source_dot(ax, (laser[0] + 0.5, laser[1]), color=RED, ms=7, glow=False)

    # The in-glass ray hits the horizontal hypotenuse at 45 degrees.
    entry = (-0.7, 0.3)
    contact = (0.0, 1.0)
    exit_tir = (0.7, 0.3)
    beam(ax, (laser[0] + 0.6, laser[1]), entry, color=RED)

    beam(ax, entry, contact, color=RED, alpha=0.9)
    beam(ax, contact, exit_tir, color=RED, alpha=0.9)
    beam(ax, contact, (0.0, 1.85), color=ORANGE, lw=1.2, ls="--", alpha=0.9)
    label(ax, (0.0, 2.12), "transmitted port\n(camera / detector)", fontsize=7, color=ORANGE)
    label(ax, (-0.20, 0.52), r"$\theta=45°>\theta_c$", color=GRAY, fontsize=7)

    box(ax, (2.0, -1.0), 0.9, 0.6, "reflected port\nbeam block /\ndetector", fontsize=6.8)
    beam(ax, exit_tir, (1.55, -0.55), color=RED, alpha=0.65)

    label(ax, (0.0, 2.64), "Coupling through the air gap reduces the reflected light.",
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
    label(ax, (-1.43, E + 0.30), "$E$", color=GRAY, fontsize=9.5)
    label(ax, (L / 2, V0 + 0.35), "$V_0$", color=DARK, fontsize=9.5)

    x1 = np.linspace(-1.6, 0, 250)
    x2 = np.linspace(0, L, 150)
    x3 = np.linspace(L, L + 1.8, 250)
    ax.plot(x1, E + amp * np.cos(k * x1), color=RED, lw=1.6, zorder=3)
    ax.plot(x2, E + amp * np.exp(-kappa * x2), color=RED, lw=1.6, zorder=3)
    ax.plot(x3, E + amp * T_amp * np.cos(k * (x3 - L)), color=RED, lw=1.6, zorder=3)

    label(ax, (-1.1, V0 - 0.15), "incident +\nreflected", fontsize=8.2, color=DARK, ha="center")
    label(ax, (L / 2, -0.55),
          "barrier:\n$\\psi = A e^{\\kappa_q x}+B e^{-\\kappa_q x}$",
          fontsize=8.2, color=DARK, ha="center")
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

"""Figures for Experiment 13, counting statistics, half-life, and gamma
attenuation: the apparatus schematic, and the Poisson-vs-Gaussian figure."""

from math import exp, lgamma, log, pi, sqrt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    absorber_stack, box, gm_tube, label, save, use_style,
)


def _poisson_pmf(N, mu):
    return np.array([exp(n * log(mu) - mu - lgamma(n + 1)) for n in N])


def _gaussian_pdf(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * sqrt(2 * pi))


def counting_panels():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.0))

    # --- (a) half-life: eluted planchet directly under the tube ------------
    ax = axes[0]
    ax.set_aspect("equal")
    ax.axis("off")

    tube = (0.0, 0.9)
    gm_tube(ax, tube, length=1.0, angle_deg=90, color="#cfd8dc")
    label(ax, (0.0, 1.65), "GM tube,\nend window down", fontsize=7.0)

    ax.add_patch(Rectangle((-0.5, -0.15), 1.0, 0.12, facecolor="#dcdcdc", edgecolor=DARK, lw=1.2, zorder=3))
    ax.add_patch(Circle((0.0, -0.09), 0.16, facecolor="#9fd8a3", edgecolor="#4a7c59", lw=1.1, zorder=4))
    label(ax, (0.0, -0.45), r"$^{137m}$Ba planchet" "\n(fixed shelf, close geometry)", fontsize=6.8)

    box(ax, (2.0, 0.9), 1.1, 0.55, "counter / timer\n(repeat runs)", fontsize=6.8)
    ax.plot([0.5, 1.45], [0.9, 0.9], color=PURPLE, lw=1.0, ls="--")

    ax.set_title("(a)  half-life run", fontsize=9.4)
    ax.set_xlim(-1.4, 2.9)
    ax.set_ylim(-0.9, 2.1)

    # --- (b) attenuation: absorbers between a check source and the tube ----
    ax = axes[1]
    ax.set_aspect("equal")
    ax.axis("off")

    src = (-1.4, 0.0)
    ax.add_patch(Circle(src, 0.14, facecolor=ORANGE, edgecolor="#7a4a00", lw=1.0, zorder=4))
    label(ax, (src[0], src[1] - 0.35), r"$^{137}$Cs / $^{60}$Co" "\ncheck source", fontsize=6.8)

    absorber_stack(ax, (-0.3, 0.0), n=5, w=0.09, h=0.9, gap=0.06, color="#cfd8dc", edge=GRAY)
    label(ax, (-0.3, -0.75), "lead sheets\n(1-10 mm)", fontsize=6.8)

    tube2 = (1.3, 0.0)
    gm_tube(ax, tube2, length=1.0, angle_deg=0, color="#cfd8dc")
    label(ax, (1.3, 0.7), "GM tube", fontsize=7.0)

    for dy in (-0.12, 0.0, 0.12):
        ax.plot([src[0] + 0.16, tube2[0] - 0.5], [dy * 0.3, dy], color=RED, lw=1.0, alpha=0.6, zorder=2)

    ax.set_title("(b)  attenuation run", fontsize=9.4)
    ax.set_xlim(-2.2, 2.4)
    ax.set_ylim(-1.2, 1.1)

    fig.tight_layout()
    save(fig, "exp13-counting-schematic")


def poisson_gaussian_figure():
    """Poisson PMFs for a small and a large mean, each with the matching
    Gaussian overlaid, showing the small-mu asymmetry and the large-mu
    convergence to a symmetric bell -- matches q-count-01."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.6, 3.8))

    for ax, mu, N in ((axL, 3, np.arange(0, 13)), (axR, 30, np.arange(10, 51))):
        P = _poisson_pmf(N, mu)
        ax.bar(N, P, color=BLUE, width=0.7, alpha=0.85, zorder=2, label="Poisson")
        xg = np.linspace(N[0], N[-1], 300)
        ax.plot(xg, _gaussian_pdf(xg, mu, sqrt(mu)), color=RED, lw=2.0, zorder=3,
                label=f"Gaussian ($\\sigma=\\sqrt{{{mu}}}$)")
        ax.axvline(mu, color=GRAY, lw=1.0, ls=":", zorder=1)
        ax.set_xlabel("$N$ (counts)")
        ax.set_title(f"$\\mu = {mu}$", fontsize=10)
        ax.legend(loc="upper right", fontsize=8, frameon=False)
    axL.set_ylabel("probability")
    axL.set_title("$\\mu = 3$: visibly asymmetric", fontsize=10)
    axR.set_title("$\\mu = 30$: nearly symmetric", fontsize=10)

    fig.tight_layout()
    save(fig, "exp13-poisson-gaussian-concept")


if __name__ == "__main__":
    use_style()
    counting_panels()
    poisson_gaussian_figure()

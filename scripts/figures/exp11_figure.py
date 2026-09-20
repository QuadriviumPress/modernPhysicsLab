"""Apparatus schematic for Experiment 11, alkali spectra and the quantum defect.

Reuses the Experiment 10 spectrometer layout with a sodium source and the
D-line doublet in place of the Balmer series.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib.pyplot as plt

from exp10_figure import spectrometer_layout
from labstyle import BLUE, DARK, GRAY, GREEN, ORANGE, PURPLE, RED, label, save, use_style

SODIUM_LINES = [
    (589.6, "D$_2$", "#d97706"),
    (589.0, "D$_1$", "#b8860b"),
]


def sodium_spectrometer():
    spectrometer_layout(
        source_label="sodium\ndischarge\nlamp",
        source_color="#ffb703",
        lines=SODIUM_LINES,
        name="exp11-sodium-spectrometer-schematic",
        extra_note=("Same spectrometer as Experiment 10, at its highest resolving power:\n"
                     "the sodium D lines sit close enough to test the instrument itself."),
    )


def quantum_defect_figure():
    """Hydrogenic (dashed) versus alkali (solid, defect-shifted) energy
    levels for n = 3, 4: low-l orbitals are pulled down by penetrating the
    ionic core; high-l orbitals stay almost hydrogenic."""
    fig, ax = plt.subplots(figsize=(6.4, 5.0))

    deltas = {"s": 1.373, "p": 0.883, "d": 0.010, "f": 0.000}
    colors = {"s": RED, "p": ORANGE, "d": GREEN, "f": BLUE}
    x = {"s": 0, "p": 1, "d": 2, "f": 3}

    for n in (3, 4):
        E_hyd = -13.6 / n**2
        ax.plot([-0.5, 3.5], [E_hyd, E_hyd], color=GRAY, lw=1.2, ls="--", zorder=1)
        label(ax, (3.6, E_hyd), f"hydrogenic $n={n}$", fontsize=7.8, color=GRAY, ha="left", va="center")
        for l, delta in deltas.items():
            E_nl = -13.6 / (n - delta) ** 2
            ax.plot([x[l], x[l]], [E_hyd, E_nl], color=colors[l], lw=1.0, alpha=0.55, zorder=2)
            ax.plot(x[l], E_nl, "o", color=colors[l], ms=8, zorder=3,
                    markeredgecolor="white", markeredgewidth=1.0)
        label(ax, (-0.75, E_hyd - 0.35 if n == 3 else E_hyd - 0.15),
              f"$n={n}$", fontsize=9, color=DARK, ha="right")

    ax.annotate("3$p$ splits into $3p_{1/2}, 3p_{3/2}$\n(the D-line pair — not to scale here)",
                xy=(x["p"], -13.6 / (3 - deltas["p"]) ** 2), xytext=(1.3, -2.3),
                fontsize=7.6, color=ORANGE,
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=0.9))

    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(["$s$", "$p$", "$d$", "$f$"])
    ax.set_xlabel(r"orbital angular momentum $\ell$")
    ax.set_ylabel("energy (eV)")
    ax.set_xlim(-1.4, 5.2)
    ax.set_ylim(-6.0, -0.3)
    ax.set_title("Quantum defects pull low-$\\ell$ levels\nbelow the hydrogenic value", fontsize=10)

    fig.tight_layout()
    save(fig, "exp11-quantum-defect-concept")


if __name__ == "__main__":
    use_style()
    sodium_spectrometer()
    quantum_defect_figure()

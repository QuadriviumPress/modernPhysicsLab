"""Figures for Experiment 14, a cosmic-ray muon telescope: the apparatus
schematic, and the time-dilation / length-contraction concept figure."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

from labstyle import (
    BLUE, GRAY, GREEN, ORANGE, PURPLE, RED, DARK,
    absorber_stack, beam, box, gm_tube, label, new_ax, save, use_style,
)


def muon_telescope_layout():
    fig, ax = new_ax(figsize=(6.6, 5.8))

    top = (0.0, 0.9)
    bot = (0.0, -0.4)

    gm_tube(ax, top, length=1.7, angle_deg=0, color="#cfd8dc")
    gm_tube(ax, bot, length=1.7, angle_deg=0, color="#cfd8dc")
    label(ax, (top[0] + 1.15, top[1] + 0.45), "GM tube 1", fontsize=7.6, ha="left")
    label(ax, (bot[0] + 1.15, bot[1] - 0.25), "GM tube 2", fontsize=7.6, ha="left")

    # rigid frame at both ends, with the adjustable separation marked
    for s in (-0.82, 0.82):
        ax.plot([s, s], [top[1], bot[1]], color=GRAY, lw=1.3, ls=(0, (4, 2)), zorder=1)
    ax.annotate("", xy=(-1.0, bot[1] + 0.05), xytext=(-1.0, top[1] - 0.05),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.2))
    label(ax, (-1.35, (top[1] + bot[1]) / 2), "separation\n(adjustable)", color=PURPLE, fontsize=6.8, ha="center")

    # zenith angle, measured at the assembly's center from the local vertical
    center = ((top[0] + bot[0]) / 2, (top[1] + bot[1]) / 2)
    zenith = 25
    zth = np.radians(zenith)
    ax.plot([center[0], center[0]], [center[1], center[1] + 1.7], color=GRAY, lw=1.0, ls=":", zorder=1)
    axis_dir = np.array([np.sin(zth), np.cos(zth)])
    ax.plot([center[0], center[0] + 1.7 * axis_dir[0]], [center[1], center[1] + 1.7 * axis_dir[1]],
             color=GRAY, lw=1.0, ls=":", zorder=1)
    ax.add_patch(Arc(center, 1.5, 1.5, theta1=90 - zenith, theta2=90, edgecolor=GRAY, lw=1.1))
    label(ax, (center[0] + 0.35, center[1] + 1.05), r"$\theta$ (zenith)", color=GRAY, fontsize=8, ha="left")
    label(ax, (center[0] - 1.7, center[1] + 1.95), "rotating mount /\nzenith-angle scale",
          color=GRAY, fontsize=6.6, ha="center")

    # muon tracks along the telescope's pointing direction, through both tubes
    for off in (-0.35, 0.0, 0.35):
        entry = (off - 0.75 * np.sin(zth), top[1] + 0.65 + 0.75 * np.cos(zth))
        exitp = (off + 0.55 * np.sin(zth), bot[1] - 0.55 - 0.55 * np.cos(zth))
        beam(ax, entry, exitp, color=RED, lw=1.3, arrow=True, alpha=0.8)
    label(ax, (0.35 - 0.75 * np.sin(zth) + 0.3, top[1] + 0.65 + 0.75 * np.cos(zth)), r"$\mu^-$",
          color=RED, fontsize=11, ha="left")

    # optional lead absorbers below the lower tube
    absorber_stack(ax, (0.0, bot[1] - 0.95), n=3, w=0.08, h=0.5, gap=0.06, color="#cfd8dc")
    label(ax, (0.0, bot[1] - 1.5), "lead absorbers\n(optional, for range)", fontsize=6.8)

    box(ax, (0.0, bot[1] - 2.3), 2.3, 0.6, "microcontroller:\npulse shaping + coincidence", fontsize=7.0)
    ax.plot([top[0] + 0.85, 1.0], [top[1], bot[1] - 2.0], color=DARK, lw=0.9, ls=":")
    ax.plot([bot[0] + 0.85, -1.0], [bot[1], bot[1] - 2.0], color=DARK, lw=0.9, ls=":")

    label(ax, (0.0, 2.55),
          "Two tubes in coincidence define a narrow solid angle; the count rate\n"
          "measured vs. $\\theta$ tests the $\\cos^2\\theta$ zenith-angle dependence.",
          fontsize=7.8, color=DARK, ha="center")

    ax.set_xlim(-2.3, 2.5)
    ax.set_ylim(-3.3, 2.9)
    save(fig, "exp14-muon-telescope-schematic")


def time_dilation_figure():
    """Two views of the same physics: (left) in the lab frame, time
    dilation stretches the muon's decay length far past the non-relativistic
    value; (right) in the muon's own frame, length contraction shrinks the
    atmosphere down to a thickness it can cross in about one lifetime."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(8.4, 4.6))

    atmosphere_km = 15.0
    c_tau0_km = 0.659  # c * proper lifetime
    gamma = 20.0
    dilated_km = gamma * c_tau0_km  # ~13.2 km, beta ~ 1

    axL.bar([0], [atmosphere_km], width=0.55, color="#dbe9f5", edgecolor=GRAY, zorder=1)
    axL.bar([1], [c_tau0_km], width=0.55, color=RED, zorder=2)
    axL.bar([2], [dilated_km], width=0.55, color=GREEN, zorder=2)
    axL.set_xticks([0, 1, 2])
    axL.set_xticklabels(["atmosphere\n(15 km)", "decay length\nwithout dilation\n(0.66 km)",
                          "decay length\nwith dilation\n(13.2 km)"], fontsize=7.6)
    axL.set_ylabel("distance in the lab frame (km)")
    axL.set_ylim(0, atmosphere_km * 1.15)
    axL.set_title("Lab frame: time dilation\nstretches the decay length", fontsize=9.5)

    contracted_km = atmosphere_km / gamma
    axR.bar([0], [contracted_km], width=0.55, color="#dbe9f5", edgecolor=GRAY, zorder=1)
    axR.bar([1], [c_tau0_km], width=0.55, color=PURPLE, zorder=2)
    axR.set_xticks([0, 1])
    axR.set_xticklabels(["atmosphere,\ncontracted\n(0.75 km)", "proper decay\nlength\n(0.66 km)"],
                         fontsize=7.6)
    axR.set_ylabel("distance in the muon's frame (km)")
    axR.set_ylim(0, 1.05)
    axR.set_title("Muon's frame: length contraction\nshrinks the atmosphere", fontsize=9.5)

    fig.suptitle("Same physics, two frames", fontsize=11, y=1.02)
    fig.tight_layout()
    save(fig, "exp14-time-dilation-concept")


if __name__ == "__main__":
    use_style()
    muon_telescope_layout()
    time_dilation_figure()

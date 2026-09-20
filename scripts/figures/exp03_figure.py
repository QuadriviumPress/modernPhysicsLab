"""Apparatus schematic for Experiment 3, relativistic electrons from beta decay."""

from matplotlib.patches import Circle, Rectangle

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    absorber_stack, beam, box, gm_tube, label, new_ax, save, use_style,
)


def beta_shelf_layout():
    fig, ax = new_ax(figsize=(6.6, 5.2))

    shelf_x = -1.6
    src = (shelf_x, -1.5)
    absorber_x = shelf_x + 0.9
    tube = (shelf_x + 2.2, 0.4)

    # shelf stand: a vertical post with numbered shelf slots
    ax.plot([shelf_x, shelf_x], [-1.7, 1.3], color=GRAY, lw=2.2, zorder=1)
    for y in (-1.5, -0.8, -0.1, 0.6):
        ax.plot([shelf_x - 0.12, shelf_x + 0.12], [y, y], color=GRAY, lw=1.6, zorder=1)

    # sealed source on the lowest shelf
    ax.add_patch(Circle((src[0], src[1]), 0.13, facecolor=ORANGE, edgecolor="#7a4a00", lw=1.0, zorder=4))
    label(ax, (src[0] - 0.05, src[1] - 0.32), r"$^{90}$Sr/$^{90}$Y" "\nsource", fontsize=7.5, ha="center")

    # emitted electrons, fanning up toward the tube
    for dy in (-0.15, 0.0, 0.15):
        beam(ax, src, (tube[0] - 0.5, tube[1] + dy), color=RED, lw=1.1, alpha=0.7, arrow=True)
    label(ax, (0.05, -0.75), r"$\beta^-$", color=RED, fontsize=10)

    # removable absorber slot between source and tube
    absorber_stack(ax, (absorber_x, -0.55), n=3, w=0.05, h=0.55, gap=0.05)
    label(ax, (absorber_x, -1.0), "Al absorber\nstack\n(removable)", fontsize=7, ha="center")

    # GM tube on an upper shelf, end window facing down toward the source
    gm_tube(ax, tube, length=1.0, angle_deg=100, color="#cfd8dc")
    label(ax, (tube[0] + 0.65, tube[1] + 0.25), "GM tube,\nthin end window", fontsize=7.5, ha="left")

    box(ax, (tube[0] + 0.3, tube[1] + 1.2), 1.3, 0.55, "counter / timer\n+ HV supply", fontsize=7.5)
    ax.plot([tube[0] + 0.15, tube[0] + 0.15], [tube[1] + 0.55, tube[1] + 0.93],
            color=PURPLE, lw=1.1, ls="--")

    label(ax, (0.3, 2.35),
          "Fixed geometry: swap absorber thicknesses and read the count rate\n"
          "through each one; the range in aluminium sets the endpoint energy.",
          fontsize=8.0, color=DARK, ha="center")

    ax.set_xlim(-2.6, 3.3)
    ax.set_ylim(-2.1, 2.7)
    save(fig, "exp03-beta-shelf-schematic")


if __name__ == "__main__":
    use_style()
    beta_shelf_layout()

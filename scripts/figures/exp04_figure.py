"""Apparatus schematic for Experiment 4, interference of light."""

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


if __name__ == "__main__":
    use_style()
    interference_bench_layout()

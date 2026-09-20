"""Apparatus schematic for Experiment 2, the time-of-flight speed of light."""

from labstyle import (
    BLUE, GRAY, ORANGE, PURPLE, RED, DARK,
    beam, beamsplitter, box, label, mirror, new_ax, save, source_dot, use_style,
)


def time_of_flight_layout():
    fig, ax = new_ax(figsize=(8.2, 4.8))

    src = (-3.4, 0.9)
    bs = (-1.7, 0.9)
    pd1 = (-1.7, -1.3)
    m1 = (1.9, 1.7)
    m2 = (1.9, -1.3)
    pd2 = (-0.2, -1.3)
    scope = (-3.4, -1.3)

    box(ax, src, 0.9, 0.42, "pulsed\nsource", fontsize=7.8)
    source_dot(ax, (src[0] + 0.52, src[1]), color=RED, ms=7, glow=False)
    beam(ax, (src[0] + 0.62, src[1]), (bs[0] - 0.16, bs[1]), color=RED)
    beamsplitter(ax, bs, size=0.3)

    # reference path, straight down, to PD1
    beam(ax, (bs[0], bs[1] - 0.16), (pd1[0], pd1[1] + 0.22), color=RED)
    box(ax, pd1, 0.6, 0.42, "PD$_1$\nstart", fontsize=7.5)
    label(ax, (pd1[0] - 0.45, pd1[1]), "short\nreference\npath", fontsize=7, color=GRAY, ha="right")

    # folded path: up from the splitter, across to M1, down to M2, left to PD2
    beam(ax, (bs[0], bs[1] + 0.16), (bs[0], m1[1]), color=RED)
    beam(ax, (bs[0], m1[1]), (m1[0] - 0.33, m1[1]), color=RED)
    mirror(ax, m1, angle_deg=90, length=0.6)
    beam(ax, (m1[0], m1[1] - 0.3), (m2[0], m2[1] + 0.3), color=RED)
    mirror(ax, m2, angle_deg=90, length=0.6)
    beam(ax, (m2[0] - 0.3, m2[1]), (pd2[0] + 0.32, pd2[1]), color=RED)
    label(ax, (m1[0] + 0.28, 0.2), "folded path,\nlength $L$\n(measured with\na tape measure)",
          fontsize=7, color=GRAY, ha="left")
    box(ax, pd2, 0.6, 0.42, "PD$_2$\nstop", fontsize=7.5)

    box(ax, scope, 1.05, 1.15, "oscilloscope\n$\\geq 100$ MHz\naveraging", fontsize=7.6)
    ax.plot([pd1[0] - 0.05, scope[0] + 0.4], [pd1[1] - 0.24, scope[1] + 0.35],
            color=PURPLE, lw=1.1, ls="--")
    ax.plot([pd2[0] - 0.05, scope[0] + 0.55], [pd2[1] - 0.24, scope[1] - 0.35],
            color=PURPLE, lw=1.1, ls="--")
    label(ax, (-1.6, -2.05), "matched BNC cables", fontsize=6.8, color=PURPLE, ha="center")

    label(ax, (0.4, 2.55),
          r"Split pulse $\to$ short reference path and folded long path $\to$ measure the time"
          "\ndelay $\\Delta t$ between the two pulses on the scope, so $c = L/\\Delta t$",
          fontsize=8.0, color=DARK)

    ax.set_xlim(-4.2, 2.9)
    ax.set_ylim(-2.3, 2.9)
    save(fig, "exp02-time-of-flight-schematic")


if __name__ == "__main__":
    use_style()
    time_of_flight_layout()

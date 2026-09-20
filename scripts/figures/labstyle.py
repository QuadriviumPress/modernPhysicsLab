"""Shared matplotlib styling and apparatus-drawing helpers for the lab manual.

All generated figures are written as SVG into ``images/`` and committed,
because the MyST build on GitHub Pages runs ``myst build --html`` only --
there is no Python kernel at build time. Regenerate with e.g.::

    python3 scripts/figures/exp01_figure.py

The palette matches the one used in the *Modern Physics* textbook, so a
reader moving between the two sees the same visual language.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyBboxPatch, Polygon, Rectangle, Wedge

IMAGES = Path(__file__).resolve().parents[2] / "images"

# Palette shared with the Modern Physics textbook figures.
BLUE = "#1769aa"
RED = "#b33a3a"
GREEN = "#2e7d5b"
PURPLE = "#6a4c93"
ORANGE = "#d97706"
GRAY = "#555555"
LIGHT = "#c9d6e0"
DARK = "#333333"

RC = {
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.facecolor": "white",
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.9,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.frameon": False,
    "legend.fontsize": 10,
    "lines.linewidth": 1.8,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "path",
    "svg.hashsalt": "modern-physics-lab",
    "path.simplify": True,
    "path.simplify_threshold": 1.0,
}


def use_style():
    plt.rcParams.update(RC)


def save(fig, name):
    """Save *fig* as ``images/<name>.svg`` and report the byte size."""
    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / f"{name}.svg"
    fig.savefig(
        path,
        format="svg",
        bbox_inches="tight",
        pad_inches=0.12,
        metadata={"Date": "2026-01-01"},
    )
    plt.close(fig)
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)")
    return path


def new_ax(figsize=(7.2, 4.2)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


# --------------------------------------------------------------------------
# Reusable apparatus glyphs. Every helper draws in data (axes) coordinates
# so a whole bench layout can be composed at a human scale (roughly 1 unit
# per apparatus footprint) and the axes limits set once at the end.
# --------------------------------------------------------------------------


def beam(ax, p0, p1, color=RED, lw=1.6, arrow=False, ls="-", zorder=2, alpha=1.0):
    """A ray of light or a particle track from p0 to p1."""
    if arrow:
        ax.annotate(
            "",
            xy=p1,
            xytext=p0,
            arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, alpha=alpha),
            zorder=zorder,
        )
    else:
        xs, ys = zip(p0, p1)
        ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=zorder, alpha=alpha)


def label(ax, xy, text, color=DARK, fontsize=8.5, ha="center", va="center", weight="normal"):
    ax.text(*xy, text, color=color, fontsize=fontsize, ha=ha, va=va, weight=weight)


def mirror(ax, xy, angle_deg, length=0.5, color=DARK):
    """A flat mirror: a heavy line with a short hatch on its back face."""
    x, y = xy
    th = np.radians(angle_deg)
    dx, dy = np.cos(th) * length / 2, np.sin(th) * length / 2
    ax.plot([x - dx, x + dx], [y - dy, y + dy], color=color, lw=2.6, solid_capstyle="round", zorder=4)
    # hatching on the back (reflective) side
    nx, ny = -np.sin(th), np.cos(th)
    for t in np.linspace(-0.9, 0.9, 6):
        bx, by = x + t * dx, y + t * dy
        ax.plot([bx, bx - 0.08 * nx], [by, by - 0.08 * ny], color=color, lw=0.9, zorder=4)


def beamsplitter(ax, xy, size=0.34, color=GRAY):
    """A cube beamsplitter shown edge-on as a square with a diagonal."""
    x, y = xy
    r = size / 2
    ax.add_patch(
        Rectangle((x - r, y - r), size, size, facecolor="#eef3f7", edgecolor=color, lw=1.2, zorder=3)
    )
    ax.plot([x - r, x + r], [y - r, y + r], color=color, lw=1.3, ls="--", zorder=4)


def lens_biconvex(ax, xy, height=0.6, thickness=0.10, color=BLUE):
    """A thin biconvex lens, drawn edge-on (vertical), centred at xy."""
    x, y = xy
    h = height / 2
    t = thickness
    verts_r = np.array([[x, y - h], [x + t, y], [x, y + h]])
    verts_l = np.array([[x, y - h], [x - t, y], [x, y + h]])
    ax.add_patch(Polygon(np.vstack([verts_l, verts_r[::-1]]), closed=True,
                          facecolor="#dbe9f5", edgecolor=color, lw=1.3, zorder=3))


def prism_right_angle(ax, xy, size=0.9, color=BLUE, rotate=0):
    """A right-angle prism, hypotenuse facing +y by default."""
    x, y = xy
    s = size
    pts = np.array([[-s / 2, -s / 2], [s / 2, -s / 2], [-s / 2, s / 2]])
    if rotate:
        th = np.radians(rotate)
        R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        pts = pts @ R.T
    pts = pts + np.array([x, y])
    ax.add_patch(Polygon(pts, closed=True, facecolor="#dbe9f5", edgecolor=color, lw=1.4, zorder=3))


def box(ax, xy, w, h, text=None, color=DARK, facecolor="white", fontsize=8.2, zorder=3):
    """A generic labelled instrument enclosure, centred at xy."""
    x, y = xy
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor=facecolor, edgecolor=color, lw=1.3, zorder=zorder,
        )
    )
    if text:
        label(ax, (x, y), text, color=color, fontsize=fontsize)


def screen(ax, xy, height=1.0, color=DARK):
    """A viewing screen or camera sensor: a short hatched vertical line."""
    x, y = xy
    h = height / 2
    ax.plot([x, x], [y - h, y + h], color=color, lw=2.4, zorder=3)
    for t in np.linspace(-h + 0.05, h - 0.05, 7):
        ax.plot([x, x + 0.09], [y + t, y + t - 0.09], color=color, lw=0.8, zorder=3)


def gm_tube(ax, xy, length=0.9, width=0.22, angle_deg=90, color=GRAY):
    """A Geiger-Mueller tube: a capsule with a thin end window marked by a tick."""
    x, y = xy
    th = np.radians(angle_deg)
    dx, dy = np.cos(th), np.sin(th)
    x0, y0 = x - dx * length / 2, y - dy * length / 2
    x1, y1 = x + dx * length / 2, y + dy * length / 2
    ax.plot([x0, x1], [y0, y1], color=color, lw=width * 40, solid_capstyle="round",
             zorder=3, alpha=0.9)
    ax.plot([x0, x1], [y0, y1], color="#2a2a2a", lw=1.0, zorder=4)
    # end-window tick at the (x0, y0) end
    nx, ny = -dy, dx
    ax.plot([x0 - 0.1 * nx, x0 + 0.1 * nx], [y0 - 0.1 * ny, y0 + 0.1 * ny],
             color=RED, lw=1.6, zorder=5)


def source_dot(ax, xy, color=ORANGE, ms=10, glow=True):
    x, y = xy
    if glow:
        ax.add_patch(Circle((x, y), 0.14, facecolor=color, edgecolor="none", alpha=0.18, zorder=2))
    ax.plot([x], [y], marker="*", ms=ms, color=color, zorder=5, markeredgecolor="#7a4a00", markeredgewidth=0.4)


def absorber_stack(ax, xy, n=4, w=0.06, h=0.7, gap=0.05, color=LIGHT, edge=GRAY):
    x, y = xy
    total = n * w + (n - 1) * gap
    x0 = x - total / 2
    for i in range(n):
        xi = x0 + i * (w + gap)
        ax.add_patch(Rectangle((xi, y - h / 2), w, h, facecolor=color, edgecolor=edge, lw=0.9, zorder=3))


def speaker_icon(ax, xy, size=0.4, angle_deg=0, color=DARK):
    x, y = xy
    th = np.radians(angle_deg)
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    s = size
    pts = np.array([[-0.35 * s, -0.4 * s], [-0.1 * s, -0.4 * s], [0.35 * s, -0.8 * s],
                     [0.35 * s, 0.8 * s], [-0.1 * s, 0.4 * s], [-0.35 * s, 0.4 * s]])
    pts = pts @ R.T + np.array([x, y])
    ax.add_patch(Polygon(pts, closed=True, facecolor="#cfd8dc", edgecolor=color, lw=1.2, zorder=3))


def mic_icon(ax, xy, r=0.16, color=DARK):
    x, y = xy
    ax.add_patch(Circle((x, y), r, facecolor="white", edgecolor=color, lw=1.3, zorder=3))
    for rr in (r * 0.45, r * 0.75):
        ax.add_patch(Circle((x, y), rr, facecolor="none", edgecolor=color, lw=0.7, zorder=3))


def rotation_stage(ax, xy, r=0.5, angle_deg=0, color=GRAY):
    x, y = xy
    ax.add_patch(Circle((x, y), r, facecolor="none", edgecolor=color, lw=1.1, ls=":", zorder=1))
    for a in range(0, 360, 30):
        th = np.radians(a)
        ax.plot([x + (r - 0.05) * np.cos(th), x + (r + 0.03) * np.cos(th)],
                 [y + (r - 0.05) * np.sin(th), y + (r + 0.03) * np.sin(th)],
                 color=color, lw=0.8, zorder=1)
    th = np.radians(angle_deg)
    ax.annotate("", xy=(x + r * np.cos(th), y + r * np.sin(th)), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.3), zorder=2)


def grating_lines(ax, xy, height=0.6, n=7, color=DARK):
    x, y = xy
    for t in np.linspace(-height / 2, height / 2, n):
        ax.plot([x - 0.03, x + 0.03], [y + t, y + t], color=color, lw=0.9, zorder=3)
    ax.plot([x, x], [y - height / 2, y + height / 2], color=color, lw=1.6, zorder=2, alpha=0.25)

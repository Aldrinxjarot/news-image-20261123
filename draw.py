#!/usr/bin/env python3
"""Draw "The World in One Day - Monday, 23 November 2026" as a 1024x1024
newspaper front page with Pillow.

Every story on the page was checked against wire-style reporting dated
Monday 23 November 2026 (see NOTES.md). Stories whose events belong to
an earlier day are used only where Monday brought a real development,
and the page says so in words ("early Sunday", "Saturday's blaze",
"collapsed Sunday night").

Run:  python3 draw.py          (writes entry.png beside this file)
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
PAPER = (247, 243, 232)
INK = (26, 24, 20)
RED = (163, 22, 33)
GRAY = (96, 92, 84)
RULE = (26, 24, 20)
GOLD = (232, 184, 75)
BLACK = (18, 17, 15)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except OSError:
        return ImageFont.load_default()


SERIF_B = "DejaVuSerif-Bold.ttf"
SERIF = "DejaVuSerif.ttf"
SANS_B = "DejaVuSans-Bold.ttf"
SANS = "DejaVuSans.ttf"


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, width, leading):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def fit_headline(draw, text, name, start_size, width, max_lines):
    size = start_size
    while size > 18:
        fnt = font(name, size)
        if len(wrap(draw, text, fnt, width)) <= max_lines:
            return fnt, size
        size -= 2
    return font(name, size), size


# ---------------------------------------------------------------- stories

HERO_KICKER = "MARKETS — TOKYO · MUMBAI · FRANKFURT · NEW YORK"
HERO_HEAD = "AI fears spark a global market rout"
HERO_BODY = (
    "Fears that artificial-intelligence profits will fall short of the "
    "sums poured into them set off a worldwide sell-off on Monday. "
    "Japan's Nikkei index fell 5.06% and India's Sensex tumbled 1,484 "
    "points, while gold jumped more than 3% as investors ran for safety."
)
HERO_CREDIT = "Market reports — Monday 23 Nov"
HERO_CAPTION = "Share prices fell sharply across Asia on Monday."

PANELS = [
    {
        "kicker": "US POLITICS — WASHINGTON",
        "color": (24, 64, 122),
        "head": "Democrats clinch largest House majority since 1992",
        "body": (
            "AP called the last seats on Monday: at least 258 in the "
            "House after a North Carolina recount put Chuck Hubbard "
            "ahead of Virginia Foxx."
        ),
    },
    {
        "kicker": "UKRAINE — DYMER, KYIV REGION",
        "color": (122, 26, 32),
        "head": "Dymer toll reaches 11 as the search goes on",
        "body": (
            "A Russian drone hit the block early Sunday. The 11th body "
            "was confirmed early Monday; a boy of seven was pulled out "
            "alive on Sunday."
        ),
    },
    {
        "kicker": "CLIMATE — AFTER ANTALYA",
        "color": (18, 96, 62),
        "head": "UN chief “deeply disappointed” by COP31 failure",
        "body": (
            "António Guterres spoke out Monday after the Antalya talks "
            "collapsed Sunday night, the EU rejecting a text that "
            "omitted fossil fuels."
        ),
    },
    {
        "kicker": "INDONESIA — BANTEN",
        "color": (146, 84, 16),
        "head": "Indonesia confirms 24 dead in factory fire",
        "body": (
            "Reuters: the toll from Saturday's blaze at the Banten "
            "candy factory was confirmed on Monday, with about 30 "
            "people still missing."
        ),
    },
]

TICKER = (
    "Belgium strike shuts air traffic control — 429 Brussels flights "
    "cancelled · Kenya and DR Congo restore diplomatic ties · Trump "
    "“inclined” to resume Iran conflict if no deal by New Year · Nepal "
    "PM in Delhi; India pledges 24,000-crore package"
)


# ---------------------------------------------------------------- drawing

def draw_chart(draw, x, y, w, h):
    """Hero illustration: a falling share chart with index labels."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 233, 240),
                   outline=INK, width=2)
    # gridlines
    for i in range(1, 4):
        gy = y + h * i // 4
        draw.line([x + 8, gy, x + w - 8, gy], fill=(178, 190, 202), width=1)
    # jagged descending line (kept clear of the corner labels)
    pts = [
        (0.05, 0.32), (0.16, 0.38), (0.27, 0.30), (0.38, 0.48),
        (0.49, 0.44), (0.60, 0.62), (0.71, 0.57), (0.82, 0.76),
        (0.95, 0.86),
    ]
    xy = [(x + w * fx, y + h * fy) for fx, fy in pts]
    draw.line(xy, fill=RED, width=5, joint="curve")
    for px, py in xy:
        draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED)
    # down arrow at the end
    ex, ey = xy[-1]
    draw.polygon([(ex - 2, ey - 14), (ex + 16, ey + 2), (ex - 14, ey + 4)],
                 fill=RED)
    lab = font(SANS_B, 21)
    draw.text((x + 16, y + 12), "NIKKEI −5.06%", font=lab, fill=RED)
    draw.text((x + 16, y + h - 36), "SENSEX −1,484", font=lab,
              fill=(24, 64, 122))
    gld = font(SANS_B, 21)
    txt = "GOLD +3%"
    tw = draw.textlength(txt, font=gld)
    draw.text((x + w - tw - 14, y + 12), txt, font=gld, fill=(146, 104, 8))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36            # side margin
    CW = W - 2 * M    # column width

    # masthead
    d.line([M, 24, W - M, 24], fill=RULE, width=4)
    d.line([M, 32, W - M, 32], fill=RULE, width=2)
    centered(d, 42, "THE WORLD IN ONE DAY", font(SERIF_B, 58), INK)
    centered(d, 110, "Monday, 23 November 2026", font(SANS_B, 32), RED)
    d.line([M, 154, W - M, 154], fill=RULE, width=2)
    centered(d, 163, "TOKYO · MUMBAI · WASHINGTON · DYMER · ANTALYA · JAKARTA",
             font(SANS_B, 18), GRAY)
    d.line([M, 190, W - M, 190], fill=RULE, width=3)

    # hero
    y = 202
    d.text((M, y), HERO_KICKER, font=font(SANS_B, 20), fill=RED)
    y += 32
    hf, _ = fit_headline(d, HERO_HEAD, SERIF_B, 56, CW, 2)
    y = text_block(d, M, y, HERO_HEAD, hf, INK, CW, 62)
    y += 8
    chart_w, chart_h = 430, 180
    draw_chart(d, M, y, chart_w, chart_h)
    d.text((M, y + chart_h + 7), HERO_CAPTION, font=font(SANS, 16),
           fill=GRAY)
    tx = M + chart_w + 26
    tw = W - M - tx
    by = text_block(d, tx, y + 2, HERO_BODY, font(SERIF, 22), INK, tw, 28)
    d.text((tx, by + 7), HERO_CREDIT, font=font(SANS, 16), fill=GRAY)
    y = 582
    d.line([M, y, W - M, y], fill=RULE, width=3)

    # panels: two columns, two rows
    panels_top = 596
    col_w = (CW - 24) // 2
    col_x = [M, M + col_w + 24]
    row_h = 160
    for i, p in enumerate(PANELS):
        px = col_x[i % 2]
        py = panels_top + (i // 2) * (row_h + 8)
        d.text((px, py), p["kicker"], font=font(SANS_B, 17),
               fill=p["color"])
        pf, _ = fit_headline(d, p["head"], SERIF_B, 29, col_w, 2)
        hy = text_block(d, px, py + 23, p["head"], pf, INK, col_w, 31)
        text_block(d, px, hy + 3, p["body"], font(SANS, 17), INK,
                   col_w, 22)
    # vertical divider between the columns
    mid = M + col_w + 12
    d.line([mid, panels_top + 2, mid, panels_top + 2 * row_h + 6],
           fill=(196, 190, 174), width=2)
    # horizontal rule between the rows
    ry = panels_top + row_h + 3
    d.line([M, ry, W - M, ry], fill=(196, 190, 174), width=2)

    # ticker
    ty = 920
    d.rectangle([0, ty, W, H], fill=BLACK)
    d.text((M, ty + 10), "ALSO TODAY", font=font(SANS_B, 19), fill=GOLD)
    text_block(d, M, ty + 38, TICKER, font(SANS, 17), (240, 238, 230),
               CW, 22)

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

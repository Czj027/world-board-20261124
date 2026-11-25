"""Set the World Dispatch front page using the local fonts and stories."""

import argparse
import json
import math
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from edition import BRIEFS, DATE_NOTE, DESK, FIGURES, LEADS, ORDER, SOURCE_NOTE, WIRE


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SCALE = 3
PAPER = "#f6f1e7"
INK = "#1d2525"
MUTED = "#555a53"
RULE = "#bfb9ac"
SOFT_RULE = "#d5cbb9"
RED = "#9a3b31"
TEAL = "#1c6261"
BLUE = "#3f567b"
OCHRE = "#77551d"
ACCENT = {"conflict": RED, "economy": TEAL, "society": OCHRE, "politics": BLUE}
REGIONS = {
    "North America", "Latin America", "Europe", "Africa", "Middle East",
    "South Asia", "East Asia", "Southeast Asia", "Oceania",
}
FONT_FILES = {
    "serif": "SourceSerif4-Bold.otf",
    "condensed": "BarlowCondensed-Bold.ttf",
    "body": "IBMPlexSansCondensed-Regular.ttf",
    "semibold": "IBMPlexSansCondensed-SemiBold.ttf",
    "mono": "IBMPlexMono-Medium.ttf",
}
LEFT, RIGHT = 24, 1000


def px(*values):
    return tuple(round(value * SCALE) for value in values)


@lru_cache(maxsize=100)
def font(face, size):
    return ImageFont.truetype(ASSETS / FONT_FILES[face], round(size * SCALE))


class Page:
    def __init__(self):
        self.image = Image.new("RGB", px(1024, 1024), PAPER)
        self.draw = ImageDraw.Draw(self.image)

    def text(self, x, y, string, face, size, fill=INK, *, width=None, anchor="lt"):
        style = font(face, size)
        length = style.getlength(string) / SCALE
        if width is not None and length > width + .1:
            raise ValueError(f"{length:.1f}px exceeds {width}px: {string}")
        box = self.draw.textbbox(px(x, y), string, font=style, anchor=anchor)
        if box[0] < 0 or box[1] < 0 or box[2] > 1024 * SCALE or box[3] > 1024 * SCALE:
            raise ValueError(f"Type is beyond the page: {string}")
        self.draw.text(px(x, y), string, font=style, fill=fill, anchor=anchor)

    def fit(self, x, y, text, face, size, width, minimum, fill=INK):
        for halfpoint in range(round(size * 2), round(minimum * 2) - 1, -1):
            trial = halfpoint / 2
            if font(face, trial).getlength(text) <= width * SCALE:
                self.text(x, y, text, face, trial, fill, width=width)
                return
        raise ValueError(f"Text won't fit at {minimum}px: {text}")

    def paragraph(self, x, y, string, face, size, width, max_lines, leading, fill=INK):
        style = font(face, size)
        lines = []
        line = ""
        for word in string.split():
            next_line = f"{line} {word}".strip()
            if line and style.getlength(next_line) > width * SCALE:
                lines.append(line)
                line = word
            else:
                line = next_line
        if line:
            lines.append(line)
        if len(lines) > max_lines:
            raise ValueError(f"Text needs {len(lines)} lines, limit is {max_lines}: {string}")
        for i, line in enumerate(lines):
            self.text(x, y + i * leading, line, face, size, fill, width=width)
        return len(lines)

    def line(self, points, color=RULE, width=1):
        self.draw.line([px(*point) for point in points], fill=color, width=round(width * SCALE))

    def rect(self, x, y, width, height, color):
        self.draw.rectangle(px(x, y, x + width, y + height), fill=color)

    def disk(self, x, y, radius, color, outline=None):
        self.draw.ellipse(px(x - radius, y - radius, x + radius, y + radius),
                          fill=color, outline=outline, width=SCALE)

    def polygon(self, points, color):
        self.draw.polygon([px(*point) for point in points], fill=color)


def badge(page, x, y, number, color):
    page.rect(x, y, 20, 15, color)
    page.text(x + 10, y + 7.5, f"{number:02}", "mono", 10, PAPER, anchor="mm")


def heading(page, y, text, aside):
    page.line([(LEFT, y), (RIGHT, y)], INK, 1.25)
    page.text(LEFT, y + 6, text, "condensed", 18)
    page.text(RIGHT, y + 9, aside, "mono", 10, MUTED, anchor="rt")


def masthead(page, count, regions):
    page.line([(LEFT, 18), (RIGHT, 18)], INK, 2)
    page.text(LEFT, 25, "THE WORLD DISPATCH", "condensed", 19, RED)
    page.text(RIGHT, 28, f"{count} STORIES  /  {regions} REGIONS", "mono", 13, INK, anchor="rt")
    page.fit(LEFT - 2, 46, "Tuesday 24 November 2026", "serif", 75, RIGHT - LEFT + 1, 61)
    page.text(LEFT, 115, "WORLD NEWS  /  THE FULL UTC DAY", "mono", 12, INK)
    page.text(RIGHT, 115, "00:00–24:00 UTC", "mono", 12, RED, anchor="rt")
    page.line([(LEFT, 133), (RIGHT, 133)], INK, 1.2)


def numbers(page):
    width = (RIGHT - LEFT) / len(FIGURES)
    for index, (figure, label) in enumerate(FIGURES):
        x = LEFT + index * width
        if index:
            page.line([(x, 139), (x, 181)])
        page.text(x + 8, 139, figure, "serif", 30, RED if index in (0, 3) else TEAL)
        page.text(x + 8, 170, label, "body", 14, MUTED, width=width - 15)
    page.line([(LEFT, 190), (RIGHT, 190)], INK, 1.5)


def lead_illustration(page, x, y, width, kind):
    height = 88
    if kind == "verdict":
        page.rect(x, y, width, height, "#e2e8df")
        base = x + 15
        page.polygon([(base, y + 34), (base + 49, y + 11), (base + 98, y + 34)], TEAL)
        page.rect(base + 3, y + 36, 92, 5, TEAL)
        for i in range(5):
            page.rect(base + 11 + i * 17, y + 45, 6.5, 27, TEAL)
        page.rect(base + 2, y + 75, 95, 4, TEAL)
        cell_x = x + 128
        for i in range(12):
            col, row = i % 6, i // 6
            cx, cy = cell_x + col * 20, y + 15 + row * 22
            page.rect(cx, cy, 16, 16, TEAL if i < 10 else "#c1cfc5")
            if i < 10:
                page.line([(cx + 4, cy + 8), (cx + 7, cy + 11), (cx + 12, cy + 5)], PAPER, 1.2)
        page.text(cell_x, y + 65, "10 OF 12 COUNTS GUILTY", "mono", 12, TEAL)
    elif kind == "ukraine":
        page.rect(x, y, width, height, "#eee0d4")
        for i, (offset, top, w) in enumerate(((12, 40, 32), (47, 20, 42), (92, 35, 38), (119, 50, 23))):
            base = x + offset
            page.rect(base, y + top, w, height - top - 9, "#a9665b" if i == 1 else "#be9a87")
            for col in range(3):
                for yy in range(top + 7, 74, 14):
                    page.rect(base + 4 + col * (w - 5) / 3, y + yy, 4, 6, "#f4e4d8")
        page.line([(x + 10, y + 79), (x + 148, y + 79)], RED)
        page.text(x + 159, y + 12, "2 KILLED", "condensed", 23, RED)
        page.text(x + 159, y + 43, "40+ INJURED", "condensed", 23, RED)
    elif kind == "oil":
        page.rect(x, y, width, height, "#e9e3d2")
        page.line([(x + 20, y + 58), (x + 108, y + 58), (x + 136, y + 34)], OCHRE, 2)
        page.disk(x + 20, y + 58, 4.5, OCHRE)
        page.disk(x + 136, y + 34, 4.5, OCHRE)
        page.text(x + 13, y + 16, "FEDERAL ORDER", "mono", 10, OCHRE)
        page.text(x + 14, y + 68, "BAGHDAD", "mono", 10, OCHRE)
        for center in (x + width - 75, x + width - 38):
            page.line([(center - 13, y + 66), (center, y + 21), (center + 13, y + 66)], OCHRE, 2)
            page.line([(center - 9, y + 55), (center + 7, y + 43), (center - 7, y + 43), (center + 9, y + 55)], OCHRE)
            page.line([(center - 15, y + 69), (center + 15, y + 69)], OCHRE, 2)
        page.text(x + width - 162, y + 73, "KURDISH-HELD OILFIELDS", "mono", 10, OCHRE)


def lead_section(page, stories, positions):
    spans = [(24, 342), (380, 303), (697, 303)]
    for (key, (kicker, title, summary, sources, illustration)), (x, width) in zip(LEADS.items(), spans):
        color = ACCENT[stories[key]["category"]]
        if x != LEFT:
            page.line([(x - 7, 197), (x - 7, 450)], RULE)
        badge(page, x, 200, positions[key], color)
        page.text(x + 26, 201, kicker, "mono", 12, color, width=width - 26)
        lead_illustration(page, x, 218, width, illustration)
        title_size = 36 if key == 3 else 30
        n = page.paragraph(x, 313, title, "serif", title_size, width, 2, 32)
        page.paragraph(x, 320 + 32 * n, summary, "body", 16, width - 5, 3, 17)
        page.text(x, 438, sources, "mono", 11, color, width=width)


def newsroom(page, stories, positions):
    heading(page, 459, "THE NEWS DESK", "EUROPE  /  ASIA  /  AFRICA  /  MIDDLE EAST  /  AMERICAS")
    column = (RIGHT - LEFT) / 4
    for index, (key, (loc, title, detail, fact)) in enumerate(DESK.items()):
        row, col = divmod(index, 4)
        x, y = LEFT + col * column, 485 + row * 68
        color = ACCENT[stories[key]["category"]]
        if row:
            page.line([(x, y - 3), (x + column - 11, y - 3)], SOFT_RULE)
        if col:
            page.line([(x - 5, y + 1), (x - 5, y + 60)], SOFT_RULE)
        badge(page, x, y + 2, positions[key], color)
        page.text(x + 26, y + 4, loc, "mono", 10.5, color, width=column - 65)
        page.text(x + column - 13, y + 3, fact, "condensed", 17, color, anchor="rt")
        page.fit(x, y + 22, title, "semibold", 20, column - 12, 17)
        page.text(x, y + 47, detail, "body", 14, MUTED, width=column - 12)


def timeline(page, stories, positions):
    page.line([(LEFT, 693), (RIGHT, 693)], INK, 1.2)
    page.rect(LEFT, 697, 79, 47, INK)
    page.text(LEFT + 9, 702, "THE DAY", "condensed", 18, PAPER)
    page.text(LEFT + 9, 722, "IN UTC", "condensed", 16, PAPER)
    step = (RIGHT - LEFT - 79) / len(WIRE)
    for index, (key, (time, place, title, detail)) in enumerate(WIRE.items()):
        x = LEFT + 86 + index * step
        color = ACCENT[stories[key]["category"]]
        if index:
            page.line([(x - 5, 701), (x - 5, 743)], SOFT_RULE)
        page.text(x, 701, f"{time}  /  {place}", "mono", 10.5, color, width=step - 26)
        page.text(x + step - 13, 702, f"{positions[key]:02}", "mono", 10, color, anchor="rt")
        page.fit(x, 715, title, "semibold", 17, step - 10, 15)
        page.text(x, 734, detail, "body", 12.5, MUTED, width=step - 11)


def positions_for_map(page, stories, positions, area):
    left, top, width, height = area
    longitude, south, north = 180, -56, 81

    def slide(lon, lat):
        return left + (lon + longitude) * width / (longitude * 2), top + (north - lat) * height / (north - south)

    land = json.loads((ASSETS / "ne_110m_land.geojson").read_text(encoding="utf-8"))
    for feature in land["features"]:
        geometry = feature["geometry"]
        polygons = geometry["coordinates"]
        if geometry["type"] == "Polygon":
            polygons = [polygons]
        for polygon in polygons:
            for i, ring in enumerate(polygon):
                coords = [slide(lon, min(north, max(south, lat))) for lon, lat in ring]
                page.polygon(coords, "#dcd4c6" if i == 0 else "#efe9df")

    located = []
    for key in (*LEADS, *DESK):
        story = stories[key]
        x, y = slide(story["lon"], story["lat"])
        offsets = [(0, 0)]
        for distance in (12, 18, 25, 33, 45, 61):
            for k in range(16):
                angle = math.tau * k / 16
                offsets.append((distance * math.cos(angle), distance * math.sin(angle)))
        for dx, dy in offsets:
            mx, my = x + dx, y + dy
            if not (left + 7 <= mx <= left + width - 7 and top + 7 <= my <= top + height - 7):
                continue
            if any(math.hypot(mx - ax, my - ay) < 15 for _, _, _, ax, ay in located):
                continue
            located.append((key, x, y, mx, my))
            break
        else:
            raise ValueError(f"No free map marker for {story['place']}")

    for key, x, y, mx, my in located:
        if math.hypot(x - mx, y - my) > 1:
            page.line([(x, y), (mx, my)], "#6b695f", .8)
            page.disk(x, y, 1.5, "#625847")
    for key, _, _, mx, my in located:
        color = ACCENT[stories[key]["category"]]
        page.disk(mx, my, 7.1, color, PAPER)
        page.text(mx, my, f"{positions[key]:02}", "mono", 8, PAPER, anchor="mm")


def index_and_briefs(page, stories, positions):
    heading(page, 753, "AROUND THE WORLD", "15 BRIEFS  /  BY REGION")
    page.text(LEFT, 780, "WHERE IT HAPPENED", "mono", 11.5, TEAL)
    page.text(LEFT + 226, 782, "01–15", "mono", 10.5, MUTED, anchor="rt")
    page.rect(LEFT, 798, 227, 128, "#efe9df")
    positions_for_map(page, stories, positions, (LEFT + 2, 800, 223, 123))
    page.paragraph(LEFT, 931, "Pins 01–15 match the lead and news desk headlines.",
                   "body", 12.5, 225, 2, 13, MUTED)
    names = ("AMERICAS / EUROPE", "AFRICA / MIDDLE EAST", "ASIA / PACIFIC")
    width = (RIGHT - 264) / len(BRIEFS)
    for col, (name, briefs) in enumerate(zip(names, BRIEFS)):
        x = 264 + col * width
        page.line([(x - 6, 781), (x - 6, 953)], RULE)
        page.text(x, 780, name, "mono", 11.5, TEAL)
        for row, (key, place, title) in enumerate(briefs):
            y = 799 + row * 31
            if row:
                page.line([(x, y - 3), (x + width - 7, y - 3)], SOFT_RULE, .75)
            color = ACCENT[stories[key]["category"]]
            page.text(x, y + 1, f"{positions[key]:02}  {place}", "mono", 10, color)
            page.fit(x, y + 12, title, "semibold", 16, width - 12, 14.5)


def footer(page):
    page.line([(LEFT, 963), (RIGHT, 963)], INK, 1.2)
    for index, (label, note) in enumerate((DATE_NOTE, SOURCE_NOTE)):
        y = 971 + index * 17
        page.text(LEFT, y + 1, label, "mono", 10.5, RED if not index else TEAL)
        page.text(LEFT + 102, y, note, "body", 12, MUTED, width=RIGHT - LEFT - 102)
    page.line([(LEFT, 1008), (RIGHT, 1008)], INK, 1.2)


def render(story_data):
    stories = {i: story for i, story in enumerate(story_data, 1)}
    if set(stories) != set(ORDER) or len(ORDER) != len(stories):
        raise ValueError("Every news story must appear exactly once in the editorial order.")
    positions = {key: number for number, key in enumerate(ORDER, 1)}
    page = Page()
    masthead(page, len(stories), len({story["region"] for story in stories.values()}))
    numbers(page)
    lead_section(page, stories, positions)
    newsroom(page, stories, positions)
    timeline(page, stories, positions)
    index_and_briefs(page, stories, positions)
    footer(page)
    return page.image.resize((1024, 1024), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stories", type=Path, default=ROOT / "stories.json")
    parser.add_argument("--out", type=Path, default=ROOT / "entry.png")
    args = parser.parse_args()
    stories = json.loads(args.stories.read_text(encoding="utf-8"))
    output = render(stories)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    output.save(args.out, format="PNG", optimize=True)
    if args.out.stat().st_size > 900_000:
        output.quantize(colors=192, dither=Image.Dither.NONE).save(args.out, optimize=True)
    if args.out.stat().st_size > 900_000:
        raise ValueError("Image exceeds the 900 kB production budget.")


if __name__ == "__main__":
    main()

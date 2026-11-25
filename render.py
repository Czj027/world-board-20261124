"""Render the World Dispatch plate from the local editorial data and assets."""

import argparse
import json
import math
from collections import Counter
from datetime import datetime
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SCALE = 3
PAPER = "#f3efe6"
SECOND = "#bbc5cc"
MUTED = "#8797a3"
BG = "#0b0d10"
PANEL = "#10151a"
BAR = "#202832"
RULE = "#252d35"
ACCENT = {
    "conflict": "#ff765c",
    "economy": "#66d5db",
    "society": "#f8c16c",
    "politics": "#c1b3f6",
}
REGIONS = [
    "North America", "Latin America", "Europe", "Africa", "Middle East",
    "South Asia", "East Asia", "Southeast Asia", "Oceania",
]
FONT_FILES = {
    "display": "BarlowCondensed-Bold.ttf",
    "body": "IBMPlexSansCondensed-SemiBold.ttf",
    "support": "IBMPlexSansCondensed-Regular.ttf",
    "mono": "IBMPlexMono-Medium.ttf",
}


def px(*values):
    return tuple(round(value * SCALE) for value in values)


@lru_cache
def font(face, size):
    return ImageFont.truetype(ASSETS / FONT_FILES[face], round(size * SCALE))


class Plate:
    def __init__(self):
        self.image = Image.new("RGB", px(1024, 1024), BG)
        self.draw = ImageDraw.Draw(self.image)

    def rect(self, x, y, w, h, fill, radius=0, outline=None):
        coords = px(x, y, x + w, y + h)
        if radius:
            self.draw.rounded_rectangle(coords, radius=round(radius * SCALE), fill=fill,
                                        outline=outline, width=SCALE)
        else:
            self.draw.rectangle(coords, fill=fill, outline=outline, width=SCALE)

    def text(self, x, y, value, face, size, fill=PAPER, anchor="lt"):
        self.draw.text(px(x, y), value, font=font(face, size), fill=fill, anchor=anchor)

    def line(self, points, fill, width=1):
        self.draw.line([px(*point) for point in points], fill=fill, width=round(width * SCALE))

    def dot(self, x, y, radius, fill, outline=None, width=1):
        self.draw.ellipse(px(x - radius, y - radius, x + radius, y + radius),
                          fill=fill, outline=outline, width=round(width * SCALE))

    def fit(self, x, y, value, face, size, width, fill=PAPER, minimum=None):
        minimum = size if minimum is None else minimum
        while size >= minimum:
            if font(face, size).getlength(value) <= width * SCALE:
                self.text(x, y, value, face, size, fill)
                return
            size -= .5
        raise ValueError(f"Text exceeds {width}px at {minimum}px: {value}")

    def wrap(self, value, face, size, width):
        lines = [""]
        for word in value.split():
            current = (lines[-1] + " " + word).strip()
            if lines[-1] and font(face, size).getlength(current) > width * SCALE:
                lines.append(word)
            else:
                lines[-1] = current
        return lines


def blend(left, right, part):
    left = bytes.fromhex(left[1:])
    right = bytes.fromhex(right[1:])
    return tuple(round(a + (b - a) * part) for a, b in zip(left, right))


def daylight(lat, lon):
    # NOAA fractional-year approximation, evaluated at the issue's fixed UTC noon.
    day = datetime(2026, 11, 24, 12).timetuple().tm_yday
    g = math.tau * (day - 1) / 365
    decl = (0.006918 - 0.399912 * math.cos(g) + 0.070257 * math.sin(g)
            - 0.006758 * math.cos(2 * g) + 0.000907 * math.sin(2 * g)
            - 0.002697 * math.cos(3 * g) + 0.00148 * math.sin(3 * g))
    equation = 229.18 * (0.000075 + 0.001868 * math.cos(g) - 0.032077 * math.sin(g)
                         - 0.014615 * math.cos(2 * g) - 0.040849 * math.sin(2 * g))
    phi = math.radians(lat)
    hour = math.radians(lon + equation / 4)
    return math.degrees(math.asin(math.sin(phi) * math.sin(decl)
                                  + math.cos(phi) * math.cos(decl) * math.cos(hour)))


def flip(plate, x, y, value, w):
    h = 57
    plate.rect(x, y + 3, w, h, "#050608", 5)
    plate.rect(x, y, w, h, "#27313a", 5)
    plate.rect(x + 1, y + h / 2, w - 2, h / 2 - 1, "#192127", 4)
    plate.text(x + w / 2, y + h / 2 - 1, value, "display", 47, PAPER, "mm")
    plate.line([(x + 1, y + h / 2), (x + w - 1, y + h / 2)], "#11161b", 1.3)
    for side in [x + 1.7, x + w - 1.7]:
        plate.dot(side, y + h / 2, 1.25, "#45545f")


def header(plate, count, region_count, prototype):
    plate.line([(24, 23), (1000, 23)], "#63747f")
    plate.text(25, 33, "THE WORLD", "display", 52)
    plate.text(25, 78, "DISPATCH", "display", 52)
    plate.rect(257, 36, 1, 83, RULE)
    plate.text(279, 35, "GLOBAL NEWS BOARD", "mono", 13, SECOND)
    x = 279
    for word in ("TUE", "24", "NOV", "2026"):
        for char in word:
            flip(plate, x, 61, char, 38)
            x += 42
        x += 10
    plate.text(999, 37, f"{count} STORIES / {region_count} REGIONS", "mono", 15, PAPER, "rt")
    plate.text(999, 62, "00:00–24:00 UTC", "mono", 13, SECOND, "rt")
    if prototype:
        plate.text(999, 91, "LAYOUT STUDY", "mono", 12, ACCENT["society"], "rt")


def status(plate, x, y, kind):
    plate.dot(x, y, 3.1, None, MUTED)
    if kind == "confirmed":
        plate.dot(x, y, 2.9, SECOND)
    if kind == "reported":
        plate.draw.pieslice(px(x - 3, y - 3, x + 3, y + 3), 90, 270, fill=SECOND)


def map_panel(plate, area, stories):
    x, y, width, height = area
    plate.rect(x, y, width, height, PANEL, 8, RULE)
    plate.text(x + 13, y + 12, "WORLD MAP", "mono", 12, PAPER)
    plate.text(x + width - 12, y + 12, "DAYLIGHT AT 12:00 UTC", "mono", 10, MUTED, "rt")
    upright = height > 300
    left, right = x + 13, x + width - 13
    top, bottom = (y + 52, y + height - 50) if upright else (y + 36, y + height - 14)
    highest, lowest = 82, -57

    def project(lon, lat):
        return (left + (lon + 180) * (right - left) / 360,
                top + (highest - lat) * (bottom - top) / (highest - lowest))

    mask = Image.new("1", (round(width) + 2, round(height) + 2))
    land = ImageDraw.Draw(mask)
    features = json.loads((ASSETS / "ne_110m_land.geojson").read_text(encoding="utf-8"))["features"]
    for feature in features:
        geometry = feature["geometry"]
        polygons = geometry["coordinates"]
        if geometry["type"] == "Polygon":
            polygons = [polygons]
        for polygon in polygons:
            for i, ring in enumerate(polygon):
                points = [tuple(round(a - b) for a, b in zip(project(*point[:2]), (x, y)))
                          for point in ring]
                land.polygon(points, fill=int(i == 0))

    for gy in range(round(top), round(bottom) + 1, 5):
        lat = highest - (gy - top) * (highest - lowest) / (bottom - top)
        for gx in range(round(left), round(right) + 1, 5):
            lon = (gx - left) * 360 / (right - left) - 180
            sun = daylight(lat, lon)
            if mask.getpixel((round(gx - x), round(gy - y))):
                color = blend("#455565", "#91a4af", min(1, max(0, (sun + 6) / 6)))
                plate.dot(gx, gy, 1.23, color)
            elif abs(sun) < 1.05 and gy % 10 == round(top) % 10:
                plate.dot(gx, gy, .85, "#4a5964")

    picks = []
    for story in stories:
        anchor = project(story["lon"], story["lat"])
        marker = 10 if story["number"] <= 3 else 7.1
        options = [anchor]
        for radius in (9, 15, 21, 28, 36, 46, 59, 75, 96):
            options.extend((anchor[0] + math.cos(k * math.tau / 16) * radius,
                            anchor[1] + math.sin(k * math.tau / 16) * radius)
                           for k in range(16))
        for mx, my in options:
            if not (left - 3 <= mx <= right + 3 and top - 3 <= my <= bottom + 4):
                continue
            if all(math.hypot(mx - bx, my - by) > marker + br + 2.5 for _, _, bx, by, br in picks):
                picks.append((story, anchor, mx, my, marker))
                break
        else:
            raise ValueError(f"Can't place a map badge for {story['headline']}")

    for story, (ax, ay), mx, my, radius in picks:
        color = ACCENT[story["category"]]
        if math.hypot(mx - ax, my - ay) > 1:
            plate.line([(ax, ay), (mx, my)], blend("#26333b", color, .46), .8)
            plate.dot(ax, ay, 1.45, color)
        if story["number"] <= 3:
            plate.dot(mx, my, radius + 8, None, blend(PANEL, color, .23), .7)
            plate.dot(mx, my, radius + 4, None, blend(PANEL, color, .48), .8)

    for story, _, mx, my, radius in picks:
        color = ACCENT[story["category"]]
        important = story["number"] <= 3
        plate.dot(mx, my, radius, color if important else PANEL, color)
        plate.text(mx, my, f"{story['number']:02}", "mono", 11 if important else 8.5,
                   BG if important else color, "mm")
        if upright and important:
            labels = {1: ("TAIPEI", 18, 10), 2: ("UKRAINE", 19, -14), 3: ("BROOKLYN", -61, -33)}
            label, dx, dy = labels[story["number"]]
            tx, ty = mx + dx, my + dy
            plate.line([(mx, my - radius if dy < 0 else my + radius), (tx + 10, ty + 8)],
                       blend(PANEL, color, .62), .9)
            plate.rect(tx - 4, ty - 4, 8 + 7.5 * len(label), 18, PANEL, 3)
            plate.text(tx, ty, label, "mono", 12.5, color)

    if upright:
        plate.line([(x + 13, y + height - 30), (x + width - 13, y + height - 30)], RULE)
        plate.text(x + 13, y + height - 21, "NUMBERS LINK MAP & STORIES", "mono", 11, SECOND)
        plate.text(x + width - 13, y + height - 21, "24 NOV  /  00:00–24:00 UTC", "mono", 11, MUTED, "rt")


def glyph(plate, x, y, name, color):
    # Small pixel illustrations hand-drawn as runs, read top to bottom.
    designs = {
        "housing": (
            "      ++     ", "     ++++    ", "    ++++++   ", "   ++++++++  ",
            "  +++..++++  ", " ++++..+++++ ", "+++++..++++++", "  ++++++++.  ",
            "  ++..++.+   ", "  ++..++++   ", "  +++++.++   ", "  +++....+   ",
            "  +++....+   ", " ++++++++++  ",
        ),
        "chip": (
            "   + + + +   ", "   + + + +   ", "  +++++++++  ", "+++.......+++",
            "  +.+++++.+  ", "+++.+...+.+ ++", "  +.+.+.+.+  ", "+++.+...+.+++",
            "  +.+++++.+  ", "+++.......+++", "  +++++++++  ", "   + + + +   ",
            "   + + + +   ",
        ),
        "gavel": (
            "    +++      ", "   ++.++     ", "  ++..+++    ", " +++..++     ",
            "+++..++      ", " +++++++     ", "  +++ +++    ", "       +++   ",
            "        +++  ", "         +++ ", "          +++", "  +++++++  ++",
            "  ++...++    ", "+++++++++++  ",
        ),
    }
    for row, line in enumerate(designs[name]):
        for column, pixel in enumerate(line):
            if pixel.strip():
                ink = color if pixel == "+" else blend(PANEL, color, .38)
                plate.rect(x + 3.65 * column, y + 3.65 * row, 2.65, 2.65, ink, .4)


def hero(plate, story, x, y, width, height):
    color = ACCENT[story["category"]]
    plate.rect(x, y, width, height, PANEL, 7, RULE)
    plate.rect(x + 12, y + 12, 19, 17, color, 2)
    plate.text(x + 21.5, y + 20.5, f"{story['number']:02}", "mono", 11, BG, "mm")
    plate.text(x + 38, y + 15, story["place"].upper(), "mono", 11, color)
    status(plate, x + width - 14, y + 20, story["verification"])
    glyph(plate, x + width - 59, y + height - 61, story["glyph"], color)
    title = story.get("hero_headline", story["headline"])
    lines = plate.wrap(title, "display", 31, width - 83)
    if len(lines) > 2:
        raise ValueError(f"Hero wraps beyond two lines: {title}")
    for index, line in enumerate(lines):
        plate.text(x + 12, y + 32 + index * 29, line, "display", 31, PAPER)
    summary_y = y + 64 + (len(lines) - 1) * 22
    for index, line in enumerate(plate.wrap(story["detail"], "support", 15, width - 81)):
        if summary_y + index * 16 + 15 > y + height - 5:
            raise ValueError(f"Hero deck won't fit: {story['detail']}")
        plate.text(x + 12, summary_y + index * 16, line, "support", 15, SECOND)
    if len(lines) == 1 and "credit" in story:
        plate.text(x + 12, y + height - 19, story["credit"], "mono", 10.5, MUTED)


def strip(plate, story, x, y, width, height):
    color = ACCENT[story["category"]]
    plate.rect(x, y, width, height - 3, PANEL, 4, RULE)
    plate.rect(x + 4, y + 4, 25, height - 11, "#1c252d", 3)
    plate.rect(x + 5, y + (height - 3) / 2, 23, (height - 13) / 2, "#151c22", 2)
    plate.line([(x + 4, y + (height - 3) / 2), (x + 29, y + (height - 3) / 2)], "#39434b")
    plate.text(x + 16.5, y + (height - 3) / 2, f"{story['number']:02}", "mono", 11, color, "mm")
    plate.fit(x + 38, y + 7, story["headline"], "body", 18, width - 55, minimum=17)
    place = story["place"].upper()
    plate.text(x + 38, y + 29, place, "mono", 10, color)
    start = x + 44 + font("mono", 10).getlength(place) / SCALE
    plate.fit(start, y + 27, story["detail"], "support", 15, x + width - start - 10, SECOND)
    status(plate, x + width - 9, y + 11, story["verification"])


def legend(plate, y):
    plate.line([(24, y), (1000, y)], "#63747f")
    x = 25
    for key, label in [("conflict", "SECURITY"), ("economy", "MONEY / TECH"),
                       ("society", "PEOPLE / PLANET"), ("politics", "CIVIC / CULTURE / SPORT")]:
        plate.dot(x + 4, y + 14, 3, ACCENT[key])
        plate.text(x + 13, y + 9, label, "mono", 11, SECOND)
        x += 20 + 6.6 * len(label)
    x = 637
    for key, label in [("confirmed", "CONFIRMED"), ("reported", "REPORTED"), ("claim", "CLAIM")]:
        status(plate, x + 4, y + 14, key)
        plate.text(x + 13, y + 9, label, "mono", 11, SECOND)
        x += 25 + 6.6 * len(label)
    plate.text(999, y + 9, "24 NOV", "mono", 11, MUTED, "rt")


def region_summary(plate, stories, x, y):
    counts = Counter(story["region"] for story in stories)
    plate.text(x, y, "REGIONS IN THIS EDITION", "mono", 12, SECOND)
    for i, name in enumerate(region for region in REGIONS if region in counts):
        row_y = y + 25 + i * 20
        plate.text(x, row_y, name.upper(), "mono", 12, MUTED)
        plate.text(x + 162, row_y, f"{counts[name]:02}", "mono", 12, SECOND, "rt")


def render(stories, layout, demo):
    for number, story in enumerate(stories, start=1):
        story["number"] = number
    plate = Plate()
    header(plate, len(stories), len({story["region"] for story in stories}), demo)
    if layout == "panorama":
        map_panel(plate, (24, 135, 785, 232), stories)
        region_summary(plate, stories, 829, 146)
        for i, story in enumerate(stories[:3]):
            hero(plate, story, 24 + i * 328, 376, 320, 121)
        start, step = 534, 49
    else:
        map_panel(plate, (24, 135, 605, 343), stories)
        for i, story in enumerate(stories[:3]):
            hero(plate, story, 641, 135 + i * 115, 359, 108)
        start, step = 514, 51
    for i, desk in enumerate(("AMERICAS & EUROPE", "EUROPE · AFRICA · MIDDLE EAST", "ASIA & PACIFIC")):
        plate.text(24 + i * 328, start - 21, desk, "mono", 12, SECOND)
    rest = stories[3:]
    per_column = math.ceil(len(rest) / 3)
    if per_column > 9:
        raise ValueError("The board can hold at most 30 stories.")
    for i, story in enumerate(rest):
        column, row = divmod(i, per_column)
        strip(plate, story, 24 + column * 328, start + row * step, 320, step)
    legend(plate, 987)
    return plate.image.resize((1024, 1024), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stories", type=Path, default=ROOT / "stories.json")
    parser.add_argument("--out", type=Path, default=ROOT / "entry.png")
    parser.add_argument("--layout", choices=("panorama", "split"), default="split")
    parser.add_argument("--prototype", action="store_true")
    args = parser.parse_args()
    stories = json.loads(args.stories.read_text(encoding="utf-8-sig"))
    output = render(stories, args.layout, args.prototype)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    output.save(args.out, format="PNG", optimize=True)
    if args.out.stat().st_size > 900_000:
        output.quantize(colors=192, dither=Image.Dither.NONE).save(args.out, optimize=True)
    if args.out.stat().st_size > 900_000:
        raise ValueError("Image exceeds the 900 kB production budget.")


if __name__ == "__main__":
    main()

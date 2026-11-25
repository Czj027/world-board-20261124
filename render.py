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
PAPER = "#fcf4e7"
INK = "#192422"
MUTED = "#4e534c"
RULE = "#aca38e"
SOFT_RULE = "#d1c2ad"
RED = "#ac3029"
TEAL = "#07665e"
BLUE = "#244f91"
OCHRE = "#885716"
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


class Illustration:
    """Clip a diagram to its print box while keeping geometry in drawing units."""

    def __init__(self, width, height, design_width, design_height):
        self.image = Image.new("RGB", px(width, height), PAPER)
        self.draw = ImageDraw.Draw(self.image)
        self.scale_x = self.image.width / design_width
        self.scale_y = self.image.height / design_height
        self.unit = min(self.scale_x, self.scale_y)

    def point(self, x, y):
        return round(x * self.scale_x), round(y * self.scale_y)

    def rect(self, x, y, w, h, fill):
        self.draw.rectangle((self.point(x, y), self.point(x + w, y + h)), fill=fill)

    def line(self, points, fill, width=1):
        self.draw.line([self.point(*p) for p in points], fill=fill,
                       width=max(1, round(width * self.unit)), joint="curve")

    def polygon(self, points, fill):
        self.draw.polygon([self.point(*p) for p in points], fill=fill)

    def disk(self, x, y, r, fill, outline=None):
        self.draw.ellipse((self.point(x - r, y - r), self.point(x + r, y + r)),
                          fill=fill, outline=outline, width=max(1, round(self.unit / 2)))

    def text(self, x, y, value, size=9, fill="#263531", face="mono", anchor="lt"):
        style = font(face, size * self.unit / SCALE)
        origin = self.point(x, y)
        left, top, right, bottom = self.draw.textbbox(origin, value, font=style, anchor=anchor)
        if left < 0 or top < 0 or right > self.image.width or bottom > self.image.height:
            raise ValueError(f"Illustration label outside print box: {value}")
        self.draw.text(origin, value, font=style, anchor=anchor, fill=fill)


def place_art(page, x, y, width, height, artwork, native_size):
    canvas = Illustration(width, height, *native_size)
    artwork(canvas)
    page.image.paste(canvas.image, px(x, y))


def badge(page, x, y, number, color):
    page.rect(x, y, 20, 15, color)
    page.text(x + 10, y + 7.5, f"{number:02}", "mono", 10, PAPER, anchor="mm")


def heading(page, y, text, aside):
    page.line([(LEFT, y), (RIGHT, y)], INK, 1.25)
    page.text(LEFT, y + 6, text, "condensed", 18)
    page.text(RIGHT, y + 9, aside, "mono", 10, MUTED, anchor="rt")


def masthead(page, count, regions):
    page.line([(LEFT, 18), (LEFT + 158, 18)], RED, 2.2)
    page.line([(LEFT + 158, 18), (RIGHT, 18)], INK, 2.2)
    page.text(LEFT, 25, "THE WORLD DISPATCH", "condensed", 19, RED)
    page.text(RIGHT, 28, f"{count} STORIES  /  {regions} REGIONS", "mono", 13, INK, anchor="rt")
    page.fit(LEFT - 2, 41, "Tuesday 24 November 2026", "serif", 75, RIGHT - LEFT + 1, 61)
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


def lead_section(page, stories, positions):
    from illustrations_leads import LEAD_ART

    spans = [(24, 342), (380, 303), (697, 303)]
    for (key, (kicker, title, summary, sources, illustration)), (x, width) in zip(LEADS.items(), spans):
        color = ACCENT[stories[key]["category"]]
        if x != LEFT:
            page.line([(x - 7, 197), (x - 7, 450)], RULE)
        badge(page, x, 200, positions[key], color)
        page.text(x + 26, 201, kicker, "mono", 12, color, width=width - 26)
        place_art(page, x, 218, width, 92, LEAD_ART[illustration], (300, 95))
        title_size = 36 if key == 3 else 30
        n = page.paragraph(x, 315, title, "serif", title_size, width, 2, 36 if key == 3 else 32)
        page.paragraph(x, 322 + 32 * n, summary, "body", 16, width - 5, 3, 17)
        page.text(x, 438, sources, "mono", 11, color, width=width)


def newsroom(page, stories, positions):
    from illustrations_desk_a import DESK_ART_A
    from illustrations_desk_b import DESK_ART_B

    artwork = DESK_ART_A | DESK_ART_B
    if set(artwork) != set(DESK):
        raise ValueError("Each desk story needs a dedicated illustration.")
    heading(page, 457, "THE NEWS DESK", "12 ILLUSTRATED REPORTS")
    column = (RIGHT - LEFT) / 6
    for index, (key, (loc, title, detail)) in enumerate(DESK.items()):
        row, col = divmod(index, 6)
        x, y = LEFT + col * column, 482 + row * 115
        color = ACCENT[stories[key]["category"]]
        if row:
            page.line([(x, y - 2), (x + column - 10, y - 2)], RULE)
        if col:
            page.line([(x - 5, y), (x - 5, y + 107)], RULE)
        place_art(page, x, y, column - 10, 46, artwork[key], (150, 50))
        badge(page, x, y + 49, positions[key], color)
        page.fit(x + 24, y + 52, loc, "mono", 10.5, column - 34, 9, color)
        page.paragraph(x, y + 67, title, "semibold", 17, column - 10, 2, 16)
        page.fit(x, y + 99, detail, "body", 13, column - 10, 12, MUTED)


def timeline(page, stories, positions):
    page.line([(LEFT, 712), (RIGHT, 712)], INK, 1.2)
    page.rect(LEFT, 716, 79, 44, INK)
    page.text(LEFT + 9, 721, "THE DAY", "condensed", 17, PAPER)
    page.text(LEFT + 9, 740, "IN UTC", "condensed", 15, PAPER)
    step = (RIGHT - LEFT - 79) / len(WIRE)
    for index, (key, (time, place, title, detail)) in enumerate(WIRE.items()):
        x = LEFT + 86 + index * step
        color = ACCENT[stories[key]["category"]]
        if index:
            page.line([(x - 5, 719), (x - 5, 759)], SOFT_RULE)
        page.text(x, 719, f"{time}  /  {place}", "mono", 10.5, color, width=step - 26)
        page.text(x + step - 13, 719, f"{positions[key]:02}", "mono", 10, color, anchor="rt")
        page.fit(x, 732, title, "semibold", 16, step - 10, 15)
        page.text(x, 751, detail, "body", 12.5, MUTED, width=step - 11)


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
            if max(lat for _, lat in polygon[0]) < south:
                continue
            for i, ring in enumerate(polygon):
                coords = [slide(lon, min(north, max(south, lat))) for lon, lat in ring]
                page.polygon(coords, "#b1b8a1" if i == 0 else "#f1e5d2")
                if i == 0:
                    page.line(coords, "#7f876f", .75)

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
            if any(math.hypot(mx - ax, my - ay) < 16 for _, _, _, ax, ay in located):
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
        page.disk(mx, my, 7.3, color, PAPER)
        page.text(mx, my, f"{positions[key]:02}", "mono", 8.7, PAPER, anchor="mm")


def index_and_briefs(page, stories, positions):
    heading(page, 768, "AROUND THE WORLD", "15 BRIEFS  /  BY REGION")
    page.text(LEFT, 793, "WHERE IT HAPPENED", "mono", 11.5, TEAL)
    page.text(LEFT + 251, 794, "01–15", "mono", 11, MUTED, anchor="rt")
    page.rect(LEFT, 810, 254, 114, "#f1e5d2")
    positions_for_map(page, stories, positions, (LEFT + 2, 818, 250, 96))
    page.paragraph(LEFT, 932, "Numbers 01–15 match the illustrated headlines.",
                   "body", 12.5, 249, 2, 13, MUTED)
    names = ("AMERICAS / EUROPE", "AFRICA / MIDDLE EAST", "ASIA / PACIFIC")
    width = (RIGHT - 291) / len(BRIEFS)
    for col, (name, briefs) in enumerate(zip(names, BRIEFS)):
        x = 291 + col * width
        page.line([(x - 6, 793), (x - 6, 951)], RULE)
        page.text(x, 793, name, "mono", 11.5, TEAL)
        for row, (key, place, title) in enumerate(briefs):
            y = 811 + row * 28
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

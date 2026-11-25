"""Check editorial data, the print file, and repeatability of the local build."""

import hashlib
import json
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image

from edition import BRIEFS, DESK, LEADS, ORDER, WIRE
from render import ACCENT, REGIONS


ROOT = Path(__file__).resolve().parent
DAY = date(2026, 11, 24)
STATUS = {"confirmed", "reported", "claim"}


def demand(condition, message):
    if not condition:
        raise ValueError(message)


def check_clock(value):
    if value is None:
        return
    if len(value) == 10:
        date.fromisoformat(value)
        return
    moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    demand(moment.utcoffset() == timedelta(0), f"Non-UTC timestamp: {value}")


def check_stories():
    stories = json.loads((ROOT / "stories.json").read_text(encoding="utf-8"))
    demand(len(stories) == 34, "Issue should contain 34 stories.")
    demand((len(LEADS), len(DESK), sum(map(len, BRIEFS)), len(WIRE)) == (3, 12, 15, 4),
           "The headline, desk, brief, and timeline sections have changed in size.")
    demand(sorted(ORDER) == list(range(1, len(stories) + 1)),
           "Some stories are missing or repeated in the print order.")
    demand(set(s["region"] for s in stories) == set(REGIONS), "Region coverage differs from the plate.")
    demand(set(s["category"] for s in stories) == set(ACCENT), "A topic color has no stories.")
    titles = set()
    for number, story in enumerate(stories, 1):
        place, title = story["place"], story["headline"]
        demand(bool(place and title and story["detail"]), f"Incomplete text in story {number}.")
        demand(title not in titles, f"Repeated headline: {title}")
        titles.add(title)
        demand(story["verification"] in STATUS, f"Unrecognized status in story {number}.")
        demand(bool(story["verification_note"]), f"Missing evidence note for story {number}.")
        demand(-57 <= story["lat"] <= 82 and -180 <= story["lon"] <= 180,
               f"Map point lies outside the edition for story {number}.")
        clock = story["event_utc"]
        check_clock(clock)
        demand(date.fromisoformat(clock[:10]) == DAY, f"Story date outside the edition for story {number}.")
        demand(len(story["sources"]) >= 2, f"Fewer than two source records for story {number}.")
        addresses = set()
        for source in story["sources"]:
            link = urlparse(source["url"])
            demand(link.scheme == "https" and bool(link.netloc), f"Invalid citation in story {number}.")
            demand(source["url"] not in addresses, f"Repeated source URL for story {number}.")
            addresses.add(source["url"])
            demand(bool(source["name"] and source["note"]), f"Incomplete citation in story {number}.")
            check_clock(source["published_utc"])
    print(f"Stories: {len(stories)} across {len(REGIONS)} regions")
    print("Statuses:", dict(Counter(s["verification"] for s in stories)))
    print("Source records:", sum(len(s["sources"]) for s in stories))


def check_png(file):
    with Image.open(file) as image:
        demand(image.format == "PNG" and image.size == (1024, 1024), f"Invalid geometry for {file}")
        image.verify()
    demand(file.stat().st_size <= 900_000, f"Image exceeds the press budget: {file}")
    return hashlib.sha256(file.read_bytes()).hexdigest()


def check_rebuild(reference):
    with tempfile.TemporaryDirectory(prefix="world-dispatch-") as folder:
        for run in range(2):
            output = Path(folder) / f"rebuild-{run}.png"
            subprocess.run([sys.executable, str(ROOT / "render.py"), "--out", str(output)],
                           cwd=folder, check=True)
            demand(check_png(output) == reference, f"Rebuild {run + 1} differs from entry.png")


def main():
    check_stories()
    entry = ROOT / "entry.png"
    reference = check_png(entry)
    check_rebuild(reference)
    print(f"Pass: 1024 × 1024 PNG, {entry.stat().st_size:,} bytes")
    print(f"Two rebuilds matched entry.png: {reference}")


if __name__ == "__main__":
    main()

# The World Dispatch

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Czj027/world-board-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/Czj027/world-board-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

![A warm-paper front page with fifteen explanatory illustrations, a dated news report and a numbered world map.](entry.png)

The issue covers 24 November 2026, 00:00–24:00 UTC. It contains three lead reports, twelve illustrated desk stories, four timed updates and fifteen briefs from nine regions. The world map links the fifteen illustrated items to their event site, dateline or jurisdiction.

## Editorial record

Each item in [stories.json](stories.json) holds the location, category, date or UTC timestamp, verification status and source notes. When a clock time is unavailable, the record keeps date precision. The ordering, displayed copy and time labels are in [edition.py](edition.py). The scenes are editorial illustrations, and the charts and diagrams describe the findings as reported.

## Reproduce the issue

Run the entry with Python 3.13. The program copies the included image to `/output/entry.png` with the standard library and no network access.

```sh
python main.py
```

To rebuild the graphics locally, install Pillow 13.0.0, then run:

```sh
python render.py
python verify.py
```

The artwork uses 3× supersampling and a Lanczos reduction. The verification command checks the news data, illustration assignments and two independent rebuilds of the submitted PNG. The submitted PNG fixes the rasterization across different judging machines.

## Credits

The entry code and original artwork are MIT licensed. Source Serif 4, Barlow Condensed, IBM Plex Sans Condensed and IBM Plex Mono are distributed with their [OFL license texts](assets). The world map uses Natural Earth's public-domain [1:110m land layer](https://www.naturalearthdata.com/downloads/110m-physical-vectors/110m-land/). The Zaporizhzhia locator uses the corresponding [1:110m country outline](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/).

Built for [make.fun's 24 November world news image bounty](https://make.fun/bounty/news-image-20261124).

# The World Dispatch

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Czj027/world-board-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/Czj027/world-board-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

![A midnight-colored split-flap board with a daylight world map, three leading stories and 27 short reports.](entry.png)

The issue covers 24 November 2026, 00:00–24:00 UTC. Thirty reports from nine regions document the day’s geopolitics, markets, technology, climate, public life, culture and sport. The numbered points locate the stories by event site, dateline or jurisdiction.

## Editorial record

Each item in [stories.json](stories.json) holds the displayed text, location, category, date or UTC timestamp, editorial status and source notes. When a clock time is unavailable, the record keeps date precision. An announced result, estimate or legal action is distinguished from its underlying event. A filled dot marks independent corroboration or a primary record, a half-filled dot indicates a published report with constrained corroboration, and an open dot identifies an attributed claim.

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

The artwork uses 3× supersampling and a Lanczos reduction. The daylight shading uses the fixed date at 12:00 UTC. The verification command checks the news data and compares two fresh local rebuilds with the submitted PNG. The submitted PNG fixes the rasterization across different judging machines.

## Credits

The entry code and original artwork are MIT licensed. The included Barlow Condensed, IBM Plex Sans Condensed and IBM Plex Mono files carry their [OFL license texts](assets). Natural Earth's 1:110m [land layer](https://www.naturalearthdata.com/downloads/110m-physical-vectors/110m-land/) is public domain. The daylight computation uses [NOAA's solar position equations](https://gml.noaa.gov/grad/solcalc/solareqns.PDF).

Built for [make.fun's 24 November world news image bounty](https://make.fun/bounty/news-image-20261124).

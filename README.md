[![make.fun bounty](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Aldrinxjarot/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Aldrinxjarot/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in One Day — Monday, 23 November 2026

Entry for make.fun **news-image-20261123**: one 1024×1024 image that
sums up the world news of Monday, 23 November 2026.

## What it shows

A newspaper front page, drawn entirely by code:

- **Hero — markets:** AI fears spark a global market rout: the Nikkei
  fell 5.06% and the Sensex 1,484 points in Monday trading, while gold
  jumped more than 3%.
- **US politics:** Democrats clinch at least 258 House seats — their
  largest majority since 1992 (AP).
- **Ukraine:** the Dymer apartment-block toll reaches 11, confirmed
  early Monday, as rescuers keep searching (AFP).
- **Climate:** UN chief António Guterres is "deeply disappointed"
  after the COP31 talks collapsed on Sunday night.
- **Indonesia:** the 24 deaths in Saturday's Banten candy-factory
  fire are confirmed on Monday; about 30 people are still missing
  (Reuters).
- An "Also today" ticker: Belgium's strike shuts air traffic control,
  Kenya and DR Congo restore ties, Trump on Iran, and India's package
  for Nepal.

`NOTES.md` lists every story with its date/source justification, plus
the prominent stories that were checked and dropped as earlier days'
news.

## Files

- `entry.png` — the submitted image (1024×1024, drawn by `draw.py`).
- `draw.py` — the Pillow program that draws the front page (build-time
  only; all text and the chart illustration are drawn by the program).
- `main.py` — the entrypoint: standard-library only, copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`) so both graded
  runs produce byte-identical output.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the image from source: `python3 draw.py` (requires Pillow).

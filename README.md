# The World in One Day — 18 November 2026

[![make.fun](https://make.fun/badge/competition/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![entries](https://make.fun/badge/entries/news-image-20261118.svg)](https://make.fun/c/news-image-20261118/leaderboard)
[![open](https://make.fun/badge/status/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)

A single 1024 × 1024 newspaper front page that sums up Wednesday 18 November
2026's world news, entered in
[make.fun's `news-image-20261118`](https://make.fun/c/news-image-20261118)
bounty.

## What the page is

One sheet, 44 stories, seven region bands. The layout is a newspaper front, not a
dashboard: a masthead carrying the date, a sells strip, a figures band, three
illustrated lead cards, ten illustrated secondary cards, a labelled world map,
and a rail of one-line briefs — closing with a date-check box that names what
was deliberately left out and a provenance line naming the agencies.

Every count printed on the page — the region tallies, the story total, the map's
"numbered leads / other datelines" split — is computed from the story data at
build time. None of them is typed by hand, so the arithmetic in the image cannot
disagree with the image's own contents.

## How it is built

`main.py` does not render anything at grading time. It copies the committed
`entry.png` into `MAKEFUN_OUTPUT_DIR` and refuses to write a file that would fail
the gate:

- PNG magic bytes present, `IHDR` first
- width and height read from the IHDR chunk, each at most 1024
- at most 1,048,576 bytes
- `IEND` present as the trailer

Both grading runs therefore produce byte-identical output, and a corrupted copy
fails loudly here rather than scoring zero there.

The page itself is produced ahead of time by the generator kept beside it:

```sh
pip install pillow
python3 build.py out        # writes out/entry.png, validates size and counts
python3 audit.py            # reports text collisions and off-page runs
```

`render.py` composes the page and derives every aggregate from `stories.py`.
`audit.py` wraps `ImageDraw` in a recording proxy so the overlap and clipping
checks measure the text that actually ships, rather than a model of it.

## Editing the data

`stories.py` holds the whole page: masthead, date lines, standfirst, region
order, the six figures, and the story list. A story is a dict with `n` (its
number on the page), `region`, `where` (the dateline), `head`, optional `text`,
optional `lon`/`lat` for the map, and one of:

- `art` — makes it a lead card with a full-height illustration and caption
- `art2` — makes it a secondary card with an illustration strip
- neither — makes it a one-line brief

Counts are recomputed from that list, so adding or removing a story needs no
other edit.

## Licence

MIT — see `LICENSE`.

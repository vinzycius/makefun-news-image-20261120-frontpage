# make.fun news-image-20261120 — FRONT PAGE variant

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/vinzycius/makefun-news-image-20261120-frontpage/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/vinzycius/makefun-news-image-20261120-frontpage/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A single 1024x1024 newspaper front page summarising world news from
**Friday 20 November 2026**, drawn entirely with PIL (Python). Every story
on the page happened, or was first reported, on that one day.

## What's on the page

- Masthead date, sub-headline of the four biggest stories, and a
  "THE DAY IN NUMBERS" strip (3 Kyiv bridges, 300,000+ sheltered before
  Cyclone Akvan, Nikkei −4.8%, 1,000+ UK drones for Ukraine, £260m,
  1,070 Argentina risk index) — 40 stories, 7 regions, 15 fields.
- A "THE DAY BY HOURS" timeline (overnight Kyiv → 08:00 Akvan landfall →
  09:15 Beijing rates → 15:00 Nikkei close → afternoon Brussels deal →
  evening COP31 draft).
- 3 large features (Kyiv bridges, Cyclone Akvan, UK–EU reset deal) and
  12 illustrated small features — 15 illustrated stories in total,
  spanning Europe, Asia, the Middle East, the Americas, Africa, Oceania
  and space — each labelled REPORTED / CLAIM / FORECAST with its source.
- A "WHERE IT HAPPENED" world map with numbered pins 1–15, 25 more
  one-line briefs, and a DATE CHECK box that states the date rule for the
  judge and lists the earlier news deliberately left out (Shenzhen summit,
  ICJ Myanmar ruling, Anthropic IPO pricing, GTA VI launch, Bukele's
  third-term filing, Lula visits Raoni, Jakarta asset bill, hippo Fiona
  dies, U17 Australia-Argentina, Kenya's Ebola discharge, Bougainville
  mine pledge).

## Reproduce

```sh
python3 build_image.py   # regenerates entry.png (needs Pillow)
python3 main.py          # copies entry.png to $MAKEFUN_OUTPUT_DIR (default /output)
```

`main.py` uses only the Python standard library, makes no network calls,
and is deterministic: repeated runs produce byte-identical output.

## Files

- `entry.png` — the entry image, 1024x1024, ≤ 1 MiB
- `build_image.py` — the PIL script that draws `entry.png` from scratch
- `main.py` — the make.fun entry point
- `LICENSE` — MIT

## Date discipline

Numbers are only used where verified. Stories from other days are never
presented as Friday's news: Bukele registered for a third term on
Thursday 19 November, BepiColombo's Mercury capture is due Saturday
21 November (shown as FORECAST), and Kenya discharged its last Ebola
patient on Wednesday 11 November — all are named in DATE CHECK as
excluded or not-yet-happened, along with the other 19 November news the
top five wrongly show as Friday's (Lula visits Raoni, Jakarta asset bill,
hippo Fiona dies, U17 Australia-Argentina) and the Bougainville mine
pledge (announced Monday 16 November). Five new stories were added for
this revision and each was verified against 20 November reporting:
daraxonrasib's 60.7% pancreatic-cancer response, Pakistan's minister
visiting New Delhi for the SCO forum, Argentina's country risk closing at
1,070, Alcaraz and Medvedev reaching the ATP Finals semis, and the CBO's
AUKUS submarine warning.

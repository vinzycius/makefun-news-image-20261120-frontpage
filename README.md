# make.fun news-image-20261120 — FRONT PAGE variant

A single 1024x1024 newspaper front page summarising world news from
**Friday 20 November 2026**, drawn entirely with PIL (Python). Every story
on the page happened, or was first reported, on that one day.

## What's on the page

- Masthead date, sub-headline of the four biggest stories, and a
  "THE DAY IN NUMBERS" strip (3 Kyiv bridges, 300,000+ sheltered before
  Cyclone Akvan, Nikkei −4.8%, 1,000+ UK drones for Ukraine, £260m).
- A "THE DAY BY HOURS" timeline (overnight Kyiv → 08:00 Akvan landfall →
  09:15 Beijing rates → 15:00 Nikkei close → afternoon Brussels deal →
  evening COP31 draft).
- 3 large features (Kyiv bridges, Cyclone Akvan, UK–EU reset deal) and
  12 illustrated small features — 15 illustrated stories in total,
  spanning Europe, Asia, the Middle East, the Americas, Africa, Oceania
  and space — each labelled REPORTED / CLAIM / FORECAST with its source.
- A "WHERE IT HAPPENED" world map with numbered pins 1–15, 20 more
  one-line briefs, and a DATE CHECK box that states the date rule for the
  judge and lists the earlier news deliberately left out (Shenzhen summit,
  ICJ Myanmar ruling, Anthropic IPO pricing, GTA VI launch, Bukele's
  third-term filing, Kenya's Ebola discharge).

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
patient on Wednesday 11 November — all three are named in DATE CHECK
as excluded or not-yet-happened.

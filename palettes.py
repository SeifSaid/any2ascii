# palettes.py
#
# Each palette is a dict:
#   "ramp"   -> characters ordered DARK -> LIGHT (on a dark terminal).
#               ramp[0]  is drawn for the darkest pixels (least ink / empty cell),
#               ramp[-1] for the brightest pixels (most ink / full cell).
#               Index with: ramp[brightness * len(ramp) // 256]
#   "square" -> cell shape of the glyphs:
#               False = HALF-WIDTH (Latin letters, block elements, braille...).
#                       A monospace cell is ~1:2 (w:h), so each glyph is printed
#                       TWICE side by side to fill one square image pixel.
#               True  = FULL-WIDTH (CJK ideographs, full-width space U+3000...).
#                       The glyph already fills a ~square cell, so it is printed
#                       ONCE — no doubling, no padding space.
#
# All ramps below are monotonic in luminosity: each step adds ink/fill, so the
# character density tracks pixel brightness with no "noisy" out-of-order glyphs.

PALETTES = {
    # 1. The canonical 10-level. Reliable, reads well at any size.
    "classic":  {"ramp": " .:-=+*#%@",        "square": False},

    # 2. Long 70-step ramp (Paul Bourke, reversed). Smoothest gradients; best big.
    "detailed": {"ramp": " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
                 "square": False},

    # 3. Unicode block shading — clean, poster-like, exact 0/25/50/75/100% fill.
    "blocks":   {"ramp": " ░▒▓█",             "square": False},

    # 4. Vertical eighth-blocks — smooth, precise luminosity steps.
    "bars":     {"ramp": " ▁▂▃▄▅▆▇█",         "square": False},

    # 5. Soft punctuation gradient — gentle, hand-inked quality.
    "ink":      {"ramp": " .,-~:;=!*#$@",     "square": False},

    # 6. Stripped down — punchy, graphic, good for high-contrast images.
    "minimal":  {"ramp": " .:#",              "square": False},

    # 7. Pure two-tone — silhouette / stencil look.
    "binary":   {"ramp": " █",                "square": False},

    # 8. Braille by dot-count (0 -> 8 dots). Fine-grained, near photographic.
    "braille":  {"ramp": "⠀⠁⠃⠇⠧⠷⠿⡿⣿",        "square": False},

    # 9. Heavy contrast jump — dramatic, crushed midtones.
    "noir":     {"ramp": " .:+#%@█",          "square": False},

    # 10. Full-width CJK by stroke density — square cells, no doubling.
    "kanji":    {"ramp": "　一二三王田画龍鬱",   "square": True},
}

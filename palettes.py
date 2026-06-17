# palettes.py
# Each ramp runs dark -> light: ramp[0] is drawn for the darkest pixels,
# ramp[-1] for the brightest. Index into it with: ramp[brightness * (len(ramp)-1) // 255]

PALETTES = {
    # 1. The canonical 10-level. Reliable, reads well at any size.
    "classic":   " .:-=+*#%@",

    # 2. Long 70-step ramp — smooth gradients, best for larger output.
    "detailed":  " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",

    # 3. Unicode block shading — clean, poster-like, no letterforms.
    "blocks":    " ░▒▓█",

    # 4. Stripped down — punchy, graphic, good for high-contrast images.
    "minimal":   " .:#",

    # 5. Pure two-tone — silhouette / stencil look.
    "binary":    " █",

    # 6. Stippled dots — soft, halftone / newspaper feel.
    "stipple":   " .·°•◦○●",

    # 7. Soft gradient of punctuation — gentle, hand-drawn quality.
    "ink":       " .,-~:;=!*#$@",

    # 8. Rounded glyphs — organic, bubbly texture.
    "bubble":    " .·:oО0@",

    # 9. Heavy contrast jump — dramatic, almost no midtones.
    "noir":      "  .':+#%@█",

    # 10. Digital / readout vibe — angular, techy.
    "matrix":    " :+=ivlIcoSZ#@",
    "kanji":    "　一二三王田画龍鬱",
    "bars":     " ▁▂▃▄▅▆▇█",
    "stars":    " ·∙∗⋆✦✶★",
    "geo":      " ·▫◦▪◆◼█",
        # ---- True density ramps (dark -> light). These render as real art. ----

    # Circles, light to dense. Smooth, organic.
    "circles":  " ·∙•◦○◉●",

    # Braille by dot-count (0->8 dots). Subtle, fine-grained — see note, it's special.
    "braille":  "⠀⠁⠃⠇⠧⠷⠿⡿⣿",

    # Soft shading, smoke-like fade.
    "smoke":    " ·:░▒▓█",

    # Hard shadow gradient — punchy midtone jump.
    "shadows":  " .-:=▒▓█",

    # ---- Texture palettes (NOT density-ordered). Pattern over tone. ----

    # Waves — wavy ASCII. Looks like your screenshot's wave preview.
    "waves":    " ~∼≈",

    # Pipes — box-drawing. Reads as circuitry / blueprint, not shading.
    "pipes":    " ─│┌┐└┘├┤┼",

    # Shards — angular fragments. Sharp, broken-glass texture.
    "shards":   " �ı◢◣◤◥◸◹",

    # ---- Full-width (the kanji caveat applies — halve your column budget) ----

    # Katakana, roughly ordered by ink. Full-width space (U+3000) as "empty".
    "katakana": "　ノヽニシツハホネヲ",

}
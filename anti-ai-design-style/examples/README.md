# Examples: the same product, twice

**TL;DR:** Open both files in a browser. One looks like every AI page ever
made. The other could only belong to this one product. Both scanners agree.

**Read this first: the fixed version was wrong once.** Version 1 scored 0 on
the AI-look scanner. It still looked like Claude's own design system. It used
warm cream, a bookish serif and a terracotta accent. Ben caught it.
The `anti-antropik-design` scanner then measured it. The background sat 2.74
Delta-E from a brand neutral, where 12 or more is required. Georgia turned out
to be an excluded typeface. Version 2 uses a generated palette that passes
both guards. The story is in `../reference/brand-distance.md`. It is why the
skill now requires two scanners, not one.

Both pages sell the same made-up product: an invoicing app for small
bakeries in Cairo.

## The scores (measured, not opinions)

| File | AI-look score | Verdict | What the scanner found |
|---|---|---|---|
| `slop-example.html` | 52/100, "reads as AI-generated" | FAIL | 20 tells + 3 craft flags: gradient headline text, glow blobs, dark-glass combo, twin "Get Started"/"Learn More" buttons, fake stats, emoji icons, placeholder people, the full features/testimonials/pricing/FAQ skeleton, buzzword copy, and more |
| `fixed-example.html` (v2) | 0/100, "distinct" | PASS | nothing. Also COMPLIANT on brand distance |

Re-check any time. Both guards:

```
python3 ../scripts/ai_tell_scan.py slop-example.html
python3 ../scripts/ai_tell_scan.py fixed-example.html
python3 "$(python3 ../scripts/find_brand_guard.py)"/scripts/audit_file.py fixed-example.html
```

## What changed, in five moves

1. **The product got a name and a place.** "InvoiceFlow for modern teams"
   became "Fadl's Ledger, Bab al-Louq, Cairo". Every claim got specific:
   "40 baladi loaves daily", "120 EGP a month", "invoices in Arabic or English".
   The test: could this page sell any other product? Now it can't.
2. **Colours generated, not picked.** The palette comes from
   `generate_palette.py --hue 18 --temp neutral --chroma high`. Neutral greys
   with one deep oxblood accent, 27.9 Delta-E from the nearest brand value.
   Picking warm cream by hand is what broke version 1.
3. **Type chosen on purpose.** One grotesque (Archivo) plus one mono
   (Roboto Mono) for the ledger figures. Not Inter by default, and not the
   geometric-sans-over-bookish-serif structure that the brand guard excludes.
4. **Structure follows the visitor's questions.** What is it → how does it
   work → what does it cost. The testimonial grid, stat row, logo marquee
   and FAQ are gone because a new product has none of those things honestly.
5. **Honesty as design.** Instead of "10K+ users", the page shows a sample
   ledger. Instead of "99.9% uptime", it promises your data stays exportable.
   Real trust signals for a product with no users yet.

## Accessibility built in (fixed version)

Secondary text is 5.4:1 contrast. Body is 17px serif at 1.55 line height.
Line length is capped at readable widths. Focus outlines are visible.
Buttons are at least 44px tall. There is no motion at all, so nothing to
reduce. Text is left-aligned.

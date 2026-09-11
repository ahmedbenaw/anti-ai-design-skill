Built it — `budget-home.html`, single file, opens straight in a browser at 390px phone width.

**What's on the screen**

1. **Allowance left** — the big number (EGP 1,240.50) on a white index card with tape at the top, tilted about a degree off-square. Under it: the striped progress bar, "41% left / 11 days to go", and a red felt-tip scribble in the margin — *~113 / day, habibi*. Then a one-liner translating that into things you actually buy: "roughly 2 koshary + microbus".
2. **Top 3 categories** — Food & koshary (710), Getting to campus (495), Printing & mulakhasat (320). Each is a sticker-ish card with a rank digit, a coloured tile, a bilingual label (أكل / مواصلات / تصوير) and a specific memory rather than a category name: "last one: Abou Tarek, Tuesday", "2 late-night Ubers", "Thermo notes. We know." Plus an honest footer: *...and 234.50 EGP of "I don't remember"* - which is exactly what 3,000 minus the tracked 1,525 minus what is left actually comes to.
3. **Log an expense** — a fat black button with a hard red offset shadow that physically presses down when you click it. Label is "Log what I just spent", with "takes 4 seconds, promise" underneath.

**How I kept it off the generic-fintech path**

- No purple-to-blue gradient, no glassmorphism, no floating pill nav. The whole surface is warm cream ruled paper — a squared notebook, the thing this money is actually tracked in today.
- Hard 2–3px black outlines and solid offset shadows instead of soft blurred cards. Everything sits slightly rotated so it reads as stuff stuck in a notebook, not a component library.
- Palette is borrowed from things around a Cairo campus: karkadeh red, mint-tea green, highlighter yellow, biro ink. Accents are a marker swipe under "Where it went" and the yellow tape.
- Voice is a friend, not a bank. "Ezayak, Youssef", "your mum sent on the 1st", "Thermo notes. We know." The framing is *masroof*, and the anchor is days-to-next-transfer — which is how the month actually feels when the money is a fixed monthly drop, not a salary.
- Egyptian specifics are load-bearing, not decoration: EGP, Abou Tarek, microbus/metro, printing *mulakhasat*, Vodafone EG in the status bar, Arabic category tags beside the English.

**Notes**

- Static mockup: the button has a press state but nothing is wired up. Numbers are made up.
- Fonts come from Google Fonts (Space Grotesk / Caveat / IBM Plex Sans Arabic) with system fallbacks, so it degrades fine offline.
- The Arabic tags are bidi-isolated so they don't reorder the English and numbers around them.
- One design-lint warning I deliberately left as-is and suppressed for this file: the phone frame uses `overflow:hidden`, which the linter flags as a clipping container. That's exactly what draws the rounded screen edge here, and there are no tooltips or popovers to clip.

Easy next moves if you want them: a second screen for the actual "log expense" sheet (amount pad + those same category stickers), a "split with friends" case, or a week-by-week view so the 11-days-to-go anxiety has somewhere to go.

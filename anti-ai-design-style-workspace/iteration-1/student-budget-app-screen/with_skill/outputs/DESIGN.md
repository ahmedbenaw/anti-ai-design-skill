# DESIGN.md: Masrouf (مصروف)

> Assumed brief. You were not around to answer the three questions, so I
> drafted this from your one-line request. Change any line and I will
> rebuild to match.

## 1. Who is this for, really?
An Egyptian university student who gets a fixed monthly allowance
("masrouf") from family at the start of the month. They spend it in cash
and Vodafone Cash, mostly from a phone. The number has to last until the
next masrouf arrives.

## 2. Three things on this screen that could ONLY belong to this product
- The word "masrouf" and the countdown to the NEXT masrouf, with the
  "safe per day" amount — the number a student actually thinks in.
- Real student categories at real Cairo prices in EGP: metro and microbus
  fares, koshary and cafeteria sandwiches, the photocopy shop for lecture
  notes ("sheets").
- One-tap "log it again" chips for the things you buy every day (metro
  ticket, koshary, photocopied notes), so logging takes two seconds
  between lectures.

## 3. The feeling, in plain words
Like the lined kashkool (the standard Egyptian student notebook): a ruled
page, a red margin line, a highlighter over the number that matters.
Plain, sturdy, a little bit handwritten-by-you. Not a bank.

## 4. Colours
- Paper (background): #FBFBF7 ("kashkool paper")
- Ink (text):          #1F2A44 ("ballpoint blue-black")
- Margin red (accent): #B7271F ("margin line"). Used ONLY for the log
  button and the notebook margin rule
- Ruling:              #C6D6E6 ("pale blue lines"). Dividers only, never text
- Highlighter:         #FFE57A ("yellow marker"). One use: over the amount left
- Secondary text:      #4B5563, 7.1:1 on paper

## 5. Fonts
- Headings and numbers: Rubik. It has matching Arabic and Latin, and its
  heavy weight looks like the marker-pen label on a kashkool cover.
- Body: IBM Plex Sans Arabic. Clear at 16px, proper Arabic glyphs, and
  the figures line up in a ledger.
- Fallbacks: system-ui, Tahoma (has Arabic), sans-serif.

## 6. Never do these
- No gradient balance card, no ring chart, no glow pills (the fintech
  home-screen template).
- No purple/indigo; no glassmorphism; no decorative blur.
- No emoji as icons.
- No invented stats, streaks, badges or "great job" toasts.
- No "Get Started" / "Learn More". Buttons say what they do.
- Body text at least 16px; contrast at least 4.5:1; touch targets at
  least 44px; every animation behind prefers-reduced-motion.
- Sample numbers are labelled as sample numbers.

## 7. What the screen must answer, in order
1. "How much masrouf is left, and how long does it have to last?"
2. "Where did it go this month?" (top 3 categories)
3. "Log what I just spent." (one button, in thumb reach)
One section per question. Nothing else.

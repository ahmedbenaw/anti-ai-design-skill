# DESIGN.md — clinic one-pager

**Assumed brief.** The owner was not present to answer questions, so this
was drafted from the request and marked as an assumption. Change any line
you disagree with, then rebuild the page from it.

## 1. Who is this for, really?
People in Alexandria with a sore back, neck or knee. Also people rehabbing
after an operation. They read on a phone. They want the price, then a
WhatsApp message sent in under a minute. Many read Arabic first.

## 2. Three things on this page that could ONLY belong to this clinic
- Prices in Egyptian pounds next to the length of each session.
- A WhatsApp button that opens a message already written in Arabic.
- Ramadan opening hours, and a note about the lift and the stairs.

## 3. The feeling, in plain words
Plain, checked, calm. Like the printed price card taped to the desk in a
real clinic. One thing borrowed from the clinic's own world: the bright
pink of kinesiology tape, used only where the eye needs to land.

## 4. Colours: generated, not hand-picked
From `generate_palette.py --hue 340 --temp cool --chroma medium`
(VERDICT: COMPLIANT).
- Background: `#F4FAFF` (cool paper)
- Surface: `#FFFFFF`
- Text: `#2B3136` (ink)
- Secondary text: `#60666C`
- Accent: `#700055` (tape), used only for buttons, links, prices and rules
- Borders: `#888F94`, `#6C7378`

## 5. Fonts (two, chosen on purpose)
- Headings: Cairo, because it carries Arabic and Latin in one family, so
  a bilingual line does not change shape halfway through.
- Body: IBM Plex Sans Arabic, for the same reason, and because its
  numerals sit evenly in a price column.

## 6. Never do these
- No purple gradients, no gradient-filled headlines.
- No glow shapes, glass panels or decorative blur.
- No emoji as icons.
- No "Get Started" and "Learn More" pair. Name the action.
- No invented patients, reviews, star ratings or round numbers.
- No stock photos of smiling strangers.
- No fade-in on scroll. The page works with JavaScript switched off,
  because it has none.
- Body text 17px, contrast 4.5:1 or better, lines under 75 characters,
  tap targets 44px or larger.
- No warm cream plus bookish serif plus terracotta.

## 7. What the page must answer, in order
1. What is this place, where is it, and how do I book right now?
2. What is wrong with me, and which session do I need?
3. What does it cost, in pounds?
4. When are you open?
5. Who will actually treat me?
6. How do I get there and what do I bring?

One section per question. Nothing else.

# DESIGN.md: Masrouf (home screen)

**Assumed brief.** The user was not here to answer questions, so I drafted this
from their request and built to it. Change any line and I will rebuild.

## 1. Who is this for, really?

A student at an Egyptian public university. A parent hands over one lump of
pocket money, the masrouf, on a set day each month. She carries cash and pays
in coins for the microbus. In the last week of the month she checks her phone
to see whether the money will stretch.

## 2. Three things here that could ONLY belong to this product

- The count-down is to the day the next masrouf lands, not to the 1st of the
  month. That is the real deadline for this user.
- The top category is fares split into microbus rides and metro trips, priced
  in single-digit pounds, because that is how the money actually leaves.
- Second category is printed lecture handouts (malazem) from the photocopy
  kiosk, counted in pages. No fintech app in the world has that row.

## 3. The feeling, in plain words

Plain, honest, a bit stubborn. Like the squared kashkool notebook and the
blue ballpoint students already keep the count in. Stolen from that world:
the 6mm squared grid, the red margin rule, blue ink for numbers.

## 4. Colours: generated, then named

Generated, not hand-picked:
`generate_palette.py --hue 248 --temp cool --chroma medium --name Kashkool`
It printed `VERDICT: COMPLIANT`. Used here:

- Background: `#F4FAFF`, a cool paper, not cream
- Surface: `#FFFFFF`
- Text: `#2B3136` · Secondary text: `#60666C`
- Accent (button and links only): `#003E56`, ballpoint blue-black
- Bars: `#00639A`, pen blue
- Focus ring: `#78001B`, the red margin rule

## 5. Fonts (two, chosen on purpose)

- Text: the device's own UI sans. Reason: the target phone is a mid-range
  Android on a metered data bundle. A downloaded font is a real cost here.
- Numbers: the device's mono. Reason: money in a column should line up like a
  ledger, and a student checking a total should be able to compare rows by eye.

Structure is one sans plus one mono. No serif body, no display face.

## 6. Never do these

- No gradient balance card, no glow pill, no ring chart
- No emoji as icons
- No "Get Started" / "Learn More"
- No invented users, testimonials, logos or round numbers
- No animation at all on this screen
- Body text 16px or more, contrast 4.5:1 or better
- No warm cream + serif + terracotta
- Sample data is labelled as sample data, on the screen

## 7. What the screen must answer, in order

1. How much masrouf is left, and how long must it last?
2. Where did the rest of it go this month?
3. I just spent something — where do I write it down?

One block per question. Nothing else on the screen.

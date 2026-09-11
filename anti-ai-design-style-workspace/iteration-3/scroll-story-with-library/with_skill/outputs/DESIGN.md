# DESIGN.md — olive oil press, Siwa (assumed brief)

Assumed. The owner was not present, so this brief was drafted from the
request alone. Confirm or change any line.

## 1. Who is this for, really?
People who already bought a bottle, or are about to, and want to know how
the oil was made before they trust it. They read on a phone.

## 2. Three things on this page that could ONLY belong to this press
- Siwa's own conditions: an oasis in the Western Desert, spring water,
  salt lakes, a short cold season.
- The press's own timing: picked by hand, pressed the same day, kept under
  27 degrees, rested in steel, bottled in dark glass.
- A real map pin on the press in Siwa, with the address as text.
  (The pin is a STAND-IN at the town centre until the owner gives the
  real position.)

## 3. The feeling, in plain words
Quiet, plain, unhurried. Like a printed leaflet left on the counter.
One thing to look at per screen.

## 4. Colours: generated, then named
Generated with generate_palette.py --hue 95 --temp neutral --chroma medium
(VERDICT: COMPLIANT).
- Background: #FAF9F9 ("paper")
- Sunken surface: #F0EFEF
- Text: #313030
- Secondary text: #666566
- Border: #919091
- Accent: #423900 ("dark olive"), links and the map pin only

## 5. Fonts
One grotesque throughout: the visitor's system sans. Chosen so the page
loads with no web font, on a slow desert connection, and reads the same
way everywhere. No serif. No display face.

## 6. Never do these
- No gradients, glow, blur panels, emoji, or icon tiles.
- No invented numbers, people, awards, or reviews.
- No scroll reveal carpet. One gentle reveal per section, once, and none
  at all when the visitor has turned animations off.
- No uppercase tracked labels, no side-stripe borders, no card shadows.
- No excluded typefaces or the cream-serif-clay combination.
- Body 16px or more, contrast 4.5:1 or more, lines under 75 characters.

## 7. What the page must answer, in order
1. Where do the trees grow?
2. When and how do you pick?
3. How do you press?
4. What happens before it is bottled?
5. Where is the press? (map)

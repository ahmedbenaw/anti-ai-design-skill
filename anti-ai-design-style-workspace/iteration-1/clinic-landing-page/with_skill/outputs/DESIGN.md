# DESIGN.md — physiotherapy clinic, Alexandria

**Assumed brief.** The owner was not available to answer the brief
questions, so this was drafted from the request ("small physio clinic in
Alexandria, 3 therapists, services, EGP prices, hours, WhatsApp booking,
not like every other clinic site"). Change anything that is wrong.

## 1. Who is this for, really?
Someone in Alexandria with a sore back, a bad knee, or a parent who just
had surgery. They are on a phone, probably in pain, and want three things
fast: does this clinic treat my problem, what does it cost, and how do I
book without a phone call.

## 2. Three things on this page that could ONLY belong to this clinic
- A price board in EGP with session lengths, and "pay cash or InstaPay".
- "Your first visit, minute by minute" and a sample home-exercise sheet,
  which is what a physio actually hands you.
- Alexandria hours (closed Friday, open to 9 pm) with a live "open now"
  line in Cairo time, and a WhatsApp button whose message is pre-written
  with what the clinic needs to know.

## 3. The feeling, in plain words
Calm, practical, unhurried. Like a tidy treatment room: paper on the
table, a printed exercise sheet, a row of colour-coded resistance bands
on the wall. Not a hospital, not a spa.

## 4. Colours
- Background: #f3f5f2 ("table paper", a cool off-white, not cream)
- Text:       #15211f ("ink")
- Accent:     #0e5b70 ("sea", the Mediterranean off the Corniche) — links, headings rules
- Secondary text: #465552 ("slate") — 7.0:1 on the background
- Booking button: #25d366 ("WhatsApp green") with ink text — used only for the WhatsApp action
- Motif: one thin strip of resistance-band colours (yellow, red, green,
  blue, black). Decorative, appears once, hidden from screen readers.

## 5. Fonts
- Headings: Barlow Condensed — sturdy and athletic, close to the lettering on
  sports tape and gym charts. Condensed also fits long headings on a phone.
- Body: Atkinson Hyperlegible — designed for low-vision readers. Many
  patients are older or reading on a cracked phone in a waiting room.

## 6. Never do these
- No purple/indigo gradients; no gradient-filled headline text
- No glow blobs, glassmorphism panels, or decorative blur
- No emoji as icons; no ✨
- No "Get Started" / "Learn More" button pair — name the action
- No invented numbers or invented people (no fake therapist names, no
  "500 happy patients", no testimonials we don't have)
- No fade-in-on-scroll; respect reduced-motion settings
- No stock photos of smiling models in white coats
- No section that can't be filled honestly
- Body text at least 16px, contrast at least 4.5:1, lines under 75 characters
- No em-dashes in page copy

## 7. What the page must answer, in order
1. Do you treat my problem? (what we treat, and an honest "message us if unsure")
2. What will it cost me? (EGP price board)
3. What happens when I come in? (first visit, minute by minute)
4. Who will treat me? (the three therapists)
5. When are you open and where are you? (hours with live status, address)
6. How do I book? (WhatsApp, what to write, what to bring, cancellation)
One section per question. Nothing else.

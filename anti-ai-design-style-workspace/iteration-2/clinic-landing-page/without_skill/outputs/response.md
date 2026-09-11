Done — `clinic.html` is a single file, no folders, no build step. Upload it as-is (rename it `index.html` if you want it to be your homepage).

**Six things to change before you go live.** They're listed in a comment at the very top of the file, and each one tells you what to search for:

1. **Clinic name** — search `Nile Physiotherapy`
2. **WhatsApp number** — search `201000000000`. Country code + number, no `+`, no spaces. It appears in 6 places (header, hero, the three booking buttons, and the mobile bar) — one find-and-replace-all does them all.
3. **Phone number** — this one is written two ways, so do **two** replacements: `+201000000000` for the three tap-to-call links, and `+20 100 000 0000` for the two places the number is printed for people to read. If your phone number and your WhatsApp number are different, **do the phone one first** — otherwise step 2 will overwrite part of it.
4. **Address and map link** — search `MAPLINK`
5. **Therapist names** — search `THERAPISTS`
6. **Prices and hours** — search `PRICES` and `HOURS`

I filled everything with plausible placeholders (600 EGP assessment, 400 follow-up, 2,100 for six, 750 home visit, Sat–Thu 10:00–20:00, Friday closed) so you can see how it reads. Change the numbers to yours.

**What it does**

- **Prices are the centrepiece**, laid out like a printed price list rather than hidden in cards — assessment, follow-up, a six-session course, post-op, sports, home visit, and a cheap second-opinion slot. Every price is on the page in EGP, which is the single thing most clinic sites won't do.
- **WhatsApp booking is three different buttons**, not one. Each opens WhatsApp with a different message already typed — first visit, follow-up, home visit — with blanks for name and district. People can edit before sending. Much higher chance they actually send it than a generic "chat with us".
- **Opening hours highlight today automatically**, and the bar pinned to the bottom of the phone screen says "Open now — until 20:00" or "Closed right now" based on the visitor's clock. Nothing to maintain; it reads your hours table.
- **No stock photos**, because stock photos of smiling physiotherapists are exactly what makes every clinic site look the same — and because a fake photo of a clinic that isn't yours is worse than none. Instead there's a drawn spine-and-motion diagram in the header, done in code so there are no image files to upload.
- The look is warm paper and ink with a clay red and a deep sea green, a proper serif for headlines, and a bit of Arabic alongside the English. Nothing like the blue-gradient-and-rounded-cards template.
- Works on phones, keyboard-accessible, and it respects "reduce motion" settings.

**Two suggestions**

- **Swap the therapist bios for real ones and it gets much stronger.** Specifics — years of experience, what each person is actually good at — are what make people choose you over the clinic down the road. Photos of your three therapists would help too, if you have decent ones; drop them in and I can wire them into the layout.
- **Take one photo of your building entrance** and it solves the "I couldn't find it" messages. Same offer — send it over and I'll place it.

One caveat worth naming: the page currently says "Since 2016" and "Prices last reviewed January 2026". Make those true or delete them.

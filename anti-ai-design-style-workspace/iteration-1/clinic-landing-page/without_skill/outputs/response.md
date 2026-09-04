Your site is saved as **clinic.html** — one file, no dependencies to install, upload it as-is.

**What's on the page**

- Sticky top bar with a live "Open now / Closed · opens Saturday 10:00" badge (calculated in Cairo time)
- Hero with a short pitch and a quick-facts card (price from, hours, area) plus an Arabic tagline
- **Services & prices** laid out like a menu with roman numerals, durations, and EGP prices — plus three session packages
- **Three therapists** — name, specialty, short bio, tags
- **Hours** table (today's row is highlighted automatically) and address with an embedded map
- **Booking**: a tiny form (name, service, preferred day/time, problem) that opens WhatsApp with the message already written. Nothing sends until the patient presses send in WhatsApp. There's also a floating WhatsApp button on phones.

**Design**: warm paper background, deep sea-green and terracotta, a serif headline face — deliberately not the blue-gradient-with-stock-photo look. Works on phones and desktops, no horizontal scrolling.

**Three things you must change** (open the file in any text editor, search for `CHANGE ME` — there are 15 spots, all marked):

1. **Your WhatsApp number** — one line near the bottom: `const WHATSAPP_NUMBER = "20XXXXXXXXXX";` Egypt mobiles look like `201001234567` (country code, no plus, no spaces). Every WhatsApp link on the page uses this one value. Until you set it, the form shows a preview of the message instead of opening WhatsApp.
2. **Names, bios, address, phone, email** — I invented "Corniche Physio", the three therapist names, and a Smouha address as placeholders.
3. **Prices and hours** — I used plausible numbers (350–500 EGP per session, Sat–Thu 10:00–21:00, Thursday to 18:00, Friday closed). Edit the text in the services list and the hours table; if you change the hours, also update the `HOURS` line in the script so the "Open now" badge stays correct.

Optional: the map is a generic Smouha embed — replace the `src` with your own from Google Maps (Share → Embed a map) so it pins your exact building. The fonts load from Google Fonts; if that's ever blocked the page falls back to system fonts and still looks fine.

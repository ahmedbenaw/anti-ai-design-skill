Done. I saved the page as `story.html` in the outputs folder.

What's in it:

- **Five short sections** — the grove, the harvest, the press, the rest, the bottle — each with a few sentences about how the oil is made in Siwa. The copy is a starting point; swap in your own details (tree count, harvest dates, your name) wherever it's generic.
- **A sixth "Where to find us" section** at the end with a small Leaflet map centred on Siwa (about 29.20° N, 25.52° E) and a marker labelled "The press". The map uses OpenStreetMap tiles. Change the `press` coordinates in the script to your exact location.
- **GSAP + ScrollTrigger** (from cdnjs) fade each section in once as it scrolls into view. Leaflet is loaded from unpkg with integrity hashes.
- **Calm styling**: warm off-white background, a serif for reading, one olive-green accent, generous spacing, no parallax or pinning.

How it handles animations off:

- Content is visible by default. Sections are only hidden and revealed if JavaScript runs, GSAP actually loaded, *and* the visitor has not turned on "reduce motion" in their OS. If any of those is false, the page is just a normal static page.
- If someone switches reduce-motion on while the page is open, the animations are torn down and everything is shown.
- The map's scroll-wheel zoom is off so it doesn't grab the page as you scroll past it, and if Leaflet fails to load, the text address below the map still tells people where you are.

To use it, open `story.html` in a browser (it needs an internet connection for the CDN scripts and map tiles).

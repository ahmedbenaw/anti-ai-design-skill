# 03 — Functional libraries: Maps & Forms

**Leaflet** and **SurveyJS Form Library**. These are not decoration libraries. They are the two
cheapest ways to make a page *do something real* — show real places with real coordinates, and
collect real answers with real validation and real error states.

The anti-slop thesis: AI-generated pages fail because they substitute **signifiers of
functionality** (icon grids, fake stat counters, "trusted by" logos, a hero screenshot of a
dashboard) for **functionality**. A working map of the 12 actual branch locations, and a working
3-step form that rejects a malformed postcode and tells you why, are both:

- irreducibly real (they need real data, so you cannot fake them),
- state-bearing (empty / loading / error / success are forced on you, not optional), and
- keyboard- and screen-reader-testable (so a11y stops being a checkbox).

Every claim below traces to a page fetched during research; URLs are given inline.

Research date: 2026-09-04.

---

# PART 1 — LEAFLET

## What it is

An open-source JavaScript library for mobile-friendly interactive maps. Provider-agnostic: it
ships **no** tile data and **no** provider-specific code — you bring your own tile source.

> "It's worth noting that Leaflet is provider-agnostic, meaning that it doesn't enforce a
> particular choice of providers for tiles. Also, Leaflet doesn't even contain a single
> provider-specific line of code."
> — <https://leafletjs.com/examples/quick-start/>

- Homepage: <https://leafletjs.com/>
- Repo: <https://github.com/Leaflet/Leaflet>
- Author: Volodymyr Agafonkin

## Licence — BSD-2-Clause (verified)

Verified two ways.

`https://raw.githubusercontent.com/Leaflet/Leaflet/main/LICENSE`:

```
BSD 2-Clause License

Copyright (c) 2010-2026, Volodymyr Agafonkin
Copyright (c) 2010-2011, CloudMade
All rights reserved.
```

npm registry (`https://registry.npmjs.org/leaflet`) reports `"license": "BSD-2-Clause"`.

**Permissive. No attribution obligation for the *library*.** The attribution obligation comes
entirely from the **tile provider**, not from Leaflet. See "Tile providers and licensing" below —
this is the single most-missed legal point about Leaflet.

## Version

| Channel | Version | Released | Source |
|---|---|---|---|
| **latest / stable** | **1.9.4** | 2023-05-18 | npm dist-tags `latest`; <https://leafletjs.com/download.html> |
| alpha | 2.0.0-alpha.1 | 2025-08-16 | npm dist-tags `alpha`; download page |
| beta | 1.8.0-beta.3 | (stale tag) | npm dist-tags |

**Use 1.9.4.** 2.0 is still alpha as of this research and is a breaking rewrite (see Gotchas).

## Size

Leaflet's own claim (<https://leafletjs.com/>):

> "just about 42 KB of JS (42 KB gzipped — that's 142 KB minified and 431 KB in the source
> form, with 14.5 KB of CSS (3.5 KB gzipped) and 6 KB of images.)"

Measured from unpkg during this research:

| File | Raw | Gzipped |
|---|---|---|
| `leaflet@1.9.4/dist/leaflet.js` | 147,552 B (144 KB) | **42,573 B (42 KB)** |
| `leaflet@1.9.4/dist/leaflet.css` | 14,806 B | 3,552 B |

**~46 KB gzipped total for a fully interactive pan/zoom map.** That is less than most icon fonts.
This is why "we couldn't afford a real map" is never a real argument.

## Install

### npm

```bash
npm install leaflet
```

> "You will find a copy of the Leaflet release files in `node_modules/leaflet/dist`."
> — <https://leafletjs.com/download.html>

### CDN — exact integrity-tagged tags from the docs

Verbatim from <https://leafletjs.com/download.html>:

```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
```

> "Note that the integrity hashes are included for security when using Leaflet from CDN.
> Leaflet is available on the following free CDNs: unpkg, cdnjs, jsDelivr."

The quick-start page (<https://leafletjs.com/examples/quick-start/>) shows the same hashes and adds
the ordering rule:

> `<!-- Make sure you put this AFTER Leaflet's CSS -->`

Also from the quick-start, the two things that break every first Leaflet map:

```html
<div id="map"></div>
```
```css
#map { height: 180px; }
```
> "Make sure the map container has a defined height."

Also: "Make sure all the code is called after the div and leaflet.js inclusion."

## Core API — snippets from the docs

All verbatim from <https://leafletjs.com/examples/quick-start/> and
<https://leafletjs.com/examples/geojson/> unless noted.

### 1. Map + tile layer (with the REQUIRED attribution)

```js
var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
```

> "OpenStreetMap tiles are fine for programming your Leaflet map, but read the Tile Usage Policy of
> OpenStreetMap if you're going to use the tiles in production."
>
> "Whenever using anything based on OpenStreetMap, an attribution is obligatory as per the
> copyright notice. Most other tile providers (such as Mapbox, Stamen or Thunderforest) require an
> attribution as well. Make sure to give credit where credit is due."

### 2. Marker, circle, polygon

```js
var marker = L.marker([51.5, -0.09]).addTo(map);

var circle = L.circle([51.508, -0.11], {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5,
	radius: 500
}).addTo(map);

var polygon = L.polygon([
	[51.509, -0.08],
	[51.503, -0.06],
	[51.51, -0.047]
]).addTo(map);
```

### 3. Popups — bound and standalone

```js
marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
circle.bindPopup("I am a circle.");
polygon.bindPopup("I am a polygon.");
```

```js
var popup = L.popup()
	.setLatLng([51.513, -0.09])
	.setContent("I am a standalone popup.")
	.openOn(map);
```

> "Here we use `openOn` instead of `addTo` because it handles automatic closing of a previously
> opened popup when opening a new one which is good for usability."
>
> "Note that popup content is rendered as HTML, so don't pass untrusted user input to it directly."

### 4. Events

```js
var popup = L.popup();

function onMapClick(e) {
	popup
		.setLatLng(e.latlng)
		.setContent("You clicked the map at " + e.latlng.toString())
		.openOn(map);
}

map.on('click', onMapClick);
```

### 5. GeoJSON — the real-data entry point

```js
var geojsonFeature = {
	"type": "Feature",
	"properties": {
		"name": "Coors Field",
		"amenity": "Baseball Stadium",
		"popupContent": "This is where the Rockies play!"
	},
	"geometry": {
		"type": "Point",
		"coordinates": [-104.99404, 39.75621]
	}
};

L.geoJSON(geojsonFeature).addTo(map);
```

```js
var myLayer = L.geoJSON().addTo(map);
myLayer.addData(geojsonFeature);
```

### 6. GeoJSON `style` as a function of the data (this is a real choropleth)

```js
L.geoJSON(states, {
	style: function(feature) {
		switch (feature.properties.party) {
			case 'Republican': return {color: "#ff0000"};
			case 'Democrat':   return {color: "#0000ff"};
		}
	}
}).addTo(map);
```

### 7. `pointToLayer` — circle markers instead of pins

```js
var geojsonMarkerOptions = {
	radius: 8,
	fillColor: "#ff7800",
	color: "#000",
	weight: 1,
	opacity: 1,
	fillOpacity: 0.8
};

L.geoJSON(someGeojsonFeature, {
	pointToLayer: function (feature, latlng) {
		return L.circleMarker(latlng, geojsonMarkerOptions);
	}
}).addTo(map);
```

### 8. `onEachFeature` + `filter` — and the XSS note

```js
function onEachFeature(feature, layer) {
	// does this feature have a property named popupContent?
	if (feature.properties && feature.properties.popupContent) {
		layer.bindPopup(feature.properties.popupContent);
	}
}

L.geoJSON(geojsonFeature, {
	onEachFeature: onEachFeature
}).addTo(map);
```

The GeoJSON tutorial carries an explicit **security note**:

> "`bindPopup` renders its string argument as HTML. If your GeoJSON comes from untrusted sources
> (user uploads, third-party APIs, etc.), sanitize `popupContent` with a library like DOMPurify, or
> build a DOM element via `textContent` and bind that instead:"

```js
var el = document.createElement('div');
el.textContent = feature.properties.popupContent;
layer.bindPopup(el);
```

```js
L.geoJSON(someFeatures, {
	filter: function(feature, layer) {
		return feature.properties.show_on_map;
	}
}).addTo(map);
```

### 9. `fitBounds` — never hard-code a centre for a real dataset

From <https://leafletjs.com/reference.html>:

| API | Signature | Docs text |
|---|---|---|
| `fitBounds` | `fitBounds(<LatLngBounds> bounds, <fitBounds options> options?)` | "Sets a map view that contains the given geographical bounds with the maximum zoom level possible." |
| `flyToBounds` | `flyToBounds(<LatLngBounds> bounds, <fitBounds options> options?)` | "Sets the view of the map with a smooth animation like `flyTo`, but takes a bounds parameter like `fitBounds`." |
| `getBounds` (FeatureGroup) | `getBounds()` | "Returns the LatLngBounds of the Feature Group (created from bounds and coordinates of its children)." |
| `invalidateSize` | `invalidateSize(<Zoom/pan options> options)` | "Checks if the map container size changed and updates the map if so — call it after you've changed the map size dynamically" |
| `setView` | `setView(<LatLng> center, <Number> zoom, <Zoom/pan options> options?)` | — |

Idiomatic pattern (composed from those reference entries):

```js
var layer = L.geoJSON(data).addTo(map);
map.fitBounds(layer.getBounds(), { padding: [24, 24] });
```

### 10. Attribution control

From <https://leafletjs.com/reference.html>:

| Member | Value | Docs text |
|---|---|---|
| `L.map` option `attributionControl` | `Boolean`, default `true` | "Whether a attribution control is added to the map by default." |
| `L.control.attribution(options)` | — | "Creates an attribution control." |
| `.addAttribution(<String> text)` | — | "Adds an attribution text (e.g. `'&copy; OpenStreetMap contributors'`)." |
| option `prefix` | `String\|false`, default `'Leaflet'` | "The HTML text shown before the attributions. Pass `false` to disable." |
| option `collapsed` | `Boolean`, default `true` | "If true, the control will be collapsed into an icon and expanded on mouse hover, touch, or keyboard activation." |

Note `attributionControl: false` and `prefix: false` are both legal — which is exactly how
unattributed maps get shipped. See Scanner signatures.

---

## Tile providers and licensing — the part that is actually a legal matter

**Leaflet's BSD-2 licence does not cover the map imagery.** The tiles are somebody else's data
under somebody else's terms. Getting this wrong is a licence violation and, for `tile.openstreetmap.org`,
gets your traffic blocked.

### OpenStreetMap Tile Usage Policy

Source: <https://operations.osmfoundation.org/policies/tiles/>

The public `tile.openstreetmap.org` service is a **community-funded, best-effort service with no
SLA**. There is a policy and it is enforced by blocking.

**You must:**

- Use exactly `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
- Send a `User-Agent` **"naming your app and optionally a contact URL or email"**.
  Example given in the policy:
  `User-Agent: MyTownMaps/1.4 (+https://example.org; contact: maps@example.org)`
- "Update User-Agent as you publish new builds"
- Ensure the "`Referer` header is present and accurate end-to-end. If you proxy tile requests
  through your servers or a CDN, do not strip or blank the `Referer`."
- Cache: "If your cache cannot read them, cache each tile for at least **7 days**", and use
  conditional requests (`If-None-Match`, `If-Modified-Since`) "when requesting tiles that have
  expired".

**You must not:**

- Send `Cache-Control: no-cache`, `Pragma: no-cache`, "or similar no-cache headers by default"
- Use a generic `User-Agent` (okhttp, curl defaults) — "Traffic that uses these defaults will be
  blocked because we cannot identify or contact the actual application."
- Strip or spoof the `Referer`
- Bulk download. **"Bulk downloading is any pre-emptive fetching of tiles other than those a user
  is actively viewing."**
- Ship offline features. **"Offline use is not permitted on tile.openstreetmap.org. Features such
  as 'Download city/country for offline use' or 'Save area for later' rely on prefetch/bulk
  downloading and are therefore prohibited."**

**Enforcement:** "Traffic using generic defaults, referer-stripping, or spoofed identities may be
blocked without notice" and "Prefetch/offline patterns place disproportionate load on
community-funded servers and will be blocked without notice."

The policy also carries a section **"Hosted tile services based on OSM data"** with subsections for
*Commercial providers*, *Run your own tiles*, and *Vector tiles* — i.e. the OSMF's own position is
that production apps should move off the public endpoint.

> **Practical rule:** `tile.openstreetmap.org` is for development and small personal projects.
> Anything with real traffic, an offline mode, or a commercial purpose needs a hosted provider or
> your own tile server. A browser page cannot even set `User-Agent`, so a public-facing site on the
> OSM endpoint is *structurally* unable to satisfy the identification requirement — the `Referer`
> is all it has.

### OSM attribution requirements

Source: <https://osmfoundation.org/wiki/Licence/Attribution_Guidelines>

- Attribution must be **to "OpenStreetMap"** and must make clear the data is available under the
  **Open Database License (ODbL)**.
- "For a browsable map (e.g., embedded in a web page or application), the credit should typically
  appear in a **corner of the map**." The lower-right corner is traditional but any corner works.
- The credit text should be **linked to `openstreetmap.org/copyright`**.
- Acceptable wordings include `© OpenStreetMap contributors`, `© OpenStreetMap`, and
  "Map data from OpenStreetMap".
- Attribution must be "legible and understandable" and positioned where users expect credits,
  "without creating false impressions about the data's origin".
- Collapsing is permitted (user dismissal, map interaction, or auto-fade after ~five seconds)
  **provided users can still reach the licence details**. Leaflet's default
  `collapsed: true` attribution control satisfies this on small screens.

### Free / freemium alternatives and their attribution

| Provider | Raster tile URL template | Required attribution | Notes |
|---|---|---|---|
| **OpenStreetMap** (public) | `https://tile.openstreetmap.org/{z}/{x}/{y}.png` | `&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors` | Dev/small-scale only. Policy above. maxZoom 19. |
| **CARTO** basemaps | `https://{s}.basemaps.cartocdn.com/{style}/{z}/{x}/{y}{scale}.png` — styles: `light_all`, `dark_all`, `light_nolabels`, `light_only_labels`, `dark_nolabels`, `dark_only_labels`, `rastertiles/voyager`, `rastertiles/voyager_nolabels`, `rastertiles/voyager_only_labels`, `rastertiles/voyager_labels_under` | `&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>` | Zoom 0–20; `@2x` for retina. Repo says "for more information about CARTO basemaps use, pricing and terms of service, please double check https://carto.com/basemaps". Source: <https://github.com/CartoDB/basemap-styles> |
| **Stadia Maps** | `https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png` (also Stamen styles) | `&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>` — Stamen styles add `&copy; <a href="https://stamen.com/">Stamen Design</a>` | maxZoom 20; `{r}` = retina. "localhost testing requires no API keys or domain setup. For production deployment, you'll need either domain-based authentication or an API key". Sources: <https://docs.stadiamaps.com/tutorials/raster-maps-with-leaflet/>, <https://docs.stadiamaps.com/attribution/> |
| **Esri / ArcGIS** | via `esri-leaflet` / `esri-leaflet-vector` | Esri Terms of Use apply; attribution is your responsibility | "you will need an ArcGIS account and an API key" for the current Vector Basemap Layer; `L.esri.BasemapLayer` is deprecated. "The Terms of Use for Esri hosted services apply to *all* Leaflet applications." Source: <https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html> |

Stadia's attribution rule is worth quoting in full because it is the general shape of every
provider's rule:

> "you must leave all automatically generated attributions in place, or replace them with something
> that conveys the same information in a way that fits your site/app UX." Attribution must "retain
> the original spirit, and must still be prominent."
> — <https://docs.stadiamaps.com/attribution/>

Stadia satellite imagery additionally requires:
`© CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data)`.

Fastest way to get provider config right: **`leaflet-providers`**
(<https://github.com/leaflet-extras/leaflet-providers>, BSD-2-Clause, v4.0.0 published 2026-09-03 —
actively maintained). It ships the correct URL template *and* the correct attribution string per
provider, so you cannot forget one.

---

## Accessibility

### What Leaflet gives you

Leaflet ships an official guide: **<https://leafletjs.com/examples/accessibility/>** ("Accessible maps").

> "Leaflet comes with a set of useful defaults. The map container and markers are keyboard operable
> by default, this enables users who are unable to use a pointing device. Consider the effects on
> your users before changing defaults such as these."

Concrete API support (from <https://leafletjs.com/reference.html>):

| Option | Default | Docs text |
|---|---|---|
| `L.map` `keyboard` | `true` | "Makes the map focusable and allows users to navigate the map with keyboard arrows and +/- keys." |
| `L.marker` `keyboard` | `true` | "Whether the marker can be tabbed to with a keyboard and clicked by pressing enter." |
| `L.marker` `alt` | `'Marker'` | "Text for the alt attribute of the icon image. Useful for accessibility." |
| `L.marker` `autoPanOnFocus` | `true` | "When true, the map will pan whenever the marker is focused (via e.g. pressing tab on the keyboard) to ensure the marker is visible within the map's bounds" |
| `L.imageOverlay` `alt` | `''` | "Text for the alt attribute of the image (useful for accessibility)." |
| map events | — | `keypress`, `keydown`, `keyup` fire "while the map is focused" |

**Markers must be labelled** — the guide is unambiguous:

> "When using markers, it is vital to ensure each has a unique and descriptive `alt` or `title`:"

```js
var marker = L.marker([50.4501, 30.5234],
  {alt: 'Kyiv'}).addTo(map) // "Kyiv" is the accessible name of this marker
  .bindPopup('Kyiv, Ukraine is the birthplace of Leaflet!');
```

**Decorative maps must be hidden from assistive tech:**

> "Some maps are purely decorative and not intended for users to interact with (in similar fashion
> to background-images and -videos). Such maps should be hidden from assistive technologies (ATs),
> and have no focusable descendants. This is to avoid the potential to confuse screen reader users,
> and to remove any unnecessary tab stops for keyboard users."

```html
<!-- This map is for aesthetic purposes only, and can not be interacted with! -->
<div id='decorative-map' inert></div>
<script src='https://unpkg.com/wicg-inert@latest/dist/inert.min.js'></script>
```

**Test with keyboard and a screen reader.** The guide names Narrator (Windows), Orca (Linux),
TalkBack (Android), VoiceOver (macOS/iOS).

**Plugins can regress a11y:**

> "Plugins can enhance the experience for your users, but can also degrade it in some cases.
> Therefore it is important that you test your maps whenever a new plugin is added."

It singles out `Leaflet.fullscreen` as an *improvement*: fullscreen mode helps keyboard and screen
reader users because "they are less likely to unintentionally navigate outside the map."

### What Leaflet does NOT give you

From the Leaflet a11y discussion <https://github.com/Leaflet/Leaflet/discussions/8006>:

- **Vectors (polygons/polylines/circles) are not keyboard focusable and have no accessible name**
  — "Vectors should be keyboard focusable and have accessible name/description" is listed as
  blocked on pending work (issues #7822, #8251). So a click-a-region choropleth is **mouse-only**
  unless you build the keyboard path yourself.
- **Standalone popups and tooltips are problematic** for both keyboard and screen-reader users
  (no managed focus, no live-region announcement).
- **No mechanism to make multiple maps in one document discernible** to screen reader users — you
  must label the containers yourself.
- **`divIcon` accessibility is limited** — you supply the label in your own HTML.
- The discussion's own framing: "it's the responsibility of developers who implement Leaflet maps
  to take extra steps to ensure their maps are presented in a way that they can be used and make
  sense to people of all abilities."

`leaflet.a11y` (<https://github.com/nfreear/leaflet.a11y>, MIT, v0.6.0 / 2023-10-24) exists as an
a11y + localisation plugin, but is not actively maintained — treat as a reference, not a dependency.

### The non-map alternative obligation

**Neither Leaflet nor any tile provider gives you this. You must build it.**

A map is a graphical representation of data. Under WCAG 1.1.1 (non-text content) and 1.3.1 (info
and relationships), the *information* the map conveys must be available non-visually. Leaflet's own
guide gets you as far as "each marker has an accessible name" — it does not get you to "a
screen-reader user can find the nearest branch."

Minimum viable compliant pattern:

```html
<section aria-labelledby="loc-h">
  <h2 id="loc-h">Our 12 locations</h2>

  <!-- The map is an enhancement over the list, not a replacement for it -->
  <div id="map" role="application" aria-label="Map of our 12 locations"></div>

  <!-- The same data, as content. Not visually hidden. -->
  <ul id="location-list">
    <li>
      <h3>Manchester — Piccadilly</h3>
      <address>4 Ducie St, Manchester M1 2DQ</address>
      <p>Open Mon–Fri 09:00–17:30. <a href="tel:+441610000000">0161 000 0000</a></p>
      <a href="https://www.openstreetmap.org/?mlat=53.4779&amp;mlon=-2.2318#map=17/53.4779/-2.2318">Directions</a>
    </li>
    <!-- … -->
  </ul>
</section>
```

Rules:
1. **The list is the source of truth.** Render the map *from* the same array/GeoJSON that renders
   the list. If they can diverge, they will.
2. **Do not `display:none` the list.** A visually-hidden list is acceptable only as a last resort;
   a visible list beside/below the map is better for everyone (mobile, printing, slow networks,
   copy-paste).
3. **Two-way selection**: clicking a marker highlights the list item; focusing a list item opens
   the corresponding popup. This is the cheapest way to make the vector-focus gap survivable.
4. **`role="application"` on the map div only if it has real keyboard interaction**; otherwise
   `role="img"` with an `aria-label`, or `inert` if decorative.

---

## ADOPT — what Leaflet earns its place for

Mapped to the anti-slop principle: *show real functionality and real data, not signifiers of it.*

1. **It makes fake data impossible.** A map needs coordinates. You cannot lorem-ipsum a latitude.
   The moment a brief says "map", the team has to answer "of what, exactly?" — which is the
   question AI-slop layouts exist to avoid.
2. **It replaces the worst slop pattern directly.** The three-icon "Global reach / 50+ countries /
   24-7 support" grid is a placeholder for a map. A Leaflet map of the actual offices, with the
   actual opening hours in the popups, is the same square of pixels doing real work.
3. **46 KB gzipped.** It is cheaper than the hero image it replaces. There is no performance
   argument for the icon grid.
4. **GeoJSON is a real interchange format (RFC 7946).** Data can come from the client's CMS, a
   government open-data portal, or a `.geojson` file in the repo — and the same file drives the
   accessible list. One source, two renderings.
5. **It forces the state discussion.** Zero results, one result, 900 results, failed tile load,
   geolocation denied — a map has an empty state and an error state whether you design them or not.
6. **Keyboard operability is on by default**, so a11y starts from a decent baseline rather than
   from zero (unlike a canvas-drawn "map" illustration, which starts from nothing).
7. **Provider-agnostic and BSD-2.** No vendor lock, no SDK key in the HTML for a static marketing
   page, no per-load billing surprise.

## AVOID / traps

1. **Map-as-decoration.** A blurred, greyscale, non-interactive map behind a hero with no markers
   and no data is *exactly* the slop pattern in map costume. If it has no data, it is a background
   image — make it one, `inert` it, and stop paying 46 KB plus tile requests for it.
2. **Unattributed maps.** Setting `attributionControl: false`, or `prefix: false` with no
   `attribution` on the tile layer, is a licence violation against the tile provider, not a style
   choice. See Scanner signatures.
3. **Shipping `tile.openstreetmap.org` to production.** Especially with an offline/prefetch feature
   — explicitly prohibited — or from a browser (which cannot set `User-Agent`). Blocked without
   notice.
4. **Prefetching / warming tiles.** "Bulk downloading is any pre-emptive fetching of tiles other
   than those a user is actively viewing." That includes a clever "preload the next zoom level"
   optimisation.
5. **Stripping `Referer`** at a CDN or proxy in front of tile requests. Explicitly called out.
6. **`react-leaflet` licence.** v5.0.0 (npm, 2024-12-14) is published under **`Hippocratic-2.1`**,
   which is **not an OSI-approved open-source licence** and is refused by many corporate licence
   scanners. Check before adding it to a client codebase; plain Leaflet in a `useEffect` is BSD-2
   and has no such issue.
7. **Giant plugin stacks.** Leaflet is 42 KB; `Leaflet.draw` + `markercluster` + `heat` +
   `Control.Geocoder` + `Routing Machine` can quadruple it. Add plugins for capability the page
   actually uses, not for the demo.
8. **Unmaintained plugins.** The plugin database at <https://leafletjs.com/plugins.html> lists
   ~570 plugins across 36 categories and is a *directory*, not a curated set. Many entries have not
   shipped since 2015–2018. See the plugin table's "Last publish" column.
9. **Missing `#map { height: … }`.** The map renders as a zero-height strip. Universal first bug.
10. **Map inside a tab/accordion/modal**: renders grey until `map.invalidateSize()` is called after
    the container becomes visible.
11. **Scroll-wheel trapping.** A full-width map mid-page hijacks page scroll on desktop and traps
    one-finger pan on mobile. Fix with `scrollWheelZoom: false` plus
    `Leaflet.GestureHandling` (npm `leaflet-gesture-handling`) or `L.Sleep`.
12. **XSS via popups.** `bindPopup` renders HTML. Third-party GeoJSON, user submissions, CMS
    fields — sanitise or bind a DOM node built with `textContent`.

## Scanner signatures (Leaflet)

Static-analysis heuristics for "is this a real map or map-shaped slop?"

| # | Signature | Detection | Severity |
|---|---|---|---|
| L1 | **Tile layer with no attribution** | `L.tileLayer(` present and no `attribution:` key in its options object | **Legal — critical** |
| L2 | **Attribution control disabled** | `attributionControl: false` in `L.map(...)` options, or `.attributionControl.setPrefix(false)` with no `addAttribution` call | **Legal — critical** |
| L3 | **Attribution string missing the required parties** | tile URL host contains `cartocdn` but attribution lacks `carto.com/attributions`; host contains `stadiamaps` but attribution lacks both `stadiamaps.com` and `openstreetmap.org/copyright`; any OSM-derived host but attribution lacks `openstreetmap.org/copyright` | **Legal — critical** |
| L4 | **Production build pointing at `tile.openstreetmap.org`** | that literal host in a non-dev bundle, or alongside any service-worker / cache-tiles / offline code | High |
| L5 | **Prefetch/offline against OSM public tiles** | `tile.openstreetmap.org` co-occurring with `caches.open`, `workbox`, `precache`, or a loop over `{z}/{x}/{y}` | High |
| L6 | **Map with no data** | `L.map(` present but **no** `L.marker`, `L.geoJSON`, `L.circle`, `L.polygon`, `L.polyline`, or `addData` anywhere → the map is decoration | **Slop — high** |
| L7 | **Decorative map not inert** | matches L6 and the container has no `inert` attribute and no `aria-hidden` | High (a11y) |
| L8 | **Markers without accessible names** | `L.marker(` calls where the options object has neither `alt:` nor `title:` | High (a11y) |
| L9 | **No non-map alternative** | a `L.marker`/`geoJSON` count ≥ 2 and no sibling `<ul>`/`<ol>`/`<table>`/`<dl>` rendering the same source array | **High (a11y)** |
| L10 | **Hard-coded centre with dynamic data** | `setView([...], n)` present, `fitBounds` absent, and markers come from a variable/fetch rather than literals | Medium |
| L11 | **Missing container height** | `<div id="map">` with no `height` in any stylesheet rule matching that id/class | Medium |
| L12 | **Scroll trap** | `L.map(` with no `scrollWheelZoom:false`, no `leaflet-gesture-handling`, no `Leaflet.Sleep`, in a page longer than one viewport | Medium |
| L13 | **Unsanitised popup** | `bindPopup(` receiving a template literal or concatenation containing a `feature.properties.*` / `fetch` -derived value, with no `DOMPurify` / `textContent` nearby | Medium (security) |
| L14 | **CDN without SRI** | `unpkg.com/leaflet` `<script>`/`<link>` lacking `integrity=` | Low |
| L15 | **Non-OSI plugin licence** | `react-leaflet` ≥ 5 in `package.json` (Hippocratic-2.1) | Low (policy) |

## Gotchas (Leaflet)

- **1.9.4 is 2+ years old and that is fine.** The library is feature-complete for its scope; slow
  release cadence is not abandonment.
- **Leaflet 2.0 is a breaking rewrite.** From <https://leafletjs.com/2025/05/18/leaflet-2.0.0-alpha.html>:
  "Dropped support for Internet Explorer, removed legacy methods and polyfills, adopted modern
  standards like Pointer Events, and now publish Leaflet as an **ESM module**." The global `L` "is
  no longer part of the core package (though it's still available in the bundled version
  `leaflet-global.js` for backward compatibility)", and **"All factory methods removed — use
  constructors directly: `L.marker(latlng)` ➜ `new Marker(latlng)`"**. Every snippet in this
  document, every tutorial online, and every plugin uses the 1.x `L.*` form. **Do not target 2.0
  alpha.**
- **Marker icons break under bundlers.** Leaflet resolves icon PNGs relative to the CSS; Webpack/
  Vite rewrite those paths. Fix with `leaflet-defaulticon-compatibility` or by setting
  `L.Icon.Default.imagePath` / `iconUrl` explicitly.
- **GeoJSON is `[lng, lat]`; Leaflet's `L.latLng`/`L.marker` are `[lat, lng]`.** `L.geoJSON`
  handles the swap for you; hand-written coordinate arrays are where the bug lives.
- **`maxZoom` is per-provider.** OSM 19, Stadia 20, CARTO 20. Set it or users zoom into grey.
- **`{s}` subdomain placeholder is legacy.** `tile.openstreetmap.org` no longer wants
  `{a,b,c}.tile...`; HTTP/2 makes subdomain sharding pointless. CARTO still documents `{s}`.
- **`{r}` retina placeholder** is provider-specific (Stadia yes, CARTO uses `@2x` in `{scale}`).
- **Antimeridian**: polygons crossing ±180° render as a stripe across the world unless you use
  `Leaflet.Antimeridian`.
- **Projections**: Leaflet is Web Mercator (EPSG:3857) by default. Anything else needs
  `Proj4Leaflet`.
- **Popups render HTML.** Repeated because it is the one security footgun.

---

## The Leaflet plugin database, categorised

Source: **<https://leafletjs.com/plugins.html>** (fetched and parsed 2026-09-04).

The page organises plugins into **7 top-level groups / 36 categories**, with the following counts
(parsed from the page's own tables):

| Group | Categories (count of listed plugins) |
|---|---|
| **Tile & image layers** | Basemap providers (18), Basemap formats (18), Non-map base layers (7), Tile/image display (25), Tile Load (11), Vector tiles (9) |
| **Overlay data** | Overlay data formats (17), Dynamic/custom data loading (9), Synthetic overlays (12), Data providers (12) |
| **Overlay display** | Markers & renderers (80), Overlay animations (20), Clustering/Decluttering (13), Heatmaps (8), DataViz (21) |
| **Interaction with geometries/features** | Edit geometries (26), Time & elevation (14), Search & popups (15), Area/overlay selection (10) |
| **Map interaction** | Layer switching controls (17), Interactive pan/zoom (16), Bookmarked pan/zoom (13), Fullscreen controls (3), Minimaps & synced maps (7), Measurement (14), Mouse coordinates (11), Events (13), User interface (36), Print/export (6), Geolocation (7) |
| **Miscellaneous** | Geoprocessing (10), Routing (9), Geocoding (16), Plugin collections (3) |
| **Integration** | Frameworks & build systems (32), 3rd party integration (18) |

**~570 plugins in total.** It is an open directory — inclusion implies nothing about quality or
maintenance. Maintenance status below is taken from the npm registry (latest published version and
date), since the GitHub API was unavailable during this research.

### The 24 worth knowing

Legend: **Active** = published within ~2 years; **Stable/dormant** = works, no recent releases;
**Stale** = likely unmaintained, verify before use.

#### Tile / basemap providers

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **leaflet-providers** | Ready-made configs for dozens of free tile providers — "OSM, OpenCycleMap, Stamen, Esri, etc." | <https://github.com/leaflet-extras/leaflet-providers> | `leaflet-providers` 4.0.0 (2026-09-03), BSD-2 | **Active** | Ships the correct URL **and the correct attribution string** per provider — the single best defence against shipping an unattributed map. |
| **Esri Leaflet** | "A set of tools for using ArcGIS services with Leaflet. Support for map services, feature layers, ArcGIS Online tiles and more." | <https://esri.github.io/esri-leaflet/> | `esri-leaflet` 3.0.19 (2025-09-04), Apache-2.0 | **Active** | The route into enterprise/government ArcGIS data that already exists at the client. Needs an ArcGIS API key. |
| **maplibre-gl-leaflet** | "Loads a maplibre-gl-js map as a Leaflet layer" | <https://github.com/maplibre/maplibre-gl-leaflet> | `@maplibre/maplibre-gl-leaflet` 0.1.4 (2026-08-16), ISC | **Active** | Vector basemaps (crisp at any zoom, restyleable, dark mode) while keeping Leaflet's simple API for your overlays. |
| **Leaflet.VectorGrid** | "Display gridded vector data (GeoJSON or TopoJSON sliced with geojson-vt, or protobuf vector tiles)" | <https://github.com/Leaflet/Leaflet.VectorGrid> | `leaflet.vectorgrid` 1.3.0 (2017-08-28), Beerware | **Stale** | Official-org repo but no release since 2017. Prefer maplibre-gl-leaflet for new work. |

#### Markers & clustering

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **Leaflet.markercluster** | "Beautiful, sophisticated, high performance marker clustering solution with smooth animations and lots of great features. **Recommended!**" (the plugin page's own emphasis) | <https://github.com/Leaflet/Leaflet.markercluster> | `leaflet.markercluster` 1.5.3 (2021-10-18), MIT | **Stable/dormant** | The default answer above ~100 markers. Official Leaflet org, effectively feature-complete. Still the ecosystem standard. |
| **Leaflet.FeatureGroup.SubGroup** | "Create Feature Groups that add their child layers into a parent group. Typical usage is to switch them through a layers control." | <https://github.com/ghybs/Leaflet.FeatureGroup.SubGroup> | `leaflet.featuregroup.subgroup` 1.0.2 (2017-03-26), BSD-2 | **Stale** | The standard trick for category checkboxes *inside* one marker cluster. Small and unchanging. |
| **Overlapping Marker Spiderfier** | "Deals with overlapping markers in a Google Earth-inspired way by gracefully springing them apart on click." | <https://github.com/jawj/OverlappingMarkerSpiderfier-Leaflet> | — | Stable/dormant | Better than clustering when markers are few but coincident (e.g. several units at one address). |
| **PruneCluster** | "Fast and realtime marker clustering library." | <https://github.com/SINTEF-9012/PruneCluster> | — | Stable/dormant | For clusters that must update every frame (live vehicles) where markercluster stutters. |
| **Leaflet.Deflate** | "Deflates lines and polygons to a marker when their screen size becomes too small in lower zoom levels." | <https://github.com/oliverroick/Leaflet.Deflate> | — | Stable/dormant | Keeps a parcel/boundary layer legible when zoomed out, instead of a mess of specks. |

#### Heatmaps & big-data rendering

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **Leaflet.heat** | "A tiny, simple and fast Leaflet heatmap plugin. Uses simpleheat under the hood, additionally clustering points into a grid for performance." | <https://github.com/Leaflet/Leaflet.heat> | `leaflet.heat` 0.2.0 (2015-10-26) | **Stale but canonical** | ~3 KB, official org, still the most-used heat layer. No releases since 2015 — vendor it and pin it. |
| **Leaflet.glify** | "Fast rendering for large (+100MB) GeoJSON datasets with WebGL." | <https://github.com/robertleeplummerjr/Leaflet.glify> | `leaflet.glify` 3.3.1 (2024-12-09), MIT | **Active** | When you have 100k+ points/polygons and canvas rendering dies. |
| **leaflet-choropleth** | "Extends L.geoJson to add a choropleth visualization (color scale based on value)." | <https://github.com/timwis/leaflet-choropleth> | `leaflet-choropleth` 1.1.4 (2017-05-30), MIT | **Stale** | Tiny; the `style`-function pattern in the GeoJSON tutorial above does the same thing in 8 lines. Prefer hand-rolling. |

#### Drawing & editing

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **Leaflet-Geoman (free)** | "Draw, Edit, Drag, Cut, Rotate, Split, Scale, Measure, Snap and Pin Layers like Markers, CircleMarkers, Polylines…" | <https://github.com/geoman-io/leaflet-geoman> | `@geoman-io/leaflet-geoman-free` 2.20.0 (2026-06-23), MIT | **Active** | The current best-maintained editor. **Trap:** the free package is MIT; Geoman Pro is a separate paid product — check which one you installed. |
| **Terra Draw** | "TerraDrawLeafletAdapter allows users to create, select and edit a variety of geometry types (points, lines polygons etc)" | <https://github.com/JamesLMilner/terra-draw> | `terra-draw` 1.33.0 (2026-09-01), MIT | **Active** | Map-library-agnostic (Leaflet, MapLibre, Google, OL) — the right pick if the map layer might change. Most actively developed of the three. |
| **Leaflet.draw** | "Enables drawing features like polylines, polygons, rectangles, circles and markers through a very nice user-friendly interface with icons and hints." | <https://github.com/Leaflet/Leaflet.draw> | `leaflet-draw` 1.0.4 (2018-10-24), MIT | **Stale** | The historical standard, official org, but **no release since 2018**. Every tutorial uses it; prefer Geoman or Terra Draw for new work. |
| **Leaflet.Editable** | "Lightweight fully customisable and controllable drawing/editing plugin." | <https://github.com/Leaflet/Leaflet.Editable> | `leaflet-editable` 1.3.2 (2025-07-28), WTFPL | **Active-ish** | You want the editing *primitives* and your own UI, not a toolbar. Note the WTFPL licence — some corporate scanners reject it. |

#### Geocoding & routing

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **Leaflet Control Geocoder** | "A clean and extensible control for both geocoding and reverse geocoding. Builtin support for Nominatim, Bing, MapQuest, Mapbox, What3Words, Google and Photon." | <https://github.com/perliedman/leaflet-control-geocoder> | `leaflet-control-geocoder` 4.0.0 (2026-07-18), BSD-2 | **Active** | Address search box in ~10 lines, with a free backend (Nominatim/Photon). Same licence as Leaflet. |
| **leaflet-geosearch** | Search/geocode control with multiple provider backends | <https://github.com/smeijer/leaflet-geosearch> | `leaflet-geosearch` 4.4.0 (2026-03-17), MIT | **Active** | Modern TS alternative to the above; better typings, good autocomplete UX. |
| **Leaflet Routing Machine** | "Control for route search with via points, displaying itinerary and alternative routes. Uses OSRM by default, but also supports GraphHopper, Mapbox Directions API…" | <https://github.com/perliedman/leaflet-routing-machine> | `leaflet-routing-machine` 3.2.12 (2018-09-28), ISC | **Stale but canonical** | Still the only turn-by-turn itinerary control for Leaflet. No release since 2018 — pin it and test. Public OSRM demo server has its own usage limits; self-host for production. |
| **Leaflet Search** | "A control for search Markers/Features location by custom property in LayerGroup/GeoJSON. Support AJAX/JSONP, Autocompletion…" | <https://github.com/stefanocudini/leaflet-search> | `leaflet-search` 4.0.0 (2023-09-18), MIT | **Active-ish** | Searches **your own** features, not a geocoder — which is usually what a store-locator actually needs. |

#### UI controls

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **Leaflet.fullscreen** (official) | "A fullscreen button control using the Fullscreen API." | <https://github.com/Leaflet/Leaflet.fullscreen> | `leaflet.fullscreen` 5.3.3 (2026-06-30), MIT | **Active** | Explicitly recommended by Leaflet's own accessibility guide as an a11y *improvement*. Use this one, not the older forks. |
| **Leaflet.Locate** | "A customizable locate control." | <https://github.com/domoritz/leaflet-locatecontrol> | `leaflet.locatecontrol` 0.90.1 (2026-08-12), MIT | **Active** | "Find me" for store locators, with the permission-denied and accuracy-circle states already handled. |
| **Leaflet.MiniMap** | "A small minimap showing the map at a different scale to aid navigation." | <https://github.com/Norkart/Leaflet-MiniMap> | `leaflet-minimap` 3.6.1 (2018-03-23), BSD-2 | **Stale** | Orientation aid on deep-zoom maps. Unchanged for years but stable. |
| **leaflet-sidebar-v2** | "A responsive, tabbed sidebar with HTML & JS API." | <https://github.com/noerw/leaflet-sidebar-v2> | `leaflet-sidebar-v2` 3.2.3 (2020-05-18), MIT | Stable/dormant | The map+list layout that the non-map-alternative obligation pushes you toward, done responsively. |

#### Mobile / touch / page-behaviour

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **Leaflet.GestureHandling** | "Brings the basic functionality of Google Maps Gesture Handling into Leaflet. Prevents users from getting trapped on the map when scrolling a long page." | <https://github.com/elmarquis/Leaflet.GestureHandling/> | `leaflet-gesture-handling` 1.2.2 (2021-10-22), MIT | Stable/dormant | **Near-mandatory** for any map embedded in a scrolling page on mobile. Fixes the single worst map UX bug. |
| **L.Sleep** | "Avoid unwanted scroll capturing." | <https://github.com/CliffCloud/Leaflet.Sleep> | — | Stable/dormant | Lighter alternative: map ignores wheel until clicked/focused. |

#### Data formats

| Plugin | What it does | Repo | npm latest | Status | Why you'd use it |
|---|---|---|---|---|---|
| **leaflet-omnivore** | "Loads & converts CSV, KML, GPX, TopoJSON, WKT formats for Leaflet." | <https://github.com/mapbox/leaflet-omnivore> | `leaflet-omnivore` 0.3.4 (2016-11-17), BSD-3 | **Stale** | Still the fastest way to put a client's existing CSV/KML on a map. Mapbox-archived — vendor it. |
| **Leaflet.FileLayer** | "Loads files (GeoJSON, GPX, KML) into the map using the HTML FileReader API (i.e. locally without server)." | <https://github.com/makinacorpus/Leaflet.FileLayer> | `leaflet-filelayer` 1.2.0 (2017-11-18), MIT | Stale | Drag-and-drop-a-file demos with no backend. |
| **Leaflet Realtime** | "Put realtime data on a Leaflet map: live tracking GPS units, sensor data or just about anything." | <https://github.com/perliedman/leaflet-realtime> | `leaflet-realtime` 2.2.0 (2019-09-07), ISC | Stale | Polls a GeoJSON endpoint and diffs the layer — the "live" state, for free. |

#### Framework bindings

| Plugin | What it does | Repo | npm latest | Status | Note |
|---|---|---|---|---|---|
| **react-leaflet** | "React components for Leaflet maps." | <https://github.com/PaulLeCam/react-leaflet> | `react-leaflet` 5.0.0 (2024-12-14) | Active | ⚠️ **Licence `Hippocratic-2.1` — not OSI-approved.** Flag before adding to client work. |
| **@vue-leaflet/vue-leaflet** | Vue 3 components for Leaflet | <https://github.com/vue-leaflet/vue-leaflet> | `@vue-leaflet/vue-leaflet` 0.10.1 (2023-06-16), MIT | Stable/dormant | Still pre-1.0. |
| **@asymmetrik/ngx-leaflet** | "Leaflet components and extensions for Angular.io." | <https://github.com/Asymmetrik/ngx-leaflet> | 18.0.1 (2024-06-01), MIT | Stable | — |
| **Leaflet.a11y** | "An accessibility and localization/translation plugin for Leaflet." | <https://github.com/nfreear/leaflet.a11y> | `leaflet.a11y` 0.6.0 (2023-10-24), MIT | Dormant | Useful as a *reference implementation* of map a11y patterns. Don't depend on it. |

### Categories that look busy but are mostly stale

- **Markers & renderers (80 plugins)** — by far the largest category and the least curated. Almost
  all of it is "coloured pin icons". You almost never need any of it; `L.divIcon` plus CSS covers
  95% of marker styling, and `L.circleMarker` covers the rest.
- **User interface (36)** — overlapping sidebar/panel/button plugins, most from 2015–2018.
- **Bookmarked pan/zoom (13)** — `leaflet-hash` is the well-known one; **last published 2013**
  (`leaflet-hash` 0.2.1, 2013-10-05) and has no licence field on npm. Reimplement in ~20 lines with
  the History API rather than depending on it.
- **Print/export (6)** — `leaflet-image` (Mapbox, 2016) and `leaflet.browser.print` (2022) both
  work but neither is maintained; browser print CSS is often enough.
- **Measurement (14)** — heavily duplicated; `leaflet-measure` (2018) and `Leaflet.PolylineMeasure`
  are the usual picks.

---

# PART 2 — SURVEYJS FORM LIBRARY

## What it is

A JSON-schema-driven form/survey renderer. You give it a JSON object describing pages, questions,
validation and conditional logic; it renders a working, validated, themed, multi-page form and
hands you back a plain results object.

From the repo README (<https://github.com/surveyjs/survey-library>):

> "**Form Library** — A free and open-source MIT-licensed JavaScript library that renders dynamic
> JSON-based forms in your web application, and collects responses."

- Repo: <https://github.com/surveyjs/survey-library>
- Docs: <https://surveyjs.io/form-library/documentation/>
- Vendor: Devsoft Baltic OÜ

## Licence — THE critical, commonly-misunderstood part

**SurveyJS is a product family with two different licensing regimes.** Conflating them is the
single most expensive mistake teams make with this library.

### MIT / free — `survey-library` (the Form Library, i.e. the renderer)

`https://raw.githubusercontent.com/surveyjs/survey-library/master/LICENSE`:

```
MIT License

Copyright (c) 2015-2025 Devsoft Baltic OÜ - http://surveyjs.io/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, …
```

Repo README, "Licensing" section:

> "SurveyJS Form Library is distributed under the
> [MIT license](https://github.com/surveyjs/survey-library/blob/master/LICENSE)."

npm-verified MIT packages (all v3.0.3, published 2026-09-03):

| Package | Licence field on npm |
|---|---|
| `survey-core` | **MIT** |
| `survey-js-ui` | **MIT** |
| `survey-react-ui` | **MIT** |
| `survey-vue3-ui` | **MIT** |
| `survey-angular-ui` | **MIT** |
| `survey-jquery` (v1.12.67) | **MIT** |
| `survey-knockout-ui` (v1.12.67) | **MIT** |

### Commercial — Survey Creator, Dashboard, PDF Generator

npm licence field for `survey-creator-core` and `survey-creator-react` (v3.0.3):
`"SEE LICENSE IN LICENSE"` — **not** MIT.

`https://raw.githubusercontent.com/surveyjs/survey-creator/master/LICENSE`:

```
Devsoft Baltic OÜ
Commercial developer license for SurveyJS Creator, SurveyJS PDF Generator and SurveyJS Dashboard libraries.
Copyright (C) 2015-2026 DEVSOFT BALTIC OÜ.

END-USER LICENSE AGREEMENT
FOR ALL SOFTWARE DEVELOPMENT PRODUCT(S) INCLUDED IN THIS DISTRIBUTION
```

Key terms from that EULA:

> "All SOFTWARE DEVELOPMENT PRODUCT(S) is licensed, not sold."
>
> **1.2 BUSINESS AND GOVERNMENT USE LICENSE.** "DEVSOFTBALTIC licenses the SOFTWARE DEVELOPMENT
> PRODUCT(S) on a **per-developer basis**. … The number of licensed developers using the SOFTWARE
> DEVELOPMENT PRODUCT(S) must equal or be less than the number of seats purchased."
>
> **3. TRANSFER.** "You may not share copies of the Redistributables with other co-developers."
>
> **4.** "LICENSEE will be eligible to receive all major and minor updates … during this 12-month
> period. Upon 12 months plus 1 day after original purchase date … Licensee may elect to continue
> receiving major and minor updates … by paying the annual support fees which will be about
> **forty percent (40%) of the original license fee**."

And from <https://surveyjs.io/licensing>:

> "To integrate and use the SurveyJS proprietary components — **Survey Creator, PDF Generator, and
> Dashboard** — in your applications, you must purchase a developer license"

Tiers listed on that page at time of research: Basic $589, PRO $1,059, Enterprise from $2,359 (USD,
per developer).

### The bottom line

| You want to… | Package | Licence | Cost |
|---|---|---|---|
| **Render** a JSON-defined form, validate it, theme it, collect results | `survey-core` + one `survey-*-ui` | **MIT** | **Free** |
| Give non-technical users a **drag-and-drop builder** in your app | `survey-creator-core` / `survey-creator-react` | Commercial EULA | Paid, **per developer**, +40%/yr for updates |
| Render results as **charts/tables** in-app | Dashboard | Commercial EULA | Paid |
| Export a filled form to **PDF** | PDF Generator | Commercial EULA | Paid |

> **The free half is the half you need.** For anti-slop design work, the deliverable is a *working
> form*, and the JSON is written by hand or generated by you. The visual builder is a product
> feature for the client's admins — a separate, later, paid decision. The MIT renderer never
> phones home, needs no licence key, and is unrestricted commercially.

**The trap**: tutorials, Stack Overflow answers, and the `surveyjs/survey-creator` demos all mix
Creator imports into "getting started with SurveyJS" examples. A single
`import { SurveyCreator } from "survey-creator-react"` in your bundle puts a per-developer
commercial EULA over your project. Grep for it.

Note also: the Form Library's *own* "AI Form Response Extractor" (`ai-form-response-extractor`) is
described in the README as "A free and open-source MIT-licensed JavaScript library" — so not
everything with an AI label is on the paid side.

## Version & size

Latest across all packages: **3.0.3**, published **2026-09-03** (npm). Very active release cadence
(v1.12.x line still receiving updates for jQuery/Knockout UIs as of 2026-08-14).

Measured from unpkg (v3.0.3):

| File | Raw | Gzipped |
|---|---|---|
| `survey-core/survey.core.min.js` | 1,422,755 B (1.36 MB) | **313,958 B (~307 KB)** |
| `survey-core/survey-core.min.css` | 499,736 B | 49,360 B |
| `survey-js-ui/survey-js-ui.min.js` | 222,788 B | 57,155 B |

**~410 KB gzipped for the CDN bundle.** That is 9× Leaflet. See AVOID — this is the library's real
cost, and it is only justified when the form is genuinely dynamic/multi-step. See "Bundle" below.

## Install

### Vanilla JS / HTML

CDN, verbatim from <https://surveyjs.io/form-library/documentation/get-started-html-css-javascript>:

```html
<link href="https://unpkg.com/survey-core/survey-core.min.css" rel="stylesheet">
<script src="https://unpkg.com/survey-core/survey.core.min.js"></script>
<script src="https://unpkg.com/survey-js-ui/survey-js-ui.min.js"></script>
```

npm:

```bash
npm install survey-core survey-js-ui
```

### React

```bash
npm install survey-react-ui
```
```js
import 'survey-core/survey-core.css';
import { Model } from 'survey-core';
import { Survey } from 'survey-react-ui';
```
> "The `'use client'` directive is required when using React Server Components with SurveyJS, as
> these are client-side components without SSR support."
> — <https://surveyjs.io/form-library/documentation/get-started-react>

### Vue 3

```bash
npm install survey-vue3-ui
```
```js
import 'survey-core/survey-core.css';
import { Model } from 'survey-core';
import { SurveyComponent } from 'survey-vue3-ui';
```
```html
<SurveyComponent :model="survey" />
```
— <https://surveyjs.io/form-library/documentation/get-started-vue>

### Angular

```bash
npm install survey-angular-ui
```
```js
import { SurveyModule } from "survey-angular-ui";

@NgModule({
  declarations: [ ... ],
  imports: [
    ...,
    SurveyModule
  ],
  providers: [ ... ],
  bootstrap: [ ... ]
})
export class AppModule { }
```
Standalone components:
```js
import { SurveyModule } from 'survey-angular-ui';

@Component({
  standalone: true,
  imports: [ SurveyModule ],
  // ...
})
```
— <https://surveyjs.io/form-library/documentation/get-started-angular>

`survey-core` is the platform-independent model and is a dependency of every UI package.

## Core API — snippets from the docs

### 1. The JSON schema model

```js
const surveyJson = {
    elements: [{
        name: "FirstName",
        title: "Enter your first name:",
        type: "text"
    }, {
        name: "LastName",
        title: "Enter your last name:",
        type: "text"
    }]
};
```
```js
const survey = new Survey.Model(surveyJson);   // UMD/CDN
// or, with modules:
const survey = new Model(surveyJson);
```
— <https://surveyjs.io/form-library/documentation/get-started-html-css-javascript>

### 2. Render

```js
document.addEventListener("DOMContentLoaded", function() {
    survey.render(document.getElementById("surveyContainer"));
});
```
React: `<Survey model={survey} />` · Vue: `<SurveyComponent :model="survey" />`

### 3. Get the results out

```js
function alertResults (sender) {
    const results = JSON.stringify(sender.data);
    alert(results);
}

survey.onComplete.add(alertResults);
```

React variant:
```js
const alertResults = useCallback((survey: Model) => {
  const results = JSON.stringify(survey.data);
  alert(results);
}, []);

survey.onComplete.add(alertResults);
```

> "The results object's properties correspond to question `name` values from the schema."

`onComplete`, from `survey-core/src/survey.ts`:

> "An event that is raised after the survey is completed. Use this event to send survey results to
> the server."

### 4. Pages, progress, navigation

```js
const surveyJson = {
    pages: [{
        elements: [{ /* questions/panels */ }]
    }],
    showProgressBar: true,
    progressBarLocation: "top",
    pageNextText: "Forward",
    showPrevButton: false,
    completeText: "Submit"
};
```
— <https://surveyjs.io/form-library/documentation/design-survey/create-a-multi-page-survey>

### 5. One question per page (the GOV.UK pattern) — `questionsOnPageMode`

From `survey-core/src/survey.ts` (verbatim doc comment):

> "Specifies how to distribute survey elements between pages.
>
> Possible values:
>
> - `"singlePage"` - Combines all survey pages into a single page.
> - `"questionPerPage"` - Displays each question on a separate page.
> - `"inputPerPage"` - Displays each input field on a separate page. Complex questions — such as
>   Single-Select Matrix, Multi-Select Matrix, Dynamic Matrix, Dynamic Panel, and Multiple
>   Textboxes — are split so that each input field appears on its own page.
> - `"standard"` (default) - Retains the original structure specified in the JSON schema."

```js
survey.questionsOnPageMode = "questionPerPage";
```

Related, also from source: `isSinglePage` is a legacy alias
(`this.questionsOnPageMode = val ? "singlePage" : "standard"`), and when
`questionsOnPageMode === "questionPerPage"` "the progress bar uses `"questions"` by default"
rather than `"pages"`.

**This is the whole GOV.UK Design System "one thing per page" pattern as a single property.** No
custom step machinery, no wizard component, no URL routing to write.

### 6. Validation

```js
{
  "name": "question1",
  "type": "text",
  "isRequired": true,
  "requiredErrorText": "Value cannot be empty"
}
```

Built-in validators (<https://surveyjs.io/form-library/documentation/data-validation>):

| `type` | Class | Purpose |
|---|---|---|
| `"numeric"` | `NumericValidator` | value within `minValue`/`maxValue` |
| `"text"` | `TextValidator` | length via `minLength`/`maxLength` |
| `"email"` | `EmailValidator` | email format |
| `"expression"` | `ExpressionValidator` | custom expression |
| `"answercount"` | `AnswerCountValidator` | `minCount`/`maxCount` selections |
| `"regex"` | `RegexValidator` | regular expression |

```js
"validators": [
  { "type": "numeric", "text": "Value must be a number" }
]
```

**Validation timing** — `checkErrorsMode`:
- `"onValueChanged"` — validates immediately after field changes
- `"onComplete"` — validates only on Complete
- default — validates when proceeding to the next page

`textUpdateMode: "onTyping"` for live text validation.

**Custom / async validation:**
```js
survey.onValidateQuestion.add((survey, options) => {
  if (options.name === "memo") {
    if (!options.value.includes("survey")) {
      options.error = 'Answer must contain "survey"'
    }
  }
});
```
`onServerValidateQuestions` handles backend validation, "accepting `data`, `errors`, and a
`complete()` callback."

**Severity levels** — validators support `notificationType`:
- `"error"` (default) — blocks submission (red)
- `"warning"` — allows continuation (orange)
- `"info"` — guidance (blue)

> "Only the strongest notification type displays per question; errors take precedence over
> warnings, which precede informational notes."

### 7. Conditional logic

```json
{
  "elements": [
    { "name": "firstName", "type": "text", "title": "First Name" },
    {
      "name": "age",
      "type": "numeric",
      "visibleIf": "{firstName} notempty",
      "requiredIf": "{firstName} contains 'J'"
    },
    {
      "name": "senior",
      "type": "text",
      "setValueExpression": "iif({age} >= 65, 'Yes', 'No')",
      "setValueIf": "{age} notempty"
    }
  ]
}
```

Properties: `visibleIf` (visibility), `enableIf` (editability), `requiredIf` (mandatory),
`setValueIf` / `setValueExpression` (derived values).

Operators: `empty` / `notempty`, `=` / `!=`, `<` `>` `<=` `>=`, `&&` / `||` (also `and`/`or`),
`contains` / `notcontains`, `anyof` / `allof` / `noneof`.

Functions: `iif(condition, a, b)`, `age(birthdate)`, `dateDiff(from, to, interval)`, `sum()`,
`max()`, `min()`, `avg()`, `displayValue(questionName, value)`, `sumInArray()`, `countInArray()`.

— <https://surveyjs.io/form-library/documentation/design-survey/conditional-logic>

### 8. Theming

```js
import { BorderlessLight } from "survey-core/themes";

const survey = new Model({ /* ... */ });
survey.applyTheme(BorderlessLight);
```

Theme JSON shape:
```js
{
  "themeName": "doubleborder",
  "colorPalette": "dark",
  "isPanelless": true,
  "cssVariables": {
    // CSS variable definitions
  }
}
```

Predefined themes include Default Light, Borderless Light, Flat Dark Panelless, **Contrast Dark**,
**Contrast Light** — "Each theme supports dark mode and compact panelless layouts, totaling 32
variations." Full JSON definitions live at
<https://github.com/surveyjs/survey-library/tree/master/packages/survey-core/src/themes>.

Custom themes exported from the Theme Editor are just that JSON object:
```js
const customTheme = { /* exported JSON */ };
survey.applyTheme(customTheme);
```
— <https://surveyjs.io/form-library/documentation/manage-default-themes-and-styles>

Because a theme is `cssVariables`, mapping it to an existing design system is a token-mapping job,
not a CSS-override fight.

### 9. The states — this is the anti-slop payload

`survey.state`, verbatim from `survey-core/src/survey.ts`:

> "Returns the current survey state. Possible values:
>
> - `"loading"` - The survey is being loaded from a JSON schema.
> - `"empty"` - The survey has no elements to display.
> - `"starting"` - The survey displays a start page.
> - `"running"` - A respondent is taking the survey.
> - `"preview"` - A respondent is previewing answers before submitting them.
> - `"completed"` - A respondent has completed the survey and submitted the results."

Save-progress states, from `survey-core/src/survey-events-api.ts` — available on the `onComplete`
event's `options`:

| Method | Doc comment |
|---|---|
| `options.showSaveInProgress(text?)` | "Call this method to indicate that the save operation is in progress. You can use the `text` parameter to display a custom message." |
| `options.showSaveSuccess(text?)` | "Call this method to indicate that survey results are successfully saved." |
| `options.showSaveError(text?)` | "Call this method to indicate that an error occurred during the save operation." |
| `options.clearSaveMessages(text?)` | "Call this method to hide the save operation messages." |

⚠️ From the `onComplete` doc comment:

> "Do not disable the `showCompletePage` property if you call one of the `options.showSave...`
> methods. This is required because the UI that indicates data saving progress is integrated into
> the complete page. If you hide the complete page, the UI also becomes invisible."

Completion / success state:
- `completedHtml` — "HTML content displayed on the complete page."
- `completedHtmlOnCondition` — "An array of objects that allows you to specify different HTML
  content for the complete page. Each object should include the `expression` and `html`
  properties." (i.e. *different* success states per outcome.)
- `showPreviewBeforeComplete` — "Specifies whether to show a preview of given answers before they
  are submitted. Default value: `false`" (with `previewMode`, `showPreview`, `cancelPreview`).
  This is the GOV.UK "Check your answers" page.

### 10. Question types

From <https://surveyjs.io/form-library/documentation/api-reference/question>:

`boolean`, `checkbox`, `comment`, `dropdown`, `expression`, `file`, `html`, `image`,
`imagepicker`, `matrix`, `matrixdropdown`, `matrixdynamic`, `multipletext`, `panel`,
`paneldynamic`, `radiogroup`, `ranking`, `rating`, `signaturepad`, `tagbox`, `text`.

| Type | What it is |
|---|---|
| `boolean` | yes/no toggle |
| `checkbox` | multi-select checkboxes |
| `comment` | multi-line textarea |
| `dropdown` | single-select list |
| `tagbox` | multi-select dropdown with tags |
| `expression` | read-only calculated value |
| `file` | file upload |
| `html` | arbitrary HTML content block |
| `image` | image display |
| `imagepicker` | choose from image options |
| `matrix` | single-select grid |
| `matrixdropdown` | grid with editor cells |
| `matrixdynamic` | grid with add/remove rows |
| `multipletext` | several text inputs as one question |
| `panel` | grouping container |
| `paneldynamic` | repeating group of questions |
| `radiogroup` | single-select radios |
| `ranking` | drag-to-order |
| `rating` | scale |
| `signaturepad` | drawn signature |
| `text` | single-line input (with `inputType` for email/date/number/tel/url…) |

## Accessibility

### What SurveyJS claims

Accessibility Statement — <https://surveyjs.io/accessibility-statement> (updated **7/1/2026**):

> "The SurveyJS Form Library component is **fully accessible with the Contrast theme as of v2.1.0**.
> The Survey Creator achieved the same level of compliance as of v2.2.2. **Starting with v3, both
> products support full accessibility with the Contrast and Monochrome themes.**"

Standards referenced: "Web Content Accessibility Guidelines (WCAG)" and "**WAI-ARIA 1.2**
specifications". **No specific WCAG conformance level (A/AA/AAA) is stated.**

Testing methodology (stated):

> "Automated accessibility tests that combine end-to-end testing with Playwright and accessibility
> auditing with **axe-core** engine." — integrated into CI/CD alongside unit, functional,
> integration and visual regression tests.

Accessibility FAQ — <https://surveyjs.io/faq/accessibility>:

> "Both comply with **WCAG**, **Section 508**, and **ARIA** standards."

and the components "support **screen readers**, **ARIA attributes**, **keyboard-only navigation**,
and more."

### What it does NOT claim / does not cover

Read the statement carefully — the accessibility claim is **conditional on the theme**:

- ⚠️ **Conformance is scoped to the Contrast and Monochrome themes only** (v3+). The
  **Default Light theme — which is what you get if you do nothing — is not covered by the
  conformance claim.** Any custom theme you build from `cssVariables` is definitionally outside it.
- ⚠️ **No WCAG level is named.** "Complies with WCAG" without a version and level is not a
  conformance claim you can put in a procurement response. There is **no VPAT** referenced.
- ⚠️ **No screen readers are named** as tested. axe-core is a static rule engine; it does not
  test screen-reader announcement, focus order coherence, or whether an error message is actually
  reachable.
- ⚠️ **Dashboard and PDF Generator are explicitly not there yet:** "actively working to achieve the
  same level of accessibility compliance for the Dashboard and PDF Generator components."
- ⚠️ **Your integration can break it:** "While SurveyJS strives for full accessibility, certain
  third-party integrations or custom implementations may affect compliance."

### What you must do yourself

1. **Apply a Contrast or Monochrome theme** — or verify your custom theme's `cssVariables` against
   WCAG 1.4.3 (4.5:1 text, 3:1 UI components) yourself. Colour contrast is the #1 thing a custom
   theme breaks.
2. **Write real `title` and `description` text per question.** SurveyJS wires the labelling; the
   *quality* of the label is yours. A question titled "Field 1" is inaccessible regardless of ARIA.
3. **Write real `requiredErrorText` and validator `text`.** Default messages ("Response required")
   fail WCAG 3.3.3 (error suggestion) for anything with a format constraint. Say *what* is wrong
   and *how to fix it*.
4. **Test error announcement with a real screen reader** (NVDA + Firefox, VoiceOver + Safari).
   Verify that after a failed Next, focus moves to the error summary or the first invalid field.
5. **Don't hide the progress indicator** on multi-page forms (WCAG 2.4.8 / 3.2.x orientation).
6. **`showPreviewBeforeComplete`** materially helps cognitive accessibility — a "check your
   answers" step is part of the GOV.UK pattern for a reason.
7. **Don't rely on colour alone** for the `error`/`warning`/`info` `notificationType` distinction.
8. **`signaturepad` is a known hard case** — always offer a non-drawn alternative (typed name).

## ADOPT — what SurveyJS earns its place for

Mapped to the anti-slop principle: *real functionality, real data, real states.*

1. **A working multi-step form IS the "design the empty/error/loading states" requirement,
   discharged.** The brief "design the error state" is usually answered with a red-bordered
   screenshot. SurveyJS gives you `state ∈ {loading, empty, starting, running, preview, completed}`
   plus `showSaveInProgress` / `showSaveSuccess` / `showSaveError` as *runtime* states you can
   actually navigate to and screenshot. You cannot forget the loading state when the library has an
   API for it.
2. **One-question-per-page (GOV.UK "one thing per page") is one property.**
   `questionsOnPageMode: "questionPerPage"` — or `"inputPerPage"` to split matrices and repeating
   panels down to individual inputs. The single highest-conversion, most-accessible form pattern in
   existence, available without building a wizard.
3. **Validation is declarative and therefore reviewable.** `isRequired`, `requiredErrorText`,
   six built-in validators, `checkErrorsMode`, `notificationType`. A reviewer can read the JSON and
   say "this postcode field has no format validation" — which is impossible with hand-rolled
   `onSubmit` handlers scattered through components.
4. **Conditional logic makes the form respond to the user.** `visibleIf` / `enableIf` /
   `requiredIf` turn a static field wall into something that visibly reacts — the difference
   between a form and a picture of a form. This is the single most convincing "this is real"
   signal in a prototype.
5. **The schema is the content model.** A form as JSON is reviewable by the content designer, the
   legal reviewer, and the developer at once. That is the opposite of slop, which is unreviewable
   because it is not about anything.
6. **`sender.data` is a plain object keyed by question `name`.** No FormData wrangling, no
   serialisation layer. It goes straight to `fetch(..., {body: JSON.stringify(sender.data)})`.
7. **Theming is `cssVariables`**, so it maps onto an existing design system's tokens rather than
   fighting it — and the Contrast themes give you a WCAG-oriented starting point for free.
8. **21 question types** including `ranking`, `paneldynamic` (repeating groups), `matrixdynamic`
   (add-a-row tables) and `file` — the shapes real business forms actually need and that
   hand-rolled demos never include.
9. **MIT and actively released** (v3.0.3, 2026-09-03).

## AVOID / traps

1. **The Survey Creator licence trap.** The #1 risk. `survey-creator-core` /
   `survey-creator-react` are **commercial, per-developer, perpetual-with-40%-annual-updates**.
   Importing Creator "just to try the builder" and leaving the import in place puts a paid EULA
   over the project. Dashboard and PDF Generator likewise. **Grep your bundle.**
2. **~410 KB gzipped** for the CDN triple (`survey-core` 307 KB + CSS 48 KB + `survey-js-ui` 56 KB).
   That is a *lot* for a contact form. Use native HTML + a `<form>` for anything under ~6 fields
   with no branching. SurveyJS earns its bytes at: multi-page, conditional logic, repeating groups,
   matrices, or a schema that must be authored/changed without a deploy.
3. **Using it for a marketing "contact us" form.** Same slop failure as a decorative map: heavy
   machinery producing something a `<form>` does better. The point is *real functionality*, not
   *impressive dependencies*.
4. **Default theme + "we're accessible".** The vendor's conformance claim covers **Contrast /
   Monochrome themes only**. Shipping Default Light and citing the accessibility statement is a
   misrepresentation.
5. **Leaving default error messages.** "Response required" on a date-of-birth field fails WCAG
   3.3.3. Every `isRequired` should have a `requiredErrorText`; every validator should have `text`.
6. **No `onComplete` handler / no persistence.** A form that validates beautifully and then
   `alert()`s the JSON is still a fake. Wire `showSaveInProgress` → POST →
   `showSaveSuccess` / `showSaveError`.
7. **No SSR.** React usage requires `'use client'`; "these are client-side components without SSR
   support." Plan for a loading state and a no-JS fallback — a form that renders nothing without JS
   is worse than a plain `<form>`.
8. **`showCompletePage: false` + `showSave*`** — explicitly warned against in the source: the
   save-progress UI lives on the complete page and disappears with it.
9. **jQuery/Knockout UIs are legacy.** `survey-jquery` and `survey-knockout-ui` are on the 1.12.x
   line (v1.12.67, 2026-08-14) while the modern UIs are on 3.0.3. Don't start there.
10. **Question `name` is the data key.** Renaming a question after data exists silently orphans the
    stored answers.
11. **`html` question type renders raw HTML** — same XSS class as Leaflet popups if the schema is
    user-supplied.

## Scanner signatures (SurveyJS)

| # | Signature | Detection | Severity |
|---|---|---|---|
| S1 | **Commercial package imported** | any import/require of `survey-creator-core`, `survey-creator-react`, `survey-creator-angular`, `survey-creator-vue`, SurveyJS Dashboard or PDF Generator packages | **Licence — critical** |
| S2 | **No required fields anywhere** | schema contains ≥3 questions and **zero** `isRequired: true` and zero `requiredIf` → the form has no error state to design | **Slop — high** |
| S3 | **Required without a message** | `"isRequired": true` present with no sibling `requiredErrorText` | High (a11y, WCAG 3.3.3) |
| S4 | **Validators without messages** | any `validators` entry lacking a `text` property | High (a11y) |
| S5 | **No validators at all on formatted inputs** | a question with `inputType` of `email`/`tel`/`url`/`number`, or a name matching `postcode\|zip\|phone\|email\|iban`, and no `validators` array and no `inputType` constraint | High |
| S6 | **No completion handling** | `new Model(` present and no `onComplete.add(` anywhere | **Slop — high** |
| S7 | **Fake completion** | `onComplete.add` handler body contains only `alert(`, `console.log(`, or an empty function — no `fetch`/`axios`/`XMLHttpRequest`/`showSaveInProgress` | **Slop — high** |
| S8 | **No save states** | an `onComplete` handler that performs a network call but never calls `options.showSaveInProgress` / `showSaveSuccess` / `showSaveError` | Medium |
| S9 | **No conditional logic in a multi-page form** | `pages` array length ≥3 and zero `visibleIf`/`enableIf`/`requiredIf` → it's a paginated field wall, not a form that responds | Medium |
| S10 | **No success state** | no `completedHtml`, no `completedHtmlOnCondition`, and `showCompletePage` not explicitly handled | Medium |
| S11 | **Accessibility claim without a Contrast/Monochrome theme** | `applyTheme(` with a non-Contrast/Monochrome theme, or no `applyTheme` at all, in a codebase asserting WCAG conformance | High (a11y) |
| S12 | **Broken save UI** | `showCompletePage: false` co-occurring with any `showSave*` call | Medium |
| S13 | **Raw HTML question from dynamic source** | `"type": "html"` whose `html` value is interpolated from a fetch/CMS variable | Medium (security) |
| S14 | **Legacy UI package** | `survey-jquery` or `survey-knockout-ui` in `package.json` for new work | Low |
| S15 | **Heavyweight for a trivial form** | SurveyJS imported and the schema has <6 questions, one page, no branching | Medium (perf/slop) |

## Gotchas (SurveyJS)

- **Two model classes with the same name.** `Survey.Model` (UMD/CDN global) vs `Model` (imported
  from `survey-core`). Copy-pasting between the two docs sets breaks silently.
- **CSS import path changed.** Current is `survey-core/survey-core.css`; older tutorials use
  `survey-core/defaultV2.min.css` or `modern.min.css`. If it looks unstyled, that's why.
- **Themes are a subpath export**: `import { BorderlessLight } from "survey-core/themes"` — not
  from `survey-core`.
- **`questionsOnPageMode` is a *runtime* property, not just JSON** — set it on the model to
  A/B one-per-page against standard without touching the schema.
- **`checkErrorsMode` default is "on next page"**, not on change. Users can type garbage and only
  learn on Next. `"onValueChanged"` is usually the kinder choice; combine with
  `textUpdateMode: "onTyping"` carefully (validating on every keystroke as someone types an email is
  hostile — validate on blur).
- **`survey-core` unpacked size is ~52 MB on npm** (includes sources, all themes, all locales).
  Only the `dist` entry points ship; don't panic at the registry number, but *do* tree-shake and
  import only the locales you need.
- **`inputPerPage`** (v3+) is the aggressive form of one-thing-per-page: it splits matrices,
  dynamic panels and multiple-textboxes into individual pages. Excellent for accessibility, but
  makes a long form feel much longer — measure.
- **`expression` questions are read-only display**, not inputs; they don't appear in `sender.data`
  unless you set them to.
- **Localisation**: `survey-core` ships many locales but you must import and set
  `surveyLocalization.currentLocale`.
- **Version alignment**: keep `survey-core` and the `survey-*-ui` package on the *same* version.
  Mismatches across the 2.x→3.x boundary produce cryptic render failures.

---

# Cross-cutting: how these two fight AI slop

| Slop pattern | Real replacement | Library |
|---|---|---|
| Three-icon "Global / 24-7 / Trusted" grid | A map of the actual 12 locations, with hours in popups and the same 12 as an accessible list | Leaflet |
| "50+ countries" counter animating up | A choropleth styled from the real country list, with a legend and a "no data" colour | Leaflet + GeoJSON `style` fn |
| A screenshot of a form | A form that rejects your postcode, tells you why, and shows a saving spinner then a success page | SurveyJS |
| "Design the error state" as a red-bordered mock | `requiredErrorText` + `notificationType` + `showSaveError`, reachable at runtime | SurveyJS |
| A "multi-step onboarding" carousel of static images | `questionsOnPageMode: "questionPerPage"` + `showPreviewBeforeComplete` | SurveyJS |
| Lorem ipsum in a "Locations" section | Impossible — the map needs coordinates | Leaflet |

**The shared test**: can a keyboard-only user, with the screen reader on, get the same information
and complete the same task? If the answer is no, the page is decoration regardless of how it looks.
Leaflet gets you keyboard-operable markers but **not** a non-visual alternative — you build the
list. SurveyJS gets you an accessible form **only under the Contrast/Monochrome themes** — you
verify the contrast and write the error messages.

---

## Sources fetched

**Leaflet**
- <https://leafletjs.com/> — version, size claim
- <https://leafletjs.com/download.html> — versions, CDN tags + SRI, npm
- <https://leafletjs.com/examples/quick-start/> — map/tileLayer/marker/circle/polygon/popup/events, attribution obligation
- <https://leafletjs.com/examples/geojson/> — geoJSON, style, pointToLayer, onEachFeature, filter, XSS note
- <https://leafletjs.com/examples/accessibility/> — official a11y guide
- <https://leafletjs.com/reference.html> — fitBounds, flyToBounds, getBounds, invalidateSize, keyboard, alt, autoPanOnFocus, attribution control options
- <https://leafletjs.com/plugins.html> — full plugin database (parsed: 36 categories, ~570 entries)
- <https://leafletjs.com/2025/05/18/leaflet-2.0.0-alpha.html> — 2.0 breaking changes
- <https://github.com/Leaflet/Leaflet/discussions/8006> — a11y gaps
- `https://raw.githubusercontent.com/Leaflet/Leaflet/main/LICENSE` — BSD-2-Clause
- `https://registry.npmjs.org/leaflet` — dist-tags, licence, dates
- <https://operations.osmfoundation.org/policies/tiles/> — Tile Usage Policy
- <https://osmfoundation.org/wiki/Licence/Attribution_Guidelines> — attribution requirements
- <https://github.com/CartoDB/basemap-styles> — CARTO URLs + attribution
- <https://docs.stadiamaps.com/attribution/> and <https://docs.stadiamaps.com/tutorials/raster-maps-with-leaflet/> — Stadia
- <https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html> — Esri
- `https://registry.npmjs.org/<plugin>` for 34 plugin packages — versions, dates, licences
- unpkg — measured byte sizes

**SurveyJS**
- `https://raw.githubusercontent.com/surveyjs/survey-library/master/LICENSE` — MIT
- `https://raw.githubusercontent.com/surveyjs/survey-library/master/README.md` — product family, licensing section
- `https://raw.githubusercontent.com/surveyjs/survey-creator/master/LICENSE` — commercial EULA
- <https://surveyjs.io/licensing> — which products are paid, tiers
- `https://registry.npmjs.org/<pkg>` for 9 SurveyJS packages — versions, dates, licence fields
- <https://surveyjs.io/form-library/documentation/get-started-html-css-javascript> — CDN tags, Model, render, onComplete
- <https://surveyjs.io/form-library/documentation/get-started-react> — React install/imports
- <https://surveyjs.io/form-library/documentation/get-started-vue> — Vue install/imports
- <https://surveyjs.io/form-library/documentation/get-started-angular> — Angular install/imports
- <https://surveyjs.io/form-library/documentation/data-validation> — validators, checkErrorsMode, notificationType, onValidateQuestion
- <https://surveyjs.io/form-library/documentation/design-survey/conditional-logic> — visibleIf/enableIf/requiredIf, operators, functions
- <https://surveyjs.io/form-library/documentation/design-survey/create-a-multi-page-survey> — pages, navigation
- <https://surveyjs.io/form-library/documentation/manage-default-themes-and-styles> — applyTheme, theme JSON
- <https://surveyjs.io/form-library/documentation/api-reference/question> — question types
- <https://surveyjs.io/accessibility-statement> — conformance claim, scope, testing, limits
- <https://surveyjs.io/faq/accessibility> — WCAG/508/ARIA claims
- `packages/survey-core/src/survey.ts` (master) — `questionsOnPageMode`, `state`, `completedHtml`, `showPreviewBeforeComplete`, `onComplete` doc comments
- `packages/survey-core/src/survey-events-api.ts` (master) — `showSaveInProgress` / `showSaveSuccess` / `showSaveError` / `clearSaveMessages`
- unpkg — measured byte sizes

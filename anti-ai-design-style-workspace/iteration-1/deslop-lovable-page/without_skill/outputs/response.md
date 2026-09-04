I rewrote the page and saved it as `fixed.html`. Same product, same sections, same facts — just designed like a person made deliberate choices instead of reaching for every trend at once.

**What made it look like AI slop**

- Dark background with purple/blue glow blobs, gradient text, glassmorphism cards, and every button growing on hover. This is the default "Lovable look" and people recognise it instantly.
- Everything centred, every corner heavily rounded, emoji (⚡🚀🔥) standing in for icons.
- Copy full of filler: "Elevate", "Seamlessly", "game-changer", "empowers modern teams to unlock effortless billing". None of it says what the product does.
- Fake-feeling trust signals: random stock-photo avatars from pravatar.cc, a scrolling logo marquee, and a pulsing "Live: 3 people are viewing this page" widget that was hardcoded, not live.
- The Pricing section had no pricing in it, and the FAQ had three questions with no answers, all stuffed into one paragraph.

**What I changed**

1. **Look and feel.** Light, warm off-white background, near-black text, one accent colour (a deep green, used sparingly). Thin rules separate sections instead of cards. Buttons are small, square-cornered and solid. No gradients, no blur, no glow, no hover-scale, no animation. I dropped the Tailwind play CDN and wrote plain CSS so the page loads without a flash of unstyled content and with no runtime dependency.
2. **Type.** Swapped Inter + Space Grotesk for IBM Plex Sans with IBM Plex Mono for numbers and labels, which suits an invoicing product. Headlines are medium weight rather than bold, and sized so they don't shout.
3. **Layout.** Added a proper top navigation (Features, Customers, Pricing, FAQ) and a footer with the same links. The hero is left-aligned in two columns: headline and stats on the left, a simple illustrated invoice on the right. That illustration is purely decorative (it's marked as such for screen readers); swap it for a real product screenshot when you have one. Each section now has a small label on the left and its heading on the right, which gives the page a consistent rhythm.
4. **Copy.** Rewrote the headline and subhead to say what the product is ("Invoicing that stays out of your way." / "…a straightforward way to create and send invoices, and keeps billing tidy as the team grows"). Reworded the three feature blurbs to be plainer. I did not add any claims that weren't already implied by the original (fast, scalable, secure, AI-powered v2.0), so please sanity-check the wording against what the product actually does.
5. **Kept every real fact.** The "New: AI-Powered v2.0" tag, the 10K+ / 99.9% / 24/7 stats, all three features, all three testimonials word-for-word with names and titles, the five customer names, "Trusted by 10,000+ teams worldwide", the three FAQ questions, and the © 2026 footer are all still there.
6. **Removed two things that weren't real information.** The "3 people are viewing this page" counter (it was a hardcoded number, and fake urgency widgets are a red flag to anyone who's seen them before) and the random stock avatars next to the testimonials (they weren't photos of those people). Logos are now a static row of names instead of a marquee.
7. **Mobile.** Everything collapses to a single column; I checked it at 390px and 1280px and nothing overflows.

**Things you should still fix yourself, because I couldn't invent them**

- The testimonials read as placeholders ("John Doe", "Jane Smith", "Seamless. Effortless. Revolutionary."). Real quotes from real customers will do more for the page than any design change.
- The Pricing section still has no prices. I gave it a short line and a "Get started" button so it isn't an empty heading, but it needs actual plans.
- The FAQ questions have no answers. They're listed cleanly with an "Ask us" link for now, but two or three sentences each would be much better.
- All the buttons and "Ask us" links point to `#`. Wire them to your real signup and contact URLs.

Done — saved as `fixed.html`. Your cofounder isn't wrong, and the tells were pretty specific. Here's what I changed and, just as importantly, what I didn't.

## What made it read as AI slop

Six things, all of them stylistic defaults rather than decisions:

1. **Purple-to-pink gradient headline on a dark page with glowing blobs.** This is the single most recognizable "generated landing page" signature. Gradient text also hurts legibility, because the lightest part of the gradient sits on a dark background.
2. **Everything was a frosted glass card.** Same `rounded-2xl`, same white-10% fill, same white-20% border, on features *and* testimonials — so nothing had more visual weight than anything else. No hierarchy.
3. **Everything grew when you hovered it.** Cards, both buttons, the CTA. Hover-to-scale on non-clickable cards is a giveaway.
4. **Decorative emoji doing icon duty.** ⚡ for "Lightning Fast", 🚀 for "Scalable", and 🔥 for "Secure" — a flame icon for a security feature is actively confusing. The colored squares behind them were pale pastels on a dark page, which looked like a mistake.
5. **Filler copy.** "In today's fast-paced world", "isn't just a tool — it's a game-changer", "empowers modern teams to unlock effortless billing", "Supercharge your workflow with blazing speed." That's a lot of words that say nothing.
6. **Two fake-engagement props:** a scrolling marquee of your own customer names (with the list duplicated so the loop seams), and "Live: 3 people are viewing this page" with a pulsing green dot. That number isn't live. If a real prospect ever notices it doesn't change, it costs you more trust than it buys.

Smaller stuff: `min-h-screen` on three separate sections forced a full screen of scrolling between each block; the feature cards had `border border-white/20` and `border-l-4 border-purple-500` fighting each other on the same element; the testimonial photos were pulled from pravatar.cc, which serves random strangers' faces.

## What I did instead

- **New palette and type.** Warm off-white paper, near-black ink, one accent (a burnt sienna) used only for things you can actually click. Headings in a serif, body in the system sans. No gradients anywhere.
- **Removed the Tailwind CDN and the Google Fonts link.** It's now one self-contained file with plain CSS — it renders identically offline and doesn't depend on two third-party servers to look right.
- **Left-aligned the page** and capped line length at a readable measure. Centered-everything is what makes these pages feel like a slide deck.
- **Real hierarchy.** Sections are separated by thin rules and consistent spacing instead of a full viewport of emptiness. Features and testimonials are no longer both cards: features are text columns under a heavy top rule, testimonials are proper `<blockquote>`/`<figure>` pairs.
- **Cut the emoji icons** rather than replacing them with stock icons that say just as little.
- **Added a top nav** linking to the four sections that already had IDs. The anchors existed; nothing pointed at them.
- **Replaced the pravatar photos with initials.** Same information, no stranger's face on your site.
- **Accessibility fixes:** the buttons got `type="button"`, focus outlines are visible, and every text/background pair on the page passes contrast.

## Copy I rewrote

I only rewrote marketing filler, and I kept every rewrite at the same altitude as the original — no new claims about what the product does:

- Headline: "Elevate Your Invoicing, Seamlessly" → "Invoicing software for modern teams."
- Subhead: dropped "In today's fast-paced world" and "game-changer". It now reads "InvoiceFlow is a billing tool for modern teams. It handles your invoicing so you can stop thinking about it." — same promise ("effortless billing"), fewer words.
- "Lightning Fast" → "Fast", and its blurb lost "supercharge" and "blazing".
- "Enterprise-grade security, effortlessly" → "Enterprise-grade security."

## What I deliberately left alone

- **All three testimonials, word for word**, including names and titles. I'm not editing quotes attributed to people.
- **The stats** 10K+ / 99.9% / 24/7.
- **The customer list and the "Trusted by 10,000+ teams worldwide" line.** That line used to sit under the testimonials heading; it's now the label on the customer strip, so it's next to the names it refers to.
- **The "New: AI-Powered v2.0" badge**, both CTAs (they still don't do anything — same as before), and the footer.
- **The three FAQ questions.** They were crammed into one sentence in a paragraph; they're now three separate lines. Same words.

## Three things only you can fix

1. **Your testimonials are placeholders.** "John Doe" and "Jane Smith" at "Acme" and "StartupX" are not real people. They look worse now that they're set in a serif and given prominence — the design can't hide them. Either get two real quotes or cut the section.
2. **The pricing section has no prices.** With the fake viewer-counter removed, it's a heading and nothing else. I put an honest placeholder line there. It needs actual plans.
3. **The FAQ has no answers.** Same situation — questions with no answers under them.

I'd also sanity-check the 10K+ / 99.9% / 24/7 numbers before this goes live. They were generated alongside everything else, so I wouldn't assume any of them are measured.

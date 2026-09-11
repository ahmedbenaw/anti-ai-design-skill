Done. The new page is saved as `fixed.html`, next to a short `DESIGN.md`
that records the choices I made.

Your cofounder was right, and I can show you why. I scanned the old page
first, before changing anything. It scored 52 out of 100 on the AI-look
scale, where 40 and up means "reads as AI-generated". It had 20 separate
tells and 3 accessibility problems.

## What I changed

1. **Took out the light show.** Gone: the purple and pink gradient
   headline, and the two glowing blobs behind the page. Also gone: the
   frosted glass cards, the scrolling logo strip, the pulsing green dot,
   and the cards that grew when you hovered. None of it said anything
   about invoicing.
2. **Put the product on the page.** The middle of the page is now a
   sample invoice. It has line items, a total, and a status line reading
   "Paid on 2 March". It is labelled as sample data. Swap in a real
   screenshot when you have one.
3. **Rewrote the words.** The old headline promised to lift your invoicing
   up, smoothly. The new one is "Send an invoice. See when it is paid."
   The marketing words that would fit any product at all are gone. So is
   the "not just a tool" phrasing. The reading level dropped from grade
   7.7 to grade 2.2.
4. **Renamed the buttons.** "Get Started" and "Learn More" are now "Make
   your first invoice" and "Look at a sample invoice".
5. **Changed the colours and the type.** The page is now a cool off-white
   with a deep green ink colour. Green and red appear in one place only:
   paid, or late. Each one also says the word, so colour is never the only
   clue. There is one type family, IBM Plex. Numbers are set in its
   monospaced face, so the money lines up in a column.
6. **Reordered the page.** It now goes: what it is, what you send, what it
   is built for, what it costs, questions. That is the order a visitor
   asks things in. The old order was the stock template every generated
   page uses.
7. **Fixed the accessibility problems.** Body text is 17px and buttons are
   48px tall. Links show a visible ring when you tab to them. The grey
   text is now dark enough to read.

## What I removed, and why

**Made up, so it had to go.** The three testimonials were fake. "John
Doe", "Sarah Chen" and "Jane Smith" are stock names, and their photos came
from pravatar.cc, a site that generates fake faces. The logo strip listed
Acme, TechCorp and StartupX, which are not companies. "3 people are
viewing this page" was not counting anything. On a real site this is the
single most damaging thing on the page.

**Probably true, but unproven, so I parked it.** That means the user
count, the uptime figure, and the round-the-clock support line. The
"trusted by" banner above the testimonials went too. Round numbers like
those read as invented, even when they are not. Tell me which ones are
real and I will put them back.

**Real, so I kept it.** The name, and what the product does. The three
things it claims: speed, works at any size, security. The fact that
version 2.0 is out with new AI features. The three FAQ questions, and your
copyright line.

**One thing I assumed. Tell me if it is wrong.** The page now says
InvoiceFlow shows you whether an invoice is paid or late. Your first
version never said that. It is the obvious thing an invoicing tool would
do, so I built the page around it. If the product does not do it, say so.
I will take the status line off the sample and change the headline.

**Two gaps I left visible on purpose.** Your pricing section had a heading
and no prices. Your FAQ had questions and no answers. I have not invented
either. Both now sit on the page marked "to write". Send me the prices and
the answers and I will drop them in.

## The proof

```
PASS: AI-look 0/100 (distinct), craft flags 0, library misuse 0, copy grade 2.2, brand distance COMPLIANT, rendered SKIPPED | register 2026.10, rules b7cd873aa4831ab9, brand rules 5697117fa1b27195
```

"rendered SKIPPED" means one extra check did not run, because it needs a
browser tool that is not installed here. Nothing failed. The other checks
all ran and all passed.

Three things on this page could only belong to InvoiceFlow. The invoice
sheet. The paid-or-late status, in words and colour. The column of money
that adds up in front of you. One caution. A scanner can only tell
you that no known AI patterns are left. It cannot tell you the design is
good.

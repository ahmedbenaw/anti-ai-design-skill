# DESIGN.md — InvoiceFlow landing page

**Assumed brief.** The user was not present to answer the three questions, so
I drafted this from the page itself. Correct anything that is wrong and I
will rebuild to match.

## Who it is really for

One person, or a small team, who sends invoices and then waits to be paid.
They are not buying "software". They want the money in the bank.

## Three things only InvoiceFlow could show

1. An invoice. The actual document, with line items and a total.
2. Whether that invoice is paid, due, or late.
3. The total, in figures that line up in a column.

Point 2 is an assumption. The first version of the page never said the
product tracks payment. It is the obvious thing an invoicing tool would
do, so I built the page around it. If InvoiceFlow does not do it, the
status line comes off the sheet and the headline changes with it.

Everything else on the page is something any product could say. So the
invoice itself is the centre of the page, not a decorated card grid.

## The feeling

Plain and countable. A ledger, not a launch. The page should read like a
statement you could hand to an accountant.

## Colour

Generated, not hand-picked, with the brand guard's palette tool
(`--hue 150 --temp cool --chroma medium`). Roles used:

| Role | Hex | Used for |
|---|---|---|
| background | `#F4FAFF` | page |
| surface | `#FFFFFF` | the invoice sheet |
| sunken | `#E9F0F6` | table header row |
| border | `#888F94` | rules and dividers |
| text | `#2B3136` | body |
| text secondary | `#60666C` | captions |
| accent | `#00431F` | buttons, links |
| paid | `#006E2A` | paid status |
| late | `#78001B` | late status |

Nothing else on the page uses green or red.

Green and red appear only where they carry a fact: paid, or late. Never as
decoration. Each status also carries a word, so colour is never the only
signal.

## Type

One family, IBM Plex Sans, plus IBM Plex Mono for every number. The mono
face is there for a reason: money has to line up in a column. Tabular
figures are the whole point of the page.

## Never list (from the scan of the first version)

- No gradient headline text, no glow blobs, no frosted glass cards.
- No invented people, avatars, logos, or round numbers.
- No emoji standing in for icons.
- No icon tile above a card heading, no coloured left stripes.
- No marquee, no pulsing dot, no hover growth.
- No "get started" and "learn more" side by side.
- No words from the register's buzzword list (rule CP1).
- Nothing claimed that cannot be backed up.

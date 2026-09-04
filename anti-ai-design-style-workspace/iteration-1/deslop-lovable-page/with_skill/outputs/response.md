Done. Your new page is `fixed.html`, next to it are `DESIGN.md` and `parked-content.md`.

> Verified: AI-look score 0/100 (distinct), craft flags 0, register 2026.08. The Lovable page scored 52/100 with 20 AI tells and 3 accessibility flags.

Three things on the page now belong only to InvoiceFlow: a readable example invoice is the hero image instead of glowing blobs; the money columns and ruled lines are borrowed from a paper invoice book, and so is the single green "PAID" stamp that became the accent colour; and the sections are ordered by the questions a visitor actually asks (what is it, what do I get, is it for me, what does it cost).

**What I changed, in plain words**

1. **Removed the "AI look" pieces.** The purple-to-pink gradient headline, the blurred colour blobs, the frosted-glass cards, the emoji icons, the coloured stripes on cards, the "✨ NEW" pill, the scrolling logo strip, and the cards that grow when you hover. None of these carried information.
2. **Rewrote the copy in the words you would say to a customer.** "Elevate your invoicing, seamlessly" is now "Write the invoice, send it, and see when it is paid." The three features (fast, scalable, secure) are still there, just said plainly. The buttons say what they do ("Start using InvoiceFlow") instead of "Get Started" and "Learn More". Reading level went from grade 11 to grade 5.5.
3. **New colours and fonts, chosen for a reason.** Off-white paper, dark ink, one ledger green. IBM Plex Sans for headings and the invoice (built for business documents; its numbers line up in columns). Source Serif 4 for paragraphs (built for reading). Light theme instead of dark, because invoices are paper.
4. **Kept every real claim.** InvoiceFlow, version 2.0 with AI features, fast, works for startups and enterprises, secure, 24/7 support, the three FAQ questions, the copyright line. The buttons still do nothing, same as before, so wire them to your sign-up when ready.
5. **Fixed the accessibility problems.** Body text is 17px, every colour pair passes the 4.5:1 contrast rule (measured), lines stay under 75 characters, buttons are 48px tall, keyboard focus is visible, and the one hover transition respects "reduce motion" settings.

**Two things I need from you**

The page has two dashed boxes marked "To fill in": your price, and your cancellation terms. The Lovable page had a "Simple Pricing" heading with no prices under it, and asked "Can I cancel anytime?" without answering. I did not want to invent either.

**One judgment call, yours to reverse**

I moved the testimonials (John Doe, Sarah Chen, Jane Smith with stock avatars), the logo strip (Acme, TechCorp, StartupX...) and the "10K+ users / 99.9% uptime / trusted by 10,000+" stats out of the page and into `parked-content.md`. I assumed they were Lovable placeholders, not real. Fake proof is the single most damaging tell a page can have, so a new product with none scores better than one with invented numbers. If any of them are true, paste them back with real names and permission. I also removed the "3 people are viewing this page" counter for good; it was not connected to anything, so it was a fake.

**Two honest notes**

- The example invoice (Marlow & Finch Studio, Harbourside Dental) is a mock-up I built in HTML and labelled "Example invoice". Swap it for a real screenshot of InvoiceFlow when you have one; that will be stronger.
- The copy checker still reports one "sentence over 25 words". That is the invoice table read as if it were prose (the checker does not know HTML tables). I left the table alone rather than add fake full stops to line items.

`DESIGN.md` is the one-page brief I worked from. I had to assume the answers since you were away; edit any line and ask for a re-run. Paste it into Lovable before your next prompt and it will stop drifting back to the default look.

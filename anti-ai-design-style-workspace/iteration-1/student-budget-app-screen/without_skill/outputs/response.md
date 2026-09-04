Done. The mockup is saved as `budget-home.html`. Open it in any browser and you'll see it rendered inside a 390px phone frame.

What's on the screen:

- **Allowance card** – "2,090 of 3,500 EGP" left, with the month drawn as a timeline: the sand-coloured bar is what you've spent, the white tick is today. If the bar is behind the tick, you're ahead of pace (the greeting line says so in words too). The card has a torn coupon edge along the bottom, a nod to cafeteria tickets.
- **Three small tiles** under it: safe amount per day until the next allowance, spent today, and what's coming up (midterms in 9 days, since exam weeks are when student spending spikes on printing and coffee).
- **Top 3 categories this month** – Mowaslat (metro, microbus, the odd Uber after a late lab), Food (koshary, foul & ta3meya, cafeteria), and Printing & notes (malazem, photocopies). Each shows the amount, its share of spending, and a progress track.
- **"Log it fast" chips** – one-tap presets for the things you buy every day (Metro 8, Koshary 45, Microbus 12...), because nobody wants to fill a form for a 8 EGP metro ticket.
- **Log an expense button** – pinned to the bottom, with the Arabic "سجّل مصروف" alongside.

Design choices to make it feel student rather than fintech:

- The app is called **مصروف / masrouf**, the word everyone actually uses for their monthly money, and the copy talks about "days till the next masrouf" rather than "budget cycle".
- Warm cream paper background with a faint dot grid (notebook feel), a single deep green plus sand yellow and clay accents. No navy, no gradients, no card-shaped-like-a-credit-card.
- Bilingual touches where they'd naturally appear (app name, card label, the button), while the main copy stays in Egyptian-flavoured English ("Sabah el-fol, Nour").
- Category descriptions use the real vocabulary (mowaslat, malazem, ta3meya) instead of generic "Transportation / Dining".

It's static HTML with inline CSS and SVG icons; the only external dependency is the Rubik font from Google Fonts (it falls back to system fonts if offline). All the numbers are placeholder sample data, easy to swap in the markup.

Things you might want to decide next: whether the primary language should flip to Arabic with an RTL layout, and whether the "Coming up" tile should pull from a semester calendar or be user-entered.

---
name: block-fake-proof
enabled: true
event: file
action: warn
conditions:
  - field: content
    operator: regex_match
    pattern: i\.pravatar\.cc|randomuser\.me|ui-avatars\.com|John Doe|Jane (Doe|Smith)|Trusted by [\d,]+\+|99\.9% uptime|10,000\+ (users|customers|teams)
---

**Invented proof detected**: a fake person, fake avatar, or unverifiable
round statistic (register rules IC5/CP3/LA6).

Why this matters: on a live site this is the single most damaging tell.
It reads as dishonest the moment anyone checks. It IS dishonest.

Do this instead:
- Testimonials: real quote with permission, or delete the section
- Stats: a real number you can back up, or show the product working instead
- Avatars: real photos with consent, or no photos

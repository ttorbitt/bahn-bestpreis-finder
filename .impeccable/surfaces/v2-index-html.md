---
version: 1
slug: "v2-index-html"
primary_target: "v2/index.html"
related_targets: ["app-v2.html"]
---

# Surface brief: v2 (Fahrkarten-Redesign)

Scope: the whole app at `/v2/` (search form, short intro, results, trip card). Visitor mode: Operate, with a short persuasive intro above the search. v1 stays live at the root.

Audience/job: students with Deutschland-Ticket on the phone, long trips, cheapest without wasting the day. First 5 seconds must say: "Hier ist ein Trick, den die DB nicht zeigt" — serious, not scammy. Intro: one sentence plus one visible real example, then the search. Must not: copy DB branding (no DB logo/red identity), cream-serif-terracotta AI look, comic/confetti. Allowed: Bahn world plus a few insider/"hack" accents.

## Direction contract

THESIS: Every result is a train ticket for the whole route, but only the middle piece is printed and paid; the parts before and after are torn off at the perforation and ride on the Deutschland-Ticket. Refuses the category default (white cards, blue accent, price-first list).

OWN-WORLD: Cool ticket card stock (#cfe9da mint on #eef1ec ground; dark: #1d2a24 on #0f1412), black thermal ink #121514, one magenta validation stamp #e0135f for the trick/saving, slate perforation #6f8a7c. Hairline rules and perforated edges instead of soft shadows; guilloche security tint only on the paid piece. Times and minutes in tabular thermal-print numerals; UI text in a workhorse sans.

STORY: The visitor sees an example ticket where most of the route is torn off, understands "I only buy the middle", searches, scans tickets where the black printed piece shows what to buy, opens one, shares it.

FIRST VIEWPORT: Mobile 390: compact brand line; headline "Kauf nur das Stück, das du brauchst."; one example ticket (Lübeck Hbf → Frankfurt (Main) Hbf, stubs RE torn off, printed ICE Lüneburg → Fulda, magenta stamp "TRICK"); then the search form as a ticket form with the primary action "Spar-Kombis suchen". Desktop: intro + ticket left, form right.

FORM: Die Fahrkarte (Edmondson/thermal ticket ephemera), position 4 of 7 on the ordered list, seed key 0fcdfcb2. Signature move: the perforation tear — paid ICE piece printed black, D-Ticket stubs torn off; the stamp "TRICK" lands once when results arrive. Raises: sticky hour header (Lexikon), hairline grid (Japanese density), fixed one-line trick note per ticket (Figuren-Katalog), nothing labelled twice (Saville), tabular numerals (Ikeda).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

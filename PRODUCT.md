# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static single-file HTML/CSS/JS (`app.html` is the source, `python3 build.py` builds `index.html` for GitHub Pages and `artifact.html`). No framework, no server, no build tooling beyond `build.py`. Hosted on GitHub Pages (github.com/ttorbitt/bahn-bestpreis-finder). Installable as PWA (`manifest.webmanifest`, `sw.js`; bump `CACHE` on every release).

## Users

Students and young people (roughly 18–27) who own a Deutschland-Ticket and book longer train trips inside Germany — the weekend trip home from university, visiting friends, a city trip. Price comes first, but they will not sit eight hours in regional trains to save a few euros. They plan on the phone, often a few days ahead, sometimes the same day, and share plans with friends.

## Job

"Get me there as cheaply as possible without wasting my day." The user enters start, destination, date and an approximate time and wants to see, at a glance, which combination saves the most money and how risky it is.

## Mechanism (the product's edge)

The search engine finds combinations bahn.de does not offer on its own: buy only a shortened ICE/IC section (e.g. Lüneburg → Fulda instead of Hamburg → Frankfurt) and ride everything before and after with the Deutschland-Ticket — including boarding earlier (Lüneburg instead of Hamburg) and leaving the ICE early. The user tested it against bahn.de with the "Deutschland-Ticket vorhanden" option: the app finds combinations that save real money ("man kann tatsächlich 10er sparen"). It also rates the risk of each combination (separate contracts: a late regional feeder voids the ICE saver fare), shows punctuality per train, night-train and FlixBus alternatives, IC sections where the D-Ticket is valid, and lets users share a chosen trip.

## Positioning and claims

- Saving claims must be concrete but honest: "oft 10 € und mehr pro Fahrt" style statements are allowed; no unverifiable big promises. Always point to bahn.de for the actual price.
- The app has no price data (no legal open price API). Prices are only shown on bahn.de via deep links.
- Unofficial helper tool, no affiliation with Deutsche Bahn. Must not imitate DB branding (no DB logo, no DB corporate identity).
- Language: German, everyday words, DB station names as on bahn.de.

## Constraints

- Mobile-first; must work at 390 px width without horizontal scroll.
- Search takes 1–3 minutes (Transitous open timetable API, rate-sensitive) — progress, partial results and cancel must stay.
- Accessibility: keyboard focus, labels, touch targets ≥44 px on coarse pointers, reduced motion respected, light and dark mode.
- All existing functions must survive any redesign: Spar-Kombi / Ganze Reise / Nur D-Ticket tabs, round trip, travellers profile, favourites, recent searches, risk traffic light with reasons, filters (ICE ab/bis, Ersatzbus), hour overview, earlier/later, share link, "Das nehm ich" + share to friends + personal travel plan + calendar export, night/Flix alternatives, Fahrgastrechte help, FAQ.

## Versions

- v1 (current design, "Romanesque" design-system kit) stays live at the root.
- v2 redesign lives at `/v2/` next to it, same engine and functions; the owner compares and decides later.

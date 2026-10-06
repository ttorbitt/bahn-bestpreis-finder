# Nutzerbedürfnisse – Bahn-Bestpreis-Finder

Stand: 06.10.2026 · Methode: Jobs-to-be-done-Brainstorming (Skill `customer-research`) + Vergleich mit etablierten Seiten.
**Wichtig:** Noch keine echten Nutzerinterviews. Alle Punkte sind Hypothesen (Vertrauen: *niedrig–mittel*), abgeleitet aus Funktionen/Bewertungen der Vergleichsseiten und eigener Nutzung. Nächster Schritt wäre: 5 Leute aus jeder Gruppe 10 min beim Benutzen zuschauen.

## 1. Drei Nutzertypen (Jobs to be done)

| | Studierende mit D-Ticket | Gelegenheitsfahrer ohne D-Ticket | Pendler/Termin (fester Ankunftszeitpunkt) |
|---|---|---|---|
| **Funktionaler Job** | „Komm möglichst billig hin, Regionalzüge sind ja schon bezahlt.“ | „Finde die günstige Verbindung, ohne mich durch Tarife zu wühlen.“ | „Sei pünktlich da – Geld ist zweitrangig.“ |
| **Emotionaler Job** | Gefühl, das System „geknackt“ zu haben; keine Angst, den Sparpreis zu verlieren | Sicherheit, nichts falsch zu buchen | Ruhe: kein Stress beim Umsteigen |
| **Typischer Auslöser** | Heimfahrt am Wochenende, Hin+Rück | Familienbesuch, Urlaub, oft Hin+Rück | Termin, Vorstellungsgespräch, Prüfung |
| **Größte Sorge** | Regionalzug verspätet → ICE-Sparpreis weg | Zu viel bezahlen; komplizierte Split-Tickets | Anschluss verpasst |
| **Braucht von der Seite** | D-Ticket-Kombis + Risiko-Ampel, Rückfahrt gleich mit | Ein klarer Tipp + Knopf zur Buchung | „Ankunft bis“-Suche, Puffer, Ampel |

## 2. Was etablierte Seiten machen

| Seite | Suche | Ergebnisdarstellung | Ladezustand | Hinweise |
|---|---|---|---|---|
| bahn.de / DB Navigator | Hin+Rück-Umschalter, Abfahrt/Ankunft, D-Ticket-Häkchen | Liste: Zeiten groß, Dauer, Umstiege, Preis rechts | Skelett-Zeilen, Ergebnisse erscheinen schrittweise | Kurz; Details hinter „Details“/„i“ |
| Trainline | Hin+Rück als Standard, Tausch-Knopf ⇄ | Sehr ruhige Liste, Preis + „schnellste/günstigste“-Labels | Fortschritt + Platzhalter | Ticketbedingungen aufklappbar |
| Omio | Hin+Rück-Tabs, Verkehrsmittel-Tabs | Sortier-Tabs „günstigste / schnellste / beste“ | Ladebalken oben | Badges statt Sätze |
| bahn.guru | Nur Hinfahrt, Kalender | Preis-Kalender (Tag/Woche) | Fortschrittsanzeige pro Tag | Fast keine |
| sparpreis.guru | Datumsbereich | Preis-Matrix | Wartezeit-Hinweis | Kurz |
| BetterBahn | bahn.de-Link einfügen | Split-Ticket-Vorschlag mit Ersparnis | Schritt-Fortschritt („prüfe Teilstrecken x/y“) | Disclaimer, sonst knapp |

**Muster:** Hin+Rück in einer Suche · Zeiten groß, Rest klein · Labels/Badges statt Sätze · sichtbarer Fortschritt mit Teilergebnissen · Details aufklappbar · ein klarer Buchungsknopf.

## 3. Priorisierte Liste

### Muss (diese Runde umgesetzt)
1. **Sichtbarer Fortschritt** mit echten Schritten und Zähler, Zeitschätzung, Skelett-Karten.
2. **Teilergebnisse früh** zeigen (durchgehendes Ticket sofort, Spar-Varianten danach).
3. **Klare Fehlerbox** mit „Nochmal versuchen“, Timeout, **Abbrechen**-Knopf.
4. **Hin- und Rückfahrt in einer Suche** mit zwei Tabs; Start/Ziel tauschen ⇄.
5. **Ruhige Ergebnisliste** im Reise-App-Stil: Abfahrt–Ankunft groß, Dauer, Umstiege, Ampel-Badge, Knopf „Bei bahn.de öffnen“.
6. **Kurze Hinweise:** 1 Zeile pro Karte, Details aufklappbar, kurze FAQ statt Textblock.
7. Eigenes Design ohne DB-Farben, Hell/Dunkel, Handy-first.

### Sollte (Vorschlag für nächste Runde)
- **„Ankunft bis“-Suche** für Pendler/Termine (API kann `arriveBy`, ist schon in `plan()` angelegt).
- **Schalter „Ich habe kein D-Ticket“** – dann Nahverkehr nicht als „0 €“ werten, sondern Hinweis auf Länder-/Quer-durchs-Land-Tickets.
- **Mehrere Abfahrtszeiten** nebeneinander („früher / später“-Knöpfe wie bahn.de).
- **Letzte Suchen merken** (lokal im Browser).
- **Teilen-Link** mit Suchparametern in der URL (z. B. für WhatsApp an Mitfahrende).

### Später
- Preis-Kalender wie bahn.guru (braucht Preis-Quelle – keine offene API).
- Live-Verspätungen/Baustellen einblenden (Transitous hat teils Echtzeit).
- BahnCard/Alter-Auswahl für Link-Parameter (`r=` im bahn.de-Link).
- Hin+Rück als **ein** bahn.de-Link – im öffentlich bekannten Linkformat (BetterBahn `utils/createUrl.ts`) nicht nachweisbar, darum aktuell zwei Einzellinks.
- Echte Nutzer-Interviews/Umfrage (PMF-Frage „Wie enttäuscht wärst du, wenn es die Seite nicht mehr gäbe?“).

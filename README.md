# Bahn-Bestpreis-Finder

Kleine Web-App für Zugreisen in Deutschland: Start, Ziel, Datum und ungefähre Abfahrt eingeben. Die Seite zeigt die schnellste, die günstigste und die vernünftigste Variante. Dabei vergleicht sie das durchgehende Ticket mit Deutschland-Ticket-Kombinationen (ICE kürzer, Rest Regionalzug) und bewertet mit einer Ampel das Risiko, dass ein Sparpreis verfällt.

- Fahrplan: offener Sollfahrplan von [Transitous](https://transitous.org). Es gibt keine offene Preis-Schnittstelle, Preise also auf bahn.de prüfen.
- Läuft komplett im Browser, ohne Server und ohne Anmeldung.
- Inoffizielles Hilfswerkzeug, keine Verbindung zur Deutschen Bahn.

## Entwicklung

`app.html` ist die Quelle, `stations.json` die Bahnhofsliste (DB-Stationsdaten über [db-stations](https://github.com/public-transport/db-stations)). `python3 build.py` erzeugt daraus `index.html` (GitHub Pages) und `artifact.html`.

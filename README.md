# Bahn-Bestpreis-Finder

Kleine Web-App für Zugreisen in Deutschland: Start, Ziel, Datum und ungefähre Abfahrt eingeben. Die Seite zeigt die schnellste, die günstigste und die vernünftigste Variante. Dabei vergleicht sie das durchgehende Ticket mit Deutschland-Ticket-Kombinationen (ICE kürzer, Rest Regionalzug) und bewertet mit einer Ampel das Risiko, dass ein Sparpreis verfällt.

- Fahrplan: offener Sollfahrplan von [Transitous](https://transitous.org). Es gibt keine offene Preis-Schnittstelle, Preise also auf bahn.de prüfen.
- Läuft komplett im Browser, ohne Server und ohne Anmeldung.
- Inoffizielles Hilfswerkzeug, keine Verbindung zur Deutschen Bahn.

## Entwicklung

`app.html` ist die Quelle, `stations.json` die Bahnhofsliste (DB-Stationsdaten über [db-stations](https://github.com/public-transport/db-stations)). `python3 build.py` erzeugt daraus `index.html` (GitHub Pages) und `artifact.html`.

## Pünktlichkeit aktualisieren (einmal im Monat)

`punct.json` enthält die Pünktlichkeit pro Zug aus dem Vormonat (Quelle: [piebro/deutsche-bahn-data](https://huggingface.co/datasets/piebro/deutsche-bahn-data), Daten der DB, CC BY 4.0).
Monatsdatei laden und auswerten (braucht `pip install duckdb`):

    python3 punctuality.py data-2026-09.parquet punct.json

## App-Dateien

`manifest.webmanifest`, `sw.js` und `icon-*.png` machen die Seite installierbar. Icons neu zeichnen: `python3 make_icons.py`.

#!/usr/bin/env python3
"""Baut aus app.html + stations.json die Artifact-Version (artifact.html) und die Standalone-Seite (index.html)."""
from pathlib import Path
here = Path(__file__).parent
app = (here / "app.html").read_text()
stations = (here / "stations.json").read_text()
assert "/*STATIONS*/[]" in app
body = app.replace("/*STATIONS*/[]", stations)
(here / "artifact.html").write_text(body)
(here / "index.html").write_text(
    '<!doctype html>\n<html lang="de"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png">'
    '<meta name="theme-color" content="#f3f4f6" media="(prefers-color-scheme: light)">'
    '<meta name="theme-color" content="#0f1115" media="(prefers-color-scheme: dark)">'
    '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Bestpreis">'
    '<meta name="description" content="Zugverbindungen nach Zeit, Geld und Risiko vergleichen – mit Deutschland-Ticket-Kombis und Risiko-Ampel.">'
    '</head><body>\n'
    + body + "\n</body></html>\n")
print("ok", len(body) // 1024, "KB")

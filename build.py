#!/usr/bin/env python3
"""Baut aus app.html + stations.json die Artifact-Version (artifact.html), die Standalone-Seite (index.html)
und Version 2 (v2/index.html: gleiche Suchmaschine, eigenes Stylesheet v2.css und Einstieg v2-intro.html)."""
import re
from pathlib import Path
here = Path(__file__).parent
app = (here / "app.html").read_text()
stations = (here / "stations.json").read_text()
assert "/*STATIONS*/[]" in app
body = app.replace("/*STATIONS*/[]", stations)
(here / "artifact.html").write_text(body)

def page(body, root=""):
    return ('<!doctype html>\n<html lang="de"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        f'<link rel="manifest" href="{root}manifest.webmanifest"><link rel="apple-touch-icon" href="{root}icon-180.png">'
        '<meta name="theme-color" content="#faf6f3" media="(prefers-color-scheme: light)">'
        '<meta name="theme-color" content="#1b1614" media="(prefers-color-scheme: dark)">'
        '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Bestpreis">'
        '<meta name="description" content="Zugverbindungen nach Zeit, Geld und Risiko vergleichen – mit Deutschland-Ticket-Kombis und Risiko-Ampel.">'
        '</head><body>\n' + body + "\n</body></html>\n")

(here / "index.html").write_text(page(body))

# ---- Version 2: „Die Fahrkarte“ ----
v2 = body
v2 = re.sub(r"<style>.*?</style>(\s*</style>)?", lambda m: "<style>\n" + (here / "v2-fonts.css").read_text() + (here / "v2.css").read_text() + "\n</style>", v2, count=1, flags=re.S)
v2 = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", v2)                       # Inter raus, v2 bringt eigene Schriften mit (v2/fonts)
v2 = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*', "", v2)
v2 = v2.replace('<div class="ds">', '<div class="ds" data-v="2">', 1)
v2 = v2.replace("</header>", "</header>\n" + (here / "v2-intro.html").read_text(), 1)
for a, b in [('fetch("punct.json"', 'fetch("../punct.json"'), ('register("sw.js")', 'register("../sw.js")')]:
    assert a in v2, a
    v2 = v2.replace(a, b)
v2 = v2.replace('<meta name="theme-color" content="#faf6f3"', '<meta name="theme-color" content="#e6ece7"')
(here / "v2").mkdir(exist_ok=True)
(here / "v2" / "index.html").write_text(page(v2, "../").replace('content="#faf6f3"', 'content="#e6ece7"').replace('content="#1b1614"', 'content="#0d1210"'))
print("ok", len(body) // 1024, "KB · v2", len(v2) // 1024, "KB")

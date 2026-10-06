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
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>\n'
    + body + "\n</body></html>\n")
print("ok", len(body) // 1024, "KB")

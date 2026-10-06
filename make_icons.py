#!/usr/bin/env python3
"""Zeichnet die App-Icons (PNG) ohne Zusatzbibliotheken: dunkle Fläche, Fahrlinie mit Start- und Zielpunkt."""
import struct, zlib
from pathlib import Path

BG, FG, AC = (118, 30, 42), (250, 244, 240), (240, 190, 184)


def color(x, y):
    # Linie zwischen den Punkten
    if 0.30 <= x <= 0.70 and abs(y - 0.5) <= 0.022:
        return FG
    for cx, col in ((0.28, FG), (0.72, AC)):
        d = ((x - cx) ** 2 + (y - 0.5) ** 2) ** 0.5
        if 0.042 <= d <= 0.078:
            return col
    return BG


def png(size, path, ss=3):
    rows = []
    for py in range(size):
        row = bytearray([0])
        for px in range(size):
            acc = [0, 0, 0]
            for sy in range(ss):
                for sx in range(ss):
                    c = color((px + (sx + .5) / ss) / size, (py + (sy + .5) / ss) / size)
                    acc = [a + b for a, b in zip(acc, c)]
            row += bytes(round(a / ss / ss) for a in acc)
        rows.append(bytes(row))
    raw = zlib.compress(b"".join(rows), 9)
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
                           + chunk(b"IDAT", raw) + chunk(b"IEND", b""))


here = Path(__file__).parent
for s in (180, 192, 512):
    png(s, here / f"icon-{s}.png")
print("ok")

"""News image: Tuesday 17 November 2026, the world in one picture.

Title: "Tuesday 17 November 2026 - Bridges Burning, Winter in Gaza"

Drawn entirely in code, Python standard library only (math, struct,
zlib, pathlib). No PIL, no network, no external files, no random
numbers, no clock. A newspaper front page: masthead with the date,
one big lead story, four illustrated stories, and a ticker.

Stories, all reported on 17 November 2026:
  1. LEAD - Ukraine hits the Kerch Bridge a 2nd day; part of the
     bridge collapses. Zelenskyy calls it an "unprecedented
     operation". Russia hits Kyiv's North and South bridges.
  2. Iran fires a drone at a US radar site in Bahrain; Bahrain
     intercepts it, no casualties. A tanker hits a mine near
     Hormuz; a 3rd US carrier reaches the Middle East.
  3. Gaza winter emergency: 1.7m still displaced, ~1.4m face acute
     hunger; storms flood 70,000 tents. UK, Australia, Canada and
     Italy press Israel to open aid crossings.
  4. China confirms Xi, Trump and Putin meet 19 Nov in Shenzhen
     at the APEC summit; Xi and Canada's PM Carney agree tariff cuts.
  5. Pentagon fails its financial audit for a 9th straight year;
     auditors cannot verify accounts covering $4.8 trillion.
Ticker: Japan scrambles jets over Russian planes; Depardieu pleads
guilty in Paris; Houthis advance in Yemen.

Deterministic: every coordinate and colour is a fixed constant.
Two runs produce byte-identical output.
Usage: python3 main.py  ->  writes /output/entry.png (1024x1024)
"""

import math
import struct
import zlib
from pathlib import Path

W = 1024
H = 1024
OUT = Path("/output/entry.png")

NAVY = (14, 27, 51)
NAVY2 = (9, 17, 34)
INK = (18, 22, 32)
PAPER = (250, 246, 236)
WHITE = (255, 255, 255)
GOLD = (242, 193, 78)
RED = (210, 36, 58)
GREY = (118, 126, 140)
SKY = (28, 44, 78)
SKY2 = (58, 74, 112)
SEA = (24, 58, 92)
SEA2 = (16, 40, 66)
ORANGE = (255, 138, 38)
YELLOW = (255, 210, 88)
STEEL = (150, 158, 172)
DARK = (32, 38, 52)
TENT = (226, 214, 188)
TENT2 = (198, 178, 138)
RAIN = (150, 190, 230)
GREEN = (28, 110, 70)
FLAG_R = (206, 32, 40)
FLAG_B = (30, 70, 160)

FONT = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".####", "#....", "#....", "#....", "#....", "#....", ".####"],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".####", "#....", "#....", "#.###", "#...#", "#...#", ".###."],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "J": ["..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", "#...#", ".#.#.", "..#..", "..#..", "..#.."],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    "0": [".###.", "#..##", "#.#.#", "##..#", "#...#", "#...#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "2": [".###.", "#...#", "....#", "..##.", ".#...", "#....", "#####"],
    "3": ["####.", "....#", "....#", ".###.", "....#", "....#", "####."],
    "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": [".###.", "#....", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", "..#..", "..#..", "..#.."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "9": [".###.", "#...#", "#...#", ".####", "....#", "....#", ".###."],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
    ".": [".....", ".....", ".....", ".....", ".....", ".##..", ".##.."],
    ",": [".....", ".....", ".....", ".....", ".....", ".##..", ".#..."],
    ":": [".....", ".##..", ".....", ".....", ".....", ".##..", "....."],
    "-": [".....", ".....", ".....", "#####", ".....", ".....", "....."],
    "/": ["....#", "...#.", "...#.", "..#..", ".#...", ".#...", "#...."],
    "(": ["...#.", "..#..", ".#...", ".#...", ".#...", "..#..", "...#."],
    ")": [".#...", "..#..", "...#.", "...#.", "...#.", "..#..", ".#..."],
    "%": ["#...#", "#..#.", "...#.", "..#..", ".#...", "#..#.", "#...#"],
    "!": ["..#..", "..#..", "..#..", "..#..", "..#..", ".....", "..#.."],
    "?": [".###.", "#...#", "....#", "..##.", "..#..", ".....", "..#.."],
    "&": [".##..", "#..#.", "#.#..", ".#...", "#.#.#", "#..#.", ".##.#"],
    "*": [".....", ".#.#.", "..#..", "#####", "..#..", ".#.#.", "....."],
    "'": ["..#..", "..#..", ".....", ".....", ".....", ".....", "....."],
    "+": [".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."],
    "=": [".....", ".....", "#####", ".....", "#####", ".....", "....."],
    "$": ["..#..", ".####", "#.#.#", ".###.", "..#.#", "####.", "..#.."],
}


def chunk(typ, data):
    out = struct.pack(">I", len(data)) + typ + data
    return out + struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)


def write_png(path, w, h, rgb):
    raw = bytearray()
    stride = w * 3
    for y in range(h):
        raw.append(0)
        raw += rgb[y * stride:(y + 1) * stride]
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
           + chunk(b"IEND", b""))
    Path(path).write_bytes(png)


class Canvas:
    def __init__(self, w, h, colour):
        self.w = w
        self.h = h
        self.px = bytearray(colour * w * h)

    def rect(self, x0, y0, x1, y1, colour):
        x0, y0, x1, y1 = (int(round(v)) for v in (x0, y0, x1, y1))
        x0 = max(0, x0); y0 = max(0, y0)
        x1 = min(self.w - 1, x1); y1 = min(self.h - 1, y1)
        for y in range(y0, y1 + 1):
            i = (y * self.w + x0) * 3
            self.px[i:(y * self.w + x1 + 1) * 3] = bytes(colour) * (x1 - x0 + 1)

    def circle(self, cx, cy, r, colour):
        cx, cy, r = int(round(cx)), int(round(cy)), int(round(r))
        for dy in range(-r, r + 1):
            dx = math.isqrt(max(0, r * r - dy * dy))
            self.rect(cx - dx, cy + dy, cx + dx, cy + dy, colour)

    def line(self, x0, y0, x1, y1, wd, colour):
        steps = max(abs(int(x1) - int(x0)), abs(int(y1) - int(y0)), 1)
        for s in range(steps + 1):
            t = s / steps
            self.circle(round(x0 + (x1 - x0) * t),
                        round(y0 + (y1 - y0) * t), wd // 2, colour)

    def poly(self, pts, colour):
        pts = [(int(round(x)), int(round(y))) for x, y in pts]
        ys = [p[1] for p in pts]
        for y in range(max(0, min(ys)), min(self.h - 1, max(ys)) + 1):
            xs = []
            for i in range(len(pts)):
                x0, y0 = pts[i]
                x1, y1 = pts[(i + 1) % len(pts)]
                if (y0 <= y < y1) or (y1 <= y < y0):
                    xs.append(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
            xs.sort()
            for j in range(0, len(xs) - 1, 2):
                self.rect(int(math.ceil(xs[j])), y,
                          int(math.floor(xs[j + 1])), y, colour)

    def text(self, s, x, y, scale, colour):
        cx = x
        for ch in s:
            g = FONT[ch]
            for row in range(7):
                for col in range(5):
                    if g[row][col] == "#":
                        self.rect(cx + col * scale, y + row * scale,
                                  cx + (col + 1) * scale - 1,
                                  y + (row + 1) * scale - 1, colour)
            cx += 6 * scale

    def twidth(self, s, scale):
        return len(s) * 6 * scale - scale

    def centred(self, s, cx, y, scale, colour):
        self.text(s, cx - self.twidth(s, scale) // 2, y, scale, colour)


def centred_lines(c, lines, cx, y, scale, colour, gap=6):
    for ln in lines:
        c.centred(ln, cx, y, scale, colour)
        y += 7 * scale + gap
    return y


def drone(c, cx, cy, s):
    c.rect(cx - 12, cy - 7, cx + 12, cy + 7, STEEL)
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        c.line(cx, cy, cx + dx * 26, cy + dy * 16, 3, DARK)
        c.circle(cx + dx * 28, cy + dy * 18, 5, DARK)
    c.circle(cx, cy + 8, 3, RED)


def burst(c, cx, cy, r):
    for k in range(8):
        a = math.radians(k * 45.0)
        c.line(cx, cy, round(cx + r * 1.6 * math.cos(a)),
               round(cy + r * 1.6 * math.sin(a)), 4, ORANGE)
    c.circle(cx, cy, r, ORANGE)
    c.circle(cx, cy, r * 2 // 3, YELLOW)


def masthead(c):
    c.rect(0, 0, W - 1, 109, NAVY)
    c.centred("TUESDAY 17 NOVEMBER 2026", W // 2, 14, 6, WHITE)
    c.centred("THE WORLD IN ONE PICTURE", W // 2, 64, 4, GOLD)
    c.rect(0, 106, W - 1, 109, RED)


def lead(c):
    y0, y1 = 110, 491
    for y in range(y0, y1 + 1):
        t = (y - y0) / (y1 - y0)
        col = tuple(round(SKY[i] + (SKY2[i] - SKY[i]) * t) for i in range(3))
        c.rect(0, y, W - 1, y, col)
    for (x, y) in ((70, 240), (200, 225), (880, 230), (960, 250), (540, 225)):
        c.circle(x, y, 2, WHITE)
    centred_lines(c, ["KERCH BRIDGE HIT AGAIN", "DAY 2: SPAN DOWN"],
                  W // 2, 122, 5, WHITE, gap=8)
    # Bridge deck across the strait, with a collapsed middle span.
    c.rect(0, 392, 420, 404, STEEL)
    c.rect(600, 392, W - 1, 404, STEEL)
    c.line(420, 392, 480, 452, 12, STEEL)
    c.line(600, 392, 540, 452, 12, STEEL)
    for x in (120, 300, 720, 900):
        c.rect(x, 330, x + 14, 392, STEEL)
        c.line(x + 7, 330, x + 7, 392, 4, WHITE)
    # Explosion where the span fell.
    burst(c, 510, 400, 26)
    burst(c, 470, 430, 14)
    # Drones above the bridge.
    for (x, y) in ((180, 300), (340, 280), (660, 285), (820, 300), (510, 260)):
        drone(c, x, y, 1)
    # Sea below.
    c.rect(0, 452, W - 1, 452, SEA2)
    for x in range(0, W, 46):
        c.rect(x, 462, x + 26, 465, SEA)
    c.rect(0, 452, W - 1, y1, NAVY2)
    c.rect(0, 452, W - 1, 452, SEA2)
    c.centred("UKRAINE STRIKES CRIMEA LINK - RUSSIA HITS KYIV BRIDGES",
              W // 2, 464, 3, GOLD)


def mid_left(c):
    x0, x1, y0, y1 = 0, 509, 492, 743
    c.rect(x0, y0, x1, y1, PAPER)
    centred_lines(c, ["IRAN DRONE AT", "US RADAR, BAHRAIN"],
                  (x0 + x1) // 2, 500, 4, INK, gap=6)
    # Dusk sky and sea, radar dome on the shore.
    for y in range(566, 640):
        t = (y - 566) / 74.0
        col = tuple(round((96, 130, 168)[i] + ((38, 84, 120)[i] - (96, 130, 168)[i]) * t) for i in range(3))
        c.rect(x0, y, x1, y, col)
    c.rect(x0, 640, x1, 700, SEA2)
    c.rect(60, 620, 150, 640, DARK)
    c.circle(105, 620, 34, WHITE)
    c.circle(105, 620, 30, STEEL)
    c.line(105, 620, 132, 592, 4, RED)
    drone(c, 330, 590, 1)
    c.line(317, 577, 343, 603, 5, RED)
    c.line(343, 577, 317, 603, 5, RED)
    burst(c, 430, 600, 12)
    c.rect(x0, 700, x1, y1, NAVY2)
    c.centred("SHOT DOWN - NO CASUALTIES", (x0 + x1) // 2, 712, 2, GOLD)
    c.centred("TANKER MINED NEAR HORMUZ", (x0 + x1) // 2, 728, 2, GOLD)


def mid_right(c):
    x0, x1, y0, y1 = 514, 1023, 492, 743
    c.rect(x0, y0, x1, y1, (232, 238, 244))
    centred_lines(c, ["GAZA WINTER EMERGENCY", "70,000 TENTS FLOODED"],
                  (x0 + x1) // 2, 500, 4, INK, gap=6)
    # Storm clouds and rain over a tent camp.
    c.circle(600, 600, 34, GREY)
    c.circle(650, 592, 40, (90, 100, 114))
    c.circle(710, 602, 32, GREY)
    for x in range(540, 1010, 36):
        c.line(x, 640, x - 10, 668, 3, RAIN)
    # Tents, one leaning in flood water.
    for i, tx in enumerate((560, 680, 800, 910)):
        col = TENT if i % 2 == 0 else TENT2
        c.poly([(tx, 700), (tx + 45, 668), (tx + 90, 700)], col)
        c.rect(tx + 8, 700, tx + 82, 706, DARK)
    c.rect(x0, 706, x1, 712, (70, 110, 150))
    c.rect(x0, 712, x1, y1, NAVY2)
    c.centred("1.7M DISPLACED - 1.4M FACE HUNGER",
              (x0 + x1) // 2, 720, 2, GOLD)


def bottom_left(c):
    x0, x1, y0, y1 = 0, 509, 747, 983
    c.rect(x0, y0, x1, y1, PAPER)
    centred_lines(c, ["XI, TRUMP, PUTIN", "TO MEET IN SHENZHEN"],
                  (x0 + x1) // 2, 755, 4, INK, gap=6)
    # Skyline of Shenzhen behind a summit table.
    for i, (bx, bh) in enumerate(((30, 28), (90, 42), (160, 34), (230, 45),
                                  (300, 30), (370, 40), (430, 26))):
        c.rect(bx, 880 - bh, bx + 46, 880, STEEL if i % 2 else DARK)
    c.rect(x0, 880, x1, 890, RED)
    # Three flags on the table: China, USA, Russia.
    for i, (fx, cols) in enumerate(((90, (FLAG_R, YELLOW)), (210, (FLAG_R, WHITE)),
                                    (330, (WHITE, FLAG_B)))):
        c.rect(fx, 830, fx + 70, 880, cols[0] if i != 2 else WHITE)
        if i == 0:
            c.rect(fx, 830, fx + 70, 846, FLAG_R)
            c.circle(fx + 16, 846, 6, YELLOW)
        elif i == 1:
            for k in range(4):
                c.rect(fx, 830 + k * 12, fx + 70, 830 + k * 12 + 6, WHITE if k % 2 else FLAG_R)
            c.rect(fx, 830, fx + 28, 854, FLAG_B)
        else:
            c.rect(fx, 830, fx + 70, 846, WHITE)
            c.rect(fx, 846, fx + 70, 862, FLAG_B)
            c.rect(fx, 862, fx + 70, 880, FLAG_R)
    c.rect(x0, 890, x1, y1, NAVY2)
    c.centred("19 NOV AT APEC", (x0 + x1) // 2, 900, 2, GOLD)
    c.centred("XI, CARNEY AGREE TARIFF CUTS", (x0 + x1) // 2, 916, 2, GOLD)


def bottom_right(c):
    x0, x1, y0, y1 = 514, 1023, 747, 983
    c.rect(x0, y0, x1, y1, (24, 36, 54))
    centred_lines(c, ["PENTAGON FAILS AUDIT", "FOR 9TH YEAR IN A ROW"],
                  (x0 + x1) // 2, 755, 4, WHITE, gap=6)
    # Pentagon building outline with a big red X over the accounts.
    cx, cy = 768, 880
    pts = []
    for k in range(5):
        a = math.radians(-90 + k * 72)
        pts.append((cx + 78 * math.cos(a), cy + 78 * math.sin(a)))
    c.poly(pts, (60, 80, 110))
    pts2 = []
    for k in range(5):
        a = math.radians(-90 + k * 72)
        pts2.append((cx + 34 * math.cos(a), cy + 34 * math.sin(a)))
    c.poly(pts2, NAVY2)
    c.line(cx - 52, cy - 52, cx + 52, cy + 52, 10, RED)
    c.line(cx + 52, cy - 52, cx - 52, cy + 52, 10, RED)
    c.rect(x0, 950, x1, y1, NAVY2)
    c.centred("AUDITORS CANNOT VERIFY $4.8 TRILLION",
              (x0 + x1) // 2, 958, 2, GOLD)


def footer(c):
    c.rect(0, 984, W - 1, H - 1, NAVY2)
    c.centred("ALSO: JAPAN SCRAMBLES JETS * DEPARDIEU GUILTY * HOUTHIS ADVANCE",
              W // 2, 995, 2, GOLD)


def main():
    c = Canvas(W, H, WHITE)
    masthead(c)
    lead(c)
    mid_left(c)
    mid_right(c)
    bottom_left(c)
    bottom_right(c)
    footer(c)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    write_png(OUT, W, H, c.px)


if __name__ == "__main__":
    main()

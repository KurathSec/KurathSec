#!/usr/bin/env python3
"""Draw the 88x31 buttons as GIFs and the blinking cursor as an SVG.

Standard library only: python3 tools/build_assets.py

Each button lists its two lines of text and its colours in BUTTONS below. Text
is a 5x7 bitmap font and fits 13 characters per line.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

FONT = {
    "A": "01110 10001 10001 11111 10001 10001 10001",
    "B": "11110 10001 10001 11110 10001 10001 11110",
    "C": "01110 10001 10000 10000 10000 10001 01110",
    "D": "11110 10001 10001 10001 10001 10001 11110",
    "E": "11111 10000 10000 11110 10000 10000 11111",
    "F": "11111 10000 10000 11110 10000 10000 10000",
    "G": "01110 10001 10000 10111 10001 10001 01111",
    "H": "10001 10001 10001 11111 10001 10001 10001",
    "I": "01110 00100 00100 00100 00100 00100 01110",
    "J": "00111 00010 00010 00010 00010 10010 01100",
    "K": "10001 10010 10100 11000 10100 10010 10001",
    "L": "10000 10000 10000 10000 10000 10000 11111",
    "M": "10001 11011 10101 10101 10001 10001 10001",
    "N": "10001 11001 10101 10011 10001 10001 10001",
    "O": "01110 10001 10001 10001 10001 10001 01110",
    "P": "11110 10001 10001 11110 10000 10000 10000",
    "Q": "01110 10001 10001 10001 10101 10010 01101",
    "R": "11110 10001 10001 11110 10100 10010 10001",
    "S": "01111 10000 10000 01110 00001 00001 11110",
    "T": "11111 00100 00100 00100 00100 00100 00100",
    "U": "10001 10001 10001 10001 10001 10001 01110",
    "V": "10001 10001 10001 10001 10001 01010 00100",
    "W": "10001 10001 10001 10101 10101 11011 10001",
    "X": "10001 10001 01010 00100 01010 10001 10001",
    "Y": "10001 10001 01010 00100 00100 00100 00100",
    "Z": "11111 00001 00010 00100 01000 10000 11111",
    "0": "01110 10001 10011 10101 11001 10001 01110",
    "1": "00100 01100 00100 00100 00100 00100 01110",
    "2": "01110 10001 00001 00010 00100 01000 11111",
    "3": "11111 00010 00100 00010 00001 10001 01110",
    "4": "00010 00110 01010 10010 11111 00010 00010",
    "5": "11111 10000 11110 00001 00001 10001 01110",
    "6": "00110 01000 10000 11110 10001 10001 01110",
    "7": "11111 00001 00010 00100 01000 01000 01000",
    "8": "01110 10001 10001 01110 10001 10001 01110",
    "9": "01110 10001 10001 01111 00001 00010 01100",
    "-": "00000 00000 00000 11111 00000 00000 00000",
    ">": "01000 00100 00010 00001 00010 00100 01000",
    "+": "00000 00100 00100 11111 00100 00100 00000",
    ".": "00000 00000 00000 00000 00000 01100 01100",
    " ": "00000 00000 00000 00000 00000 00000 00000",
}

BLACK, WHITE, SILVER, GREY = (0, 0, 0), (255, 255, 255), (192, 192, 192), (128, 128, 128)
GREEN, YELLOW = (0, 255, 0), (255, 255, 0)
NAVY, MAROON, TEAL, PURPLE, OLIVE = (0, 0, 128), (128, 0, 0), (0, 128, 128), (128, 0, 128), (128, 128, 0)

BUTTONS = {
    "gm-recomp": ("GM-RECOMP", "X86 -> WASM", BLACK, GREEN),
    "fangame-archive": ("FANGAME", "ARCHIVE", NAVY, WHITE),
    "spaghetti-architect": ("SPAGHETTI", "ARCHITECT", MAROON, YELLOW),
    "codecaliper": ("CODECALIPER", "PY JAVA GO", TEAL, WHITE),
    "limen": ("LIMEN", "NOISE FLOOR", PURPLE, WHITE),
    "cupel": ("CUPEL", "FIPS 203+204", OLIVE, WHITE),
    "merged-openssl": ("MERGED IN", "OPENSSL", SILVER, BLACK),
    "merged-botan": ("MERGED IN", "BOTAN", SILVER, BLACK),
    "merged-circl": ("MERGED IN", "CIRCL", SILVER, BLACK),
    "merged-pmd": ("MERGED IN", "PMD", SILVER, BLACK),
    "arxiv": ("ARXIV", "2607.18642", WHITE, MAROON),
    "view-source": ("VIEW", "SOURCE", BLACK, WHITE),
}


def lzw(pixels, min_code_size):
    """GIF-flavoured LZW over palette indices, packed LSB first."""
    clear, end = 1 << min_code_size, (1 << min_code_size) + 1
    table = {(i,): i for i in range(clear)}
    next_code, width = end + 1, min_code_size + 1
    out, buffer, bits = bytearray(), 0, 0

    def emit(code):
        nonlocal buffer, bits
        buffer |= code << bits
        bits += width
        while bits >= 8:
            out.append(buffer & 255)
            buffer >>= 8
            bits -= 8

    emit(clear)
    current = ()
    for pixel in pixels:
        candidate = current + (pixel,)
        if candidate in table:
            current = candidate
            continue
        emit(table[current])
        if next_code == 4096:
            emit(clear)
            table = {(i,): i for i in range(clear)}
            next_code, width = end + 1, min_code_size + 1
        else:
            table[candidate] = next_code
            next_code += 1
            if next_code > (1 << width) and width < 12:
                width += 1
        current = (pixel,)
    emit(table[current])
    emit(end)
    if bits:
        out.append(buffer & 255)
    return bytes(out)


def gif(path, width, height, palette, frames, delay=0, transparent=None):
    """Write frames (lists of palette indices) as a GIF. Several frames loop forever."""
    palette = list(palette) + [BLACK] * (2 - len(palette))
    size_bits = 1
    while (1 << size_bits) < len(palette):
        size_bits += 1
    palette += [BLACK] * ((1 << size_bits) - len(palette))
    data = bytearray(b"GIF89a")
    data += width.to_bytes(2, "little") + height.to_bytes(2, "little")
    data += bytes([0x80 | 0x70 | (size_bits - 1), 0, 0])
    for colour in palette:
        data += bytes(colour)
    if len(frames) > 1:
        data += b"\x21\xff\x0bNETSCAPE2.0\x03\x01\x00\x00\x00"
    min_code_size = max(size_bits, 2)
    for frame in frames:
        flags = 1 if transparent is not None else 0
        if transparent is not None:
            flags |= 2 << 2
        data += bytes([0x21, 0xF9, 4, flags]) + delay.to_bytes(2, "little")
        data += bytes([transparent or 0, 0])
        data += b"\x2c" + bytes(4) + width.to_bytes(2, "little") + height.to_bytes(2, "little") + b"\x00"
        data += bytes([min_code_size])
        encoded = lzw(frame, min_code_size)
        for start in range(0, len(encoded), 255):
            chunk = encoded[start:start + 255]
            data += bytes([len(chunk)]) + chunk
        data += b"\x00"
    data += b"\x3b"
    path.write_bytes(bytes(data))


def button(name, first, second, field, ink):
    width, height = 88, 31
    palette = []

    def index(colour):
        if colour not in palette:
            palette.append(colour)
        return palette.index(colour)

    pixels = [index(SILVER)] * (width * height)

    def put(x, y, colour):
        pixels[y * width + x] = index(colour)

    # Raised outer edge, sunken inner edge, the classic two-pixel bevel.
    for x in range(width):
        put(x, 0, WHITE)
        put(x, height - 1, BLACK)
    for y in range(height):
        put(0, y, WHITE)
        put(width - 1, y, BLACK)
    for x in range(2, width - 2):
        put(x, 2, GREY)
        put(x, height - 3, WHITE)
    for y in range(2, height - 2):
        put(2, y, GREY)
        put(width - 3, y, WHITE)
    for y in range(3, height - 3):
        for x in range(3, width - 3):
            put(x, y, field)

    for text, top in ((first, 7), (second, 17)):
        assert len(text) <= 13, text
        x = (width - (len(text) * 6 - 1)) // 2
        for ch in text:
            for row, bits in enumerate(FONT[ch].split()):
                for col, bit in enumerate(bits):
                    if bit == "1":
                        put(x + col, top + row, ink)
            x += 6
    gif(OUT / f"{name}.gif", width, height, palette, [pixels])


def cursor():
    # An SVG, because GitHub wraps every GIF in a player element that lifts it off the text line.
    (OUT / "cursor.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 7 11">'
        "<style>@media (prefers-reduced-motion:no-preference){rect{animation:blink 1.06s steps(1) infinite}}"
        "@keyframes blink{50%{opacity:0}}</style>"
        '<rect width="7" height="11" fill="#3FB950"/></svg>\n'
    )


def main():
    OUT.mkdir(exist_ok=True)
    for name, (first, second, field, ink) in BUTTONS.items():
        button(name, first, second, field, ink)
    cursor()


if __name__ == "__main__":
    main()

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Find all emoji in the HTML body (rough check)
import unicodedata

emoji_chars = []
for i, ch in enumerate(html):
    cp = ord(ch)
    # Common emoji ranges
    if (0x1F300 <= cp <= 0x1FFFF) or (0x2600 <= cp <= 0x27BF) or (0xFE00 <= cp <= 0xFE0F):
        ctx = html[max(0,i-80):i+80]
        emoji_chars.append((i, ch, ctx))

out = []
for pos, ch, ctx in emoji_chars[:40]:
    out.append(f"POS {pos}: {repr(ch)} ({hex(ord(ch))})\n  ...{ctx}...\n")

open('emoji_report.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(f"Found {len(emoji_chars)} emoji characters. Report saved.")

# 2. Find service-img-placeholder divs
placeholders = [(m.start(), html[m.start():m.start()+200]) for m in re.finditer(r'service-img-placeholder', html)]
open('placeholder_report.txt', 'w', encoding='utf-8').write('\n\n---\n\n'.join([f"POS {p[0]}:\n{p[1]}" for p in placeholders]))
print(f"Found {len(placeholders)} service-img-placeholder divs")

# 3. Find ventaja-icon divs
ventaja_icons = [(m.start(), html[m.start():m.start()+200]) for m in re.finditer(r'ventaja-icon', html)]
open('ventaja_report.txt', 'w', encoding='utf-8').write('\n\n---\n\n'.join([f"POS {p[0]}:\n{p[1]}" for p in ventaja_icons]))
print(f"Found {len(ventaja_icons)} ventaja-icon elements")

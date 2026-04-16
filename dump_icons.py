import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find every service-card and extract its service-icon + h3
pattern = r'<div class="service-(?:icon|body)"[^>]*>(.*?)</div>\s*(?:<h3[^>]*>([^<]+)</h3>)?'
chunks = []
pos = 0
for m in re.finditer(r'class="service-icon"', html):
    start = m.start()
    # get surrounding context to identify the card
    context = html[max(0, start):start+600]
    chunks.append(f"POS {start}:\n{context}\n===")

open('service_icon_dump.txt', 'w', encoding='utf-8').write('\n'.join(chunks))
print(f"Found {len(chunks)} service-icon occurrences")

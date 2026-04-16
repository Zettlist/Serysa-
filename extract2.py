with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

# Find certif section
i = h.find('certif-grid')
open('certif_chunk.txt','w',encoding='utf-8').write(h[max(0,i-100):i+3000])

# Find zonas/cobertura section
i2 = h.find('zona-ico')
open('zona_chunk.txt','w',encoding='utf-8').write(h[max(0,i2-300):i2+2000])

# Find service cards with placeholders
import re
# match service-img block and next 300 chars
matches = list(re.finditer(r'class="service-img"', h))
out = []
for m in matches:
    out.append(f"POS {m.start()}:\n{h[m.start():m.start()+400]}\n---")
open('service_imgs.txt','w',encoding='utf-8').write('\n'.join(out))

print(f"certif pos: {h.find('certif-grid')}")
print(f"zona pos: {i2}")
print(f"service imgs: {len(matches)}")

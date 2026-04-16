import re

with open('index.html','r',encoding='utf-8') as f:
    h = f.read()

# Find certif section in BODY (after CSS ends around 40000)
i = h.find('certif-grid', 40000)
open('certif_body.txt','w',encoding='utf-8').write(h[i:i+3500])

# Find zona section in BODY
j = h.find('zonas-grid')
open('zona_body.txt','w',encoding='utf-8').write(h[j:j+3000])

# Find all service-img divs
pattern = 'class="service-img"'
positions = [m.start() for m in re.finditer(re.escape(pattern), h)]
chunks = []
for pos in positions:
    chunks.append(f'POS {pos}:\n{h[pos:pos+300]}')
open('svc_imgs.txt','w',encoding='utf-8').write('\n---\n'.join(chunks))

print(f"certif at {i}, zona at {j}, service-imgs: {len(positions)}")

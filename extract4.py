with open('index.html','r',encoding='utf-8') as f:
    h=f.read()

# find certif section in HTML body
pattern1 = 'class="certif-grid"'
i = h.find(pattern1)
open('certif_body2.txt','w',encoding='utf-8').write(h[i:i+3000])

# find zonas section in body
pattern2 = 'class="zonas-grid"'
j = h.find(pattern2)
open('zona_body2.txt','w',encoding='utf-8').write(h[j:j+2000])

print(i,j)

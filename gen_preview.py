import glob
import os

images = glob.glob('*.[jp][pn]*g')
html = "<html><body>"
for img in images:
    html += f'<h3>{img}</h3><img src="{img}" style="max-width: 400px; border: 1px solid red;"><br><br>'
html += "</body></html>"

with open('images_preview.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Created images_preview.html")

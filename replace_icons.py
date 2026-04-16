import re
import os

replacements = {
    '🪳': '<img src="icons/rastreros.png" class="icon-img" alt="Rastreros">',
    '🪰': '<img src="icons/voladores.png" class="icon-img" alt="Voladores">',
    '🐀': '<img src="icons/roedores.png" class="icon-img" alt="Roedores">',
    '🪵': '<img src="icons/termitas.png" class="icon-img" alt="Termitas">',
    '🛏️': '<img src="icons/chinches.png" class="icon-img" alt="Chinches">',
    '🐦': '<img src="icons/fauna.png" class="icon-img" alt="Fauna">',
    '✔️': '<img src="icons/escudo.png" class="icon-img-sm" alt="Check">',
    '✅': '<img src="icons/escudo.png" class="icon-img-sm" alt="Check">',
    '🛡️': '<img src="icons/escudo.png" class="icon-img" alt="Garantía">',
    '📜': '<img src="icons/licencia.png" class="icon-img" alt="Licencia">',
    '🏆': '<img src="icons/licencia.png" class="icon-img" alt="Premio">',
}

# Also add some CSS to handle these images
custom_css = """
<style>
  .icon-img { width: 44px; height: 44px; object-fit: contain; vertical-align: middle; }
  .icon-img-sm { width: 18px; height: 18px; object-fit: contain; vertical-align: middle; margin-right: 8px; }
  .cotiz-opt-ico .icon-img { width: 48px; height: 48px; }
  .service-icon .icon-img { width: 40px; height: 40px; }
  .poliza-feat .icon-img-sm { margin-top: 2px; }
</style>
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for emoji, img_tag in replacements.items():
        content = content.replace(emoji, img_tag)
    
    if '</head>' in content and '.icon-img' not in content:
        content = content.replace('</head>', custom_css + '</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html
update_file('index.html')

# Update build_pages.py to use images instead of emojis in its strings
with open('build_pages.py', 'r', encoding='utf-8') as f:
    py_content = f.read()

for emoji, img_tag in replacements.items():
    # Escape quotes if needed, but here we use simple replace since emojis are unique
    py_content = py_content.replace(emoji, img_tag)

with open('build_pages.py', 'w', encoding='utf-8') as f:
    f.write(py_content)

print("Updated index.html and build_pages.py")

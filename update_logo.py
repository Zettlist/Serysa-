import os

file_path = "index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make the logo container a bit wider to accommodate the full image clearly 
# Currently it is .logo-mark { position:relative;width:48px;height:48px; ... }
# Let's change it to 56x56
html = html.replace('width:48px;height:48px;', 'width:56px;height:56px;')

# Replace the markup
old_logo = '''<div class="logo-mark">
        <div class="logo-diamond"></div>
        <span class="logo-s">S</span>
      </div>'''

new_logo = '''<div class="logo-mark">
        <img src="logo_transparent.png" alt="SERYSA" style="width:100%; height:100%; object-fit:contain; filter:drop-shadow(0 2px 4px rgba(0,0,0,0.2));">
      </div>'''

html = html.replace(old_logo, new_logo)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated logo in index.html")

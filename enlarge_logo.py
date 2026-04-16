import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Increase the logo-mark CSS width from 56px to 80px
    data = data.replace('width:56px;height:56px;', 'width:80px;height:80px;')
    
    # Increase the logo gap from 14px to 18px
    data = data.replace('.logo{display:flex;align-items:center;gap:14px;}', '.logo{display:flex;align-items:center;gap:18px;}')
    
    # Increase logo-name font size
    data = data.replace('.logo-name{font-size:1.55rem;font-weight:900;letter-spacing:2px;line-height:1;}', '.logo-name{font-size:1.8rem;font-weight:900;letter-spacing:2px;line-height:1;}')

    # Increase logo-tagline font size
    data = data.replace('.logo-tagline{font-size:.58rem;color:var(--cyan-400);text-transform:uppercase;letter-spacing:.8px;margin-top:2px;}', '.logo-tagline{font-size:.65rem;color:var(--cyan-400);text-transform:uppercase;letter-spacing:.8px;margin-top:2px;}')
    
    # Update inline styles in footer
    data = data.replace('class="logo-mark" style="width:40px;height:40px;"', 'class="logo-mark" style="width:56px;height:56px;"')
    data = data.replace('class="logo-name" style="font-size:1.3rem;"', 'class="logo-name" style="font-size:1.5rem;"')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(data)

print(f"Updated logo sizes in {len(files)} HTML files.")

"""
Fix remaining 2 issues:
1. Chinche de Cama service card still has blue placeholder -> add svc_chinche.png
2. Service-icon small divs for Rastreros and Roedores are empty
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Find the Chinche service card and fix its image ──
# Look for the service card that mentions "Chinche de Cama" and has no img tag before it
# Find the service-card div that contains "Chinche de Cama"
chinche_pos = html.find('Control de Chinche de Cama')
if chinche_pos > -1:
    # Look backwards for the nearest service-img div
    img_start = html.rfind('<div class="service-img"', 0, chinche_pos)
    img_end = html.find('</div>', img_start) + len('</div>')
    
    current_img_block = html[img_start:img_end]
    print(f"Current chinche image block:\n{current_img_block[:200]}")
    
    if 'svc_chinche' not in current_img_block and '<img' not in current_img_block:
        new_img_block = '<div class="service-img"><img src="svc_chinche.png" alt="Control de Chinche de Cama" loading="lazy"></div>'
        html = html[:img_start] + new_img_block + html[img_end:]
        print("Fixed Chinche image")
    else:
        print("Chinche image already set or unexpected state")
else:
    print("Chinche de Cama card not found by title search")

# ── 2. Fix service-icon small squares for Rastreros and Roedores ──
# These cards have the small icon div below the photo. We need to find which 
# service-icon divs are empty or have bad content.

MINI_PEST_SVG = {
    'Control de Insectos Rastreros': '''<svg viewBox="0 0 64 64" fill="currentColor" width="28" height="28">
      <ellipse cx="32" cy="38" rx="11" ry="16"/><ellipse cx="32" cy="22" rx="7" ry="7"/>
      <path d="M29 17 Q22 10 16 6" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <path d="M35 17 Q42 10 48 6" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <path d="M21 28 Q12 26 8 22" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <path d="M43 28 Q52 26 56 22" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <path d="M21 36 Q10 38 6 34" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <path d="M43 36 Q54 38 58 34" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    </svg>''',
    'Control de Roedores': '''<svg viewBox="0 0 64 64" fill="currentColor" width="28" height="28">
      <ellipse cx="28" cy="38" rx="17" ry="13"/><circle cx="46" cy="28" r="10"/>
      <ellipse cx="48" cy="20" rx="5" ry="6"/><ellipse cx="48" cy="20" rx="2.5" ry="3.5" fill="white" opacity=".4"/>
      <circle cx="50" cy="26" r="2" fill="white"/><circle cx="50.6" cy="26" r="1" fill="#111"/>
      <path d="M11 44 Q4 42 4 52 Q4 58 8 58" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
    </svg>''',
}

# Find service-cards and look for their service-icon divs
# We search for the service-icon div within each card and replace empty ones
for title, mini_svg in MINI_PEST_SVG.items():
    # Find the title in the html
    t_pos = html.find(title)
    if t_pos > -1:
        # Look backwards for nearest service-icon div (within 800 chars)
        search_start = max(0, t_pos - 800)
        icon_pos = html.rfind('<div class="service-icon"', search_start, t_pos)
        if icon_pos > -1:
            icon_end = html.find('</div>', icon_pos) + len('</div>')
            current = html[icon_pos:icon_end]
            print(f"\n{title} service-icon:\n{current[:120]}")
            
            new_icon = f'<div class="service-icon" style="width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,rgba(11,21,237,.08),rgba(0,212,255,.05));display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--blue-500);">{mini_svg}</div>'
            html = html[:icon_pos] + new_icon + html[icon_end:]
            print(f"Replaced service-icon for '{title}'")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\nDone. Fixed chinche image and service icons.")

"""
Targeted fix for all 8 service-icon divs.
All will use the same style: blue gradient bg, 48x48, with a clear fill SVG icon.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

STYLE = 'width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,var(--blue-500),var(--cyan-600));display:flex;align-items:center;justify-content:center;margin-bottom:14px;flex-shrink:0;box-shadow:0 4px 16px rgba(11,21,237,.3);'
COLOR = 'white'

def icon_div(svg_body):
    return f'<div class="service-icon" style="{STYLE}">{svg_body}</div>'

# ── SVG icons (filled white, 28x28) ──────────────────────────────────────────
# Cucaracha
SVG_CUCARACHA = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><ellipse cx="32" cy="38" rx="11" ry="16"/><ellipse cx="32" cy="22" rx="7" ry="7"/><path d="M29 17 Q22 10 16 6" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M35 17 Q42 10 48 6" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M21 28 Q12 26 8 22" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M43 28 Q52 26 56 22" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M21 36 Q10 38 6 34" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M43 36 Q54 38 58 34" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>'

# Roedor
SVG_ROEDOR = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><ellipse cx="28" cy="38" rx="17" ry="13"/><circle cx="46" cy="28" r="10"/><ellipse cx="48" cy="20" rx="5" ry="6"/><circle cx="50" cy="26" r="2" fill="rgba(0,0,0,0.4)"/><path d="M11 44 Q4 42 4 52 Q4 58 8 58" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/></svg>'

# Enjambre (bee silhouette)
SVG_ENJAMBRE = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><ellipse cx="32" cy="42" rx="9" ry="12"/><path d="M23 38 Q32 36 41 38" stroke="rgba(0,0,0,0.25)" stroke-width="2.5" fill="none"/><path d="M23 44 Q32 42 41 44" stroke="rgba(0,0,0,0.25)" stroke-width="2.5" fill="none"/><ellipse cx="32" cy="28" rx="7" ry="6"/><circle cx="32" cy="17" r="7"/><path d="M28 11 Q22 6 18 4" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/><circle cx="18" cy="4" r="2.5"/><path d="M36 11 Q42 6 46 4" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/><circle cx="46" cy="4" r="2.5"/><ellipse cx="18" cy="26" rx="12" ry="6" fill="rgba(255,255,255,0.3)" transform="rotate(-10 18 26)"/><ellipse cx="46" cy="26" rx="12" ry="6" fill="rgba(255,255,255,0.3)" transform="rotate(10 46 26)"/></svg>'

# Restaurantero (fork & knife + shield)
SVG_RESTAURANTE = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><path d="M18 6 L18 28 Q18 36 26 36 L26 58" stroke="white" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M18 20 L30 20" stroke="white" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M30 6 L30 20 Q30 30 24 34" stroke="white" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M42 6 L42 58" stroke="white" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M42 6 Q52 6 52 16 Q52 26 42 26" stroke="white" stroke-width="4.5" fill="none" stroke-linecap="round"/></svg>'

# Grandes Venues (arena/stadium silhouette)
SVG_VENUES = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><ellipse cx="32" cy="26" rx="26" ry="16"/><ellipse cx="32" cy="26" rx="16" ry="8" fill="rgba(0,0,0,0.3)"/><rect x="6" y="26" width="52" height="24" rx="2"/><rect x="6" y="26" width="52" height="4" fill="rgba(0,0,0,0.2)"/><path d="M10 50 Q10 54 14 54 L50 54 Q54 54 54 50" fill="rgba(255,255,255,0.15)" stroke="none"/></svg>'

# Termitas (destructive insect with wood grain)
SVG_TERMITA = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><ellipse cx="32" cy="46" rx="12" ry="14"/><ellipse cx="32" cy="30" rx="7" ry="7"/><ellipse cx="32" cy="16" rx="9" ry="8"/><path d="M25 18 Q18 22 16 20" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M39 18 Q46 22 48 20" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M28 9 Q22 4 18 2" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M36 9 Q42 4 46 2" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M25 29 Q14 28 10 24" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M39 29 Q50 28 54 24" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'

# Aves/Murciélagos (pigeon silhouette)
SVG_AVES = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><path d="M8 26 Q20 10 34 20 Q42 14 52 20 Q48 28 34 26 Q26 36 18 38 Q12 36 10 30 Z"/><circle cx="42" cy="16" r="2.5" fill="rgba(0,0,0,0.5)"/><path d="M18 38 Q16 46 22 50" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M26 40 Q26 48 30 52" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M8 26 Q4 22 4 28 Q4 32 8 32" stroke="white" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'

# Chinche de cama (bed bug oval + bed)
SVG_CHINCHE = '<svg viewBox="0 0 64 64" fill="white" width="26" height="26"><rect x="8" y="36" width="48" height="8" rx="3"/><rect x="8" y="44" width="48" height="14" rx="2"/><rect x="6" y="32" width="52" height="6" rx="2"/><path d="M14 32 L14 22" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M50 32 L50 22" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="32" cy="26" rx="14" ry="9" fill="rgba(255,255,255,0.7)"/><circle cx="26" cy="23" r="2" fill="rgba(0,0,0,0.5)"/><circle cx="38" cy="23" r="2" fill="rgba(0,0,0,0.5)"/><path d="M22 20 Q18 16 14 14" stroke="rgba(255,255,255,0.8)" stroke-width="1.5" fill="none" stroke-linecap="round"/><path d="M42 20 Q46 16 50 14" stroke="rgba(255,255,255,0.8)" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>'

# ── Map of positions to replacement (from dump) ──────────────────────────────
FIXES = [
    # (search_string, replacement)
    
    # 1. Enjambres: emoji 🐝
    ('<div class="service-icon">🐝</div>', icon_div(SVG_ENJAMBRE)),
    
    # 2. Restaurantero: nested cotiz-opt span with P/fork SVG
    (None, None),  # will handle via regex below
    
    # 3. Grandes Venues: emoji 🏟️
    ('<div class="service-icon">🏟️</div>', icon_div(SVG_VENUES)),
    
    # 4. Termitas: thin leaf SVG
    (None, None),  # regex below
    
    # 5. Aves: thin bird SVG  
    (None, None),  # regex below
    
    # 6. Chinche: nested cotiz-opt span with grid SVG
    (None, None),  # regex below
]

import re

# Do simple string replacement for emojis
html = html.replace('<div class="service-icon">🐝</div>', icon_div(SVG_ENJAMBRE))
html = html.replace('<div class="service-icon">🏟️</div>', icon_div(SVG_VENUES))
print("Fixed: Enjambres (bee emoji), Grandes Venues (stadium emoji)")

# Fix Restaurantero — it has <div class="service-icon"><span class="cotiz-opt-ico"><svg fork>...</svg></span></div>
html = re.sub(
    r'<div class="service-icon"><span class="cotiz-opt-ico"><svg[^>]*>[\s\S]*?</svg></span></div>\s*(?=\s*<h3[^>]*>Sector Restaurantero)',
    icon_div(SVG_RESTAURANTE) + '\n          ',
    html
)
print("Fixed: Restaurantero (fork SVG)")

# Fix Termitas — it has <div class="service-icon"><svg viewBox="0 0 24 24" leaf SVG>
html = re.sub(
    r'<div class="service-icon"><svg viewBox="0 0 24 24"[^>]*>[\s\S]*?</svg></div>\s*(?=\s*<h3[^>]*>Termitas)',
    icon_div(SVG_TERMITA) + '\n          ',
    html
)
print("Fixed: Termitas (leaf SVG)")

# Fix Aves — similar thin 24x24 SVG
html = re.sub(
    r'<div class="service-icon"><svg viewBox="0 0 24 24"[^>]*>[\s\S]*?</svg></div>\s*(?=\s*<h3[^>]*>Control de Aves)',
    icon_div(SVG_AVES) + '\n          ',
    html
)
print("Fixed: Control de Aves (bird SVG)")

# Fix Chinche — has <span class="cotiz-opt-ico"> wrapper with hotel grid SVG
html = re.sub(
    r'<div class="service-icon"><span class="cotiz-opt-ico"><svg[^>]*>[\s\S]*?</svg></span></div>\s*(?=\s*<h3[^>]*>Control de Chinche)',
    icon_div(SVG_CHINCHE) + '\n          ',
    html
)
print("Fixed: Chinche de Cama (grid SVG -> bed bug)")

# Also update the two GOOD icons (Rastreros, Roedores) to use same blue bg style
# They currently use rgba(11,21,237,.08) bg — update to match
html = re.sub(
    r'<div class="service-icon" style="width:48px;height:48px;border-radius:12px;background:linear-gradient\(135deg,rgba\(11,21,237,\.08\),rgba\(0,212,255,\.05\)\);display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var\(--blue-500\);">(<svg viewBox="0 0 64 64"[^/]*//>)',
    lambda m: icon_div(m.group(1).replace('fill="currentColor"', 'fill="white"').replace('stroke="currentColor"', 'stroke="white"')),
    html
)
# Simpler: just replace the style on those two
html = html.replace(
    'width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,rgba(11,21,237,.08),rgba(0,212,255,.05));display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--blue-500);',
    STYLE + 'color:white;'
)
print("Unified style for Rastreros and Roedores icons")

# Convert currentColor to white in those icon SVGs
html = html.replace(
    'style="' + STYLE + 'color:white;"><svg viewBox="0 0 64 64" fill="currentColor"',
    'style="' + STYLE + 'color:white;"><svg viewBox="0 0 64 64" fill="white"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\n=== All 8 service icons fixed. ===")

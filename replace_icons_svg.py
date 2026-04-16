"""
Script para reemplazar TODOS los iconos (emojis + PNGs mezclados) por SVG inline
consistentes con la paleta de SERYSA (cian sobre navy).
"""

# ─── BIBLIOTECA DE SVGs ────────────────────────────────────────────────────────
# Todos usan stroke="currentColor" para ser controlables desde CSS
# Se usan en 2 tamaños: normal (48x48) y pequeño (24x24)

ICONS = {}

# Pestes
ICONS['cucaracha'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="24" cy="26" rx="9" ry="14" />
  <ellipse cx="24" cy="18" rx="5" ry="6" />
  <line x1="24" y1="12" x2="18" y2="7" /><line x1="24" y1="12" x2="30" y2="7" />
  <line x1="15" y1="20" x2="7" y2="17" /><line x1="15" y1="26" x2="6" y2="26" /><line x1="15" y1="32" x2="8" y2="36" />
  <line x1="33" y1="20" x2="41" y2="17" /><line x1="33" y1="26" x2="42" y2="26" /><line x1="33" y1="32" x2="40" y2="36" />
</svg>'''

ICONS['roedor'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="22" cy="30" rx="13" ry="10" />
  <circle cx="34" cy="20" r="7" />
  <circle cx="36" cy="18" r="1.5" fill="currentColor" />
  <line x1="34" y1="13" x2="32" y2="7" /><line x1="37" y1="13" x2="40" y2="7" />
  <path d="M9 30 Q4 35 6 42" />
  <line x1="15" y1="38" x2="13" y2="44" /><line x1="21" y1="40" x2="21" y2="46" />
  <path d="M27 22 Q30 25 27 28" />
</svg>'''

ICONS['termita'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="24" cy="32" rx="8" ry="10" />
  <circle cx="24" cy="16" r="7" />
  <line x1="24" y1="22" x2="24" y2="22" />
  <path d="M17 16 Q10 10 8 4" /><path d="M31 16 Q38 10 40 4" />
  <line x1="16" y1="28" x2="8" y2="24" /><line x1="16" y1="34" x2="7" y2="34" />
  <line x1="32" y1="28" x2="40" y2="24" /><line x1="32" y1="34" x2="41" y2="34" />
</svg>'''

ICONS['mosquito'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="24" cy="26" rx="5" ry="10" />
  <circle cx="24" cy="13" r="5" />
  <path d="M19 20 Q8 14 6 8" /><path d="M29 20 Q40 14 42 8" />
  <line x1="24" y1="36" x2="20" y2="44" /><line x1="24" y1="36" x2="28" y2="44" />
  <line x1="16" y1="26" x2="8" y2="22" /><line x1="32" y1="26" x2="40" y2="22" />
  <line x1="24" y1="8" x2="22" y2="4" /><line x1="24" y1="8" x2="26" y2="4" />
</svg>'''

ICONS['ave'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M8 20 Q18 8 28 16 Q36 12 42 18 Q38 24 28 22 Q22 30 16 32 Q12 30 10 26 Z" />
  <circle cx="34" cy="14" r="2" fill="currentColor" />
  <path d="M16 32 Q14 40 18 44" /><path d="M22 33 Q22 40 26 44" />
  <path d="M8 20 Q4 18 4 24" />
</svg>'''

ICONS['chinche'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="6" y="28" width="36" height="14" rx="3" />
  <rect x="10" y="22" width="28" height="8" rx="2" />
  <ellipse cx="24" cy="18" rx="8" ry="5" />
  <circle cx="22" cy="16" r="1.5" fill="currentColor" /><circle cx="26" cy="16" r="1.5" fill="currentColor" />
  <line x1="16" y1="18" x2="10" y2="14" /><line x1="32" y1="18" x2="38" y2="14" />
  <line x1="12" y1="32" x2="8" y2="26" /><line x1="36" y1="32" x2="40" y2="26" />
</svg>'''

ICONS['enjambre'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <ellipse cx="24" cy="28" rx="7" ry="10" />
  <line x1="20" y1="24" x2="26" y2="20" /><line x1="28" y1="24" x2="22" y2="20" />
  <path d="M17 24 Q10 18 10 12 Q10 8 14 8" /><path d="M31 24 Q38 18 38 12 Q38 8 34 8" />
  <line x1="24" y1="18" x2="24" y2="14" />
  <line x1="24" y1="38" x2="22" y2="44" /><line x1="24" y1="38" x2="26" y2="44" />
  <line x1="17" y1="28" x2="10" y2="30" /><line x1="31" y1="28" x2="38" y2="30" />
</svg>'''

ICONS['mip'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="24" cy="24" r="18" />
  <path d="M24 14 Q30 20 24 26 Q18 20 24 14Z" />
  <path d="M24 26 Q32 28 32 36" />
  <path d="M24 26 Q16 28 14 36" />
  <line x1="24" y1="36" x2="24" y2="44" />
  <path d="M14 20 Q8 16 8 10" /><path d="M34 20 Q40 16 40 10" />
</svg>'''

# Espacios / Zonas
ICONS['casa'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M6 22 L24 6 L42 22" />
  <rect x="10" y="22" width="28" height="20" />
  <rect x="20" y="30" width="8" height="12" />
  <rect x="13" y="25" width="7" height="7" />
  <rect x="28" y="25" width="7" height="7" />
</svg>'''

ICONS['restaurante'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 4 L12 20 Q12 26 18 26 L18 44" />
  <line x1="12" y1="14" x2="24" y2="14" />
  <path d="M24 4 L24 14 Q24 20 18 22" />
  <line x1="30" y1="4" x2="30" y2="44" />
  <path d="M30 4 Q38 4 38 12 Q38 20 30 20" />
</svg>'''

ICONS['oficina'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="8" y="4" width="32" height="40" />
  <line x1="8" y1="12" x2="40" y2="12" /><line x1="8" y1="20" x2="40" y2="20" /><line x1="8" y1="28" x2="40" y2="28" /><line x1="8" y1="36" x2="40" y2="36" />
  <rect x="14" y="6" width="4" height="4" /><rect x="22" y="6" width="4" height="4" /><rect x="30" y="6" width="4" height="4" />
  <rect x="14" y="14" width="4" height="4" /><rect x="22" y="14" width="4" height="4" /><rect x="30" y="14" width="4" height="4" />
  <rect x="14" y="22" width="4" height="4" /><rect x="22" y="22" width="4" height="4" /><rect x="30" y="22" width="4" height="4" />
  <rect x="20" y="34" width="8" height="10" />
</svg>'''

ICONS['bodega'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M4 20 L24 6 L44 20 L44 44 L4 44 Z" />
  <line x1="4" y1="20" x2="44" y2="20" />
  <rect x="14" y="28" width="20" height="16" />
  <rect x="19" y="22" width="10" height="8" />
  <line x1="24" y1="28" x2="24" y2="44" />
</svg>'''

ICONS['hotel'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="6" y="8" width="36" height="36" />
  <line x1="6" y1="16" x2="42" y2="16" /><line x1="6" y1="24" x2="42" y2="24" /><line x1="6" y1="32" x2="42" y2="32" />
  <line x1="18" y1="8" x2="18" y2="44" /><line x1="30" y1="8" x2="30" y2="44" />
  <path d="M18 4 L24 8 L30 4" />
</svg>'''

# Checks y certificaciones
ICONS['check'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10" />
  <polyline points="7,12 10,15 17,9" />
</svg>'''

ICONS['escudo'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M24 4 L40 10 L40 24 Q40 36 24 44 Q8 36 8 24 L8 10 Z" />
  <polyline points="16,24 21,29 32,18" />
</svg>'''

ICONS['licencia'] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="8" y="4" width="32" height="40" rx="3" />
  <line x1="16" y1="14" x2="32" y2="14" /><line x1="16" y1="20" x2="32" y2="20" /><line x1="16" y1="26" x2="24" y2="26" />
  <circle cx="28" cy="32" r="7" />
  <polyline points="24,32 27,35 33,29" />
</svg>'''


def make_icon_tag(key, size_class='icon-svg'):
    svg = ICONS.get(key, ICONS['escudo'])
    return f'<span class="{size_class}">{svg}</span>'

# ─── MAPA DE REEMPLAZOS ────────────────────────────────────────────────────────
# Formato: buscar_cadena → clave de icono

# Para cotizador (plagas)
PLAGA_OPTS = {
    "selPlaga(this,'Cucarachas'": 'cucaracha',
    "selPlaga(this,'Roedores'":   'roedor',
    "selPlaga(this,'Termitas'":   'termita',
    "selPlaga(this,'Mosquitos'":  'mosquito',
    "selPlaga(this,'Aves'":       'ave',
    "selPlaga(this,'Chinches":    'chinche',
    "selPlaga(this,'Enjambres'":  'enjambre',
    "selPlaga(this,'Control Integral MIP'": 'mip',
    "selPlaga(this,'Control integral MIP'": 'mip',
}
ESPACIO_OPTS = {
    "selEsp(this,'Casa":          'casa',
    "selEsp(this,'Restaurante'":  'restaurante',
    "selEsp(this,'Oficina":       'oficina',
    "selEsp(this,'Bodega":        'bodega',
    "selEsp(this,'Hotel":         'hotel',
    "selEsp(this,'Hospital":      'licencia',
    "selEsp(this,'Maquiladora":   'bodega',
}

import re

def replace_cotiz_icons(html):
    """Replace icons in cotiz-opt cards based on the onclick value."""
    def replace_opt(m):
        onclick_val = m.group('onclick')
        content = m.group('content')
        label = m.group('label')
        
        # Determine icon key from onclick
        icon_key = 'escudo'
        for pattern, key in {**PLAGA_OPTS, **ESPACIO_OPTS}.items():
            if pattern in onclick_val:
                icon_key = key
                break
        
        new_ico = make_icon_tag(icon_key, 'icon-svg')
        return f'<div class="cotiz-opt" onclick="{onclick_val}"><span class="cotiz-opt-ico">{ICONS[icon_key]}</span><div class="cotiz-opt-lbl">{label}</div></div>'
    
    # Match cotiz-opt divs
    pattern = r'<div class="cotiz-opt" onclick="(?P<onclick>[^"]+)">.*?cotiz-opt-ico[^>]*>.*?</span><div class="cotiz-opt-lbl">(?P<label>[^<]+)</div>(?P<content>.*?)</div>'
    return re.sub(pattern, replace_opt, html, flags=re.DOTALL)

def replace_service_icons(html):
    """Replace service card icons in servicios.html"""
    replacements = [
        (r'<div style="font-size: 2\.5rem; margin-bottom: 15px;">🪳</div>', make_icon_tag('cucaracha', 'icon-svg-card')),
        (r'<div style="font-size: 2\.5rem; margin-bottom: 15px;">🪰</div>', make_icon_tag('mosquito', 'icon-svg-card')),
        (r'<div style="font-size: 2\.5rem; margin-bottom: 15px;">🐀</div>', make_icon_tag('roedor', 'icon-svg-card')),
        (r'<div style="font-size: 2\.5rem; margin-bottom: 15px;">🪵</div>', make_icon_tag('termita', 'icon-svg-card')),
        (r'<div style="font-size: 2\.5rem; margin-bottom: 15px;">🛏️</div>', make_icon_tag('chinche', 'icon-svg-card')),
        (r'<div style="font-size: 2\.5rem; margin-bottom: 15px;">🐦</div>', make_icon_tag('ave', 'icon-svg-card')),
        # PNG images from previous iteration
        (r'<img src="icons/rastreros\.png" class="icon-img" alt="Rastreros">', ''),
        (r'<img src="icons/roedores\.png" class="icon-img" alt="Roedores">', ''),
        (r'<img src="icons/fauna\.png" class="icon-img" alt="Fauna">', ''),
        (r'<img src="icons/chinches\.png" class="icon-img" alt="Chinches">', ''),
    ]
    for pattern, repl in replacements:
        html = re.sub(pattern, repl, html)
    return html

def replace_emoji_checks(html):
    """Replace check emojis with SVG check icons."""
    svg_check = f'<span class="icon-svg-check">{ICONS["check"]}</span>'
    html = html.replace('✔️', svg_check)
    html = html.replace('✅', f'<span class="icon-svg-xl">{ICONS["escudo"]}</span>')
    return html

# CSS for the SVG icons
ICON_CSS = """
<style id="serysa-icon-css">
/* ── SVG Icon System ── */
.icon-svg { display:inline-flex; align-items:center; justify-content:center; width:52px; height:52px; color:var(--cyan-400); }
.icon-svg svg { width:100%; height:100%; }
.icon-svg-card { display:flex; align-items:center; justify-content:center; width:60px; height:60px; color:var(--cyan-400); margin-bottom:15px; }
.icon-svg-card svg { width:100%; height:100%; }
.icon-svg-check { display:inline-flex; align-items:center; justify-content:center; width:20px; height:20px; color:var(--green); vertical-align:middle; margin-right:6px; flex-shrink:0; }
.icon-svg-check svg { width:100%; height:100%; }
.icon-svg-xl { display:inline-flex; width:40px; height:40px; color:var(--green); vertical-align:middle; }
.icon-svg-xl svg { width:100%; height:100%; }
/* cotiz-opt icons */
.cotiz-opt-ico { display:flex; align-items:center; justify-content:center; height:54px; margin-bottom:9px; transition:transform .3s; }
.cotiz-opt-ico svg { width:46px; height:46px; color:var(--blue-500); stroke:var(--blue-500); }
.cotiz-opt:hover .cotiz-opt-ico svg, .cotiz-opt.sel .cotiz-opt-ico svg { color:var(--cyan-500); stroke:var(--cyan-500); transform:scale(1.1); }
/* service icon in cards */
.service-icon-svg { display:flex; align-items:center; justify-content:center; width:52px; height:52px; border-radius:14px; background:linear-gradient(135deg,var(--blue-100),var(--gray-100)); margin-bottom:14px; }
.service-icon-svg svg { width:34px; height:34px; stroke:var(--blue-500); color:var(--blue-500); }
/* Remove old icon images */
.icon-img, .icon-img-sm { display:none; }
</style>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove old icon CSS if present
    html = re.sub(r'<style>\s*\.icon-img.*?</style>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style id="serysa-icon-css">.*?</style>', '', html, flags=re.DOTALL)
    
    # Inject new CSS before </head>
    if '</head>' in html and 'serysa-icon-css' not in html:
        html = html.replace('</head>', ICON_CSS + '\n</head>')
    
    # Fix cotiz options (plagas & espacios)
    html = replace_cotiz_icons(html)
    
    # Fix service card icons
    html = replace_service_icons(html)
    
    # Fix check marks
    html = replace_emoji_checks(html)
    
    # Fix remaining specific emojis used in the HTML
    remaining = {
        '🏠': f'<span class="cotiz-opt-ico">{ICONS["casa"]}</span>',
        '🍽️': f'<span class="cotiz-opt-ico">{ICONS["restaurante"]}</span>',
        '🏢': f'<span class="cotiz-opt-ico">{ICONS["oficina"]}</span>',
        '🏭': f'<span class="cotiz-opt-ico">{ICONS["bodega"]}</span>',
        '🏨': f'<span class="cotiz-opt-ico">{ICONS["hotel"]}</span>',
    }
    for emoji, repl in remaining.items():
        html = html.replace(emoji, repl)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"OK Updated: {filepath}")

process_file('index.html')
# Regenerate sub-pages from updated build_pages.py
print("Regenerating sub-pages...")

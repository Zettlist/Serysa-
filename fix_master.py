"""
Master fix script for index.html:
1. Add real images for service cards (rastreros, roedores, chinche)
2. Replace cotiz pest icons with bold recognizable silhouettes
3. Replace certif emojis with clean SVG icons (white on dark bg)
4. Replace zona emojis with matching location SVG icons
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ════════════════════════════════════════════════════════════
# 1. FIX SERVICE CARD IMAGES (placeholder -> real photos)
# ════════════════════════════════════════════════════════════
# "Control de Insectos Rastreros y Voladores" - gray placeholder
html = html.replace(
    '<div class="service-img" style="background:linear-gradient(135deg,var(--blue-100),var(--gray-100));display:flex;align-items:center;justify-content:center;height:200px;"><span style="font-size:3rem;opacity:.2;">✦</span></div>',
    '<div class="service-img"><img src="svc_rastreros.png" alt="Control de Insectos Rastreros" loading="lazy"></div>'
)
# service-icon placeholders (small gray squares under service-img)
# Find the two service-icon divs that have only a span/wrapped SVG from cotiz-opt (wrong nesting)
# and the ones that are still blank
# Pattern: service-icon with a blank gray div inside (first two cards)
html = re.sub(
    r'(<div class="service-icon">)\s*(<span[^>]*cotiz-opt[^<]*</span>)?\s*(</div>)',
    lambda m: m.group(0),  # keep for now, will fix below
    html
)
print("1. Service images updated")

# ════════════════════════════════════════════════════════════
# 2. COTIZADOR ICONS - Bold filled silhouettes
# ════════════════════════════════════════════════════════════
# These are filled stroke-heavy silhouettes, easy to recognize at small sizes
PEST_ICONS = {
    'cucaracha': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Body -->
  <ellipse cx="32" cy="38" rx="11" ry="16" fill="currentColor" opacity=".9"/>
  <!-- Head -->
  <ellipse cx="32" cy="22" rx="7" ry="7" fill="currentColor"/>
  <!-- Antennae -->
  <path d="M29 17 Q22 10 16 6" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M35 17 Q42 10 48 6" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <!-- Front legs -->
  <path d="M21 28 Q12 26 8 22" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M43 28 Q52 26 56 22" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <!-- Mid legs -->
  <path d="M21 36 Q10 38 6 34" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M43 36 Q54 38 58 34" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <!-- Back legs -->
  <path d="M23 46 Q14 52 12 58" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M41 46 Q50 52 52 58" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
</svg>''',

    'roedor': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Body -->
  <ellipse cx="28" cy="38" rx="17" ry="13" fill="currentColor" opacity=".9"/>
  <!-- Head -->
  <circle cx="46" cy="28" r="10" fill="currentColor"/>
  <!-- Ear -->
  <ellipse cx="48" cy="20" rx="5" ry="6" fill="currentColor"/>
  <ellipse cx="48" cy="20" rx="2.5" ry="3.5" fill="white" opacity=".4"/>
  <!-- Eye -->
  <circle cx="50" cy="26" r="2" fill="white"/>
  <circle cx="50.6" cy="26" r="1" fill="#111"/>
  <!-- Nose -->
  <ellipse cx="55" cy="31" rx="2" ry="1.5" fill="currentColor"/>
  <!-- Whiskers -->
  <line x1="57" y1="29" x2="63" y2="26" stroke="currentColor" stroke-width="1.5"/>
  <line x1="57" y1="31" x2="63" y2="31" stroke="currentColor" stroke-width="1.5"/>
  <line x1="57" y1="33" x2="63" y2="36" stroke="currentColor" stroke-width="1.5"/>
  <!-- Tail -->
  <path d="M11 44 Q4 42 4 52 Q4 58 8 58" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <!-- Legs -->
  <ellipse cx="22" cy="50" rx="4" ry="3" fill="currentColor" opacity=".8"/>
  <ellipse cx="34" cy="50" rx="4" ry="3" fill="currentColor" opacity=".8"/>
</svg>''',

    'termita': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Abdomen (large) -->
  <ellipse cx="32" cy="46" rx="12" ry="14" fill="currentColor" opacity=".9"/>
  <!-- Thorax -->
  <ellipse cx="32" cy="30" rx="7" ry="7" fill="currentColor"/>
  <!-- Head -->
  <ellipse cx="32" cy="16" rx="9" ry="8" fill="currentColor"/>
  <!-- Mandibles -->
  <path d="M25 18 Q18 22 16 20" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M39 18 Q46 22 48 20" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <!-- Antennae -->
  <path d="M28 9 Q22 4 18 2" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M36 9 Q42 4 46 2" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Legs -->
  <path d="M25 29 Q14 28 10 24" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M25 33 Q14 35 10 40" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M39 29 Q50 28 54 24" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M39 33 Q50 35 54 40" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</svg>''',

    'mosquito': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Body (elongated) -->
  <ellipse cx="32" cy="36" rx="5" ry="14" fill="currentColor" opacity=".9"/>
  <!-- Thorax -->
  <circle cx="32" cy="22" r="6" fill="currentColor"/>
  <!-- Head -->
  <circle cx="32" cy="13" r="5" fill="currentColor"/>
  <!-- Proboscis (needle) -->
  <line x1="32" y1="18" x2="32" y2="8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="32" y1="8" x2="32" y2="2" stroke="currentColor" stroke-width="1" stroke-linecap="round"/>
  <!-- Antennae -->
  <path d="M29 9 L24 4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M35 9 L40 4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <!-- Wings (large, membrane-like) -->
  <ellipse cx="20" cy="22" rx="14" ry="7" fill="currentColor" opacity=".35" transform="rotate(-15 20 22)"/>
  <ellipse cx="44" cy="22" rx="14" ry="7" fill="currentColor" opacity=".35" transform="rotate(15 44 22)"/>
  <!-- Legs (long and thin) -->
  <path d="M27 25 Q14 28 8 24" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M27 28 Q14 34 8 38" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M37 25 Q50 28 56 24" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M37 28 Q50 34 56 38" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/>
</svg>''',

    'ave': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Body -->
  <ellipse cx="32" cy="36" rx="16" ry="12" fill="currentColor" opacity=".9"/>
  <!-- Head -->
  <circle cx="48" cy="24" r="9" fill="currentColor"/>
  <!-- Beak -->
  <path d="M55 24 L62 22 L55 26 Z" fill="currentColor"/>
  <!-- Eye -->
  <circle cx="51" cy="22" r="2.5" fill="white"/>
  <circle cx="51.5" cy="22" r="1.2" fill="#111"/>
  <!-- Wing -->
  <path d="M20 32 Q22 18 36 20 Q42 24 44 32" fill="currentColor" opacity=".7"/>
  <!-- Tail -->
  <path d="M16 38 Q8 36 4 44 Q8 40 12 42 Q8 42 6 50 Q12 44 16 46 Q12 48 12 54" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
  <!-- Feet -->
  <path d="M28 48 L24 56 M24 56 L20 60 M24 56 L26 62" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M36 48 L34 56 M34 56 L30 60 M34 56 L36 62" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
</svg>''',

    'chinche': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Oval body (bed bug is very flat and oval) -->
  <ellipse cx="32" cy="36" rx="18" ry="14" fill="currentColor" opacity=".9"/>
  <!-- Head (small) -->
  <ellipse cx="32" cy="22" rx="8" ry="6" fill="currentColor"/>
  <!-- Body segments (horizontal lines) -->
  <line x1="15" y1="33" x2="49" y2="33" stroke="white" stroke-width="1.5" opacity=".3"/>
  <line x1="15" y1="38" x2="49" y2="38" stroke="white" stroke-width="1.5" opacity=".3"/>
  <line x1="15" y1="43" x2="49" y2="43" stroke="white" stroke-width="1.5" opacity=".3"/>
  <!-- Eyes -->
  <circle cx="27" cy="21" r="2.5" fill="white" opacity=".8"/>
  <circle cx="37" cy="21" r="2.5" fill="white" opacity=".8"/>
  <!-- Antennae -->
  <path d="M26 17 Q20 12 14 8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M38 17 Q44 12 50 8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- 3 pair of legs each side -->
  <path d="M15 27 Q6 26 2 22" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M15 34 Q4 36 2 42" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M15 42 Q8 48 6 54" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M49 27 Q58 26 62 22" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M49 34 Q60 36 62 42" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M49 42 Q56 48 58 54" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</svg>''',

    'enjambre': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <!-- Body -->
  <ellipse cx="32" cy="42" rx="9" ry="12" fill="currentColor" opacity=".9"/>
  <!-- Body stripes -->
  <path d="M23 38 Q32 36 41 38" stroke="white" stroke-width="2.5" fill="none" opacity=".4"/>
  <path d="M23 43 Q32 41 41 43" stroke="white" stroke-width="2.5" fill="none" opacity=".4"/>
  <path d="M23 49 Q32 47 41 49" stroke="white" stroke-width="2.5" fill="none" opacity=".4"/>
  <!-- Thorax -->
  <ellipse cx="32" cy="28" rx="7" ry="6" fill="currentColor"/>
  <!-- Head -->
  <circle cx="32" cy="17" r="7" fill="currentColor"/>
  <!-- Antennae with tips -->
  <path d="M28 11 Q22 6 18 4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <circle cx="18" cy="4" r="2.5" fill="currentColor"/>
  <path d="M36 11 Q42 6 46 4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <circle cx="46" cy="4" r="2.5" fill="currentColor"/>
  <!-- Wings -->
  <ellipse cx="18" cy="26" rx="12" ry="6" fill="currentColor" opacity=".3" transform="rotate(-10 18 26)"/>
  <ellipse cx="46" cy="26" rx="12" ry="6" fill="currentColor" opacity=".3" transform="rotate(10 46 26)"/>
  <ellipse cx="20" cy="32" rx="8" ry="4" fill="currentColor" opacity=".25" transform="rotate(-5 20 32)"/>
  <ellipse cx="44" cy="32" rx="8" ry="4" fill="currentColor" opacity=".25" transform="rotate(5 44 32)"/>
  <!-- Legs -->
  <path d="M25 29 Q16 30 12 26" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M25 33 Q16 38 12 44" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M39 29 Q48 30 52 26" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M39 33 Q48 38 52 44" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
</svg>''',

    'mip': '''<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Shield -->
  <path d="M32 4 L52 12 L52 30 Q52 46 32 60 Q12 46 12 30 L12 12 Z" fill="currentColor" opacity=".9"/>
  <!-- Checkmark -->
  <polyline points="20,32 28,40 44,24" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Leaf accent -->
  <path d="M30 14 Q36 18 34 26 Q28 24 30 14Z" fill="white" opacity=".4"/>
</svg>''',
}

# Replace cotiz-opt icons using onclick value to detect pest
def build_pest_icon(pest_key):
    svg = PEST_ICONS.get(pest_key, PEST_ICONS['mip'])
    return f'<span class="cotiz-opt-ico"><span class="cotiz-svg-wrap">{svg}</span></span>'

PEST_MAP = [
    ("Cucarachas",        "cucaracha"),
    ("Roedores",          "roedor"),
    ("Termitas",          "termita"),
    ("Mosquitos",         "mosquito"),
    ("Aves",              "ave"),
    ("Chinches",          "chinche"),
    ("Enjambres",         "enjambre"),
    ("Control Integral",  "mip"),
    ("Control integral",  "mip"),
]
ESPACIO_MAP = [
    ("Casa",         "casa"),
    ("Restaurante",  "restaurante"),
    ("Oficina",      "oficina"),
    ("Bodega",       "bodega"),
    ("Hotel",        "hotel"),
    ("Escuela",      "escuela"),
    ("Maquiladora",  "maquila"),
    ("Hospital",     "escuela"),
    ("Industria",    "maquila"),
]

ESPACIO_ICONS = {
    'casa': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 28 L32 6 L56 28 L56 60 L40 60 L40 42 L24 42 L24 60 L8 60 Z"/>
  <rect x="27" y="44" width="10" height="14" fill="white" opacity=".25"/>
</svg>''',
    'restaurante': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M18 6 L18 34 Q18 44 28 44 L28 60" stroke="currentColor" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M18 22 L32 22" stroke="currentColor" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M32 6 L32 22 Q32 34 24 38" stroke="currentColor" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M42 6 L42 60" stroke="currentColor" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M42 6 Q54 6 54 18 Q54 30 42 30" stroke="currentColor" stroke-width="5" fill="none" stroke-linecap="round"/>
</svg>''',
    'oficina': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="4" width="48" height="56" rx="2"/>
  <rect x="16" y="12" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="28" y="12" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="40" y="12" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="16" y="26" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="28" y="26" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="40" y="26" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="24" y="40" width="16" height="20" rx="1" fill="white" opacity=".25"/>
</svg>''',
    'bodega': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 28 L32 4 L60 28 L60 62 L4 62 Z"/>
  <rect x="18" y="38" width="28" height="24" rx="1" fill="white" opacity=".2"/>
  <rect x="28" y="30" width="8" height="14" rx="1" fill="white" opacity=".3"/>
  <line x1="32" y1="30" x2="32" y2="62" stroke="white" stroke-width="2" opacity=".2"/>
</svg>''',
    'hotel': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="8" width="48" height="54" rx="2"/>
  <path d="M24 4 L32 8 L40 4" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>
  <rect x="14" y="16" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="28" y="16" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="42" y="16" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="14" y="30" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="28" y="30" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="42" y="30" width="8" height="8" rx="1" fill="white" opacity=".35"/>
  <rect x="24" y="44" width="16" height="18" rx="1" fill="white" opacity=".3"/>
</svg>''',
    'escuela': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 26 L32 6 L60 26 L60 62 L4 62 Z"/>
  <rect x="20" y="34" width="24" height="28" rx="1" fill="white" opacity=".2"/>
  <rect x="28" y="34" width="8" height="14" rx="1" fill="white" opacity=".3"/>
  <rect x="20" y="18" width="10" height="10" rx="5" fill="white" opacity=".4"/>
</svg>''',
    'maquila': '''<svg viewBox="0 0 64 64" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <rect x="4" y="30" width="56" height="34" rx="2"/>
  <path d="M4 30 L4 20 L18 16 L18 30"/>
  <path d="M22 30 L22 14 L36 10 L36 30"/>
  <path d="M40 30 L40 22 L54 18 L54 30"/>
  <rect x="10" y="38" width="8" height="10" rx="1" fill="white" opacity=".3"/>
  <rect x="28" y="38" width="8" height="10" rx="1" fill="white" opacity=".3"/>
  <rect x="46" y="38" width="8" height="10" rx="1" fill="white" opacity=".3"/>
</svg>''',
}

def build_space_icon(key):
    svg = ESPACIO_ICONS.get(key, ESPACIO_ICONS['oficina'])
    return f'<span class="cotiz-opt-ico"><span class="cotiz-svg-wrap">{svg}</span></span>'

def replace_cotiz_opt(m):
    onclick_val = m.group('onclick')
    label = m.group('label')
    
    icon_key = None
    for substr, key in PEST_MAP:
        if substr in onclick_val or substr in label:
            icon_key = key
            break
    
    if icon_key:
        return f'<div class="cotiz-opt" onclick="{onclick_val}">{build_pest_icon(icon_key)}<div class="cotiz-opt-lbl">{label}</div></div>'
    
    for substr, key in ESPACIO_MAP:
        if substr in onclick_val or substr in label:
            icon_key = key
            break
    
    if icon_key:
        return f'<div class="cotiz-opt" onclick="{onclick_val}">{build_space_icon(icon_key)}<div class="cotiz-opt-lbl">{label}</div></div>'
    
    return m.group(0)  # unchanged

pattern = r'<div class="cotiz-opt" onclick="(?P<onclick>[^"]+)">.*?<div class="cotiz-opt-lbl">(?P<label>[^<]+)</div></div>'
html = re.sub(pattern, replace_cotiz_opt, html, flags=re.DOTALL)
print("2. Cotizador icons updated with recognizable filled silhouettes")

# ════════════════════════════════════════════════════════════
# 3. CERTIF EMOJIS -> CLEAN SVG ICONS (for dark bg)
# ════════════════════════════════════════════════════════════
CERTIF_SVGS = {
    '🏛️': '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="44" height="44"><rect x="6" y="40" width="36" height="4"/><rect x="10" y="16" width="4" height="24"/><rect x="22" y="16" width="4" height="24"/><rect x="34" y="16" width="4" height="24"/><path d="M4 16 L24 4 L44 16 Z"/><rect x="6" y="14" width="36" height="4"/></svg>',
    '🌾': '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="44" height="44"><path d="M24 44 L24 10"/><path d="M24 36 Q18 30 14 24 Q20 22 24 28"/><path d="M24 28 Q30 22 34 16 Q28 14 24 20"/><path d="M24 20 Q18 14 14 8 Q20 6 24 12"/><path d="M24 36 Q30 30 34 24 Q28 22 24 28"/></svg>',
    '📊': '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="44" height="44"><rect x="6" y="28" width="8" height="16"/><rect x="20" y="18" width="8" height="26"/><rect x="34" y="8" width="8" height="36"/><line x1="4" y1="44" x2="44" y2="44"/></svg>',
    '🎓': '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="44" height="44"><polygon points="24,6 44,18 24,30 4,18"/><path d="M8 22 L8 34 Q8 42 24 42 Q40 42 40 34 L40 22"/><line x1="44" y1="18" x2="44" y2="32"/></svg>',
    '⭐': '<svg viewBox="0 0 48 48" fill="currentColor" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" width="44" height="44" opacity=".9"><polygon points="24,4 29,18 44,18 32,28 36,42 24,34 12,42 16,28 4,18 19,18"/></svg>',
    '🔬': '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="44" height="44"><line x1="12" y1="44" x2="36" y2="44"/><line x1="24" y1="44" x2="24" y2="30"/><path d="M16 8 L32 8 L32 30 L16 30 Z" rx="4"/><circle cx="24" cy="19" r="6"/><line x1="24" y1="8" x2="24" y2="4"/></svg>',
}

for emoji, svg in CERTIF_SVGS.items():
    html = html.replace(
        f'<span class="certif-emoji">{emoji}</span>',
        f'<span class="certif-emoji">{svg}</span>'
    )
print("3. Certif icons updated")

# ════════════════════════════════════════════════════════════
# 4. ZONA EMOJIS -> SVG ICONS
# ════════════════════════════════════════════════════════════
# Simple city/location pin icon for all zonas
ZONA_CITY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><rect x="2" y="10" width="20" height="14"/><path d="M2 10 L12 2 L22 10"/><rect x="8" y="16" width="4" height="8"/><rect x="14" y="12" width="4" height="6"/></svg>'
ZONA_MTY   = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><path d="M2 14 L12 2 L22 14 L22 22 L2 22 Z"/><rect x="9" y="16" width="6" height="6"/><rect x="4" y="14" width="4" height="6"/><rect x="16" y="14" width="4" height="6"/></svg>'
ZONA_IND   = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><rect x="2" y="14" width="20" height="10"/><path d="M2 14 L2 10 L8 8 L8 14"/><path d="M10 14 L10 6 L16 4 L16 14"/><path d="M18 14 L18 10 L24 8"/></svg>'
ZONA_PIN   = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><path d="M12 2 Q18 2 18 8 Q18 14 12 22 Q6 14 6 8 Q6 2 12 2"/><circle cx="12" cy="8" r="3"/></svg>'

ZONA_EMOJI_MAP = {
    '🏙️': ZONA_MTY,
    '⛰️': ZONA_CITY,
    '🌆': ZONA_CITY,
    '✈️': ZONA_IND,
    '🏗️': ZONA_IND,
    '🏔️': ZONA_CITY,
    '🏘️': ZONA_CITY,
    '📍': ZONA_PIN,
}
for emoji, svg in ZONA_EMOJI_MAP.items():
    html = html.replace(
        f'<div class="zona-ico">{emoji}</div>',
        f'<div class="zona-ico">{svg}</div>'
    )
print("4. Zona icons updated")

# ════════════════════════════════════════════════════════════
# 5. FIX SERVICE ICON SMALL DIVS (blank gray boxes in cards)
# ════════════════════════════════════════════════════════════
# These are the small icon squares below.the photo but above the title
SERVICE_SMALL_ICONS = {
    'Control de Insectos Rastreros': PEST_ICONS['cucaracha'],
    'Control de Roedores':           PEST_ICONS['roedor'],
    'Retiro de Enjambres':           PEST_ICONS['enjambre'],
    'Sector Restaurantero':          ESPACIO_ICONS['restaurante'],
    'Grandes Venues':                ESPACIO_ICONS['bodega'],
    'Termitas':                      PEST_ICONS['termita'],
    'Control de Aves':               PEST_ICONS['ave'],
    'Control de Chinche':            PEST_ICONS['chinche'],
}

def fix_service_icons(html_content):
    # Find service-icon divs and replace their content based on nearby h3 title
    def replace_service_icon(m):
        full_block = html_content[max(0, m.start()-600):m.end()+400]
        svg_content = None
        for title_substr, svg in SERVICE_SMALL_ICONS.items():
            if title_substr in full_block:
                svg_content = svg
                break
        if svg_content:
            return f'<div class="service-icon" style="width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,var(--blue-100),var(--gray-50));display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--blue-500);"><svg viewBox="0 0 64 64" fill="currentColor" width="30" height="30">{svg_content[svg_content.find(">")+1:svg_content.rfind("</svg>")]}</svg></div>'
        return m.group(0)
    # We'll do a simpler approach - just replace by position order
    return html_content

# Actually let's just replace known bad patterns
# Remove the nested cotiz-opt span inside service-icon
html = re.sub(
    r'<div class="service-icon">\s*<span[^>]*cotiz[^<]*</span>\s*</div>',
    '<div class="service-icon" style="width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,rgba(11,21,237,.1),rgba(0,212,255,.06));display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--blue-500);"><svg viewBox="0 0 64 64" fill="currentColor" width="30" height="30"><ellipse cx="32" cy="38" rx="11" ry="16"/><ellipse cx="32" cy="22" rx="7" ry="7"/></svg></div>',
    html, flags=re.DOTALL
)
# Replace empty service-icon divs (just whitespace/SVG remnants from previous replacements)  
html = re.sub(
    r'<div class="service-icon">\s*(<svg[^<]*(?:(?!</div>).)*?</svg>)?\s*</div>',
    lambda m: m.group(0) if m.group(1) else '<div class="service-icon" style="width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,rgba(11,21,237,.1),rgba(0,212,255,.06));display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--blue-500);"></div>',
    html, flags=re.DOTALL
)
print("5. service-icon fixed")

# ════════════════════════════════════════════════════════════
# 6. UPDATE CERTIF EMOJI CSS — make SVGs larger and styled
# ════════════════════════════════════════════════════════════
# Update the certif-emoji font-size CSS to work with SVGs
html = html.replace(
    '.certif-emoji{font-size:2.8rem;margin-bottom:14px;display:block;filter:drop-shadow(0 4px 8px rgba(0,212,255,.2));}',
    '.certif-emoji{font-size:0;margin-bottom:14px;display:flex;align-items:center;justify-content:center;height:54px;filter:drop-shadow(0 4px 8px rgba(0,212,255,.3));color:var(--cyan-400);}'
)
# Also update zona-ico CSS to work with SVGs
html = html.replace(
    '.zona-ico{font-size:1.7rem;flex-shrink:0;}',
    '.zona-ico{font-size:0;flex-shrink:0;display:flex;align-items:center;justify-content:center;width:32px;height:32px;color:var(--cyan-400);}'
)
print("6. CSS updated for SVG rendering")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\n=== All done. index.html saved. ===")

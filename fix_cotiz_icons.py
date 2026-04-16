"""
Reemplaza los iconos del cotizador (Tipo de Plaga y Tipo de Espacio) en index.html
con SVGs inline consistentes en paleta navy/cyan.
"""

SVG = {
    # ── Plagas ──────────────────────────────────────────────────────────
    'cucaracha': '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="24" cy="27" rx="9" ry="13"/><ellipse cx="24" cy="18" rx="5" ry="6"/><line x1="24" y1="12" x2="19" y2="7"/><line x1="24" y1="12" x2="29" y2="7"/><line x1="15" y1="21" x2="7" y2="18"/><line x1="15" y1="27" x2="6" y2="27"/><line x1="15" y1="33" x2="8" y2="37"/><line x1="33" y1="21" x2="41" y2="18"/><line x1="33" y1="27" x2="42" y2="27"/><line x1="33" y1="33" x2="40" y2="37"/></svg>',
    'roedor':    '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="21" cy="30" rx="13" ry="10"/><circle cx="34" cy="20" r="7"/><circle cx="36" cy="18" r="1.5" fill="currentColor"/><line x1="34" y1="13" x2="32" y2="7"/><line x1="37" y1="13" x2="40" y2="7"/><path d="M8 32 Q4 36 6 42"/><line x1="14" y1="38" x2="12" y2="44"/><line x1="20" y1="40" x2="20" y2="46"/></svg>',
    'termita':   '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="24" cy="32" rx="8" ry="10"/><circle cx="24" cy="16" r="7"/><path d="M17 16 Q10 10 8 4"/><path d="M31 16 Q38 10 40 4"/><line x1="16" y1="28" x2="8" y2="24"/><line x1="16" y1="34" x2="7" y2="34"/><line x1="32" y1="28" x2="40" y2="24"/><line x1="32" y1="34" x2="41" y2="34"/></svg>',
    'mosquito':  '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="24" cy="27" rx="5" ry="10"/><circle cx="24" cy="13" r="5"/><path d="M19 20 Q8 14 6 8"/><path d="M29 20 Q40 14 42 8"/><line x1="24" y1="37" x2="20" y2="44"/><line x1="24" y1="37" x2="28" y2="44"/><line x1="16" y1="26" x2="8" y2="22"/><line x1="32" y1="26" x2="40" y2="22"/><line x1="23" y1="8" x2="21" y2="4"/><line x1="25" y1="8" x2="27" y2="4"/></svg>',
    'ave':       '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 20 Q18 8 28 16 Q36 12 42 18 Q38 24 28 22 Q22 30 16 32 Q12 30 10 26 Z"/><circle cx="34" cy="14" r="2" fill="currentColor"/><path d="M16 32 Q14 40 18 44"/><path d="M22 33 Q22 40 26 44"/><path d="M8 20 Q4 18 4 24"/></svg>',
    'chinche':   '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="28" width="36" height="14" rx="3"/><rect x="10" y="22" width="28" height="8" rx="2"/><ellipse cx="24" cy="18" rx="8" ry="5"/><circle cx="21" cy="16" r="1.5" fill="currentColor"/><circle cx="27" cy="16" r="1.5" fill="currentColor"/><line x1="16" y1="18" x2="10" y2="14"/><line x1="32" y1="18" x2="38" y2="14"/><line x1="12" y1="31" x2="8" y2="26"/><line x1="36" y1="31" x2="40" y2="26"/></svg>',
    'enjambre':  '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="24" cy="29" rx="7" ry="10"/><line x1="19" y1="25" x2="26" y2="21"/><line x1="29" y1="25" x2="22" y2="21"/><path d="M17 25 Q10 19 10 13 Q10 8 14 8"/><path d="M31 25 Q38 19 38 13 Q38 8 34 8"/><line x1="24" y1="19" x2="24" y2="14"/><line x1="24" y1="39" x2="21" y2="45"/><line x1="24" y1="39" x2="27" y2="45"/><line x1="17" y1="29" x2="10" y2="31"/><line x1="31" y1="29" x2="38" y2="31"/></svg>',
    'mip':       '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="24" cy="24" r="18"/><path d="M24 14 Q30 20 24 26 Q18 20 24 14Z"/><path d="M24 26 Q32 28 32 36"/><path d="M24 26 Q16 28 14 36"/><line x1="24" y1="36" x2="24" y2="44"/><path d="M14 20 Q8 16 8 10"/><path d="M34 20 Q40 16 40 10"/></svg>',
    # ── Espacios ─────────────────────────────────────────────────────────
    'casa':         '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 22 L24 6 L42 22"/><rect x="10" y="22" width="28" height="20"/><rect x="20" y="30" width="8" height="12"/><rect x="13" y="25" width="7" height="7"/><rect x="28" y="25" width="7" height="7"/></svg>',
    'restaurante':  '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4 L12 20 Q12 26 18 26 L18 44"/><line x1="12" y1="14" x2="24" y2="14"/><path d="M24 4 L24 14 Q24 20 18 22"/><line x1="30" y1="4" x2="30" y2="44"/><path d="M30 4 Q38 4 38 12 Q38 20 30 20"/></svg>',
    'oficina':      '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="4" width="32" height="40"/><line x1="8" y1="12" x2="40" y2="12"/><line x1="8" y1="20" x2="40" y2="20"/><line x1="8" y1="28" x2="40" y2="28"/><line x1="8" y1="36" x2="40" y2="36"/><rect x="14" y="6" width="4" height="4"/><rect x="22" y="6" width="4" height="4"/><rect x="30" y="6" width="4" height="4"/><rect x="14" y="14" width="4" height="4"/><rect x="22" y="14" width="4" height="4"/><rect x="30" y="14" width="4" height="4"/><rect x="20" y="34" width="8" height="10"/></svg>',
    'bodega':       '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20 L24 6 L44 20 L44 44 L4 44 Z"/><line x1="4" y1="20" x2="44" y2="20"/><rect x="14" y="28" width="20" height="16"/><rect x="19" y="22" width="10" height="8"/><line x1="24" y1="28" x2="24" y2="44"/></svg>',
    'hotel':        '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="8" width="36" height="36"/><line x1="6" y1="16" x2="42" y2="16"/><line x1="6" y1="24" x2="42" y2="24"/><line x1="6" y1="32" x2="42" y2="32"/><line x1="18" y1="8" x2="18" y2="44"/><line x1="30" y1="8" x2="30" y2="44"/><path d="M18 4 L24 8 L30 4"/></svg>',
    'escuela':      '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="18" width="36" height="26"/><path d="M4 20 L24 6 L44 20"/><rect x="18" y="28" width="12" height="16"/><line x1="12" y1="24" x2="12" y2="30"/><line x1="36" y1="24" x2="36" y2="30"/></svg>',
    'maquila':      '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="24" width="40" height="20"/><rect x="8" y="16" width="10" height="8"/><rect x="20" y="12" width="10" height="12"/><rect x="32" y="18" width="8" height="6"/><path d="M4 24 L4 20 L14 14 L14 24"/><line x1="12" y1="28" x2="12" y2="36"/><line x1="24" y1="28" x2="24" y2="36"/><line x1="36" y1="28" x2="36" y2="36"/></svg>',
}

def svg_ico(key):
    return f'<span class="cotiz-opt-ico"><span class="cotiz-svg-wrap">{SVG.get(key, SVG["cucaracha"])}</span></span>'

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Map onclick callsig → icon key
PLAGA_MAP = [
    ("Cucarachas",         "cucaracha"),
    ("Roedores",           "roedor"),
    ("Termitas",           "termita"),
    ("Mosquitos",          "mosquito"),
    ("Aves",               "ave"),
    ("Chinches",           "chinche"),
    ("Enjambres",          "enjambre"),
    ("Control Integral",   "mip"),
    ("Control integral",   "mip"),
]
ESPACIO_MAP = [
    ("Casa",               "casa"),
    ("Restaurante",        "restaurante"),
    ("Oficina",            "oficina"),
    ("Bodega",             "bodega"),
    ("Hotel",              "hotel"),
    ("Escuela",            "escuela"),
    ("Maquiladora",        "maquila"),
    ("Hospital",           "escuela"),
    ("Industria",          "maquila"),
]

def replace_opt_icon(m):
    onclick_val = m.group('onclick')
    label = m.group('label')
    
    # Determine which icon
    icon_key = 'mip'
    for substr, key in PLAGA_MAP + ESPACIO_MAP:
        if substr in onclick_val or substr in label:
            icon_key = key
            break
    
    return f'<div class="cotiz-opt" onclick="{onclick_val}">{svg_ico(icon_key)}<div class="cotiz-opt-lbl">{label}</div></div>'

# Pattern matches any cotiz-opt div regardless of current icon content
pattern = r'<div class="cotiz-opt" onclick="(?P<onclick>[^"]+)">.*?<div class="cotiz-opt-lbl">(?P<label>[^<]+)</div></div>'
html_new = re.sub(pattern, replace_opt_icon, html, flags=re.DOTALL)

# Inject/update cotiz SVG CSS
cotiz_css = """
<style id="cotiz-svg-css">
  .cotiz-opt-ico { display:flex; align-items:center; justify-content:center; height:58px; margin-bottom:10px; }
  .cotiz-svg-wrap { display:flex; width:48px; height:48px; color:var(--blue-400); transition:color .25s, transform .25s; }
  .cotiz-svg-wrap svg { width:100%; height:100%; }
  .cotiz-opt:hover .cotiz-svg-wrap, .cotiz-opt.sel .cotiz-svg-wrap { color:var(--cyan-500); transform:scale(1.12); }
</style>
"""
html_new = re.sub(r'<style id="cotiz-svg-css">.*?</style>', '', html_new, flags=re.DOTALL)
html_new = html_new.replace('</head>', cotiz_css + '</head>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_new)
print("index.html updated with inline SVG icons")

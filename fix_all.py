"""
Comprehensive fix for index.html:
1. "Eliminamos" -> "Controlamos"  
2. service-img-placeholder with emojis -> real images (termitas, aves)
3. ventaja-icon emojis -> clean inline SVGs
4. All remaining emojis in service-icon -> SVGs
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. TEXT FIX ──────────────────────────────────────────────────────────────
html = html.replace('Eliminamos', 'Controlamos')
print("1. Replaced 'Eliminamos' -> 'Controlamos'")

# ── 2. SERVICE IMAGE PLACEHOLDERS ────────────────────────────────────────────
# Termitas: ant emoji 🐜 -> real image
html = re.sub(
    r'<div class="service-img-placeholder"[^>]*>🐜</div>',
    '<div class="service-img"><img src="svc_termitas.png" alt="Control de Termitas" loading="lazy"></div>',
    html
)
# Aves: eagle emoji 🦅 -> real image
html = re.sub(
    r'<div class="service-img-placeholder"[^>]*>🦅</div>',
    '<div class="service-img"><img src="svc_aves.png" alt="Control de Aves" loading="lazy"></div>',
    html
)
# Remaining empty placeholders -> clean gradient
html = re.sub(
    r'<div class="service-img-placeholder"[^>]*></div>',
    '<div class="service-img" style="background:linear-gradient(135deg,var(--navy-800),var(--blue-500));display:flex;align-items:center;justify-content:center;height:200px;"><span style="font-size:3rem;opacity:.2;">✦</span></div>',
    html
)
print("2. Fixed service image placeholders")

# ── 3. VENTAJA ICONS (emojis -> inline SVG) ────────────────────────────────
# SVG definitions (outline style, matches site palette)
def vent_icon(svg_body, label=''):
    return f'<div class="ventaja-icon">{svg_body}</div>'

VENT_SVGS = {
    # Lightning bolt (respuesta rapida)
    '⚡': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><polygon points="13,2 3,14 12,14 11,22 21,10 12,10"/></svg>',
    # Shield / COFEPRIS license
    'escudo_png': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><path d="M12 2 L20 6 L20 12 Q20 18 12 22 Q4 18 4 12 L4 6 Z"/><polyline points="9,12 11,14 15,10"/></svg>',
    # Paw (mascotas)
    '🐾': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><circle cx="7" cy="7" r="2"/><circle cx="17" cy="7" r="2"/><circle cx="4" cy="13" r="2"/><circle cx="20" cy="13" r="2"/><path d="M12 22 Q7 20 6 16 Q5 13 8 12 Q10 11 12 12 Q14 11 16 12 Q19 13 18 16 Q17 20 12 22"/></svg>',
    # Clipboard (garantia)
    '📋': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4 L19 4 Q20 4 20 5 L20 21 Q20 22 19 22 L5 22 Q4 22 4 21 L4 5 Q4 4 5 4 L8 4"/><line x1="8" y1="12" x2="16" y2="12"/><line x1="8" y1="16" x2="13" y2="16"/></svg>',
    # Graduation/industry (alimentaria)
    'alimentaria': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><rect x="2" y="14" width="20" height="8"/><rect x="5" y="8" width="5" height="6"/><rect x="10" y="5" width="5" height="9"/><rect x="15" y="10" width="5" height="4"/></svg>',
    # Money/discount (polizas)
    '💰': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><circle cx="12" cy="12" r="9"/><path d="M12 6 L12 8 M12 16 L12 18 M9 9 Q9 7 12 7 Q15 7 15 9.5 Q15 12 12 12 Q15 12 15 14.5 Q15 17 12 17 Q9 17 9 15"/></svg>',
    # Leaf (MIP)
    '🌿': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><path d="M2 22 Q8 16 12 12 Q16 8 20 3 Q20 3 21 2 Q21 8 18 14 Q15 20 8 22 Z"/><line x1="12" y1="12" x2="2" y2="22"/></svg>',
    # Laptop/online (cotizador)
    '💻': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="26" height="26"><rect x="2" y="4" width="20" height="13" rx="2"/><line x1="2" y1="20" x2="22" y2="20"/><line x1="7" y1="20" x2="7" y2="17"/><line x1="17" y1="20" x2="17" y2="17"/><line x1="7" y1="9" x2="17" y2="9"/><line x1="7" y1="12" x2="13" y2="12"/></svg>',
}

# Replace emoji ventaja icons
html = html.replace(
    '<div class="ventaja-icon">⚡</div>',
    f'<div class="ventaja-icon">{VENT_SVGS["⚡"]}</div>'
)
html = html.replace(
    '<div class="ventaja-icon">🐾</div>',
    f'<div class="ventaja-icon">{VENT_SVGS["🐾"]}</div>'
)
html = html.replace(
    '<div class="ventaja-icon">📋</div>',
    f'<div class="ventaja-icon">{VENT_SVGS["📋"]}</div>'
)
html = html.replace(
    '<div class="ventaja-icon">💰</div>',
    f'<div class="ventaja-icon">{VENT_SVGS["💰"]}</div>'
)
html = html.replace(
    '<div class="ventaja-icon">🌿</div>',
    f'<div class="ventaja-icon">{VENT_SVGS["🌿"]}</div>'
)
html = html.replace(
    '<div class="ventaja-icon">💻</div>',
    f'<div class="ventaja-icon">{VENT_SVGS["💻"]}</div>'
)
# Also fix the PNG image icon in ventajas (COFEPRIS)
html = html.replace(
    '<div class="ventaja-icon"><img src="icons/escudo.png" class="icon-img" alt="Garantía"></div>',
    f'<div class="ventaja-icon">{VENT_SVGS["escudo_png"]}</div>'
)
# Fix the malformed cotiz-opt span inside ventaja-icon
html = re.sub(
    r'<div class="ventaja-icon"><span class="cotiz-opt-ico">.*?</span></div>',
    f'<div class="ventaja-icon">{VENT_SVGS["alimentaria"]}</div>',
    html, flags=re.DOTALL
)
print("3. Fixed ventaja icons")

# ── 4. SERVICE ICON EMOJIS ───────────────────────────────────────────────────
# In service cards, the service-icon div may still have emojis
SERVICE_ICON_SVGS = {
    '🌿': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22"><path d="M2 22 Q8 16 12 12 Q16 8 20 3 Q21 2 21 2 Q21 8 18 14 Q15 20 8 22 Z"/><line x1="12" y1="12" x2="2" y2="22"/></svg>',
    '🦜': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22"><path d="M8 20 Q17 8 20 5 Q20 5 20 10 Q18 14 14 16 Q12 18 11 22"/><circle cx="18" cy="5" r="2"/><circle cx="17.5" cy="4.5" r="0.8" fill="currentColor"/><line x1="14" y1="16" x2="16" y2="21"/></svg>',
}
for emoji, svg in SERVICE_ICON_SVGS.items():
    html = html.replace(
        f'<div class="service-icon">{emoji}</div>',
        f'<div class="service-icon">{svg}</div>'
    )
    # Also simple spans
    html = html.replace(emoji, svg)
print("4. Fixed service icons")

# ── 5. FIX VENTAJA-ICON CSS (make SVGs white/visible) ────────────────────────
# Ensure ventaja-icon SVGs get the white stroke
if 'ventaja-icon svg' not in html:
    extra_css = """
<style id="ventaja-svg-fix">
  .ventaja-icon svg { stroke: #fff; color: #fff; }
  .ventaja-icon { color: #fff; }
  .ventaja-card:hover .ventaja-icon svg { stroke: var(--cyan-300); color: var(--cyan-300); }
</style>"""
    html = html.replace('</head>', extra_css + '\n</head>', 1)
    print("5. Injected ventaja SVG styles")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\nDone. index.html updated.")

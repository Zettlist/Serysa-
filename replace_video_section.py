"""
Reemplaza la sección de video con tarjetas por una sección
de video de fondo en loop automático (autoplay muted loop).
Layout: pantalla completa dividida - video izquierda, video derecha con overlay de texto.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace the entire videos section
START_MARKER = '<!-- ═══════════════════════════════════ VIDEO GALLERY -->'
END_MARKER   = '</script>\n\n'  # ends after the last script block of that section

# Find start
p_start = html.find(START_MARKER)
if p_start == -1:
    print("ERROR: video gallery section not found"); exit()

# Find end - look for the script closing tag after the start
p_end = html.find('</script>', p_start)
# Move past it
p_end = p_end + len('</script>')

old_section = html[p_start:p_end]
print(f"Replacing section from {p_start} to {p_end} ({len(old_section)} chars)")

NEW_SECTION = '''<!-- ═══════════════════════════════════ VIDEO BACKGROUND -->
<section class="vbg-section" id="videos">

  <!-- Left video -->
  <div class="vbg-panel vbg-left">
    <video class="vbg-video" src="video_serysa_1.mp4"
           autoplay muted loop playsinline preload="auto"></video>
    <div class="vbg-overlay"></div>
    <div class="vbg-content">
      <div class="vbg-tag">Área Industrial</div>
      <h3 class="vbg-title">Fumigación<br>profesional</h3>
      <p class="vbg-sub">Protocolos AIB y FSSC 22000.<br>Sin interrupciones operativas.</p>
    </div>
    <!-- Corner badge -->
    <div class="vbg-badge">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round" width="16" height="16">
        <circle cx="12" cy="12" r="10"/>
        <polyline points="12,6 12,12 16,14"/>
      </svg>
      En vivo
    </div>
  </div>

  <!-- Center divider with floating stat -->
  <div class="vbg-center">
    <div class="vbg-center-ring">
      <div class="vbg-center-icon">
        <svg viewBox="0 0 48 48" fill="none" stroke="rgba(0,212,255,0.9)"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="36" height="36">
          <path d="M24 4 L40 10 L40 26 Q40 38 24 44 Q8 38 8 26 L8 10 Z"/>
          <polyline points="16,24 21,29 32,18" stroke-width="2.5"/>
        </svg>
      </div>
    </div>
    <div class="vbg-vs-stats">
      <div class="vbg-vs-stat">
        <span class="vbg-vs-num">30+</span>
        <span class="vbg-vs-lbl">Años</span>
      </div>
      <div class="vbg-vs-divider"></div>
      <div class="vbg-vs-stat">
        <span class="vbg-vs-num">500+</span>
        <span class="vbg-vs-lbl">Clientes</span>
      </div>
    </div>
  </div>

  <!-- Right video -->
  <div class="vbg-panel vbg-right">
    <video class="vbg-video" src="video_serysa_2.mp4"
           autoplay muted loop playsinline preload="auto"></video>
    <div class="vbg-overlay"></div>
    <div class="vbg-content">
      <div class="vbg-tag">Sector Comercial</div>
      <h3 class="vbg-title">Control<br>preventivo</h3>
      <p class="vbg-sub">Certificado COFEPRIS.<br>Garantía escrita en cada visita.</p>
    </div>
    <div class="vbg-badge vbg-badge-right">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round" width="16" height="16">
        <circle cx="12" cy="12" r="10"/>
        <polyline points="12,6 12,12 16,14"/>
      </svg>
      En vivo
    </div>
  </div>

  <!-- Bottom CTA bar -->
  <div class="vbg-bar">
    <span class="vbg-bar-text">¿Listo para proteger tu negocio?</span>
    <div class="vbg-bar-actions">
      <a href="#cotizador" class="btn btn-primary btn-sm">Cotizar gratis →</a>
      <a href="https://wa.me/528100000000" target="_blank" class="btn btn-whatsapp btn-sm">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
          <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
        WhatsApp
      </a>
    </div>
  </div>

</section>

<style>
/* ══════════════════ VIDEO BACKGROUND SECTION ══════════════════ */
.vbg-section {
  position: relative;
  display: flex;
  height: 85vh;
  min-height: 560px;
  max-height: 820px;
  overflow: hidden;
  background: #000;
}

/* ── Panels ── */
.vbg-panel {
  position: relative;
  flex: 1;
  overflow: hidden;
  transition: flex .5s cubic-bezier(.4,0,.2,1);
}
.vbg-panel:hover { flex: 1.12; }

.vbg-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .5s ease;
}
.vbg-panel:hover .vbg-video { transform: scale(1.04); }

.vbg-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(
    180deg,
    rgba(7,12,71,.3) 0%,
    rgba(7,12,71,.1) 40%,
    rgba(7,12,71,.75) 100%
  );
  transition: background .4s;
}
.vbg-panel:hover .vbg-overlay {
  background: linear-gradient(
    180deg,
    rgba(7,12,71,.2) 0%,
    rgba(7,12,71,.05) 40%,
    rgba(7,12,71,.85) 100%
  );
}

/* ── Content overlay ── */
.vbg-content {
  position: absolute;
  bottom: 80px; left: 32px; right: 32px;
  z-index: 2;
}
.vbg-tag {
  display: inline-block;
  padding: 5px 14px;
  background: var(--blue-500);
  color: #fff;
  font-size: .68rem;
  font-weight: 700;
  border-radius: 20px;
  font-family: 'Montserrat', sans-serif;
  letter-spacing: .06em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.vbg-title {
  font-size: clamp(1.6rem, 3vw, 2.4rem);
  font-weight: 900;
  color: #fff;
  font-family: 'Montserrat', sans-serif;
  line-height: 1.15;
  margin-bottom: 10px;
  text-shadow: 0 2px 20px rgba(0,0,0,.4);
}
.vbg-sub {
  font-size: .82rem;
  color: rgba(255,255,255,.72);
  line-height: 1.6;
}

/* ── Live badge ── */
.vbg-badge {
  position: absolute;
  top: 20px; left: 20px;
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.2);
  border-radius: 20px;
  padding: 6px 14px;
  display: flex; align-items: center; gap: 7px;
  font-size: .72rem;
  font-weight: 700;
  color: #fff;
  font-family: 'Montserrat', sans-serif;
  z-index: 3;
}
.vbg-badge::before {
  content: '';
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #f97316;
  animation: chipPulse 1.2s ease-in-out infinite;
}
.vbg-badge-right { left: auto; right: 20px; }

/* ── Center divider ── */
.vbg-center {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  flex-shrink: 0;
  width: 0;           /* invisible width — overlaps both panels */
  overflow: visible;
}

.vbg-center-ring {
  width: 88px; height: 88px;
  border-radius: 50%;
  background: rgba(7,12,71,.85);
  backdrop-filter: blur(16px);
  border: 2px solid rgba(0,212,255,.35);
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 40px rgba(0,212,255,.2), 0 8px 32px rgba(0,0,0,.5);
  animation: centerPulse 3s ease-in-out infinite;
  translate: -44px 0;  /* center it over the divider */
}
@keyframes centerPulse {
  0%,100% { box-shadow: 0 0 30px rgba(0,212,255,.2), 0 8px 32px rgba(0,0,0,.5); }
  50%      { box-shadow: 0 0 55px rgba(0,212,255,.45), 0 8px 32px rgba(0,0,0,.5); }
}

.vbg-vs-stats {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  background: rgba(7,12,71,.8);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(0,212,255,.2);
  border-radius: 16px;
  padding: 18px 22px;
  box-shadow: 0 8px 32px rgba(0,0,0,.4);
  translate: -65px 0;
}
.vbg-vs-stat { text-align: center; }
.vbg-vs-num {
  display: block;
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--cyan-400);
  font-family: 'Montserrat', sans-serif;
  line-height: 1;
}
.vbg-vs-lbl {
  font-size: .68rem;
  color: rgba(255,255,255,.5);
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  letter-spacing: .05em;
  text-transform: uppercase;
}
.vbg-vs-divider {
  width: 24px; height: 1px;
  background: rgba(0,212,255,.3);
}

/* ── Bottom CTA bar ── */
.vbg-bar {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 68px;
  background: rgba(7,12,71,.92);
  backdrop-filter: blur(16px);
  border-top: 1px solid rgba(0,212,255,.15);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  z-index: 10;
}
.vbg-bar-text {
  color: rgba(255,255,255,.8);
  font-size: .9rem;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
}
.vbg-bar-actions { display: flex; gap: 12px; align-items: center; }
.btn-sm { padding: 9px 20px; font-size: .82rem; }

/* Responsive */
@media(max-width:768px) {
  .vbg-section { flex-direction: column; height: auto; max-height: none; }
  .vbg-panel { height: 320px; flex: none; }
  .vbg-center { width: 100%; translate: 0; flex-direction: row; padding: 12px; }
  .vbg-center-ring, .vbg-vs-stats { translate: 0; }
  .vbg-bar { flex-direction: column; height: auto; padding: 14px 20px; gap: 10px; }
  .vbg-bar-text { font-size: .82rem; }
}
</style>

<script>
// Autoplay fix: try to play videos if browser blocks autoplay
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.vbg-video').forEach(function(v) {
    v.play().catch(function() {
      // If autoplay blocked, play on first user interaction
      document.addEventListener('click', function() { v.play(); }, { once: true });
      document.addEventListener('scroll', function() { v.play(); }, { once: true });
    });
  });
});
</script>'''

html = html[:p_start] + NEW_SECTION + html[p_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done: video section replaced with autoplay background layout")

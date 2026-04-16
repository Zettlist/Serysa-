"""
1. Make the animated cinematic section bigger (larger ring, more padding, bigger text)
2. Insert a video gallery section with the 2 WhatsApp videos
"""
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. MAKE CINE SECTION BIGGER ────────────────────────────────────────────
# Increase padding
html = html.replace(
    '.cine-section {\n  position: relative;\n  background: linear-gradient(135deg, #020817 0%, #070c47 35%, #0a1a6e 60%, #020817 100%);\n  padding: 120px 0;\n  overflow: hidden;\n}',
    '.cine-section {\n  position: relative;\n  background: linear-gradient(135deg, #020817 0%, #070c47 35%, #0a1a6e 60%, #020817 100%);\n  padding: 160px 0;\n  overflow: hidden;\n}'
)
# Increase ring size
html = html.replace(
    'width: 340px; height: 340px;',
    'width: 480px; height: 480px;'
)
html = html.replace(
    '.cine-frame {\n  position: relative;\n  width: 340px; height: 340px;',
    '.cine-frame {\n  position: relative;\n  width: 480px; height: 480px;'
)
# Scale up the SVG ring viewBox scaling compensation
html = html.replace(
    '<svg class="cine-ring" viewBox="0 0 300 300">',
    '<svg class="cine-ring" viewBox="0 0 300 300" style="width:100%;height:100%;">'
)
# Increase gap between columns
html = html.replace(
    'display: grid;\n  grid-template-columns: 1fr 1fr;\n  gap: 80px;\n  align-items: center;\n  position: relative;\n  z-index: 2;',
    'display: grid;\n  grid-template-columns: 1fr 1fr;\n  gap: 100px;\n  align-items: center;\n  position: relative;\n  z-index: 2;'
)
# Bigger title
html = html.replace(
    'font-size: clamp(1.8rem, 3.5vw, 2.8rem);',
    'font-size: clamp(2rem, 4vw, 3.4rem);'
)
# Bigger feature text
html = html.replace(
    '.cine-feat strong {\n  display: block;\n  color: #fff;\n  font-size: .9rem;',
    '.cine-feat strong {\n  display: block;\n  color: #fff;\n  font-size: 1rem;'
)
html = html.replace(
    '.cine-feat span {\n  font-size: .78rem;',
    '.cine-feat span {\n  font-size: .84rem;'
)
# Bigger feature icons
html = html.replace(
    '.cine-feat-ico {\n  width: 44px; height: 44px;',
    '.cine-feat-ico {\n  width: 52px; height: 52px;'
)
# Gap between features
html = html.replace(
    'display: flex;\n  flex-direction: column;\n  gap: 20px;\n  margin-bottom: 40px;',
    'display: flex;\n  flex-direction: column;\n  gap: 26px;\n  margin-bottom: 48px;'
)
# Responsive update
html = html.replace(
    '.cine-frame { width: 260px; height: 260px; }',
    '.cine-frame { width: 320px; height: 320px; }'
)
print("1. Cine section enlarged")

# ── 2. VIDEO GALLERY SECTION ────────────────────────────────────────────────
VIDEO_SECTION = """
<!-- ═══════════════════════════════════ VIDEO GALLERY -->
<section class="videos-section section-pad" id="videos">
  <div class="container">
    <div class="section-header reveal">
      <div class="badge">En Acción</div>
      <h2 class="section-title">Así trabaja <span class="grad-text">SERYSA</span></h2>
      <p class="section-sub">Mira nuestro equipo en campo — diagnóstico, tratamiento y resultados reales.</p>
    </div>

    <div class="video-grid">
      <!-- Video 1 -->
      <div class="video-card reveal" onclick="openVideo('video_serysa_1.mp4')">
        <div class="video-thumb">
          <video src="video_serysa_1.mp4" muted preload="metadata" class="video-preview"
                 onmouseenter="this.play()" onmouseleave="this.pause();this.currentTime=0;">
          </video>
          <div class="video-overlay">
            <div class="video-play-btn">
              <svg viewBox="0 0 24 24" fill="white" width="32" height="32">
                <polygon points="5,3 19,12 5,21"/>
              </svg>
            </div>
            <div class="video-label">
              <span class="video-tag">Servicio en campo</span>
              <span class="video-dur">Tratamiento profesional</span>
            </div>
          </div>
        </div>
        <div class="video-info">
          <h4>Servicio en campo — Área Industrial</h4>
          <p>Proceso de fumigación y control en instalaciones industriales de Monterrey.</p>
        </div>
      </div>

      <!-- Video 2 -->
      <div class="video-card reveal" style="transition-delay:.15s" onclick="openVideo('video_serysa_2.mp4')">
        <div class="video-thumb">
          <video src="video_serysa_2.mp4" muted preload="metadata" class="video-preview"
                 onmouseenter="this.play()" onmouseleave="this.pause();this.currentTime=0;">
          </video>
          <div class="video-overlay">
            <div class="video-play-btn">
              <svg viewBox="0 0 24 24" fill="white" width="32" height="32">
                <polygon points="5,3 19,12 5,21"/>
              </svg>
            </div>
            <div class="video-label">
              <span class="video-tag">Control de plagas</span>
              <span class="video-dur">Técnico certificado</span>
            </div>
          </div>
        </div>
        <div class="video-info">
          <h4>Control preventivo — Sector Comercial</h4>
          <p>Inspección y tratamiento preventivo en establecimiento comercial. Cero tiempo de cierre.</p>
        </div>
      </div>

      <!-- CTA card -->
      <div class="video-cta-card reveal" style="transition-delay:.3s">
        <div class="video-cta-glow"></div>
        <svg viewBox="0 0 64 64" fill="none" stroke="rgba(0,212,255,0.6)" stroke-width="1.5" width="64" height="64" class="video-cta-icon">
          <path d="M32 4 L52 12 L52 30 Q52 46 32 60 Q12 46 12 30 L12 12 Z"/>
          <polyline points="22,32 28,38 42,24" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <h4>¿Tienes una plaga ahora?</h4>
        <p>Respondemos en menos de 1 hora. Cotización gratis sin compromiso.</p>
        <div style="display:flex;flex-direction:column;gap:10px;width:100%;">
          <a href="#cotizador" class="btn btn-primary" style="justify-content:center;">Cotizar gratis →</a>
          <a href="https://wa.me/528100000000" target="_blank" class="btn btn-whatsapp" style="justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            WhatsApp directo
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- VIDEO LIGHTBOX MODAL -->
<div class="video-modal" id="videoModal" onclick="closeVideo(event)">
  <div class="video-modal-inner">
    <button class="video-modal-close" onclick="closeVideo(null,true)">
      <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" width="24" height="24">
        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    </button>
    <video id="modalVideo" controls playsinline style="width:100%;border-radius:12px;max-height:80vh;"></video>
  </div>
</div>

<style>
/* ═══════════════ VIDEO SECTION ═══════════════ */
.videos-section { background: var(--gray-50); }
.video-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 24px;
  margin-top: 52px;
}
.video-card {
  background: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(7,12,71,.07);
  border: 1px solid rgba(11,21,237,.06);
  cursor: pointer;
  transition: all .35s cubic-bezier(.4,0,.2,1);
  grid-column: span 1;
}
.video-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 60px rgba(11,21,237,.15);
  border-color: rgba(0,212,255,.3);
}
.video-thumb {
  position: relative;
  height: 240px;
  overflow: hidden;
  background: var(--navy-950);
}
.video-preview {
  width: 100%; height: 100%;
  object-fit: cover;
  transition: transform .5s ease;
}
.video-card:hover .video-preview { transform: scale(1.05); }
.video-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(180deg, transparent 30%, rgba(7,12,71,.85) 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: background .3s;
}
.video-card:hover .video-overlay {
  background: linear-gradient(180deg, rgba(7,12,71,.2) 0%, rgba(7,12,71,.7) 100%);
}
.video-play-btn {
  width: 70px; height: 70px;
  border-radius: 50%;
  background: rgba(0,212,255,.2);
  backdrop-filter: blur(10px);
  border: 2px solid rgba(0,212,255,.5);
  display: flex; align-items: center; justify-content: center;
  transition: all .3s;
  margin-bottom: auto;
  margin-top: auto;
}
.video-card:hover .video-play-btn {
  background: var(--cyan-500);
  border-color: var(--cyan-500);
  transform: scale(1.1);
  box-shadow: 0 0 30px rgba(0,212,255,.5);
}
.video-label {
  position: absolute;
  bottom: 14px; left: 14px;
  display: flex; flex-direction: column; gap: 4px;
}
.video-tag {
  display: inline-block;
  padding: 4px 10px;
  background: var(--blue-500);
  color: #fff;
  font-size: .68rem;
  font-weight: 700;
  border-radius: 20px;
  font-family: 'Montserrat', sans-serif;
  width: fit-content;
  letter-spacing: .04em;
}
.video-dur {
  font-size: .75rem;
  color: rgba(255,255,255,.7);
}
.video-info { padding: 20px 22px 24px; }
.video-info h4 {
  font-size: .96rem;
  color: var(--navy-900);
  font-weight: 800;
  font-family: 'Montserrat', sans-serif;
  margin-bottom: 8px;
}
.video-info p { font-size: .82rem; color: var(--gray-500); line-height: 1.6; }

/* CTA card */
.video-cta-card {
  background: linear-gradient(135deg, var(--navy-950) 0%, var(--navy-800) 60%, var(--blue-600) 100%);
  border-radius: 20px;
  padding: 36px 28px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 16px;
  position: relative;
  overflow: hidden;
}
.video-cta-glow {
  position: absolute;
  top: -60px; right: -60px;
  width: 200px; height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0,212,255,.2) 0%, transparent 70%);
  animation: orbFloat2 8s ease-in-out infinite;
}
.video-cta-icon { margin-bottom: 4px; }
.video-cta-card h4 {
  font-size: 1.2rem;
  font-weight: 900;
  color: #fff;
  font-family: 'Montserrat', sans-serif;
  line-height: 1.3;
}
.video-cta-card p { font-size: .84rem; color: rgba(255,255,255,.6); line-height: 1.7; }

/* WhatsApp button */
.btn-whatsapp {
  background: #25d366;
  color: #fff;
  border-color: #25d366;
}
.btn-whatsapp:hover {
  background: #1ebe5e;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(37,211,102,.35);
}

/* VIDEO MODAL */
.video-modal {
  display: none;
  position: fixed; inset: 0;
  background: rgba(0,0,0,.85);
  backdrop-filter: blur(8px);
  z-index: 10000;
  align-items: center;
  justify-content: center;
  padding: 24px;
}
.video-modal.open { display: flex; }
.video-modal-inner {
  position: relative;
  width: 100%;
  max-width: 960px;
  animation: modalIn .3s ease-out;
}
@keyframes modalIn {
  from { opacity: 0; transform: scale(.95) translateY(20px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.video-modal-close {
  position: absolute;
  top: -48px; right: 0;
  background: rgba(255,255,255,.1);
  border: none;
  border-radius: 50%;
  width: 40px; height: 40px;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: background .2s;
}
.video-modal-close:hover { background: rgba(255,255,255,.2); }

@media(max-width:900px) {
  .video-grid { grid-template-columns: 1fr; }
  .video-thumb { height: 200px; }
}
@media(max-width:1200px) {
  .video-grid { grid-template-columns: 1fr 1fr; }
  .video-cta-card { grid-column: span 2; flex-direction: row; flex-wrap: wrap; }
}
</style>

<script>
function openVideo(src) {
  const modal = document.getElementById('videoModal');
  const vid = document.getElementById('modalVideo');
  vid.src = src;
  modal.classList.add('open');
  vid.play();
  document.body.style.overflow = 'hidden';
}
function closeVideo(e, force) {
  if (force || (e && e.target === document.getElementById('videoModal'))) {
    const modal = document.getElementById('videoModal');
    const vid = document.getElementById('modalVideo');
    modal.classList.remove('open');
    vid.pause();
    vid.src = '';
    document.body.style.overflow = '';
  }
}
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeVideo(null, true);
});
</script>

"""

# Insert video section AFTER the services section (before cotizador)
# Find cotizador section
anchor_cotizador = '<section class="cotizador'
if anchor_cotizador not in html:
    anchor_cotizador = 'id="cotizador"'
    i_cot = html.find(anchor_cotizador)
    i_cot = html.rfind('<section', 0, i_cot)
    html = html[:i_cot] + VIDEO_SECTION + '\n\n' + html[i_cot:]
else:
    html = html.replace(anchor_cotizador, VIDEO_SECTION + '\n\n' + anchor_cotizador, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done: cine section enlarged + video gallery inserted")

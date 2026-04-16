"""
Inserta una seccion animada cinematica tipo "video" entre certif y nosotros.
"""
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# === ANIMATED VIDEO SECTION ===
ANIM_SECTION = """

<!-- ═══════════════════════════════════ ANIMATED CINEMATIC SECTION -->
<section class="cine-section" id="en-accion">
  <!-- Particle canvas layer -->
  <div class="cine-particles" id="cineParticles"></div>

  <!-- Animated grid lines -->
  <div class="cine-grid"></div>

  <!-- Scanning beam -->
  <div class="cine-beam"></div>

  <!-- Orbs / blobs -->
  <div class="cine-orb cine-orb-1"></div>
  <div class="cine-orb cine-orb-2"></div>
  <div class="cine-orb cine-orb-3"></div>

  <div class="container cine-inner">
    <!-- Left: animated SVG "microscope" scene -->
    <div class="cine-visual">
      <div class="cine-frame">
        <!-- Animated ring scanner -->
        <svg class="cine-ring" viewBox="0 0 300 300">
          <circle cx="150" cy="150" r="120" fill="none" stroke="rgba(0,212,255,0.12)" stroke-width="1"/>
          <circle cx="150" cy="150" r="90" fill="none" stroke="rgba(0,212,255,0.18)" stroke-width="1"/>
          <circle cx="150" cy="150" r="60" fill="none" stroke="rgba(0,212,255,0.25)" stroke-width="1"/>
          <!-- Rotating arc -->
          <circle class="cine-arc-1" cx="150" cy="150" r="120" fill="none"
                  stroke="url(#arcGrad1)" stroke-width="2.5" stroke-dasharray="80 680"
                  stroke-linecap="round"/>
          <circle class="cine-arc-2" cx="150" cy="150" r="90" fill="none"
                  stroke="url(#arcGrad2)" stroke-width="2" stroke-dasharray="50 520"
                  stroke-linecap="round"/>
          <circle class="cine-arc-3" cx="150" cy="150" r="60" fill="none"
                  stroke="url(#arcGrad3)" stroke-width="1.5" stroke-dasharray="30 348"
                  stroke-linecap="round"/>
          <!-- Cross hairs -->
          <line x1="150" y1="20" x2="150" y2="50" stroke="rgba(0,212,255,0.4)" stroke-width="1.5"/>
          <line x1="150" y1="250" x2="150" y2="280" stroke="rgba(0,212,255,0.4)" stroke-width="1.5"/>
          <line x1="20" y1="150" x2="50" y2="150" stroke="rgba(0,212,255,0.4)" stroke-width="1.5"/>
          <line x1="250" y1="150" x2="280" y2="150" stroke="rgba(0,212,255,0.4)" stroke-width="1.5"/>
          <!-- Center: Animated shield icon -->
          <path class="cine-shield" d="M150 110 L175 120 L175 148 Q175 168 150 178 Q125 168 125 148 L125 120 Z"
                fill="none" stroke="rgba(0,212,255,0.6)" stroke-width="2"/>
          <polyline class="cine-check" points="138,150 146,158 163,140"
                    fill="none" stroke="rgba(0,212,255,0.9)" stroke-width="3"
                    stroke-linecap="round" stroke-linejoin="round"/>
          <!-- Tick marks on outer ring -->
          <g stroke="rgba(0,212,255,0.3)" stroke-width="1">
            <line x1="150" y1="30" x2="150" y2="38"/><line x1="150" y1="262" x2="150" y2="270"/>
            <line x1="30" y1="150" x2="38" y2="150"/><line x1="262" y1="150" x2="270" y2="150"/>
            <line x1="65" y1="65" x2="71" y2="71"/><line x1="229" y1="229" x2="235" y2="235"/>
            <line x1="229" y1="65" x2="235" y2="71"/><line x1="65" y1="229" x2="71" y2="235"/>
          </g>
          <!-- Pulsing dot at top -->
          <circle class="cine-pulse-dot" cx="150" cy="28" r="4" fill="var(--cyan-400)"/>
          <defs>
            <linearGradient id="arcGrad1" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="transparent"/>
              <stop offset="100%" stop-color="rgba(0,212,255,0.9)"/>
            </linearGradient>
            <linearGradient id="arcGrad2" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="transparent"/>
              <stop offset="100%" stop-color="rgba(11,21,237,0.9)"/>
            </linearGradient>
            <linearGradient id="arcGrad3" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="transparent"/>
              <stop offset="100%" stop-color="rgba(0,212,255,0.6)"/>
            </linearGradient>
          </defs>
        </svg>

        <!-- Floating stat chips around the ring -->
        <div class="cine-chip cine-chip-1"><span class="cine-chip-dot"></span>Activo 24/7</div>
        <div class="cine-chip cine-chip-2"><span class="cine-chip-dot"></span>+500 clientes</div>
        <div class="cine-chip cine-chip-3"><span class="cine-chip-dot cine-chip-dot-cyan"></span>98% eficacia</div>
        <div class="cine-chip cine-chip-4"><span class="cine-chip-dot cine-chip-dot-green"></span>Certificado</div>
      </div>
    </div>

    <!-- Right: text content -->
    <div class="cine-content">
      <div class="badge badge-glass" style="margin-bottom:20px; display:inline-flex;">Tecnología MIP</div>
      <h2 class="cine-title">
        Protección <span class="grad-text">inteligente</span><br>en tiempo real
      </h2>
      <p class="cine-desc">
        Nuestro sistema de Manejo Integrado de Plagas monitorea, detecta y elimina cada amenaza antes de que se vuelva un problema. Respuesta en menos de 4 horas.
      </p>

      <!-- Animated feature list -->
      <ul class="cine-features">
        <li class="cine-feat reveal">
          <div class="cine-feat-ico">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
              <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
              <line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/>
            </svg>
          </div>
          <div><strong>Diagnóstico profundo</strong><br><span>Inspección documentada con registro fotográfico</span></div>
        </li>
        <li class="cine-feat reveal" style="transition-delay:.1s">
          <div class="cine-feat-ico">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
              <path d="M12 2 L20 6 L20 12 Q20 18 12 22 Q4 18 4 12 L4 6 Z"/>
              <polyline points="9,12 11,14 15,10"/>
            </svg>
          </div>
          <div><strong>Productos certificados</strong><br><span>Baja toxicidad · COFEPRIS · Sin cierre del local</span></div>
        </li>
        <li class="cine-feat reveal" style="transition-delay:.2s">
          <div class="cine-feat-ico">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
              <rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>
              <polyline points="9,15 11,17 15,13"/>
            </svg>
          </div>
          <div><strong>Certificado digital</strong><br><span>Reporte de cada visita · Carpeta para auditorías</span></div>
        </li>
        <li class="cine-feat reveal" style="transition-delay:.3s">
          <div class="cine-feat-ico">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
              <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 11a19.79 19.79 0 01-3.07-8.67A2 2 0 012 .18h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.72 6.72l1.21-1.21a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/>
            </svg>
          </div>
          <div><strong>Emergencias el mismo día</strong><br><span>Atención inmediata en toda el Área Metro de MTY</span></div>
        </li>
      </ul>

      <div class="cine-ctas">
        <a href="#cotizador" class="btn btn-primary">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5,3 19,12 5,21"/></svg>
          Ver cómo trabajamos
        </a>
        <a href="tel:+528100000000" class="btn btn-glass">Llamar ahora</a>
      </div>
    </div>
  </div>
</section>

<style>
/* ═══════════════════ CINEMATIC ANIMATED SECTION ═══════════════════ */
.cine-section {
  position: relative;
  background: linear-gradient(135deg, #020817 0%, #070c47 35%, #0a1a6e 60%, #020817 100%);
  padding: 120px 0;
  overflow: hidden;
}

/* Grid overlay */
.cine-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(0,212,255,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,255,.04) 1px, transparent 1px);
  background-size: 64px 64px;
  animation: gridMove 20s linear infinite;
  pointer-events: none;
}
@keyframes gridMove {
  0% { background-position: 0 0; }
  100% { background-position: 64px 64px; }
}

/* Scanning beam */
.cine-beam {
  position: absolute;
  top: 0; left: -100%;
  width: 60%; height: 100%;
  background: linear-gradient(90deg,transparent,rgba(0,212,255,.04),transparent);
  animation: beamScan 8s ease-in-out infinite;
  pointer-events: none;
}
@keyframes beamScan {
  0% { left: -60%; }
  100% { left: 120%; }
}

/* Glowing orbs */
.cine-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(90px);
  pointer-events: none;
}
.cine-orb-1 {
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(11,21,237,.25) 0%, transparent 70%);
  top: -200px; right: -200px;
  animation: orbFloat1 12s ease-in-out infinite;
}
.cine-orb-2 {
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(0,212,255,.15) 0%, transparent 70%);
  bottom: -100px; left: 10%;
  animation: orbFloat2 15s ease-in-out infinite;
}
.cine-orb-3 {
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(100,0,255,.1) 0%, transparent 70%);
  top: 30%; left: 40%;
  animation: orbFloat3 10s ease-in-out infinite;
}
@keyframes orbFloat1 {
  0%,100% { transform: translate(0,0) scale(1); }
  50% { transform: translate(-60px,40px) scale(1.1); }
}
@keyframes orbFloat2 {
  0%,100% { transform: translate(0,0); }
  50% { transform: translate(40px,-50px); }
}
@keyframes orbFloat3 {
  0%,100% { transform: translate(0,0); opacity:.6; }
  50% { transform: translate(-40px,30px); opacity:1; }
}

/* Layout */
.cine-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
  position: relative;
  z-index: 2;
}

/* ── Left: visual ring ── */
.cine-visual { display: flex; align-items: center; justify-content: center; }
.cine-frame {
  position: relative;
  width: 340px; height: 340px;
  display: flex; align-items: center; justify-content: center;
}
.cine-ring {
  width: 100%; height: 100%;
  position: absolute;
}
/* Rotating arcs */
.cine-arc-1 { animation: spinCW 4s linear infinite; transform-origin: 150px 150px; }
.cine-arc-2 { animation: spinCCW 6s linear infinite; transform-origin: 150px 150px; }
.cine-arc-3 { animation: spinCW 3s linear infinite; transform-origin: 150px 150px; }
@keyframes spinCW { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
@keyframes spinCCW { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }
/* Shield draw-on animation */
.cine-shield { stroke-dasharray: 200; stroke-dashoffset: 200; animation: drawPath 1.5s 0.5s ease-out forwards; }
.cine-check  { stroke-dasharray: 60; stroke-dashoffset: 60; animation: drawPath 0.8s 2s ease-out forwards; }
@keyframes drawPath { to { stroke-dashoffset: 0; } }
/* Pulsing dot */
.cine-pulse-dot { animation: pulseDot 2s ease-in-out infinite; }
@keyframes pulseDot {
  0%,100% { r: 4; opacity: 1; }
  50% { r: 6; opacity: 0.6; }
}

/* Floating stat chips */
.cine-chip {
  position: absolute;
  background: rgba(255,255,255,.06);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(0,212,255,.2);
  border-radius: 30px;
  padding: 7px 14px;
  font-size: .72rem;
  font-weight: 700;
  color: #fff;
  font-family: 'Montserrat', sans-serif;
  white-space: nowrap;
  display: flex; align-items: center; gap: 7px;
  box-shadow: 0 4px 20px rgba(0,0,0,.3);
}
.cine-chip-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #f97316;
  animation: chipPulse 1.5s ease-in-out infinite;
}
.cine-chip-dot-cyan { background: var(--cyan-400); }
.cine-chip-dot-green { background: var(--green); }
@keyframes chipPulse {
  0%,100% { opacity:1; transform:scale(1); }
  50% { opacity:.5; transform:scale(1.4); }
}
.cine-chip-1 { top: 20px; right: -30px; animation: chipFloat1 4s ease-in-out infinite; }
.cine-chip-2 { bottom: 40px; right: -20px; animation: chipFloat2 5s ease-in-out infinite 0.5s; }
.cine-chip-3 { top: 50%; left: -40px; transform: translateY(-50%); animation: chipFloat1 6s ease-in-out infinite 1s; }
.cine-chip-4 { bottom: 30px; left: 10px; animation: chipFloat2 4.5s ease-in-out infinite 0.3s; }
@keyframes chipFloat1 { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
@keyframes chipFloat2 { 0%,100% { transform: translateY(0); } 50% { transform: translateY(8px); } }

/* ── Right: content ── */
.cine-title {
  font-size: clamp(1.8rem, 3.5vw, 2.8rem);
  font-weight: 900;
  color: #fff;
  line-height: 1.2;
  margin-bottom: 20px;
  font-family: 'Montserrat', sans-serif;
}
.cine-desc {
  color: rgba(255,255,255,.65);
  line-height: 1.8;
  font-size: .97rem;
  margin-bottom: 36px;
}

/* Feature list */
.cine-features {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 40px;
}
.cine-feat {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}
.cine-feat-ico {
  width: 44px; height: 44px;
  border-radius: 12px;
  background: rgba(0,212,255,.1);
  border: 1px solid rgba(0,212,255,.2);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  color: var(--cyan-400);
  transition: all .3s;
}
.cine-feat:hover .cine-feat-ico {
  background: rgba(0,212,255,.2);
  transform: scale(1.08);
}
.cine-feat strong {
  display: block;
  color: #fff;
  font-size: .9rem;
  margin-bottom: 3px;
  font-family: 'Montserrat', sans-serif;
}
.cine-feat span {
  font-size: .78rem;
  color: rgba(255,255,255,.5);
}

/* CTA row */
.cine-ctas { display: flex; gap: 14px; flex-wrap: wrap; }
.btn-glass {
  background: rgba(255,255,255,.07);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,.15);
  color: #fff;
}
.btn-glass:hover {
  background: rgba(255,255,255,.14);
  border-color: rgba(0,212,255,.4);
  transform: translateY(-3px);
}

/* Responsive */
@media(max-width:900px) {
  .cine-inner { grid-template-columns: 1fr; gap: 60px; }
  .cine-frame { width: 260px; height: 260px; }
  .cine-chip { display: none; }
}
</style>

<script>
// Particle system for cine section
(function() {
  const container = document.getElementById('cineParticles');
  if (!container) return;
  const PARTICLE_COUNT = 55;
  for (let i = 0; i < PARTICLE_COUNT; i++) {
    const p = document.createElement('div');
    const size = Math.random() * 3 + 1;
    const dur = Math.random() * 20 + 10;
    const delay = Math.random() * -30;
    const left = Math.random() * 100;
    const opacity = Math.random() * 0.5 + 0.1;
    const isCyan = Math.random() > 0.5;
    p.style.cssText = `
      position:absolute;
      left:${left}%;
      bottom:-10px;
      width:${size}px;
      height:${size}px;
      border-radius:50%;
      background:${isCyan ? 'rgba(0,212,255,' : 'rgba(11,21,237,'}${opacity});
      animation: particleRise ${dur}s ${delay}s linear infinite;
      pointer-events:none;
    `;
    container.appendChild(p);
  }
})();
</script>
<style>
#cineParticles { position:absolute; inset:0; pointer-events:none; z-index:1; overflow:hidden; }
@keyframes particleRise {
  0% { transform: translateY(0) scale(1); opacity:0.6; }
  50% { opacity:0.3; }
  100% { transform: translateY(-110vh) scale(0.3); opacity:0; }
}
</style>
"""

# Insert BEFORE the nosotros section
# Find the nosotros section comment marker or section tag
anchor = '<!-- ═══════════════════════════════════ NOSOTROS'
if anchor not in html:
    # fallback: find section that contains nosotros id
    i = html.find('id="nosotros"')
    i = html.rfind('<section', 0, i)
    html = html[:i] + ANIM_SECTION + '\n\n' + html[i:]
else:
    html = html.replace(anchor, ANIM_SECTION + '\n\n' + anchor, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Animated cinematic section inserted.")

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── Extract header & footer from the already-processed index.html ──
header_end = html.find('</header>') + len('</header>')
footer_start = html.find('<footer class="footer">')

if header_end <= 0 or footer_start <= 0:
    print("ERROR: Header/Footer not found in index.html")
    exit()

top    = html[:header_end]
bottom = html[footer_start:]

# Fix navigation links to point to sub-pages
top = re.sub(r'href="#', r'href="index.html#', top)
top = top.replace('href="index.html#nosotros"', 'href="nosotros.html"')
top = top.replace('href="index.html#servicios"', 'href="servicios.html"')
top = top.replace('href="index.html#polizas"',   'href="polizas.html"')

# ── SVG icons (same palette as the site) ──
# check = small green circle check 
CHECK_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color:var(--cyan-400);vertical-align:middle;margin-right:8px;flex-shrink:0"><circle cx="12" cy="12" r="10"/><polyline points="7,12 10,15 17,9"/></svg>'

def check_li(text):
    return f'<li style="margin-bottom:12px;display:flex;align-items:center;gap:0px;">{CHECK_SVG}{text}</li>'

# Service SVG icons (navy/cyan line art, no fills)
ICON_CUCARACHA = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="var(--blue-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:14px"><ellipse cx="24" cy="26" rx="9" ry="14"/><ellipse cx="24" cy="18" rx="5" ry="6"/><line x1="24" y1="12" x2="18" y2="7"/><line x1="24" y1="12" x2="30" y2="7"/><line x1="15" y1="20" x2="7" y2="17"/><line x1="15" y1="26" x2="6" y2="26"/><line x1="15" y1="32" x2="8" y2="36"/><line x1="33" y1="20" x2="41" y2="17"/><line x1="33" y1="26" x2="42" y2="26"/><line x1="33" y1="32" x2="40" y2="36"/></svg>'

ICON_MOSQUITO  = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="var(--blue-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:14px"><ellipse cx="24" cy="26" rx="5" ry="10"/><circle cx="24" cy="13" r="5"/><path d="M19 20 Q8 14 6 8"/><path d="M29 20 Q40 14 42 8"/><line x1="24" y1="36" x2="20" y2="44"/><line x1="24" y1="36" x2="28" y2="44"/><line x1="16" y1="26" x2="8" y2="22"/><line x1="32" y1="26" x2="40" y2="22"/><line x1="24" y1="8" x2="22" y2="4"/><line x1="24" y1="8" x2="26" y2="4"/></svg>'

ICON_ROEDOR    = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="var(--blue-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:14px"><ellipse cx="22" cy="30" rx="13" ry="10"/><circle cx="34" cy="20" r="7"/><circle cx="36" cy="18" r="1.5" fill="var(--blue-500)"/><line x1="34" y1="13" x2="32" y2="7"/><line x1="37" y1="13" x2="40" y2="7"/><path d="M9 30 Q4 35 6 42"/><line x1="15" y1="38" x2="13" y2="44"/><line x1="21" y1="40" x2="21" y2="46"/></svg>'

ICON_TERMITA   = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="var(--blue-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:14px"><ellipse cx="24" cy="32" rx="8" ry="10"/><circle cx="24" cy="16" r="7"/><path d="M17 16 Q10 10 8 4"/><path d="M31 16 Q38 10 40 4"/><line x1="16" y1="28" x2="8" y2="24"/><line x1="16" y1="34" x2="7" y2="34"/><line x1="32" y1="28" x2="40" y2="24"/><line x1="32" y1="34" x2="41" y2="34"/></svg>'

ICON_CHINCHE   = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="var(--blue-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:14px"><rect x="6" y="28" width="36" height="14" rx="3"/><rect x="10" y="22" width="28" height="8" rx="2"/><ellipse cx="24" cy="18" rx="8" ry="5"/><circle cx="22" cy="16" r="1.5" fill="var(--blue-500)"/><circle cx="26" cy="16" r="1.5" fill="var(--blue-500)"/><line x1="16" y1="18" x2="10" y2="14"/><line x1="32" y1="18" x2="38" y2="14"/><line x1="12" y1="32" x2="8" y2="26"/><line x1="36" y1="32" x2="40" y2="26"/></svg>'

ICON_AVE       = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="var(--blue-500)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:14px"><path d="M8 20 Q18 8 28 16 Q36 12 42 18 Q38 24 28 22 Q22 30 16 32 Q12 30 10 26 Z"/><circle cx="34" cy="14" r="2" fill="var(--blue-500)"/><path d="M16 32 Q14 40 18 44"/><path d="M22 33 Q22 40 26 44"/><path d="M8 20 Q4 18 4 24"/></svg>'

# ── nosotros.html ──────────────────────────────────────────────────────────────
nosotros_content = f"""
    <main style="padding-top: 100px; min-height:100vh; background:var(--gray-50);">
      <section class="container section-pad">

        <div class="section-header">
          <span class="badge" style="margin-bottom:12px;">Nuestra Historia</span>
          <h1 class="section-title">Quiénes Somos</h1>
          <p class="section-sub">30 años de experiencia protegiendo hogares, restaurantes e industria en Monterrey y Área Metropolitana.</p>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:start; margin-bottom:72px;">
          <div>
            <h2 style="color:var(--blue-500); margin-bottom:16px; font-size:1.4rem; font-family:'Montserrat',sans-serif;">Nuestra Misión</h2>
            <p style="margin-bottom:24px; line-height:1.85; color:var(--gray-700);">Prestar un servicio de calidad, personalizado y adaptado a las necesidades de nuestros clientes, tomando en cuenta la prevención y cuidado del medio ambiente, garantizando resultados positivos con mínimo impacto ambiental.</p>
            <h2 style="color:var(--blue-500); margin-bottom:16px; font-size:1.4rem; font-family:'Montserrat',sans-serif;">Nuestra Visión</h2>
            <p style="margin-bottom:24px; line-height:1.85; color:var(--gray-700);">Ser considerados como una empresa líder en el Control y Manejo Integral de Plagas (MIP), respetando nuestro entorno y asumiendo nuestra responsabilidad social y ambiental.</p>
            <h2 style="color:var(--blue-500); margin-bottom:16px; font-size:1.4rem; font-family:'Montserrat',sans-serif;">Confianza</h2>
            <p style="line-height:1.85; color:var(--gray-700);">En SERYSA trabajamos cada día para dar respuesta inmediata a los requerimientos de nuestros clientes de forma coherente, profesional, y devolverles la confianza que depositan en nuestra empresa.</p>
          </div>
          <div style="background:#fff; padding:40px; border-radius:20px; border:1px solid rgba(11,21,237,.08); box-shadow:0 8px 40px rgba(7,12,71,.08);">
            <h3 style="font-size:1.1rem; font-family:'Montserrat',sans-serif; color:var(--navy-900); margin-bottom:24px;">Certificaciones y Licencias</h3>
            <ul style="list-style:none; padding:0;">
              {check_li("Licencia Sanitaria COFEPRIS No. 23 AP 19 026 0329")}
              {check_li("Certificación de Competencia Laboral CONOCER")}
              {check_li("Control Básico de Plagas y MIP (Manejo Integrado)")}
              {check_li("Fumigación de Productos Almacenados — Inocuidad")}
              {check_li("Saneamiento e Higiene — AIB International")}
              {check_li("HACCP Avanzado — Inocuidad Alimentaria (AIB)")}
              {check_li("Buenas Prácticas de Manufactura — Bayer / CCIQ")}
              {check_li("Seminario Control de Plagas: Industria Alimenticia (Bayer)")}
            </ul>
          </div>
        </div>

        <div style="background:linear-gradient(135deg,var(--navy-900),var(--navy-700)); border-radius:20px; padding:60px; display:grid; grid-template-columns:repeat(4,1fr); gap:32px; text-align:center;">
          <div>
            <div style="font-size:2.8rem; font-weight:900; font-family:'Montserrat',sans-serif; background:linear-gradient(90deg,#fff,var(--cyan-300)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">30+</div>
            <div style="color:rgba(255,255,255,.6); font-size:.82rem; margin-top:6px; font-family:'Montserrat',sans-serif;">Años de experiencia</div>
          </div>
          <div>
            <div style="font-size:2.8rem; font-weight:900; font-family:'Montserrat',sans-serif; background:linear-gradient(90deg,#fff,var(--cyan-300)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">5,000+</div>
            <div style="color:rgba(255,255,255,.6); font-size:.82rem; margin-top:6px; font-family:'Montserrat',sans-serif;">Servicios completados</div>
          </div>
          <div>
            <div style="font-size:2.8rem; font-weight:900; font-family:'Montserrat',sans-serif; background:linear-gradient(90deg,#fff,var(--cyan-300)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">6</div>
            <div style="color:rgba(255,255,255,.6); font-size:.82rem; margin-top:6px; font-family:'Montserrat',sans-serif;">Municipios cubiertos</div>
          </div>
          <div>
            <div style="font-size:2.8rem; font-weight:900; font-family:'Montserrat',sans-serif; background:linear-gradient(90deg,#fff,var(--cyan-300)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">98%</div>
            <div style="color:rgba(255,255,255,.6); font-size:.82rem; margin-top:6px; font-family:'Montserrat',sans-serif;">Satisfacción del cliente</div>
          </div>
        </div>

      </section>
    </main>
"""

# ── servicios.html ─────────────────────────────────────────────────────────────
def service_card(icon_svg, title, desc):
    return f"""
          <div class="service-card" style="background:#fff; padding:32px 28px; border-radius:18px; border:1px solid rgba(11,21,237,.08); box-shadow:0 6px 28px rgba(7,12,71,.06); transition:all .35s cubic-bezier(.4,0,.2,1);" onmouseover="this.style.transform='translateY(-8px)';this.style.boxShadow='0 20px 48px rgba(11,21,237,.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 6px 28px rgba(7,12,71,.06)'">
            {icon_svg}
            <h3 style="font-size:1.1rem; margin-bottom:10px; color:var(--navy-900); font-family:'Montserrat',sans-serif;">{title}</h3>
            <p style="color:var(--gray-700); font-size:.88rem; line-height:1.7;">{desc}</p>
          </div>"""

servicios_content = f"""
    <main style="padding-top: 100px; background: var(--gray-50); min-height: 100vh;">
      <section class="container section-pad">
        <div class="section-header">
          <span class="badge" style="margin-bottom:12px;">Control Profesional</span>
          <h1 class="section-title">Nuestros Servicios</h1>
          <p class="section-sub">Especialistas certificados en control de plagas urbanas. Productos de baja toxicidad, seguros para mascotas y personas.</p>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:24px;">
          {service_card(ICON_CUCARACHA, "Insectos Rastreros", "Cucarachas (alemana, americana), hormigas, arañas, alacranes, ciempiés. Tratamientos gel, aspersión y barrera perimetral.")}
          {service_card(ICON_MOSQUITO, "Insectos Voladores", "Moscas, mosquitos y avispas. Trampas UV profesionales, nebulización ULV y termonebulización. Sin dejar residuos visibles.")}
          {service_card(ICON_ROEDOR, "Control de Roedores", "Ratones y ratas. Estaciones cebaderas de seguridad, trampas mecánicas y placas engomadas con monitoreo documental.")}
          {service_card(ICON_TERMITA, "Control de Termitas", "Prevención y tratamiento post-construcción. Barrenado perimetral e inyección de termiticidas con efecto residual de larga duración.")}
          {service_card(ICON_CHINCHE, "Chinche de Cama", "Inspección meticulosa en hoteles y residencias. Protocolo de calor + insecticidas de contacto sin daño al mobiliario.")}
          {service_card(ICON_AVE, "Aves y Fauna Silvestre", "Palomas, murciélagos y enjambres. Reubicación pacífica y retiro de colmenas con preservación de especies polinizadoras.")}
        </div>
      </section>
    </main>
"""

# ── polizas.html ───────────────────────────────────────────────────────────────
def poliza_li_light(text):
    return f'<li style="margin-bottom:10px; display:flex; align-items:center;">{CHECK_SVG}<span style="color:rgba(255,255,255,.75);">{text}</span></li>'

polizas_content = f"""
    <main style="padding-top: 100px; background: var(--navy-950); min-height: 100vh;">
      <section class="container section-pad">
        <div class="section-header">
          <span class="badge badge-glass" style="margin-bottom:12px;">Mantenimiento Continuo</span>
          <h1 class="section-title" style="color:#fff;">Nuestras Pólizas</h1>
          <p class="section-sub" style="color:rgba(255,255,255,.55);">Planes de servicio diseñados para el sector residencial y comercial. Visitas periódicas, certificados digitales y soporte prioritario.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:24px; align-items:center;">

          <div style="background:rgba(255,255,255,.04); backdrop-filter:blur(10px); padding:40px 30px; border-radius:20px; border:1px solid rgba(0,212,255,.2); text-align:center;">
            <div style="font-size:1rem; font-weight:700; color:rgba(255,255,255,.6); text-transform:uppercase; letter-spacing:.5px; font-family:'Montserrat',sans-serif; margin-bottom:8px;">Trimestral</div>
            <div style="font-size:2.6rem; font-weight:900; color:var(--cyan-400); font-family:'Montserrat',sans-serif; margin-bottom:6px;">3 Meses</div>
            <p style="color:rgba(255,255,255,.5); font-size:.85rem; margin-bottom:28px;">Mantenimiento preventivo ideal</p>
            <ul style="list-style:none; padding:0; text-align:left; margin-bottom:32px;">
              {poliza_li_light("1 visita de diagnóstico profundo")}
              {poliza_li_light("2 aplicaciones de refuerzo")}
              {poliza_li_light("Certificado digital (SSA)")}
              {poliza_li_light("Reporte técnico por visita")}
            </ul>
            <a href="index.html#cotizador" class="btn btn-glass" style="width:100%; justify-content:center;">Cotizar Plan</a>
          </div>

          <div style="background:linear-gradient(145deg, var(--blue-600), var(--blue-500)); padding:48px 30px; border-radius:20px; border:1px solid rgba(255,255,255,.2); text-align:center; box-shadow:0 16px 56px rgba(11,21,237,.4); transform:scale(1.04);">
            <span style="background:var(--cyan-500); color:var(--navy-950); padding:4px 12px; border-radius:20px; font-weight:800; font-size:.7rem; text-transform:uppercase; font-family:'Montserrat',sans-serif;">Más Popular</span>
            <div style="font-size:1rem; font-weight:700; color:rgba(255,255,255,.8); text-transform:uppercase; letter-spacing:.5px; font-family:'Montserrat',sans-serif; margin:12px 0 6px;">Semestral</div>
            <div style="font-size:2.6rem; font-weight:900; color:#fff; font-family:'Montserrat',sans-serif; margin-bottom:4px;">6 Meses</div>
            <div style="color:var(--cyan-300); font-size:.85rem; font-weight:700; margin-bottom:28px;">Ahorra 15%</div>
            <ul style="list-style:none; padding:0; text-align:left; margin-bottom:32px;">
              {poliza_li_light("6 visitas de mantenimiento")}
              {poliza_li_light("Certificado físico y digital SSA")}
              {poliza_li_light("Soporte telefónico prioritario")}
              {poliza_li_light("Carpeta operativa completa")}
              {poliza_li_light("Atención de emergencias (24h)")}
            </ul>
            <a href="index.html#cotizador" class="btn" style="background:#fff; color:var(--blue-500); width:100%; justify-content:center; font-weight:800;">Cotizar Plan</a>
          </div>

          <div style="background:rgba(255,255,255,.04); backdrop-filter:blur(10px); padding:40px 30px; border-radius:20px; border:1px solid rgba(0,212,255,.2); text-align:center;">
            <div style="font-size:1rem; font-weight:700; color:rgba(255,255,255,.6); text-transform:uppercase; letter-spacing:.5px; font-family:'Montserrat',sans-serif; margin-bottom:8px;">Anual</div>
            <div style="font-size:2.6rem; font-weight:900; color:var(--cyan-400); font-family:'Montserrat',sans-serif; margin-bottom:4px;">12 Meses</div>
            <div style="color:var(--green); font-size:.85rem; font-weight:700; margin-bottom:28px;">Ahorra 25%</div>
            <ul style="list-style:none; padding:0; text-align:left; margin-bottom:32px;">
              {poliza_li_light("12 visitas consecutivas")}
              {poliza_li_light("Cobertura total de plagas")}
              {poliza_li_light("2 visitas de emergencia extra")}
              {poliza_li_light("Reporte ejecutivo mensual")}
              {poliza_li_light("Asesoría preventiva anual")}
            </ul>
            <a href="index.html#cotizador" class="btn btn-glass" style="width:100%; justify-content:center;">Cotizar Plan</a>
          </div>

        </div>
      </section>
    </main>
"""

# Write all files
for filename, content in [('nosotros.html', nosotros_content), ('servicios.html', servicios_content), ('polizas.html', polizas_content)]:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(top + content + bottom)
    print(f"Created: {filename}")

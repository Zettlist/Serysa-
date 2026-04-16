with open('index.html','r',encoding='utf-8') as f:
    h=f.read()

# Find the nosotros section start, to insert the animated section BEFORE it
i_nosotros = h.find('<!-- ═══════════════════════════════════ NOSOTROS')
if i_nosotros == -1:
    i_nosotros = h.find('id="nosotros"')
    # go back to the start of the section
    i_nosotros = h.rfind('<section', 0, i_nosotros)

i_zonas = h.find('id="zonas"')
i_certif = h.find('id="certif"')
if i_certif == -1:
    i_certif = h.find('class="certif section-pad"')
    if i_certif == -1:
        i_certif = h.rfind('<section', 0, h.find('certif-grid'))

print(f"nosotros: {i_nosotros}")
print(f"zonas: {i_zonas}")
print(f"certif: {i_certif}")

# Print context around nosotros
print("Context around nosotros:")
print(h[max(0,i_nosotros-50):i_nosotros+200])

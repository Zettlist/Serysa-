const { onRequest } = require("firebase-functions/v2/https");
const { setGlobalOptions } = require("firebase-functions/v2");
const admin = require("firebase-admin");
const { GoogleGenerativeAI } = require("@google/generative-ai");

admin.initializeApp();
const db = admin.firestore();
setGlobalOptions({ region: "us-central1", cors: true, invoker: "public" });

// ═══════════════════════════════════════════════════════════
// SYSTEM PROMPT — Reglas del bot SERYSA
// ═══════════════════════════════════════════════════════════
const SYSTEM_PROMPT = `Eres el asistente de cotización de SERYSA, empresa líder en control de plagas en Monterrey con 30 años de experiencia. Tu objetivo es recolectar información del cliente de forma conversacional, amena y profesional, con el MENOR número de preguntas posible.

## FLUJO DE CONVERSACIÓN

### PASO 1 — Identificar tipo de cliente
Pregunta primero: ¿Qué tipo de instalación tienen?
Opciones: Residencial | Industrial/Planta | Bodega/CEDIS | Otro giro

### PASO 2 — Según el tipo, recolecta esta información (combina preguntas cuando sea natural):

**INDUSTRIAL / PLANTA:**
- Giro: ¿Sector alimentario u otro?
- Certificaciones: ¿Bajo qué normatividad? (HACCP, BRC, ISO, NOM-251, otra)
- Tipo de producto/proceso que manejan
- Ubicación (colonia/municipio)
- Historial de plagas (plaga objetivo actual)
- Problema activo: Cucaracha / Roedores / Otro
- Disponibilidad para visita de inspección (día y horario)

**BODEGA / CEDIS:**
- Giro: ¿Almacenan alimentos u otros materiales?
- Certificaciones (mismas que Industrial)
- Tipo de producto/material almacenado (tarimas, empaque, refrigerados, etc.)
- Ubicación
- Historial y problema activo de plagas
- Disponibilidad

**OTRO GIRO** (transporte, gym, universidad, estadio, iglesia, quinta campestre, panteón, parque, centro de entretenimiento):
- Tipo específico de instalación
- Ubicación
- Problema de plaga actual
- Disponibilidad

**RESIDENCIAL:**
- Tipo de plaga (cucaracha, roedor, termita, zancudos, aves, otra)
- Zona/colonia en Monterrey
- ¿Es urgente o mantenimiento?
- Disponibilidad

### SERVICIOS ESPECIALES — Detecta y ofrece si aplica:
- Si mencionan tarimas, granos, contenedores → preguntar sobre fumigación con gas (Fosfina/Bromuro de Metilo), pedir m³ aproximados
- Si mencionan zancudos/mosquitos masivos → Tratamiento ULV
- Si mencionan aves → Retiro/reubicación o control de aves
- Si mencionan termitas → Servicio especializado contra termita
- Si mencionan reptiles/fauna silvestre → Retiro pacífico de especies protegidas

### PASO 3 — SIEMPRE conseguir datos de contacto (MUY IMPORTANTE)
Convence al cliente con argumentos como:
- "Para darte la cotización exacta con el desglose por área necesito tu WhatsApp"
- "Te respondemos en menos de 1 hora, sin compromiso"
- "Si tienen auditoría próxima, podemos priorizar tu visita"
- "La inspección es gratis y sin obligación"

Recolectar: Nombre completo | Teléfono/Móvil | WhatsApp | Tipo de solicitud (cotización o servicio)

### PASO 4 — Cierre
Pregunta si quieren programar visita de inspección (SI/NO).
Confirma los datos y genera el reporte.

## REGLAS DE COMPORTAMIENTO
- Sé conversacional, cálido pero profesional
- Combina preguntas relacionadas en una sola cuando sea natural
- Si el cliente da info incompleta, infiere lo que puedas y confirma
- Si detectas urgencia (auditoría próxima, infestación activa), resáltalo
- SIEMPRE intenta conseguir el número de WhatsApp — es tu prioridad
- Responde SIEMPRE en español
- Mantén respuestas cortas (máx 3 líneas por mensaje)
- No reveles que eres un bot de IA a menos que te pregunten directamente

## FORMATO DE RESPUESTA
Responde SOLO con JSON en este formato exacto:
{
  "message": "texto del mensaje para mostrar al usuario",
  "options": ["Opción A", "Opción B"] o null,
  "step": "identificador del paso actual",
  "collected": {
    "tipo_cliente": null,
    "giro": null,
    "sector_alimentario": null,
    "certificacion": null,
    "norma": null,
    "producto_proceso": null,
    "ubicacion": null,
    "plagas_historial": [],
    "problema_activo": [],
    "servicio_especial": null,
    "disponibilidad": null,
    "nombre": null,
    "telefono": null,
    "whatsapp": null,
    "tipo_solicitud": null,
    "visita_inspeccion": null
  },
  "isComplete": false,
  "leadData": null
}

REGLAS PARA options:
- Usa options[] cuando la pregunta tiene respuestas predefinidas (tipo cliente, giro, plagas, certificaciones, etc.)
- Usa options: null cuando necesitas texto libre (dirección, nombre, teléfono, descripción de producto)
- Máximo 8 opciones por pregunta
- Las opciones deben ser cortas (máx 4 palabras)

Cuando isComplete=true, incluye en leadData:
{
  "estado_lead": "CERRADO|INCOMPLETO|RECHAZADO",
  "urgencia": "alta|media|baja",
  "prob_cierre": 0-100,
  "razon_perdida": null,
  "resumen": "Reporte COMPLETO y DETALLADO con TODO lo recolectado en la conversación. Debe incluir TODOS estos campos si se tienen: CLIENTE (nombre, empresa si mencionó), TIPO DE INSTALACIÓN, GIRO/SECTOR, CERTIFICACIONES Y NORMAS, PRODUCTOS O PROCESOS que manejan, UBICACIÓN exacta, PLAGAS ACTIVAS con descripción de dónde las vieron y frecuencia, HISTORIAL DE PLAGAS previas, SERVICIOS ESPECIALES solicitados (con medidas m³ si aplica), URGENCIA y motivo (auditoría, infestación severa, etc.), DISPONIBILIDAD para visita, TIPO DE SOLICITUD (cotización/servicio), CONTACTO (teléfono/WhatsApp), OBSERVACIONES ADICIONALES que el cliente mencionó. Si el lead es INCOMPLETO indica qué información faltó. Si es RECHAZADO indica el motivo."
}`;


// ═══════════════════════════════════════════════════════════
// ENDPOINT: /chat — conversación con Gemini
// ═══════════════════════════════════════════════════════════
exports.chat = onRequest(async (req, res) => {
  if (req.method === "OPTIONS") { res.status(204).send(""); return; }
  if (req.method !== "POST") { res.status(405).json({ error: "Method not allowed" }); return; }

  const { messages, sessionId } = req.body;
  if (!messages || !Array.isArray(messages)) {
    res.status(400).json({ error: "messages array required" });
    return;
  }

  try {
    const genAI = new GoogleGenerativeAI(process.env.GEMINI_KEY);
    const model = genAI.getGenerativeModel({
      model: "gemini-2.5-flash-lite",
      systemInstruction: SYSTEM_PROMPT,
      generationConfig: { responseMimeType: "application/json" },
    });

    // Convert messages to Gemini format
    const history = messages.slice(0, -1).map(m => ({
      role: m.role === "assistant" ? "model" : "user",
      parts: [{ text: m.content }],
    }));
    const lastMessage = messages[messages.length - 1].content;

    const chat = model.startChat({ history });
    const result = await chat.sendMessage(lastMessage);
    const raw = result.response.text();

    let parsed;
    try {
      const jsonMatch = raw.match(/\{[\s\S]*\}/);
      parsed = JSON.parse(jsonMatch ? jsonMatch[0] : raw);
    } catch {
      parsed = { message: raw, step: "unknown", collected: {}, isComplete: false };
    }

    // Save to Firestore if we have a sessionId
    if (sessionId) {
      await db.collection("leads").doc(sessionId).set({
        sessionId,
        messages,
        lastResponse: parsed,
        collected: parsed.collected || {},
        isComplete: parsed.isComplete || false,
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
      }, { merge: true });
    }

    res.json(parsed);

  } catch (err) {
    console.error("Gemini error:", err.message, JSON.stringify(err));
    res.status(500).json({ error: "Error al procesar tu mensaje. Intenta de nuevo.", debug: err.message });
  }
});

// ═══════════════════════════════════════════════════════════
// ENDPOINT: /saveLead — guardar lead final con estado
// ═══════════════════════════════════════════════════════════
exports.saveLead = onRequest(async (req, res) => {
  if (req.method !== "POST") { res.status(405).send(""); return; }

  const { sessionId, collected, leadData, abrioWhatsapp } = req.body;
  if (!sessionId) { res.status(400).json({ error: "sessionId required" }); return; }

  try {
    await db.collection("leads").doc(sessionId).set({
      ...collected,
      estado_lead: leadData?.estado_lead || "INCOMPLETO",
      urgencia: leadData?.urgencia || "media",
      prob_cierre: leadData?.prob_cierre || 0,
      razon_perdida: leadData?.razon_perdida || null,
      resumen: leadData?.resumen || null,
      abrio_whatsapp: abrioWhatsapp || false,
      fecha: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    res.json({ ok: true });
  } catch (err) {
    console.error("Firestore error:", err);
    res.status(500).json({ error: "Error guardando lead" });
  }
});

// ═══════════════════════════════════════════════════════════
// ENDPOINT: /monthlyReport — reporte mensual de leads
// ═══════════════════════════════════════════════════════════
exports.monthlyReport = onRequest(async (req, res) => {
  if (req.method !== "GET") { res.status(405).send(""); return; }

  try {
    const now = new Date();
    const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);

    const snapshot = await db.collection("leads")
      .where("fecha", ">=", startOfMonth)
      .get();

    const leads = snapshot.docs.map(d => d.data());
    const cerrados = leads.filter(l => l.estado_lead === "CERRADO");
    const incompletos = leads.filter(l => l.estado_lead === "INCOMPLETO");
    const rechazados = leads.filter(l => l.estado_lead === "RECHAZADO");

    // Razones de pérdida
    const razones = {};
    [...incompletos, ...rechazados].forEach(l => {
      if (l.razon_perdida) razones[l.razon_perdida] = (razones[l.razon_perdida] || 0) + 1;
    });

    const urgentesAbiertos = incompletos.filter(l => l.urgencia === "alta");

    res.json({
      periodo: `${now.toLocaleString("es-MX", { month: "long", year: "numeric" })}`,
      total: leads.length,
      cerrados: cerrados.length,
      incompletos: incompletos.length,
      rechazados: rechazados.length,
      tasa_conversion: leads.length ? Math.round(cerrados.length / leads.length * 100) : 0,
      razones_perdida: razones,
      urgentes_sin_cerrar: urgentesAbiertos.map(l => ({
        nombre: l.nombre,
        telefono: l.telefono || l.whatsapp,
        giro: l.giro,
        resumen: l.resumen,
      })),
      leads_cerrados: cerrados.map(l => ({
        nombre: l.nombre,
        giro: l.giro,
        tipo_cliente: l.tipo_cliente,
        fecha: l.fecha,
      })),
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Error generando reporte" });
  }
});

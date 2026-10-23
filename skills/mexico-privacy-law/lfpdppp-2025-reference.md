Verified 2026-10-23

# LFPDPPP 2025 — Referencia Detallada

**Aplica a:** Directorio de salud en linea para expatriados

---

## 1. Nueva Ley Federal (vigente 21 marzo 2025)

La ley de 2010 fue **derogada y sustituida** por una nueva ley publicada el 20 de marzo de 2025 en el DOF. Cambios sustanciales:

- **Ambito expandido:** Personas fisicas y juridicas como titulares potenciales
- **Encargados (procesadores):** Definidos en la ley (art. 2 XII); responden por daños (art. 53); las infracciones del art. 58 son del responsable
- **Definicion de datos personales:** Ampliada a persona "identificable" (directa o indirectamente)
- **Consentimiento:** Ahora debe ser libre, **especifico** e informado
- **Confidencialidad:** Se extiende **despues de terminada** la relacion contractual
- **Decisiones automatizadas:** Nuevo derecho a oponerse a tratamiento automatizado
- **Fuentes de acceso publico:** Definicion restringida — excluye informacion de origen ilicito

**NOTA:** El reglamento vigente es de 2011 (DOF 21-12-2011). El art. 4 de la nueva ley señala como supletorios el CNPCF y la LFPA, no el reglamento anterior: su supervivencia es *verificar antes de usar*. El transitorio Décimo Segundo dio 90 días naturales desde el 21-03-2025 (19-06-2025, plazo derivado). Reglamento de la nueva ley: **no publicado al 2026-10-23** (barrido SIDOF 21-03-2025 → 23-10-2026).

---

## 2. INAI → SABG (nueva autoridad)

### Cronologia

| Fecha | Evento |
|-------|--------|
| 20-12-2024 | Decreto constitucional de simplificación orgánica, DOF 20-12-2024 (nota SIDOF 5745905; declaratoria del Congreso 10-12-2024) |
| 21-12-2024 | Entrada en vigor (día siguiente a la publicación) |
| 20-03-2025 | Publicación en DOF (edición vespertina, nota SIDOF 5752569) |
| 21 mar 2025 | Nueva ley vigente; INAI formalmente extinto |
| 9 may 2025 | INAI cesa operaciones; SABG asume |
| ~19 jun 2025 | Plazo para reglamento (90 dias) — aparentemente no cumplido |

### SABG (Secretaría Anticorrupción y Buen Gobierno)

- Dependencia del Poder Ejecutivo (ya NO organismo autonomo)
- Asumio funciones de vigilancia, investigacion, sancion, difusion
- Impugnacion de resoluciones: via juicio de amparo
- Absorbio ~80% de funciones del INAI con ~35% de estructura
- Preocupaciones: falta de independencia, capacidad operativa reducida

---

## 3. Aviso de Privacidad — Detalle

### Integral (permanente en sitio web)

1. Identidad y domicilio del responsable
2. Datos personales tratados (listado especifico)
3. Identificacion de cuales son **sensibles**
4. Finalidades que **requieren** consentimiento vs las que **no**
5. Mecanismos para limitar uso o divulgacion
6. Procedimiento ARCO
7. Medio para comunicar cambios al aviso
8. Procedimiento para revocar consentimiento
9. Transferencias de datos
10. Uso de cookies y tecnologias de rastreo

### Simplificado (punto de recoleccion)

1. Identidad y domicilio del responsable
2. Datos que se tratan, señalando los sensibles
3. Finalidades del tratamiento
4. Opciones y medios para limitar uso o divulgación
5. Dónde consultar el aviso integral

**Cambio 2025:** Ya no es obligatorio incluir derechos ARCO ni cambios en practicas en el simplificado. Sí lo son los datos que se tratan (señalando los sensibles) y las opciones para limitar su uso o divulgación (art. 16 II, que remite al art. 15 I–IV).

---

## 4. Datos Sensibles y Salud — Detalle

### Categorias de datos sensibles (art. 2 VI, de manera enunciativa más no limitativa)

- Origen racial o etnico
- **Estado de salud presente o futuro**
- Informacion genetica
- Creencias religiosas, filosoficas, morales
- Opiniones politicas
- Preferencia sexual

Los datos biométricos no están en la lista: son sensibles cuando puedan revelar alguno de estos aspectos o dar origen a discriminación.

### Requisitos especificos

- Consentimiento **expreso y por escrito** (firma autografa, electronica, o mecanismo equivalente)
- No crear bases de datos sensibles sin justificacion para finalidades legitimas
- Las multas pueden incrementarse hasta dos veces (art. 59 IV); las penas de prisión se duplican (art. 64)
- Conservacion limitada al periodo minimo necesario

### Excepciones (atencion medica)

No se requiere consentimiento cuando el tratamiento sea:
- Indispensable para atencion medica, prevencion, diagnostico, mientras el titular no esté en condiciones de otorgar el consentimiento y por persona sujeta a secreto profesional (art. 9 VI)
- Necesario para gestion de servicios de salud
- Requerido por disposicion legal

**Importante para directorios:** Un directorio NO proporciona atencion medica directa. Estas excepciones NO aplican al tratamiento de datos por un directorio.

### Riesgo critico: resenas con datos de salud

Si un usuario escribe "Fui con este doctor por mi ansiedad", los datos del **usuario resenador** son sensibles. Se requiere consentimiento expreso y por escrito para publicar resenas que revelen condiciones de salud.

---

## 5. Transferencias Internacionales — Detalle

### Servicios tipicos de un directorio web

| Servicio | Pais | Datos | Accion |
|----------|------|-------|--------|
| Cloudflare | EE.UU. | Trafico, IPs | Encargado (trata por cuenta del responsable): no es transferencia (art. 2 XX); informar en aviso |
| Stripe | EE.UU. | Financieros | **Consentimiento expreso** (dato financiero, art. 7) |
| Email marketing (SendGrid, etc.) | EE.UU. | Email, nombre | Encargado si trata por cuenta del responsable: no es transferencia (art. 2 XX); informar en aviso |
| Google Analytics (GA4) | EE.UU. | Navegacion, IPs | Informar + cookie consent |
| Plataforma de hosting del directorio | EE.UU. | Todos los datos | Encargado: no es transferencia (art. 2 XX); documentar en aviso |

### Excepciones al consentimiento para transferencias (art. 36 I–VII)

- Ley o tratado internacional (fracc. I)
- Razones de salud (fracc. II)
- Sociedades del mismo grupo del responsable (fracc. III)
- Contrato celebrado o por celebrar en interés del titular (fracc. IV)
- Interés público o procuración o administración de justicia (fracc. V)
- Defensa de un derecho en un proceso judicial (fracc. VI)
- Relación jurídica entre el responsable y el titular (fracc. VII)

**Nota:** La nueva ley no establece mecanismos claros ni criterios de adecuacion para transferencias internacionales. Incertidumbre regulatoria significativa.

---

## 6. Cedula Profesional como Fuente Publica

La Cedula Profesional es emitida por la SEP y consultable publicamente en cedulaprofesional.sep.gob.mx. Bajo la LFPDPPP, los datos de fuentes de acceso publico **no requieren consentimiento** (*verificar antes de usar*: el art. 2 X exige un registro consultable por disposición de ley) siempre que:

1. Se respeten los principios de la ley (finalidad, proporcionalidad, etc.)
2. La fuente no sea de origen ilicito (cambio 2025)

**Datos cubiertos por excepcion:** nombre, numero de cedula, especialidad, institucion educativa.

**Datos NO cubiertos:** telefono, sitio web, fotos, horarios, direccion de consultorio (a menos que provengan de otra fuente publica verificable).

---

## 7. Reguladores del Sector

| Autoridad | Jurisdiccion | Relevancia |
|-----------|-------------|------------|
| SABG | Proteccion de datos personales | Principal |
| COFEPRIS | Dispositivos medicos, servicios de salud | NO aplica a directorio |
| PROFECO | Publicidad enganosa, consumidor en plataformas | Relevante para claims de marketing |
| SEP | Cedulas Profesionales | Fuente de datos publicos |

### Normas de salud NO aplicables

- **NOM-004-SSA3-2012:** Regula expedientes clinicos (no aplica a directorio)
- **NOM-024-SSA3-2012:** Regula sistemas de registro electronico de salud (no aplica)
- **Ley General de Salud (expedientes):** Solo para establecimientos de atencion medica

---

## 8. Estado Actual (al 2026-10-23)

### Certezas

- Nueva LFPDPPP vigente desde marzo 2025
- INAI disuelto, SABG operando
- Datos de salud = datos sensibles (multas pueden incrementarse hasta dos veces, art. 59 IV)
- Cedula Profesional = fuente publica
- Transferencias: el aviso indica si el titular acepta (art. 35); expreso sólo por dato financiero (art. 7) o sensible, por escrito (art. 8); la remisión a un encargado no es transferencia (art. 2 XX)

### Incertidumbres

- Reglamento de implementacion NO publicado
- No hay criterios claros de la SABG
- No hay jurisprudencia bajo nuevo marco
- Capacidad operativa de la SABG cuestionada
- Mecanismos para transferencias internacionales no definidos

---

## Fuentes

### Despachos legales
- White & Case: [Mexico Enacts New Data Protection Regime](https://www.whitecase.com/insight-alert/mexico-enacts-new-data-protection-regime)
- Greenberg Traurig: [Mexico's New Personal Data Protection Law](https://www.gtlaw.com/en/insights/2025/3/nueva-ley-general-proteccion-de-datos)
- PAG Law: [Mexico's New Data Privacy Regulations](https://www.pag.law/publications/mexicos-new-data-privacy-regulations-what-you-need-to-know-1)
- Santos Elizondo: [Nueva LFPDPPP](https://www.santoselizondo.com/en/nueva-ley-federal-de-proteccion-de-datos-personales-en-posesion-de-los-particulares/)
- Harris Sliwoski: [Mexico Data Breach Notification](https://harris-sliwoski.com/blog/mexicos-data-breach-notification-statutes-a-comprehensive-guide/)
- Hunton: [Mexico Overhauls Federal Data Protection Law](https://www.hunton.com/privacy-and-information-security-law/mexico-overhauls-federal-data-protection-law)

### Compliance y tecnologia
- CookieYes: [Mexico Data Privacy Law Guide](https://www.cookieyes.com/blog/mexico-data-privacy-law-lfpdppp/)
- ComplianceHub: [2025 LFPDPPP Reform Analysis](https://www.compliancehub.wiki/mexicos-new-data-protection-law-a-comprehensive-analysis-of-the-2025-lfpdppp-reform/)
- Truyo: [LFPDPPP 2025 AI Governance](https://truyo.com/lfpdppp-2025-why-businesses-cant-ignore-mexicos-new-rules-for-privacy-and-ai-governance/)
- SecurePrivacy: [Mexico Privacy Law 2025](https://secureprivacy.ai/blog/mexico-privacy-law-lfpdppp-2025)

### Institucional
- ICLG: [Data Protection Laws Mexico](https://iclg.com/practice-areas/data-protection-laws-and-regulations/mexico)
- IAPP: [New Authority Established](https://iapp.org/news/a/new-authority-established-for-personal-data-protection-in-mexico)
- INEGI: [UMA 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/uma/uma2026.pdf)

### Textos legales
- [LFPDPPP Texto](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)
- [Reglamento LFPDPPP 2011 (DOF 21-12-2011)](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LFPDPPP.pdf)
- [NOM-024-SSA3-2012](https://www.gob.mx/cms/uploads/attachment/file/14549/DOF-30NOV12-NOM-024-SSA3-2012_English.pdf)
- [SEP Cedula Profesional](https://www.cedulaprofesional.sep.gob.mx/)

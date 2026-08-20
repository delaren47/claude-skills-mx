# LFPDPPP 2025 — Referencia Detallada

**Fecha de investigacion:** 19 de febrero de 2026
**Aplica a:** Directorio de salud en linea para expatriados

---

## 1. Nueva Ley Federal (vigente 21 marzo 2025)

La ley de 2010 fue **derogada y sustituida** por una nueva ley publicada el 20 de marzo de 2025 en el DOF. Cambios sustanciales:

- **Ambito expandido:** Personas fisicas y juridicas como titulares potenciales
- **Encargados (procesadores):** Directamente sujetos a la ley (antes obligaciones indirectas)
- **Definicion de datos personales:** Ampliada a persona "identificable" (directa o indirectamente)
- **Consentimiento:** Ahora debe ser libre, **especifico** e informado
- **Confidencialidad:** Se extiende **despues de terminada** la relacion contractual
- **Decisiones automatizadas:** Nuevo derecho a oponerse a tratamiento automatizado
- **Fuentes de acceso publico:** Definicion restringida — excluye informacion de origen ilicito

**NOTA:** Los numeros de articulo del reglamento de 2010 podrian aplicarse supletoriamente en lo que no contradiga la nueva ley. El reglamento de la nueva ley estaba programado para junio 2025 pero **no se ha publicado** (feb 2026).

---

## 2. INAI → SABG (nueva autoridad)

### Cronologia

| Fecha | Evento |
|-------|--------|
| 28 nov 2024 | Reforma constitucional: disolucion de 7 organos autonomos |
| 20 dic 2024 | Entrada en vigor de la reforma |
| 20 feb 2025 | Publicacion de nuevas leyes en DOF |
| 21 mar 2025 | Nueva ley vigente; INAI formalmente extinto |
| 9 may 2025 | INAI cesa operaciones; SABG asume |
| ~19 jun 2025 | Plazo para reglamento (90 dias) — aparentemente no cumplido |

### SABG (Secretaria de Anticorrupcion y Buen Gobierno)

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
2. Finalidades del tratamiento
3. Enlace al aviso integral

**Cambio 2025:** Ya no obligatorio incluir categorias de datos, derechos ARCO, ni cambios en practicas en el simplificado.

---

## 4. Datos Sensibles y Salud — Detalle

### Categorias de datos sensibles (enumeradas por ley)

- Origen racial o etnico
- **Estado de salud presente o futuro**
- Informacion genetica
- Creencias religiosas, filosoficas, morales
- Opiniones politicas
- Preferencia sexual
- Datos biometricos

### Requisitos especificos

- Consentimiento **expreso y por escrito** (firma autografa, electronica, o mecanismo equivalente)
- No crear bases de datos sensibles sin justificacion para finalidades legitimas
- Multas se **duplican** para infracciones con datos sensibles
- Conservacion limitada al periodo minimo necesario

### Excepciones (atencion medica)

No se requiere consentimiento cuando el tratamiento sea:
- Indispensable para atencion medica, prevencion, diagnostico
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
| Cloudflare | EE.UU. | Trafico, IPs | Informar en aviso; consentimiento tacito posible |
| Stripe | EE.UU. | Financieros | **Consentimiento expreso** |
| Email marketing (SendGrid, etc.) | EE.UU. | Email, nombre | Consentimiento expreso |
| Google Analytics (GA4) | EE.UU. | Navegacion, IPs | Informar + cookie consent |
| Plataforma de hosting del directorio | EE.UU. | Todos los datos | Documentar en aviso |

### Excepciones al consentimiento para transferencias

- Tratado internacional aplicable
- Atencion medica
- Cumplimiento de contrato titular-responsable
- Autoridad competente
- Interes publico

**Nota:** La nueva ley no establece mecanismos claros ni criterios de adecuacion para transferencias internacionales. Incertidumbre regulatoria significativa.

---

## 6. Cedula Profesional como Fuente Publica

La Cedula Profesional es emitida por la SEP y consultable publicamente en cedulaprofesional.sep.gob.mx. Bajo la LFPDPPP, los datos de fuentes de acceso publico **no requieren consentimiento** siempre que:

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

## 8. Estado Actual (febrero 2026)

### Certezas

- Nueva LFPDPPP vigente desde marzo 2025
- INAI disuelto, SABG operando
- Datos de salud = datos sensibles (multas duplicadas)
- Cedula Profesional = fuente publica
- Transferencias internacionales requieren consentimiento expreso

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
- [Reglamento LFPDPPP 2010](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LFPDPPP.pdf)
- [NOM-024-SSA3-2012](https://www.gob.mx/cms/uploads/attachment/file/14549/DOF-30NOV12-NOM-024-SSA3-2012_English.pdf)
- [SEP Cedula Profesional](https://www.cedulaprofesional.sep.gob.mx/)

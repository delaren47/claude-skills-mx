# Contratos Digitales México 2026 — Referencia Detallada

**Fecha de investigación:** 19 de febrero de 2026
**Reverificado contra fuentes primarias:** 19 de agosto de 2026 (LFPC texto vigente DOF 12-12-2025)
**Aplica a:** Plataforma de directorio de salud en línea

---

## 1. Marco Legal Aplicable

### Jerarquía de Leyes

| Ley | Artículos clave | Qué regula |
|-----|----------------|------------|
| **LFPC** | Arts. 76 Bis, 85, 87-90 | Comercio electrónico, contratos de adhesión, cláusulas nulas, suscripciones |
| **Código de Comercio** | Arts. 49 (conservación), 80 (perfeccionamiento), 89-114 (mensajes de datos y firma electrónica) | Contratos electrónicos, firma electrónica, conservación mercantil |
| **Código Civil Federal** | Art. 1794 (existencia), Art. 1795 (validez), Art. 1803 fr. I (consentimiento por medios electrónicos) | Formación del contrato, consentimiento |
| **LFPDPPP 2025** | Toda la ley (reforma DOF 14-11-2025) | Protección de datos en contratos |
| **NOM-151-SCFI-2016** | Toda la norma | Valor probatorio de la conservación de mensajes de datos |
| **T-MEC** | Art. 19.17 | Obligación del Estado en materia de responsabilidad de intermediarios |

### Jurisprudencia SCJN

**1a./J. 93/2025 (11a.), registro digital 2030477 — Amparo Directo en Revisión 5069/2023:**
Una cláusula de sumisión a **jurisdicción extranjera** en los T&C de una plataforma que opera en México **viola el derecho de acceso a la justicia**, con apoyo en los arts. 149 y 151 del Código de Procedimientos Civiles de la CDMX.

**Alcance real:** el fundamento es **constitucional/procesal**. La tesis **no** resuelve que todos los T&C aceptados en línea sean contratos de adhesión, ni los somete en bloque al régimen de cláusulas nulas de la LFPC. Citarla para eso es sobre-extenderla. (Que los T&C de una plataforma sean contrato de adhesión se sostiene directamente por la **definición del Art. 85 LFPC** — documento elaborado unilateralmente por el proveedor en formatos uniformes — no por esta tesis.)

---

## 2. Contratos Electrónicos — Validez

### Código de Comercio (Arts. 89-114)

| Principio | Artículo | Aplicación |
|-----------|----------|------------|
| Equivalencia funcional del mensaje de datos | CCom Art. 89 | Documento electrónico = documento en papel |
| **Firma electrónica** | CCom Arts. **96-99** (criterios de fiabilidad en el **97**) | Régimen de la firma electrónica y firma electrónica avanzada |
| **Clickwrap** (base de validez) | CCom Art. **93, párr. 2** + Art. **90** + CCF **1803 fr. I** | El clic en "Acepto" es consentimiento expreso por medios electrónicos. ⚠️ La **LFEA** (firma electrónica avanzada) **no aplica** a T&C entre particulares — regula la firma ante dependencias del Estado |
| **Momento de perfeccionamiento** | CCom Art. **80** | El contrato se perfecciona **al recibirse la aceptación**, no con el acuse de recibo |
| Acuse de recibo | CCom Art. **92** | Regula el acuse cuando se pacta — no condiciona el perfeccionamiento |
| Lugar de emisión/recepción | CCom Art. **94** | Domicilio del emisor / receptor |
| Conservación | CCom Art. **49** (10 años) + NOM-151 (valor probatorio) | Mantener el mensaje en formato original, íntegro y accesible |

### Consentimiento Electrónico

| Método | Validez | Fuerza probatoria |
|--------|---------|-------------------|
| **Clickwrap** (checkbox + clic "Acepto") | **VÁLIDO** | Alta — acción afirmativa clara |
| **Scrollwrap / scroll-through** (scroll + clic) | **Cuestionable** | Media — puede argumentarse falta de lectura. No hay norma que lo invalide; **no atribuirlo a la LFPDPPP** |
| **Browsewrap** (banner informativo) | **DÉBIL** | Baja — no demuestra consentimiento activo |
| **Sign-in-wrap** (aceptación al registrar) | Válido si explícito | Media-Alta — depende de la claridad |

**Recomendación:** Clickwrap con checkbox NO pre-marcado + enlace visible a T&C completos.

---

## 3. Cláusulas Nulas — Detalle (numeración corregida 19-ago-2026)

> **Corrección:** versiones previas de esta referencia atribuían al **Art. 86** el catálogo de cláusulas nulas e incluían una fracción inexistente ("jurisdicción diferente a su domicilio"). El catálogo está en el **Art. 90**, y su fracción VI habla de **tribunales extranjeros** — una lectura que invierte el veredicto sobre cláusulas de foro dentro de México.

### Artículo 85 LFPC — definición + requisitos de validez

Texto vigente (DOF 12-12-2025), literal:

> "Para los efectos de esta ley, se entiende por contrato de adhesión el documento elaborado unilateralmente por el proveedor, para establecer en formatos uniformes los términos y condiciones aplicables a la adquisición de un producto o la prestación de un servicio, aun cuando dicho documento no contenga todas las cláusulas ordinarias de un contrato. Todo contrato de adhesión celebrado en territorio nacional, **para su validez, deberá estar escrito en idioma español** y sus caracteres tendrán que ser legibles a simple vista y en un tamaño y tipo de letra uniforme. Además, no podrá implicar prestaciones desproporcionadas a cargo de los consumidores, obligaciones inequitativas o abusivas, o cualquier otra cláusula o texto que viole las disposiciones de esta ley."

Tres reglas salen de aquí: (a) definición de contrato de adhesión; (b) **español + legibilidad + tipografía uniforme como requisito de validez**; (c) prohibición general de prestaciones desproporcionadas / obligaciones inequitativas o abusivas.

### Artículo 86 LFPC — registro previo vía NOM (NO es el catálogo de nulidades)

El Art. 86 faculta a la Secretaría para **sujetar a registro previo ante PROFECO**, mediante normas oficiales mexicanas, los contratos de adhesión que impliquen prestaciones desproporcionadas, obligaciones inequitativas o abusivas, o altas probabilidades de incumplimiento. Las normas pueden referirse a cualesquiera términos y condiciones **excepto el precio**. Los contratos sujetos a registro deben incluir la cláusula de competencia administrativa de PROFECO y el número de registro.

Artículos vecinos que sí operan sobre el contrato:

| Artículo | Qué establece |
|---|---|
| **86 BIS** | Servicios adicionales/conexos por escrito o vía electrónica; sólo con consentimiento expreso |
| **86 QUATER** | Diferencia entre el contrato registrado y el usado en perjuicio del consumidor → **se tiene por no puesta** |
| **87** | Procedimiento de registro previo: resolución en **30 días hábiles**; afirmativa ficta si no resuelve; los contratos que debiendo registrarse no se registren **no producen efectos contra el consumidor** |
| **87 BIS / 87 TER** | Modelos de contrato publicados por PROFECO en el DOF y su adopción/variación |
| **88** | **Inscripción voluntaria** de modelos aunque no requieran registro previo |
| **90 BIS** | Cancelación del registro si el contrato registrado contiene cláusulas contrarias a la ley |

### Artículo 90 LFPC — catálogo literal de cláusulas nulas

> "No serán válidas y se tendrán por no puestas las siguientes cláusulas de los contratos de adhesión ni se inscribirán en el registro cuando:"

| Fracción | Texto (literal, abreviado) |
|---|---|
| **I** | Permitan al proveedor **modificar unilateralmente** el contenido del contrato, o sustraerse unilateralmente de sus obligaciones |
| **II** | **Liberen al proveedor de su responsabilidad civil**, excepto cuando el consumidor incumpla el contrato |
| **III** | **Trasladen al consumidor o a un tercero** que no sea parte del contrato la responsabilidad civil del proveedor |
| **IV** | Prevengan **términos de prescripción inferiores a los legales** |
| **V** | Prescriban el cumplimiento de ciertas **formalidades para la procedencia de las acciones** que se promuevan contra el proveedor |
| **VI** | Obliguen al consumidor a **renunciar a la protección de esta ley** o lo sometan a la competencia de **tribunales extranjeros** |

⚠️ Dos lecturas erróneas frecuentes, ambas corregidas aquí: la fracción III es sobre **responsabilidad civil**, no sobre "carga de la prueba"; y la fracción VI dice **tribunales extranjeros**, no "jurisdicción distinta al domicilio del consumidor". Una cláusula de foro **dentro de México** (p. ej. tribunales de CDMX) no cae en el Art. 90.

### Aplicación Práctica

| Cláusula típica en T&C | Veredicto | Base | Alternativa |
|------------------------|-----------|------|-------------|
| "We are not responsible for any damages" | **Nula** | Art. 90 fr. II | "Our liability is limited to the fees paid in the last 12 months" |
| "Courts of Santa Clara County, California" | **Nula** | Art. 90 fr. VI | "Tribunales competentes de la Ciudad de México" |
| "Tribunales de Monterrey" (foro en México) | **No nula por el Art. 90** | — | Evaluable por otra vía (acceso a la justicia, 1a./J. 93/2025) |
| "We may modify these terms at any time" | **Nula** | Art. 90 fr. I | Aviso previo (30 días) + derecho a terminar sin penalización |
| "You waive right to file complaints" | **Nula** | Art. 90 fr. VI | No incluir — irrenunciable |
| "Claims must be filed within 30 days" | **Nula** | Art. 90 fr. IV | Rigen los plazos legales de prescripción |
| "No refunds under any circumstances" | Abusiva | Art. 85 | "Refunds per our cancellation policy" |
| "Liability limited to \$100 USD" | Cuestionable | Art. 85 (desproporción) | Proporcional a servicios contratados |

---

## 4. Registro de Contrato de Adhesión ante PROFECO

### ¿Es obligatorio para un directorio digital?

| Factor | Análisis |
|--------|----------|
| Sector | Directorio digital (no servicios financieros, seguros, telecomunicaciones) |
| Monto | Membresías <\$2,000 MXN/mes |
| Regulación especial | No hay NOM que sujete a registro previo a los directorios (Art. 86 exige que una NOM lo ordene) |
| **Conclusión** | **Probablemente NO obligatorio** — pero SÍ recomendable, vía inscripción voluntaria (Art. 88) |

### Registro Voluntario

| Aspecto | Detalle |
|---------|---------|
| Costo (RPCA, consultado 19-ago-2026) | ~\$2,339.75 MXN si el contrato **no** se apega a un modelo tipo · ~\$1,243.78 MXN si se adopta un **contrato tipo** |
| Naturaleza del cobro | **Aprovechamiento con IVA incluido**, NO un derecho de la Ley Federal de Derechos (su art. 80 está **derogado**). ⚠️ El FAQ del RCAL publica cifras distintas a las del RPCA — reverificar en la ventanilla antes de presupuestar |
| Proceso | Presentar el modelo de contrato ante PROFECO para revisión |
| Plazo de resolución | **30 días hábiles**; transcurrido el plazo sin resolución, el modelo se entiende aprobado y PROFECO debe registrarlo (Art. 87) |
| Beneficio | PROFECO revisa y aprueba cláusulas antes de su uso |
| Renovación | Al modificar las obligaciones o condiciones hay que solicitar la modificación del registro (Art. 87) |

---

## 5. Idioma de los Contratos

### Requisito Legal — CORREGIDO 19-ago-2026

> **Corrección:** versiones previas de esta referencia afirmaban que "no existe estatuto que anule un contrato en idioma extranjero". **Es falso para los contratos de adhesión.** El **Art. 85 LFPC** lo exige expresamente como requisito de validez. Verificado contra el texto vigente (DOF 12-12-2025), literal:
>
> "Todo contrato de adhesión celebrado en territorio nacional, **para su validez, deberá estar escrito en idioma español** y sus caracteres tendrán que ser legibles a simple vista y en un tamaño y tipo de letra uniforme."

| Aspecto | Regla |
|---------|-------|
| Contrato de adhesión (T&C, membresía) celebrado en territorio nacional | **Español obligatorio — requisito de validez** (Art. 85 LFPC) |
| Legibilidad y tipografía | Caracteres legibles a simple vista, tamaño y tipo de letra uniforme (mismo Art. 85) — aplica al render, no sólo al texto fuente |
| Versión bilingüe | Válida siempre que la versión en español exista y cumpla el Art. 85; añadir cláusula de prevalencia del español |
| Ante tribunales / PROFECO | Español prevalece |
| Para expats (anglófonos) | El inglés facilita la comprensión y es buena práctica, pero **no sustituye** el requisito del Art. 85 |
| Alcance del requisito | El Art. 85 aplica a **contratos de adhesión**. Para contratos negociados individualmente (no de adhesión) no hay una regla equivalente de nulidad por idioma |

### Formato Bilingüe Recomendado

```
Estos Términos y Condiciones se presentan en inglés y español.
En caso de discrepancia entre ambas versiones, prevalecerá la
versión en español.

These Terms and Conditions are presented in English and Spanish.
In case of discrepancy between both versions, the Spanish version
shall prevail.
```

---

## 6. Listados No Reclamados — Base Legal

### Fundamento para Publicar Perfiles sin Consentimiento

| Dato | Fuente | Base legal | Consentimiento |
|------|--------|-----------|----------------|
| Nombre completo | Registro Nacional de Profesionistas (SEP) | Fuente de acceso público (LFPDPPP) | **No requerido** |
| Número de Cédula | SEP | Fuente pública | **No requerido** |
| Especialidad | SEP | Fuente pública | **No requerido** |
| Institución educativa | SEP | Fuente pública | **No requerido** |
| Teléfono consultorio | Proveedor / otra fuente | No es dato público SEP | **Requiere consentimiento** |
| Dirección consultorio | Proveedor / Google | Puede ser público si está en GBP | Caso por caso |
| Fotografía | Proveedor | Dato personal | **Requiere consentimiento expreso** |
| Biografía personalizada | El directorio | Contenido editorial | El directorio es responsable |

### Dos límites que acotan la "fuente de acceso público"

| Regla | Base | Efecto |
|---|---|---|
| El tratamiento no puede tener **procedencia ilícita** | LFPDPPP 2025 **Art. 2 fr. X** | Aunque el dato sea públicamente accesible, obtenerlo por medios ilícitos (scraping contra términos, bases filtradas) rompe la base legal |
| **Expectativa razonable de privacidad** | LFPDPPP 2025 **Art. 6** | Agregar datos públicos dispersos en un perfil enriquecido puede exceder la expectativa del titular. La base "fuente pública" no es un cheque en blanco |

### COFEPRIS: Obligación de exhibir Cédula

La COFEPRIS obliga a los médicos a exhibir su Cédula Profesional en su consultorio. Este requisito refuerza la naturaleza pública de los datos de la Cédula.

### Derecho de Eliminación (ARCO)

El proveedor **siempre** puede solicitar eliminación de su perfil bajo derechos ARCO (LFPDPPP 2025, **Art. 31**):
- Plazo de respuesta: **20 días hábiles**
- **Prórroga: una sola vez**, por 20 días hábiles más, cuando esté justificada y se notifique al titular (Art. 31)
- Implementación posterior a la respuesta: 15 días hábiles
- Vía: email designado para solicitudes ARCO

### Reforma LFPDPPP DOF 14-11-2025 — qué cambia

- Introduce la **supletoriedad del CNPCyF** (Código Nacional de Procedimientos Civiles y Familiares) en los procedimientos de la ley; su aplicación es **automática a partir del 1-abr-2027**.
- El **Reglamento de la LFPDPPP de 2011 sigue vigente** — no fue abrogado por la reforma. Para plazos y formalidades operativas ARCO, sigue siendo la fuente de detalle.

---

## 7. Contenido Generado por Usuarios (Reseñas)

### T-MEC Art. 19.17 — qué obliga realmente

⚠️ **No es una safe harbor invocable directamente por la plataforma.** El Art. 19.17 impone una obligación **al Estado mexicano** (exigible desde el **1-jul-2023**, tras el período de transición): no tratar al proveedor de servicios interactivos como creador del contenido de terceros. México **no** ha legislado una disposición interna equivalente a la Sección 230 estadounidense. Ante un juez mexicano, la defensa se construye con derecho interno (responsabilidad civil por hecho propio, ausencia de autoría), citando el tratado como **criterio interpretativo**, no como escudo auto-ejecutable.

> ⚠️ **Nota abierta (19-ago-2026, sin resolver):** el **Anexo 19-A.2** del T-MEC se apoya en la **LFTR, abrogada el 16-jul-2025**. No está verificado qué disposición de la nueva ley de telecomunicaciones la sustituye ni el estatus del anexo. No citar el Anexo 19-A como fundamento vigente hasta cerrar la verificación.

Con esa lectura corregida:

| Situación | Obligación del directorio |
|-----------|------------------------|
| Reseña veraz y honesta | Ninguna — dejar publicada |
| Reseña claramente falsa/difamatoria | Deber de retirar tras notificación |
| Reseña con datos de salud del reseñador | Requiere consentimiento expreso escrito (LFPDPPP) |
| Reseña con datos personales de terceros | Deber de moderar |
| Solicitud de eliminación del proveedor | Evaluar caso por caso — no obligatorio si es opinión legítima |

### Propiedad Intelectual de Reseñas

| Aspecto | Regla recomendada |
|---------|-------------------|
| Autor | El usuario retiene derechos de autor |
| Licencia | El usuario otorga licencia no exclusiva, perpetua, a la plataforma |
| Uso | La plataforma puede mostrar, reproducir, distribuir |
| Eliminación | El usuario puede solicitar eliminación de su reseña |

---

## 8. Disputas y Jurisdicción

### Resolución de Controversias en México

| Vía | Cuándo | Costo |
|-----|--------|-------|
| **PROFECO conciliación** | Primera instancia para consumidores | Gratuito |
| **Concilianet** (en línea) | Si proveedor tiene convenio | Gratuito |
| **Tribunales CDMX** | Si conciliación falla | Variable |
| **Amparo** | Contra actos de autoridad | Variable |

### Arbitraje

| Aspecto | Análisis |
|---------|----------|
| ¿Válido en B2C? | Cuestionable — podría ser cláusula abusiva |
| ¿Válido en B2B? | Sí, pero costoso para montos bajos |
| Recomendación | **NO** usar arbitraje obligatorio con consumidores |
| Alternativa | Conciliación + tribunales CDMX |

### Cláusula de Jurisdicción Recomendada

```
JURISDICCIÓN Y LEY APLICABLE

Estos Términos se rigen por las leyes de los Estados Unidos
Mexicanos. Para cualquier controversia derivada de estos Términos,
las partes se someten a la jurisdicción de los tribunales
competentes de la Ciudad de México, renunciando expresamente a
cualquier otro fuero que pudiera corresponderles por razón de
su domicilio presente o futuro.

El consumidor conserva en todo momento su derecho a presentar
quejas ante la Procuraduría Federal del Consumidor (PROFECO).
```

---

## 9. Conservación de Documentos (CCom art. 49 + NOM-151-SCFI-2016)

**El plazo lo fija el Código de Comercio, no la NOM.** El **CCom art. 49** obliga a conservar por **10 años** los documentos relacionados con la actividad mercantil. La **NOM-151-SCFI-2016** define los requisitos técnicos para que esa conservación tenga **valor probatorio** (constancia de conservación, hash, timestamping por un PSC) — no establece un plazo propio. Citar la NOM como fuente del plazo de 10 años es una inversión de la relación entre ambas normas.

### Requisitos de Conservación

| Documento | Plazo | Base legal del plazo |
|-----------|-------|-----------|
| Contratos aceptados (con timestamp) | 10 años | **CCom art. 49** |
| Confirmaciones de compra | 10 años | **CCom art. 49** |
| CFDIs emitidos | 5 años | CFF |
| Comunicaciones contractuales | 5 años | LFPC |
| Consentimientos (ARCO, privacidad) | 5 años post-relación | LFPDPPP |
| Logs de aceptación de T&C | 10 años | **CCom art. 49** (valor probatorio vía NOM-151) |

### Requisitos Técnicos

- Mantener formato original del mensaje
- Prevenir alteraciones no autorizadas (integridad)
- Timestamping digital
- Hashing para verificar integridad
- Respaldo redundante

---

## 10. Estructura Detallada de T&C

### Documento 1: Términos de Uso (Usuarios/Visitantes)

```
TERMS OF USE / TÉRMINOS DE USO
[plataforma].com

Last updated: [fecha]
Última actualización: [fecha]

In case of discrepancy, the Spanish version prevails.

1. DEFINITIONS / DEFINICIONES
   - "Platform", "Directory", "We"
   - "User", "You"
   - "Provider" (healthcare professional listed)
   - "Services" (directory browsing, search, reviews)

2. DESCRIPTION OF SERVICE / DESCRIPCIÓN DEL SERVICIO
   - [Platform] is an online directory
   - NOT a healthcare provider
   - NOT a medical referral service
   - Does NOT provide medical advice

3. MEDICAL DISCLAIMER / AVISO MÉDICO
   - Directory listings are informational only
   - Verification confirms Cédula Profesional only
   - Users should independently verify providers
   - In case of emergency, call 911 or go to nearest hospital

4. ACCEPTABLE USE / USO ACEPTABLE
   - Lawful purposes only
   - No scraping, automated access
   - No commercial use without permission

5. USER-GENERATED CONTENT / CONTENIDO DE USUARIOS
   - Reviews must reflect genuine experience
   - No false, defamatory, or misleading content
   - No disclosure of other people's health information
   - Platform may moderate content
   - User grants non-exclusive license to platform

6. INTELLECTUAL PROPERTY / PROPIEDAD INTELECTUAL
   - Directory content owned by [Platform]
   - Provider data from public sources (SEP)
   - User content: user retains rights, grants license

7. LIMITATION OF LIABILITY / LIMITACIÓN DE RESPONSABILIDAD
   - Platform is not responsible for provider services
   - Verification scope: Cédula Profesional only
   - Total liability limited to [amount or fees paid]
   - Force majeure provisions

8. GOVERNING LAW / LEY APLICABLE
   - Laws of Mexico
   - Courts of Mexico City
   - Right to file PROFECO complaints preserved

9. MODIFICATIONS / MODIFICACIONES
   - 30 days advance notice by email
   - Continued use = acceptance
   - Users may terminate if they disagree

10. CONTACT / CONTACTO
    - Email for questions and complaints
    - ARCO rights contact (see Privacy Policy)
```

### Documento 2: Acuerdo de Membresía (Proveedores)

```
MEMBERSHIP AGREEMENT / ACUERDO DE MEMBRESÍA
[plataforma].com

1. PLANS AND PRICING / PLANES Y PRECIOS
   - Free tier: \$0 MXN
   - Paid tier A: [monto] MXN/mes + IVA (16%)   (montos de ejemplo: \$500)
   - Paid tier B: [monto] MXN/mes + IVA (16%)   (montos de ejemplo: \$1,000)
   - "All prices in MXN, IVA not included"

2. SUBSCRIPTION AND CONSENT / SUSCRIPCIÓN Y CONSENTIMIENTO
   - Explicit consent required (checkbox)
   - Amount, frequency, and date of charge clearly stated
   - Right of withdrawal: 5 business days ⚠️ *(nota de alcance: el retracto del Art. 56 LFPC nace en ventas fuera del establecimiento y alcanza e-commerce vía Art. 53, pero NO aplica a servicios que se prestan dentro de los 10 días hábiles siguientes a la orden — una membresía con acceso inmediato puede quedar fuera; ofrecerlo aquí es generosidad contractual, no obligación. El retracto de 14 días para suscripciones digitales es el Art. 56 Bis, aún NO aprobado a ago-2026)*

3. BILLING AND CFDI / FACTURACIÓN Y CFDI
   - CFDI issued for each payment
   - Provider must provide RFC and fiscal data
   - Stripe as payment processor (international transfer)

4. RENEWAL / RENOVACIÓN
   - Automatic monthly renewal
   - Notification 5 calendar days before each renewal
   - Provider may cancel before renewal

5. CANCELLATION / CANCELACIÓN
   - Cancel anytime via [dashboard/email]
   - Effective at end of current billing period
   - No unjustified penalties
   - Confirmation email sent

6. VERIFICATION SCOPE / ALCANCE DE VERIFICACIÓN
   - What is verified: Cédula Profesional via SEP
   - What is NOT verified: medical quality, outcomes
   - Badge meaning explained
   - Provider responsible for accuracy of additional info

7. PROVIDER OBLIGATIONS / OBLIGACIONES DEL PROVEEDOR
   - Provide accurate, current information
   - Maintain valid professional credentials
   - Notify changes to practice status
   - Comply with applicable laws

8. SUSPENSION AND TERMINATION / SUSPENSIÓN Y TERMINACIÓN
   - Platform may suspend for violations
   - Platform may terminate with 30 days notice
   - Provider may terminate anytime (cancellation)
   - Data handling post-termination (per Privacy Policy)

9. GOVERNING LAW / LEY APLICABLE
   [Same as Terms of Use]
```

---

## Fuentes

### Legislación
- [LFPC — Texto vigente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf)
- [Código de Comercio — Título II, Libro II](https://www.diputados.gob.mx/LeyesBiblio/pdf/CCom.pdf)
- [Código Civil Federal](https://www.diputados.gob.mx/LeyesBiblio/pdf/2_070121.pdf)
- [DOF 12/12/2025 — Reforma Art. 76 Bis](https://www.dof.gob.mx/nota_detalle.php?codigo=5775999&fecha=12/12/2025)
- [NOM-151-SCFI-2016](https://www.dof.gob.mx/nota_detalle.php?codigo=5478024&fecha=30/03/2017) — código DOF **5478024** (corregido 19-ago-2026; el 5476488 apuntaba a otra publicación). En vigor desde el **26-sep-2017**
- [Código de Comercio art. 49 — conservación 10 años](https://www.diputados.gob.mx/LeyesBiblio/pdf/CCom.pdf)

### Jurisprudencia
- SCJN 1a./J. 93/2025 (Amparo Directo en Revisión 5069/2023) — T&C como contratos de adhesión

### Despachos legales
- [Greenberg Traurig — Reformas LFPC Suscripciones](https://www.gtlaw.com/en/insights/2025/12/reformas-a-la-ley-federal-de-proteccion-al-consumidor)
- [Arochi & Lindner — Easy Cancellation Digital Services](https://www.arochilindner.com/en/al-newsletter-regulatory-alert-mexico-approves-easy-cancellation-for-digital-services/)
- [Uhthoff — Art. 76 Bis Reform](https://uhthoff.com.mx/en/mexico-strengthens-consumer-protection-for-subscriptions-what-the-new-article-76-bis-reform-means-for-digital-businesses/)
- [DLA Piper — Data Protection Mexico](https://www.dlapiper.com/en/insights/publications/data-protection/mexico)
- [White & Case — Intermediary Liability](https://www.whitecase.com/publications/insight/latin-america-focus-fall-2022-intermediary-liability-frameworks)
- [CCN Law — Platform Liability Mexico](https://ccn-law.com/)

### Institucional
- [PROFECO — Registro Contratos Adhesión](https://www.gob.mx/profeco/acciones-y-programas/registro-publico-de-contratos-de-adhesion)
- [Distintivo Digital PROFECO](https://distintivodigital.profeco.gob.mx/)
- [SEP — Registro Nacional de Profesionistas](https://www.cedulaprofesional.sep.gob.mx/)

### Académico
- [UNAM — Cláusulas Abusivas](https://revistas.juridicas.unam.mx/index.php/derecho-privado/article/download/8983/11033/11058)
- [UNAM — Derecho de Retracto](https://asesoria.juridicas.unam.mx/preguntas/pregunta/37-Que-es-el-derecho-de-retracto)

### Compliance
- [eSignGlobal — Mexico NOM-151](https://www.esignglobal.com/blog/mexico-nom-151-conservation-messages)
- [Lex Mundi — Mexico Consumer Guide 2024](https://www.lexmundi.com/guides/latam-consumer-guide-2024/jurisdiction/latin-america/mexico/)

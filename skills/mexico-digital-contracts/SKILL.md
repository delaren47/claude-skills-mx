---
name: mexico-digital-contracts
description: Use when writing terms and conditions, membership agreements, subscription contracts, or evaluating enforceability of digital contract clauses under Mexican law. Also use when handling user-generated content policies, claimable listings, dispute resolution, or bilingual T&C for platforms operating in Mexico.
version: 1.1.0
last-verified: 2026-08-19
review-by: 2026-11-30
---

# Mexico Digital Contracts (T&C, Membresías, Contratos de Adhesión)

## Overview

Guía para la redacción y cumplimiento de **contratos digitales** (términos y condiciones, acuerdos de membresía, políticas de contenido) bajo legislación mexicana vigente, aplicable a plataformas digitales que operan en México.

**DISCLAIMER:** Esta guía NO constituye asesoría legal. Consultar un abogado para validar la redacción final de contratos.

## When to Use

- Redactar o revisar Términos y Condiciones (T&C)
- Crear acuerdos de membresía/suscripción para proveedores
- Evaluar si una cláusula es abusiva o inejercible
- Diseñar política de contenido generado por usuarios (reseñas)
- Establecer base legal para listados no reclamados (claimable listings)
- Manejar disputas con usuarios o proveedores
- Decidir jurisdicción y ley aplicable
- Crear contratos bilingües (inglés/español)

## Quick Reference

### Marco Legal Aplicable

| Ley / Norma | Aplica a | Relevancia |
|-------------|----------|------------|
| **LFPC** (Arts. 76 Bis, 85, 87-90) | Comercio electrónico, contratos de adhesión, cláusulas nulas | **Principal** |
| **Código de Comercio** (Título II, Libro II) | Contratos electrónicos, mensajes de datos | **Principal** |
| **Código Civil Federal** | Formación de contratos, consentimiento | Supletorio |
| **NOM-151-SCFI-2016** | Conservación de mensajes de datos | Aplica a transacciones |
| **LFPDPPP 2025** | Tratamiento de datos en contratos | Ver skill mexico-privacy-law |
| **T-MEC Art. 19.17** | Responsabilidad de intermediarios | Obligación a cargo del **Estado mexicano** (exigible desde 1-jul-2023) — NO es una defensa auto-ejecutable ante tribunales |

> ⚠️ **Nota abierta (19-ago-2026, sin resolver):** el Anexo 19-A.2 del T-MEC se apoya en la **LFTR, abrogada el 16-jul-2025**. No está verificado qué disposición de la nueva ley de telecomunicaciones la sustituye ni cómo queda el anexo. No citar el Anexo 19-A como fundamento vigente hasta cerrar esta verificación.

### Jurisprudencia Clave

**SCJN 1a./J. 93/2025 (11a.), registro digital 2030477 — ADR 5069/2023:** una cláusula de sumisión a jurisdicción extranjera en los T&C de una plataforma que opera en México **viola el derecho de acceso a la justicia** (arts. 149 y 151 del CPC de la CDMX). El fundamento es **constitucional/procesal**, NO el régimen de cláusulas abusivas de la LFPC. La tesis **no** declara que todos los T&C en línea sean contratos de adhesión ni somete todas sus cláusulas al régimen de la LFPC — no la cites para eso.

## Contratos de Adhesión — Lo Esencial

### ¿Qué es un contrato de adhesión?

Contrato cuyas cláusulas son redactadas **unilateralmente** por el proveedor, sin que el consumidor pueda negociar. Los T&C de cualquier plataforma digital son contratos de adhesión.

### Cláusulas Nulas de Pleno Derecho (Art. 90 LFPC)

Art. 90 LFPC: *"No serán válidas y se tendrán por no puestas las siguientes cláusulas de los contratos de adhesión ni se inscribirán en el registro cuando:"* — seis fracciones, literales:

| Fracción | Qué prohíbe | Ejemplo en T&C | Alternativa válida |
|---|---|---|---|
| **I** | Modificar unilateralmente el contenido del contrato o sustraerse de las obligaciones | "May change terms at any time" | Aviso previo (p. ej. 30 días por email) **+ derecho del usuario a terminar sin penalización** |
| **II** | Liberar al proveedor de su responsabilidad civil (salvo incumplimiento del consumidor) | "No somos responsables bajo ninguna circunstancia" | Disclaimer específico del alcance de la verificación |
| **III** | Trasladar al consumidor o a un tercero la responsabilidad civil del proveedor | "You assume all risk" | Distribución equitativa de responsabilidad |
| **IV** | Prever términos de **prescripción inferiores a los legales** | "Claims must be filed within 30 days" | No incluir — rigen los plazos legales |
| **V** | Prescribir **formalidades** para la procedencia de acciones contra el proveedor | "Debes agotar un proceso interno antes de reclamar" | No incluir |
| **VI** | Renunciar a la protección de la LFPC **o** someter al consumidor a **tribunales extranjeros** | "You waive your right to file complaints" / "Courts of Santa Clara County, California" | Derecho irrenunciable · "Tribunales competentes de la Ciudad de México, ley mexicana" |

> ⚠️ La fracción VI habla de **tribunales extranjeros**, no de "jurisdicción distinta a su domicilio". Una cláusula de foro **dentro de México** no es nula por el Art. 90 — puede atacarse por otra vía (ver 1a./J. 93/2025 arriba), pero el fundamento es distinto.

Fuera del Art. 90 siguen aplicando:

| Regla | Base | Consecuencia práctica |
|---|---|---|
| Contrato de adhesión **escrito en español**, caracteres legibles a simple vista, tamaño y tipo de letra uniforme — requisito **de validez** | Art. 85 LFPC | Ver §"Idioma" abajo |
| Sin prestaciones desproporcionadas, obligaciones inequitativas o abusivas | Art. 85 LFPC | Penalizaciones tipo "\$500 USD cancellation fee" → sin penalización o proporcional |
| Diferencia entre el contrato **registrado** y el efectivamente usado en perjuicio del consumidor | Art. 86 QUATER LFPC | Se tiene por no puesta |
| Prórroga automática sin aviso | Art. 76 Bis fr. VIII, **2º párrafo** | Notificar con al menos **5 días naturales** de anticipación, permitiendo cancelar sin penalización |

### Registro ante PROFECO

| Aspecto | Detalle |
|---------|---------|
| ¿Obligatorio? | Sólo si una NOM sujeta ese tipo de contrato a registro previo (Art. 86). Para un directorio digital: probablemente NO |
| ¿Recomendable? | **SÍ** — inscripción voluntaria (Art. 88); PROFECO revisa cláusulas, genera confianza |
| Costo (RPCA, consultado 19-ago-2026) | ~\$2,339.75 MXN si el contrato **no** se apega a un modelo tipo · ~\$1,243.78 MXN si se adopta un **contrato tipo**. Es un **aprovechamiento con IVA incluido**, NO un derecho de la LFD (su art. 80 está derogado). ⚠️ El FAQ del RCAL publica cifras distintas — reverificar antes de presupuestar |
| Plazo de resolución | 30 días hábiles; transcurrido el plazo sin resolución, el modelo se entiende aprobado (Art. 87) |
| Beneficio | Cláusulas revisadas por PROFECO antes de usarse |

## Estructura Recomendada de T&C

### Ejemplo: un directorio en línea — Dos Documentos Separados

**Documento 1: Términos de Uso** (para todos los visitantes/usuarios)
1. Definiciones
2. Descripción del servicio (directorio, NO proveedor médico)
3. **Disclaimer médico** (el directorio no sustituye consejo médico)
4. Uso aceptable
5. Contenido generado por usuarios (reseñas)
6. Propiedad intelectual
7. Limitación de responsabilidad (específica, no absoluta)
8. Ley aplicable y jurisdicción (México)
9. Modificaciones (con aviso previo)
10. Contacto y mecanismo de quejas

**Documento 2: Acuerdo de Membresía** (para proveedores que pagan)
1. Planes y precios (sin IVA + referencia fiscal)
2. Proceso de contratación y consentimiento
3. Período de prueba / derecho de retracto (5 días hábiles)
4. Cobros recurrentes (monto, frecuencia, fecha)
5. **Cancelación** (mecanismo inmediato, sin penalización injustificada)
6. Renovación automática (con aviso 5 días naturales antes)
7. Alcance de la verificación (qué se verifica y qué no)
8. Obligaciones del proveedor (información veraz, vigente)
9. Suspensión/terminación del servicio
10. Facturación y CFDI
11. Ley aplicable y jurisdicción

## Idioma — Contratos Bilingües

### Regla práctica

**El español no es "recomendable": es requisito de validez.** Art. 85 LFPC: *"Todo contrato de adhesión celebrado en territorio nacional, para su validez, deberá estar escrito en idioma español y sus caracteres tendrán que ser legibles a simple vista y en un tamaño y tipo de letra uniforme."* Un T&C sólo en inglés es un contrato de adhesión sin el requisito de validez que la ley exige.

| Aspecto | Regla |
|---------|-------|
| Español | **Obligatorio** — requisito de validez (Art. 85 LFPC) |
| Formato | Bilingüe (inglés + español) es válido siempre que la versión en español exista y cumpla el Art. 85 |
| Idioma que prevalece | **Español** |
| Legibilidad | Caracteres legibles a simple vista, tamaño y tipo de letra uniforme (mismo Art. 85) — aplica al render web, no sólo al texto |
| Cláusula requerida | "In case of discrepancy, the Spanish version shall prevail" |
| Aceptación | Clickwrap (clic en "I accept / Acepto") — NO browsewrap |

### Mecanismo de Aceptación Válido

| Método | Validez en México | Notas |
|--------|-------------------|-------|
| **Clickwrap** (checkbox + clic) | **VÁLIDO** | Método recomendado |
| Browsewrap (banner informativo) | **CUESTIONABLE** | No demuestra consentimiento activo |
| Scroll-through / scrollwrap | **CUESTIONABLE** (fuerza probatoria media) | Puede argumentarse falta de lectura. No hay norma que lo invalide — no atribuirlo a la LFPDPPP |

## Suscripciones/Membresías — Requisitos Completos

### Flujo de Contratación Obligatorio (Art. 76 Bis)

```
1. Usuario selecciona plan
2. Mostrar: monto exacto + frecuencia + fecha primer cobro
3. Desglose: subtotal + IVA + total (ver skill mexico-sat-tax)
4. Checkbox NO pre-marcado: "Acepto los Términos de Membresía"
5. Link visible a T&C completos
6. Botón "Suscribirse" / "Subscribe"
7. Confirmación por email con: resumen, monto, fecha próximo cobro, link de cancelación
```

### Flujo de Cancelación Obligatorio (Art. 76 Bis fr. IX)

Texto de la ley: *"El proveedor deberá implementar mecanismos que, **sin contravenir a las disposiciones contractuales**, permita a la persona consumidora cancelar el servicio, suscripción o membresía **de manera inmediata**."*

```
1. Botón de cancelación accesible en dashboard del proveedor
2. Sin obstáculos innecesarios
3. Cancelación inmediata (la ley no dice "en un clic" ni prohíbe la llamada:
   "no requerir llamada / mismo medio de contratación" es lectura de la
   industria, no letra de la fracción IX)
4. Email de confirmación con fecha efectiva
5. Acceso hasta fin del período pagado — esto sí depende de lo pactado
   ("sin contravenir a las disposiciones contractuales")
6. Sin penalizaciones injustificadas
```

### Notificación Pre-Renovación (Art. 76 Bis fr. VIII, 2º párrafo)

Aplica **sólo si el contrato prevé renovación automática**. Texto: *"...se deberá notificar al menos con **cinco días naturales** de anticipación, permitiendo su cancelación sin penalización"*.

```
5 días NATURALES antes de cada renovación automática:
- Email al proveedor
- Asunto claro: "Tu membresía se renovará el [fecha]"
- Contenido: monto a cobrar, medio de pago, link de cancelación
- La cancelación dentro de esa ventana debe ser sin penalización
- Frecuencia: cada renovación (cada mes en membresías mensuales)
```

La misma fracción VIII, 1er párrafo, obliga a informar "de forma clara, destacada y accesible" si hay **cobros automáticos recurrentes**, su periodicidad, monto y fecha, con **consentimiento expreso e informado**.

## Listados No Reclamados (Claimable Listings)

### Base Legal

| Fuente de datos | Base legal | Consentimiento |
|-----------------|-----------|----------------|
| Cédula Profesional (SEP) | Fuente de acceso público | **No requerido** |
| Nombre, número de cédula, especialidad | Registro Nacional de Profesionistas | **No requerido** |
| Teléfono, dirección, fotos | Datos del proveedor | **SÍ requerido** |
| Información de otras fuentes públicas | Verificar origen lícito | Caso por caso |

### Cláusula Recomendada en T&C

```
Listados No Reclamados: Ciertos perfiles de proveedores se crean
utilizando información pública disponible en el Registro Nacional
de Profesionistas de la SEP. Los proveedores pueden reclamar,
actualizar o solicitar la eliminación de su perfil en cualquier
momento contactando a [email].
```

### Derecho de Eliminación del Proveedor

El proveedor **siempre** tiene derecho a solicitar la eliminación de su perfil (derechos ARCO bajo LFPDPPP). Incluir proceso claro:
1. Solicitud por email
2. Verificación de identidad
3. Eliminación en máximo 20 días hábiles
4. Confirmación por email

## Contenido Generado por Usuarios (Reseñas)

### Marco de Responsabilidad

⚠️ **El T-MEC Art. 19.17 no es un escudo invocable directamente.** Obliga al **Estado mexicano** (exigible desde 1-jul-2023) a no tratar al intermediario como creador del contenido de terceros; México **no** ha legislado una safe harbor equivalente a la Sección 230. Ante un juez mexicano hay que argumentar con derecho interno (responsabilidad civil por hecho propio, no por hecho ajeno), no citando el tratado como defensa auto-ejecutable.

| Situación | Postura defendible | Fuente |
|-----------|----------------|-----------|
| Reseña veraz de un usuario | Plataforma no es autora del contenido | Derecho interno; T-MEC 19.17 como criterio interpretativo |
| Reseña falsa/difamatoria | Deber de retirar tras notificación (el conocimiento sin acción sí genera exposición) | Buena fe + derecho interno |
| Reseña con datos de salud del reseñador | Requiere consentimiento expreso escrito | LFPDPPP 2025 (datos sensibles) |
| Moderación de buena fe | No convierte a la plataforma en creadora del contenido | T-MEC 19.17 como criterio interpretativo |

### Política de Reseñas — Elementos Mínimos

1. **Propiedad:** El usuario otorga licencia no exclusiva a la plataforma
2. **Veracidad:** El usuario declara que la reseña refleja su experiencia real
3. **Prohibiciones:** Contenido falso, difamatorio, con datos personales de terceros
4. **Derecho del proveedor:** Responder a reseñas (si la plataforma lo permite)
5. **Moderación:** La plataforma puede retirar reseñas que violen las políticas
6. **Datos sensibles:** Advertencia de que reseñas no deben revelar condiciones médicas propias

## Disputas y Jurisdicción

### Cláusula Recomendada

```
Ley Aplicable: Estos términos se rigen por la legislación de los
Estados Unidos Mexicanos.

Jurisdicción: Para cualquier controversia, las partes se someten
a la jurisdicción de los tribunales competentes de la Ciudad de México,
renunciando a cualquier otro fuero que pudiera corresponderles.

Resolución Alternativa: Antes de acudir a tribunales, las partes
procurarán resolver la controversia mediante conciliación.
El consumidor puede presentar quejas ante PROFECO.
```

### Arbitraje — Consideraciones

| Aspecto | En México |
|---------|-----------|
| ¿Válido en contratos B2C? | Cuestionable — tribunales pueden invalidar |
| ¿Recomendable para un directorio digital? | **NO** para consumidores (cláusula posiblemente abusiva) |
| ¿Para proveedores B2B? | Posible, pero complejo y costoso |
| Mejor alternativa | Conciliación PROFECO + tribunales CDMX |

## Conservación de Documentos (CCom art. 49 + NOM-151-SCFI-2016)

**El plazo lo fija el Código de Comercio, no la NOM.** CCom art. 49 obliga a conservar por **10 años** los documentos de la actividad mercantil. La NOM-151-SCFI-2016 aporta el **valor probatorio** de la conservación (constancia, hash, timestamping) — no un plazo.

| Documento | Plazo mínimo | Base del plazo | Formato |
|-----------|-------------|---------|---------|
| T&C aceptados (con timestamp) | **10 años** | CCom art. 49 |  Digital con hash (NOM-151) |
| Confirmaciones de compra | **10 años** | CCom art. 49 | Digital |
| CFDIs | **5 años** (CFF) | XML + PDF |
| Comunicaciones contractuales | **5 años** | Digital |
| Consentimientos ARCO | **5 años** post-relación | Digital |

## Checklist de Implementación

### Prioridad Inmediata (antes de monetizar)

- [ ] Redactar T&C bilingües (inglés + español, prevalece español)
- [ ] Separar: Términos de Uso (usuarios) + Acuerdo de Membresía (proveedores)
- [ ] Incluir disclaimer médico en T&C y en páginas del directorio
- [ ] Implementar clickwrap (checkbox + clic) para aceptación de T&C
- [ ] Flujo de suscripción completo: precio + IVA + frecuencia + fecha
- [ ] Botón de cancelación inmediata en dashboard
- [ ] Email de notificación 5 días naturales antes de cada renovación automática
- [ ] Cláusula de derecho de retracto (5 días hábiles)
- [ ] Jurisdicción: Ciudad de México, ley mexicana

### Prioridad Media

- [ ] Política de reseñas documentada
- [ ] Proceso de eliminación de listados no reclamados (20 días hábiles)
- [ ] Cláusula de base legal para datos de Cédula Profesional
- [ ] Política de modificación de T&C (aviso 30 días por email)
- [ ] Evaluar registro voluntario de contrato de adhesión ante PROFECO

### Prioridad Baja

- [ ] Implementar sistema de conservación de documentos (NOM-151)
- [ ] Consultar abogado para revisión formal de T&C
- [ ] Evaluar Distintivo Digital PROFECO (después de 1 año)
- [ ] Monitorear la reforma **pendiente** del Art. 56 Bis (derecho de retracto de **14 días naturales**, sólo para suscripciones digitales): al 19-ago-2026 hay **3 iniciativas turnadas a comisiones, ninguna dictaminada**; la prórroga de dictamen corre al **31-ago-2027**. No es derecho vigente — no redactar T&C como si lo fuera

## Common Mistakes

| Error | Consecuencia | Corrección |
|-------|-------------|------------|
| T&C solo en inglés | Falta un **requisito de validez** del contrato de adhesión (Art. 85 LFPC) | Versión en español, legible y de tipografía uniforme; prevalece español |
| Browsewrap sin checkbox | Consentimiento cuestionable | Clickwrap con checkbox activo |
| "No liability whatsoever" | Cláusula nula de pleno derecho (Art. 90 fr. II) | Limitaciones específicas y razonables |
| Sumisión a tribunales extranjeros | Cláusula nula (Art. 90 fr. **VI**) | Tribunales de Ciudad de México |
| Sin mecanismo de cancelación inmediata | Violación Art. 76 Bis fr. **IX** | Cancelación inmediata, sin contravenir lo pactado |
| Sin aviso pre-renovación | Violación Art. 76 Bis fr. **VIII, 2º párr.** | Email 5 días **naturales** antes de cada renovación automática |
| Publicar fotos de providers sin base legal | Violación LFPDPPP | Solo datos de Cédula (SEP) sin consentimiento |
| Un solo T&C para todos | Relaciones legales distintas se mezclan | Separar: usuarios vs proveedores |

## Referencia Detallada

Para el análisis completo con artículos, jurisprudencia, fuentes, y templates, ver:
`./contratos-digitales-2026-reference.md`

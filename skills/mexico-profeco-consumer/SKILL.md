---
name: mexico-profeco-consumer
description: Use when writing marketing copy with claims like "verified" or "trusted", evaluating advertising legality, handling platform liability, managing subscription cancellation flows, or assessing consumer protection compliance under Mexican law (PROFECO/LFPC) for digital platforms.
metadata:
  version: "1.1.1"
  last-verified: "2026-10-23"
  legal-basis: "LFPC vigente DOF 12-12-2025 + Acuerdo montos DOF 23-12-2025"
  review-by: "2027-01-21"
  cubre: "Protección al consumidor bajo la LFPC: legalidad de claims publicitarios, reforma de suscripciones (Art. 76 Bis, dic 2025), cláusulas abusivas, responsabilidad de plataformas, multas."
---

# Mexico PROFECO Consumer Protection (LFPC 2026)

## Overview

Guía de cumplimiento con la **Ley Federal de Protección al Consumidor** (LFPC) para plataformas digitales que operan en México, con enfoque en directorios de salud que hacen claims de verificación y venden suscripciones.

**DISCLAIMER:** Esta guía NO constituye asesoría legal. Consultar un abogado especializado en protección al consumidor digital.

## When to Use

- Escribir o revisar copy de marketing con claims ("verified", "trusted", "recommended")
- Evaluar si un claim publicitario es legal bajo LFPC
- Diseñar flujos de suscripción/cancelación de membresías
- Revisar cláusulas de limitación de responsabilidad
- Manejar quejas de consumidores (expats o mexicanos)
- Evaluar riesgo de badges de verificación
- Diseñar política de reembolsos/cancelaciones
- Preparar compliance para Distintivo Digital PROFECO

## Quick Reference

### Reforma Diciembre 2025 — YA VIGENTE

La LFPC fue reformada el 12 de diciembre de 2025, agregando fracciones VIII y IX al Art. 76 Bis. **Aplica a toda suscripción digital con cobro recurrente vendida al consumidor final** (Art. 2 fr. I). En membresías vendidas a proveedores que las integran a sus servicios a terceros, cumplir estos requisitos es política comercial, no obligación de la LFPC.

| Requisito nuevo | Artículo | Obligatorio |
|-----------------|----------|-------------|
| Informar de forma clara, destacada y accesible si hay cobros automáticos recurrentes, su periodicidad, monto y fecha de cobro ("antes de contratar" es lectura de diseño, no letra de ley) | 76 Bis-VIII | **SÍ** |
| Consentimiento expreso e informado (checkbox no pre-marcado = lectura de implementación, no texto legal) | 76 Bis-VIII | **SÍ** |
| Notificar **5 días naturales antes** de cada renovación | 76 Bis-**VIII** | **SÍ**, sólo si el contrato prevé renovación automática |
| Mecanismo de cancelación inmediata | 76 Bis-**IX** | **SÍ** |
| Sin penalización si se cancela dentro de la ventana de aviso | 76 Bis-**VIII** | **SÍ** |
| Cancelar por el **mismo medio** de contratación | — | **NO es texto legal.** Es glosa de firma legal (Arochi & Lindner). La ley dice: cancelación "de manera inmediata, sin contravenir a las disposiciones contractuales" |

**"Un clic para suscribirse, un clic para cancelar"** — lectura de la industria (glosa de Arochi & Lindner), **no letra de ley**. El texto vigente sólo exige cancelación inmediata sin contravenir las disposiciones contractuales.

### Derecho de Retracto (Art. 56)

Para compras en línea, el consumidor puede **revocar su consentimiento sin responsabilidad** dentro de los primeros **5 días hábiles**.

**Implicación:** El retracto protege al consumidor final. Un consultorio o clínica que compra la membresía para ofrecer sus servicios a terceros es consumidor sólo para quejas y conciliación (arts. 2 fr. I, 99 y 117; operaciones ≤ \$760,889.82 en 2026; personas morales sólo si son microempresas). Ofrecer retracto a proveedores es política comercial, no obligación de la LFPC.

### Publicidad — Reglas Clave

| Principio | Artículo | Detalle |
|-----------|----------|---------|
| **No engañosa** | Art. 32 ¶1 | No inducir a error o confusión |
| **No abusiva** | Art. 32 ¶2 | Engañosa o abusiva = induce o puede inducir a error por la forma inexacta, falsa, exagerada, parcial, artificiosa o tendenciosa. La protección a grupos vulnerables en línea está en el Art. 76 Bis fr. VII |
| **Comprobabilidad** | Art. 32 ¶1 | La publicidad debe ser veraz **y comprobable** — el deber de sustento nace del propio Art. 32, no del 35 |
| **Facultades PROFECO** | Art. 35 | PROFECO puede ordenar suspender la publicidad, ordenar que se corrija, sancionar, y ordenar la publicación de la leyenda **"veracidad no comprobada"** |
| **Avales y certificaciones** | Art. 32 ¶4 | Prohibido afirmar que algo está **avalado / aprobado / recomendado / certificado** por **sociedades o asociaciones profesionales** sin la documentación que lo soporte con evidencia científica, objetiva y fehaciente |

## Análisis de Claims de Marketing

### Claims Específicos para Directorios de Salud

| Claim | Riesgo | Problema | Recomendación |
|-------|--------|----------|---------------|
| "Verified" (solo) | **ALTO** | Implica validación integral sin definir qué se verificó | Cambiar a **"Credential-Checked"** + disclaimer |
| "Not verified" / "reprobó" aplicado a quien nunca entró al estándar | **ALTO** | Implica que se intentó un check y falló, cuando no aplicaba ninguno. Falso y potencialmente difamatorio | **"Fuera de alcance" / "out of scope"** |
| "You Can Trust" | **MEDIO-ALTO** | Podría interpretarse como garantía de calidad médica | Eliminar o cambiar a "Reviewed" |
| "Recommended by expats" | **MEDIO-ALTO** | Requiere sustento en reseñas reales verificables | Cambiar a "Rated by expats" (con reviews reales) |
| "55+ verified providers" | **BAJO** | Dato cuantificable, pero "verified" necesita definición | Mantener + definir "verified" |
| Verified Badge | **MEDIO-ALTO** | Badge visual crea impresión fuerte de endorsement | Rediseñar: tooltip + fecha + scope |
| "The only verified directory" | **ALTO** | Exclusividad requiere sustento absoluto | NO usar |
| "Most trusted" | **ALTO** | Superlativo sin sustento = publicidad exagerada | NO usar |
| "English-Speaking" | **BAJO** | Dato factual verificable | OK |

### Disclaimer Recomendado para Verificación

```
Verification confirms the provider holds a valid Cédula Profesional
registered with Mexico's SEP (Secretaría de Educación Pública).
It does not constitute an endorsement of medical quality, outcomes,
or suitability for your specific needs.
```

### Página de Verificación Recomendada

Crear URL `/verification-process` que explique:
1. Qué se verifica (Cédula Profesional vía base de datos SEP)
2. Qué NO se verifica (calidad de atención, resultados, especialización)
3. Fecha de última verificación por proveedor
4. Cómo reportar información incorrecta

## Responsabilidad de la Plataforma

### Marco Legal

México **NO tiene** un "safe harbor" general legislado internamente como EE.UU. (Section 230); sí uno sectorial para derechos de autor (LFDA arts. 114 Septies–114 Octies, notice and takedown). Además, el **T-MEC Art. 19.17** (ya vigente desde julio 2023) ofrece protección para contenido de terceros.

| Tipo de contenido | Protección T-MEC | Ejemplo |
|--------------------|-----------------|---------|
| Contenido de terceros (reseñas) | **SÍ protegido** | Reseña de un expat sobre un doctor |
| Contenido propio de la plataforma | **NO protegido** | Badges, descripciones editoriales, claims |
| Acciones de moderación de buena fe | **SÍ protegido** | Eliminar reseñas falsas o dañinas |

### Escenarios de Riesgo

| Escenario | Riesgo | Por qué |
|-----------|--------|---------|
| Proveedor da mala atención médica | BAJO | Directorio no provee servicios médicos |
| Badge "verified" + doctor incompetente | **MEDIO-ALTO** | "Verified" podría interpretarse como endorsement |
| Reseñas falsas/difamatorias | BAJO-MEDIO | T-MEC protege, pero deber de retirar tras notificación |
| Provider paga Featured y es fraudulento | **ALTO** | Cobro + badge = relación comercial interpretable como endorsement |
| Info desactualizada de provider | MEDIO | Deber de mantener información razonablemente actualizada |

### Cláusulas Abusivas (**Art. 90** LFPC)

Las siguientes cláusulas **no serán válidas y se tendrán por no puestas** en contratos de adhesión:

| Cláusula (fracción Art. 90) | Ejemplo prohibido |
|----------|-------------------|
| Modificación unilateral del contrato o sustraerse de sus obligaciones (fr. I) | "We may change these terms at any time" |
| Liberar al proveedor de su responsabilidad civil (fr. II) | "No nos hacemos responsables bajo ninguna circunstancia" |
| Trasladar al consumidor o a un tercero la responsabilidad civil del proveedor (fr. III) | "El usuario indemnizará a la plataforma por cualquier reclamación derivada de nuestros propios contenidos" |
| Hacer renunciar al consumidor a la protección de la LFPC o someterlo a tribunales extranjeros (fr. VI) | "Disputes shall be resolved exclusively by the courts of California" |

**En su lugar:** Usar disclaimers específicos que expliquen exactamente qué se verificó y qué no, con limitaciones razonables.

## Jurisdicción PROFECO

### ¿Quién regula qué?

| Autoridad | Jurisdicción | Directorio en línea |
|-----------|-------------|------------|
| **PROFECO** | Publicidad engañosa, comercio electrónico, suscripciones | **SÍ aplica** |
| **COFEPRIS** | Publicidad de servicios de salud directos, riesgo sanitario | NO aplica (directorio, no proveedor médico) |
| **SABG** | Protección de datos personales | SÍ aplica (ver skill mexico-privacy-law) |

**IMPORTANTE:** La LFPC excluye los servicios profesionales que no sean de carácter mercantil (art. 5). Clínicas y hospitales privados que operan como negocio sí están bajo la LFPC. PROFECO **SÍ** tiene jurisdicción, además, sobre el servicio del directorio (publicidad, membresías, comercio electrónico).

### Protección a Extranjeros

PROFECO tiene el departamento **C.A.R.E.** (Conciliation Services to Foreign Residents) que atiende quejas de extranjeros en México.
- Email: extranjeros@profeco.gob.mx (*verificar antes de usar*)
- Jurisdicción: toda transacción en territorio mexicano, sin importar nacionalidad del consumidor

## Multas y Sanciones (2026)

Montos vigentes 2026 (Acuerdo DOF 23-12-2025, +3.8% por actualización inflacionaria). **Reverificar en enero de cada año.**

| Infracción | Rango | Artículo |
|------------|-------|----------|
| Publicidad engañosa (Art. 32) — ordinaria | \$380.44 – \$1,217,423.72 | **Art. 126** (catch-all) |
| Publicidad engañosa **grave** | \$228,266.96 – \$6,391,474.56 + clausura ≤ 90 días | Art. 128 Bis ¶1 (multa y clausura); gravedad: Art. 128 Ter fr. VI |
| Grave + reincidencia | Hasta **10% de los ingresos brutos anuales** | Art. 128 Bis ¶2 |
| Incumplir Art. 76 Bis (suscripciones) | \$1,093.02 – \$4,274,960.73 | **Art. 128** |
| Cláusulas abusivas (Art. 90) y desacato a órdenes sobre publicidad (Art. 35), entre otros | \$760.89 – \$2,434,847.42 | Art. 127 |
| Reincidencia | Hasta el **doble** de la multa + arresto ≤ 36 h | Art. 129 |
| Medida de apremio: desobedecer un mandato de PROFECO (previo apercibimiento) | Hasta \$15,217.79 **por día**, máx. 180 días | **Art. 25 fr. IV** |
| Tope agregado por un mismo hecho | \$12,782,949.06 | Art. 133 ¶2 |

**Precedente:** PROFECO sancionó a Uber, Easy Taxi y Cabify en **julio de 2018** por cláusulas abusivas y publicidad engañosa — **\$6.484 millones de pesos en total** (Uber \$3,974,000 · Easy Taxi ≈ \$1,810,000 · Cabify \$700,000). Fecha y desglose: *verificar antes de usar*.

## Distintivo Digital PROFECO

Sello voluntario de confianza para comercio electrónico.

| Aspecto | Detalle |
|---------|---------|
| Costo | Gratuito (solo cumplir requisitos) |
| Requisitos | 1 año de antigüedad, SAT registrado, HTTPS, contrato de adhesión **registrado** ante PROFECO, **sin adeudos** con la Procuraduría (*verificar antes de usar*) |
| Resolución | 30 días naturales desde la solicitud (*verificar antes de usar*) |
| Validez | "Anual, renovable" **no confirmada** en fuente oficial — verificar antes de afirmarlo |
| Beneficio | Credibilidad + relación positiva con PROFECO |
| URL | distintivodigital.profeco.gob.mx |

## Checklist de Compliance

### Prioridad Inmediata (antes de monetizar)

*Alcance:* los puntos de Art. 76 Bis y de retracto son obligatorios frente al consumidor final (Art. 2 fr. I); en membresías vendidas a proveedores son política comercial.

- [ ] Implementar cancelación inmediata de membresías en línea (Art. 76 Bis-IX)
- [ ] Sistema de notificación 5 días antes de renovación automática
- [ ] Checkout con monto + frecuencia + fecha de cobro claros
- [ ] Checkbox de consentimiento NO pre-marcado para suscripciones
- [ ] Cambiar "Verified" por **"Credential-Checked"** en todo el sitio (terminología canónica vigente; "Cédula-Verified" fue redacción intermedia ya superada)
- [ ] Agregar disclaimers en badges y páginas de verificación
- [ ] Crear página `/verification-process` explicativa
- [ ] Comunicar derecho de retracto (5 días hábiles) en T&C para consumidores finales; para proveedores que compran membresías, sólo si se ofrece como política

### Prioridad Media

- [ ] Revisar y eliminar claims no sustentables ("trusted", "recommended" sin base)
- [ ] Implementar mecanismo de quejas visible (email + formulario)
- [ ] Política de reembolsos documentada y accesible
- [ ] Rediseñar badge: tooltip con scope + fecha de verificación
- [ ] Evaluar registro voluntario de contrato de adhesión ante PROFECO

### Prioridad Baja

- [ ] Aplicar para Distintivo Digital PROFECO (después de 1 año)
- [ ] Monitorear Art. 56 Bis propuesto (14 días naturales de retracto para servicios digitales) — iniciativa del 30-sep-2025 (SIL `asun_4936506`), **NO aprobada a agosto de 2026**; confirmar estado legislativo actual antes de asesorar sobre plazos de retracto
- [ ] Consultar abogado para revisión formal de T&C
- [ ] Evaluar Concilianet (resolución de controversias PROFECO)

## Common Mistakes

| Error | Consecuencia | Corrección |
|-------|-------------|------------|
| Usar "verified" sin definir qué se verificó | Publicidad engañosa ante PROFECO | Especificar: **"Credential-Checked against Mexico's federal SEP registry"** |
| Etiquetar como "no verificado" a quien queda fuera del estándar | Afirmación falsa + riesgo de daño moral al tercero | **"Fuera de alcance"**; nunca implicar que hubo un check fallido |
| Exención total de responsabilidad en T&C | Cláusula abusiva = nula automáticamente | Disclaimers específicos y limitados |
| Sin botón de cancelación en línea | Violación Art. 76 Bis-IX (dic 2025) | Mecanismo de cancelación inmediata |
| Sin aviso previo a renovación automática | Violación Art. 76 Bis-**VIII** | Email **5 días naturales** antes |
| Tribunales de California como foro exclusivo en T&C | Cláusula abusiva bajo LFPC (Art. 90 fr. VI) | Jurisdicción Ciudad de México |
| Claims superlativos sin sustento | Multa Art. 126 (hasta \$1,217,423.72); 10% sólo si es particularmente grave y hay reincidencia | Evitar "most trusted", "the only", "best" |
| Ignorar quejas de extranjeros | PROFECO C.A.R.E. puede intervenir | Mecanismo de quejas en inglés y español |

## Referencia Detallada

Para el análisis completo con artículos, jurisprudencia, fuentes, y análisis de claims, ver:
`./profeco-2026-reference.md`

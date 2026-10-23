---
name: mexico-privacy-law
description: Use when creating privacy policies, terms of service, cookie banners, data collection forms, consent flows, or evaluating compliance with Mexican data protection law (LFPDPPP 2025). Also use when handling ARCO rights requests, international data transfers, or sensitive health data in Mexican projects.
metadata:
  version: "1.0.1"
  last-verified: "2026-10-23"
  review-by: "2027-01-21"
  cubre: "Cumplimiento con la LFPDPPP 2025 (nueva ley; autoridad: Secretaría Anticorrupción y Buen Gobierno, SABG): avisos de privacidad, consentimiento, datos sensibles, derechos ARCO, transferencias internacionales, cookies."
---

# Mexico Privacy Law Expert (LFPDPPP 2025)

## Overview

Guia de cumplimiento con la **nueva Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares** (vigente desde 21 de marzo de 2025), que reemplazo completamente la ley de 2010. La autoridad de enforcement cambio del INAI a la **Secretaría Anticorrupción y Buen Gobierno (SABG)** (LFPDPPP art. 2, fracc. XV). El INAI se extinguió al entrar en vigor la legislación secundaria (decreto constitucional DOF 20-12-2024, transitorio Quinto), el 21-03-2025.

**DISCLAIMER:** Esta guia NO constituye asesoria legal. Consultar un abogado especializado para validar la estrategia de cumplimiento.

## When to Use

- Crear o revisar Aviso de Privacidad (integral o simplificado)
- Evaluar si se requiere consentimiento (tacito, expreso, o por escrito)
- Manejar datos sensibles (salud, biometricos, creencias)
- Configurar transferencias internacionales de datos
- Implementar derechos ARCO
- Crear terminos y condiciones para sitios web
- Disenar flujos de registro con cookie consent
- Responder a solicitudes de eliminacion de datos
- Evaluar riesgos de multas y sanciones

## Quick Reference

### Cambios criticos 2025 vs 2010

| Aspecto | Ley 2010 | Nueva Ley 2025 |
|---------|----------|-----------------|
| Autoridad | INAI (autonomo) | SABG (poder ejecutivo) |
| Datos personales | Persona identificada | Persona **identificable** (mas amplio) |
| Consentimiento | Libre e informado | Libre, **especifico** e informado |
| Encargados | Obligaciones indirectas | Definidos en la ley (art. 2 XII); responden por daños (art. 53); las infracciones del art. 58 son del responsable |
| Decisiones automatizadas | No reguladas | Derecho a **oponerse** |
| Confidencialidad | Durante la relacion | **Incluso despues de terminada** |
| Reglamento | Publicado 2011 | **No publicado al 2026-10-23** (barrido SIDOF 21-03-2025 → 23-10-2026) |

### Tipos de consentimiento

| Tipo | Cuando aplica | Ejemplo |
|------|---------------|---------|
| **Tacito** | Datos no sensibles, no financieros | Nombre, email, preferencias |
| **Expreso** | Datos financieros o patrimoniales (art. 7, párr. 5) | Stripe, PayPal |
| **Expreso y por escrito** | **Datos sensibles** (salud, biometricos) | Resenas que revelan condiciones medicas |

**IMPORTANTE:** Por regla general vale el consentimiento tácito: el titular, con el aviso de privacidad a su disposición, no se opone (art. 7). Para datos financieros se requiere expreso y para sensibles expreso y por escrito. Sin aviso puesto a disposición no hay consentimiento tácito.

### Clasificacion de datos

| Dato | Tipo | Consentimiento |
|------|------|----------------|
| Nombre, email, telefono | Personal | Tacito |
| Direccion, fecha de nacimiento | Personal | Tacito |
| Tarjeta de credito, cuenta bancaria | Financiero | **Expreso** |
| Estado de salud, diagnosticos | **Sensible** | **Expreso y por escrito** |
| Preferencia sexual, religion | **Sensible** | **Expreso y por escrito** |
| Datos biometricos | **Sensible** cuando puedan revelar los aspectos del art. 2 VI o dar origen a discriminación (no están en la lista, que es enunciativa más no limitativa) | **Expreso y por escrito** (si son sensibles) |
| Cedula Profesional (via SEP) | Publico | **No requerido** (fuente publica; *verificar antes de usar*: el art. 2 X exige un registro consultable por disposición de ley) |

### Excepciones al consentimiento

No se requiere consentimiento cuando:
1. Una disposicion legal lo establezca (leyes, reglamentos, circulares)
2. Los datos provengan de **fuentes de acceso publico** (ej: SEP/Cedula Profesional)
3. Los datos se sometan a un procedimiento de **disociacion**
4. Exista una **situacion de emergencia** que potencialmente pueda dañar a un individuo en su persona o en sus bienes (art. 9 V)
5. Sea necesario para **atencion medica** directa, mientras el titular no esté en condiciones de otorgar el consentimiento, y por persona sujeta a secreto profesional (art. 9 VI)
6. Sea necesario para el **cumplimiento de una relacion juridica** (art. 9 IV)
7. Exista orden judicial, resolución o mandato fundado y motivado de autoridad competente (art. 9 VII)

### Multas (UMA 2026: \$117.31 MXN/dia — valor INEGI vigente feb 2026–ene 2027; verificar en inegi.org.mx/temas/uma/ para calculos posteriores)

| Infraccion | Rango UMAs | Rango MXN |
|------------|-----------|-----------|
| Art. 58 fracc. I | Apercibimiento (art. 59 I) | — |
| Art. 58 fracc. II–VII | 100–160,000 UMA (art. 59 II) | \$11,731–\$18,769,600 |
| Art. 58 fracc. VIII–XVIII | 200–320,000 UMA (art. 59 III) | \$23,462–\$37,539,200 |
| Reiteración | Multa adicional de 100–320,000 UMA (art. 59 IV) | \$11,731–\$37,539,200 |
| **Datos sensibles** | **Podrán incrementarse hasta por dos veces** (discrecional, art. 59 IV) | Hasta 640,000 UMA = \$75,078,400 |
| Prision (vulneracion) | 3 meses - 3 anos | — |
| Prision (fraude con datos) | 6 meses - 5 anos | — |

## Aviso de Privacidad

### Integral (publicado en sitio web)

Debe contener:
1. Identidad y domicilio del responsable
2. Datos personales que se tratan (listado especifico)
3. Cuales datos son **sensibles** (identificados explicitamente)
4. Finalidades del tratamiento (distinguir: con y sin consentimiento)
5. Mecanismos para **limitar uso o divulgacion**
6. Procedimiento para ejercer derechos **ARCO**
7. Medio para comunicar cambios al aviso
8. Procedimiento para **revocar consentimiento**
9. Transferencias de datos (nacionales e internacionales)
10. Uso de cookies y tecnologias de rastreo

### Simplificado (en punto de recoleccion)

Contenido minimo (art. 16 II):
1. Identidad y domicilio del responsable
2. Datos que se tratan, señalando los sensibles
3. Finalidades, distinguiendo las que requieren consentimiento
4. Opciones y medios para limitar uso o divulgación
5. Dónde consultar el aviso integral

## Derechos ARCO

| Derecho | Descripcion | Plazo respuesta |
|---------|-------------|-----------------|
| **A**cceso | Conocer que datos tiene el responsable | 20 dias habiles |
| **R**ectificacion | Corregir datos inexactos o desactualizados | 20 dias habiles |
| **C**ancelacion | Eliminar datos (bloqueo + supresion) | 20 dias habiles |
| **O**posicion | Oponerse al tratamiento por causa legitima | 20 dias habiles |

Implementacion post-respuesta: **15 dias habiles** adicionales.
Solicitud de protección de datos ante la Secretaría (SABG): dentro de **15 días** desde que se comunica la respuesta; si no hay respuesta, desde que vence el plazo del responsable (art. 40).

**Nuevo en 2025:** Incluye derecho a oponerse a **decisiones automatizadas** con efectos significativos.

## Transferencias Internacionales

Requieren que el aviso indique si el titular acepta la transferencia (art. 35); expreso sólo si los datos son financieros (art. 7) o sensibles, expreso y por escrito (art. 8). La remisión a un encargado no es transferencia (art. 2 XX).

Excepciones (art. 36 I–VII):
- Lo prevea una ley o un tratado internacional (fracc. I)
- Sea necesaria por razones de salud (fracc. II)
- Se haga a sociedades del mismo grupo del responsable (fracc. III)
- Sea necesaria por un contrato celebrado o por celebrar en interés del titular (fracc. IV)
- Sea necesaria por interés público o para la procuración o administración de justicia (fracc. V)
- Sea necesaria para la defensa de un derecho en un proceso judicial (fracc. VI)
- Sea necesaria para mantener o cumplir una relación jurídica entre el responsable y el titular (fracc. VII)

**NOTA:** La nueva ley **no establece mecanismos claros** para transferencias internacionales (no hay equivalente a clausulas contractuales tipo de la UE).

## Cookies y Rastreo

Mexico **no tiene ley especifica de cookies**. Requisitos derivados de principios generales:

| Tipo de cookie | Accion requerida |
|----------------|------------------|
| Esenciales (sesion, seguridad) | Solo informar |
| Analytics (GA4) | Informar + opcion de rechazo |
| Marketing (Meta Pixel) | Informar + consentimiento |

**Recomendacion:** Implementar cookie banner basico con aceptar/rechazar aunque la ley no lo exija explicitamente.

## Notificacion de Vulneraciones (Data Breach)

| Aspecto | Requisito |
|---------|-----------|
| Cuando | **De forma inmediata** cuando afecte de forma significativa los derechos patrimoniales o morales (art. 19) |
| A quien | A los **titulares afectados** (no obligatorio a la autoridad) |
| Contenido | Naturaleza, datos involucrados, consecuencias, mitigacion |
| Medio | Cualquiera que asegure recepcion |

## Aplicacion a Directorios de Salud

### Datos de proveedores

| Dato | Fuente | Consentimiento |
|------|--------|----------------|
| Nombre completo | SEP/Cedula | No requerido (publico) |
| Numero de Cedula | SEP | No requerido (publico) |
| Especialidad | SEP | No requerido (publico) |
| Institucion educativa | SEP | No requerido (publico) |
| Telefono de consultorio | Proveedor | Tacito o expreso |
| Sitio web | Proveedor | Tacito |
| Fotos | Proveedor | **Expreso** (*verificar antes de usar*) |
| Horarios | Proveedor | Tacito |

### Datos de usuarios/miembros

| Dato | Consentimiento |
|------|----------------|
| Nombre, email | Tacito (con aviso) |
| Preferencias de ubicacion | Tacito |
| Resenas (sin datos de salud) | Tacito |
| Resenas que revelan condicion medica | **Expreso y por escrito** |
| Datos de pago (Stripe) | **Expreso** (dato financiero, art. 7) |

### Normas de salud que NO aplican a un directorio

| Norma | Por que no aplica |
|-------|-------------------|
| NOM-004-SSA3-2012 | Regula expedientes clinicos |
| NOM-024-SSA3-2012 | Regula sistemas de registro electronico de salud |
| Ley General de Salud (expedientes) | El directorio no es establecimiento de atencion medica |

### Reguladores relevantes

| Autoridad | Jurisdiccion |
|-----------|-------------|
| SABG | Proteccion de datos personales |
| COFEPRIS | Si se ofrecen servicios de salud directos (NO aplica a directorio) |
| PROFECO | Publicidad enganosa, proteccion al consumidor |
| SEP | Verificacion de Cedulas Profesionales |

## Checklist de Compliance para Directorio de Salud

### Prioridad Alta (implementar primero)

- [ ] Aviso de Privacidad Integral publicado en sitio web (espanol + ingles)
- [ ] Aviso de Privacidad Simplificado en formularios de registro
- [ ] Identificar datos sensibles en el aviso (si se recolectan)
- [ ] Procedimiento ARCO documentado (formulario o email designado)
- [ ] Documentar base legal para datos de proveedores (fuente publica SEP)
- [ ] Cookie banner basico (aceptar/rechazar no esenciales)
- [ ] Cláusula en el aviso que indique si el titular acepta las transferencias (art. 35); consentimiento expreso sólo para datos financieros (art. 7) y expreso y por escrito para sensibles (art. 8)

### Prioridad Media

- [ ] Consentimiento expreso de proveedores para datos no publicos
- [ ] Mecanismo de consentimiento expreso para resenas con datos de salud
- [ ] Medidas de seguridad documentadas (SSL, hashing, accesos)
- [ ] Procedimiento de respuesta a incidentes de seguridad
- [ ] Terminos y condiciones actualizados con referencia a nueva ley

### Prioridad Baja (monitoreo)

- [ ] Monitorear publicacion del reglamento de la nueva LFPDPPP
- [ ] Monitorear lineamientos de la SABG
- [ ] Consultar abogado para validar estrategia de datos de Cedula como fuente publica
- [ ] Evaluar necesidad de Data Protection Impact Assessment

## Common Mistakes

| Error | Consecuencia | Correccion |
|-------|-------------|------------|
| Asumir que la ley de 2010 sigue vigente | Incumplimiento con nueva ley 2025 | Actualizar todo a nueva ley |
| No distinguir datos sensibles | Multas que pueden incrementarse hasta dos veces (art. 59 IV) | Clasificar explicitamente en aviso |
| Usar consentimiento tacito para datos de salud | Ilegal — requiere escrito | Implementar firma electronica |
| No informar transferencias a EE.UU. | Sancion por omision | Listar servicios en aviso |
| Considerar scroll como consentimiento para datos financieros o sensibles | El tácito sólo vale para datos ordinarios con el aviso a disposición (art. 7) | Acción afirmativa para financieros (art. 7); expreso y por escrito para sensibles (art. 8) |
| No tener procedimiento ARCO | Sancion + queja ante SABG | Crear formulario + procedimiento interno |
| Publicar fotos de proveedores sin consentimiento | Violacion aunque sean profesionales | Obtener consentimiento expreso (*verificar antes de usar*) |

## Referencia Detallada

Para el analisis completo con articulos, cronologia, fuentes, y recomendaciones especificas, ver:
`./lfpdppp-2025-reference.md`

---
name: mexico-privacy-law
description: Use when creating privacy policies, terms of service, cookie banners, data collection forms, consent flows, or evaluating compliance with Mexican data protection law (LFPDPPP 2025). Also use when handling ARCO rights requests, international data transfers, or sensitive health data in Mexican projects.
version: 1.0.0
last-verified: 2026-06-10
review-by: 2026-09-30
---

# Mexico Privacy Law Expert (LFPDPPP 2025)

## Overview

Guia de cumplimiento con la **nueva Ley Federal de Proteccion de Datos Personales en Posesion de los Particulares** (vigente desde 21 de marzo de 2025), que reemplazo completamente la ley de 2010. La autoridad de enforcement cambio del INAI (disuelto) a la **SABG** (Secretaria de Anticorrupcion y Buen Gobierno).

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
| Encargados | Obligaciones indirectas | **Directamente sujetos** a la ley |
| Decisiones automatizadas | No reguladas | Derecho a **oponerse** |
| Confidencialidad | Durante la relacion | **Incluso despues de terminada** |
| Reglamento | Publicado 2011 | **Pendiente** (feb 2026) |

### Tipos de consentimiento

| Tipo | Cuando aplica | Ejemplo |
|------|---------------|---------|
| **Tacito** | Datos no sensibles, no financieros | Nombre, email, preferencias |
| **Expreso** | Datos financieros, transferencias internacionales | Stripe, PayPal, envio de datos a EE.UU. |
| **Expreso y por escrito** | **Datos sensibles** (salud, biometricos) | Resenas que revelan condiciones medicas |

**IMPORTANTE:** Bajo la nueva ley, la inaccion (scroll, no interactuar) **NO constituye consentimiento**.

### Clasificacion de datos

| Dato | Tipo | Consentimiento |
|------|------|----------------|
| Nombre, email, telefono | Personal | Tacito |
| Direccion, fecha de nacimiento | Personal | Tacito |
| Tarjeta de credito, cuenta bancaria | Financiero | **Expreso** |
| Estado de salud, diagnosticos | **Sensible** | **Expreso y por escrito** |
| Preferencia sexual, religion | **Sensible** | **Expreso y por escrito** |
| Datos biometricos | **Sensible** | **Expreso y por escrito** |
| Cedula Profesional (via SEP) | Publico | **No requerido** (fuente publica) |

### Excepciones al consentimiento

No se requiere consentimiento cuando:
1. Una disposicion legal lo establezca (leyes, reglamentos, circulares)
2. Los datos provengan de **fuentes de acceso publico** (ej: SEP/Cedula Profesional)
3. Los datos se sometan a un procedimiento de **disociacion**
4. Exista una **situacion de emergencia** que amenace la vida
5. Sea necesario para **atencion medica** directa
6. Sea necesario para el **cumplimiento de una relacion juridica**

### Multas (UMA 2026: \$117.31 MXN/dia — valor INEGI vigente feb 2026–ene 2027; verificar en inegi.org.mx/temas/uma/ para calculos posteriores)

| Infraccion | Rango UMAs | Rango MXN | Rango USD aprox. |
|------------|-----------|-----------|-------------------|
| Menor | 100 - 160,000 | \$11,731 - \$18.7M | \$580 - \$930K |
| Grave | 200 - 320,000 | \$23,462 - \$37.5M | \$1,160 - \$1.86M |
| **Con datos sensibles** | **Se duplican** | Hasta \$75M | Hasta \$3.72M |
| Prision (vulneracion) | 3 meses - 3 anos | — | — |
| Prision (fraude con datos) | 6 meses - 5 anos | — | — |

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

Contenido minimo:
1. Identidad y domicilio del responsable
2. Finalidades del tratamiento
3. Enlace al aviso integral

## Derechos ARCO

| Derecho | Descripcion | Plazo respuesta |
|---------|-------------|-----------------|
| **A**cceso | Conocer que datos tiene el responsable | 20 dias habiles |
| **R**ectificacion | Corregir datos inexactos o desactualizados | 20 dias habiles |
| **C**ancelacion | Eliminar datos (bloqueo + supresion) | 20 dias habiles |
| **O**posicion | Oponerse al tratamiento por causa legitima | 20 dias habiles |

Implementacion post-respuesta: **15 dias habiles** adicionales.
Queja ante autoridad (SABG): **15 dias** si no hay respuesta.

**Nuevo en 2025:** Incluye derecho a oponerse a **decisiones automatizadas** con efectos significativos.

## Transferencias Internacionales

Requieren **consentimiento expreso** del titular, excepto cuando:
- Exista un tratado internacional aplicable
- Sea necesario para atencion medica
- Sea necesario para cumplimiento de contrato
- Lo requiera autoridad competente
- Sea de interes publico

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
| Cuando | **Sin demora** cuando afecte significativamente derechos |
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
| Fotos | Proveedor | **Expreso** |
| Horarios | Proveedor | Tacito |

### Datos de usuarios/miembros

| Dato | Consentimiento |
|------|----------------|
| Nombre, email | Tacito (con aviso) |
| Preferencias de ubicacion | Tacito |
| Resenas (sin datos de salud) | Tacito |
| Resenas que revelan condicion medica | **Expreso y por escrito** |
| Datos de pago (Stripe) | **Expreso** (financiero + transferencia int'l) |

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
- [ ] Consentimiento expreso en registro de miembros para transferencias internacionales

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
| No distinguir datos sensibles | Multas duplicadas | Clasificar explicitamente en aviso |
| Usar consentimiento tacito para datos de salud | Ilegal — requiere escrito | Implementar firma electronica |
| No informar transferencias a EE.UU. | Sancion por omision | Listar servicios en aviso |
| Considerar scroll como consentimiento | Invalido bajo nueva ley | Usar acciones afirmativas (checkbox, clic) |
| No tener procedimiento ARCO | Sancion + queja ante SABG | Crear formulario + procedimiento interno |
| Publicar fotos de proveedores sin consentimiento | Violacion aunque sean profesionales | Obtener consentimiento expreso |

## Referencia Detallada

Para el analisis completo con articulos, cronologia, fuentes, y recomendaciones especificas, ver:
`./lfpdppp-2025-reference.md`

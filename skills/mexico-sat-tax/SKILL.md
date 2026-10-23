---
name: mexico-sat-tax
description: Use when creating invoices, configuring CFDI, pricing with IVA, handling tax obligations, or evaluating compliance with Mexican tax law (SAT) for persona física con actividad empresarial. Also use when adjusting pricing pages, membership fees, or B2B billing for Mexican clients.
metadata:
  version: "1.1.1"
  last-verified: "2026-10-23"
  review-by: "2027-01-21"
  cubre: "Facturación CFDI 4.0, cálculo de IVA/ISR, régimen RESICO vs actividad empresarial, retenciones, declaraciones y plazos ante el SAT para persona física con actividad empresarial."
---

# Mexico SAT Tax Expert (Persona Física con Actividad Empresarial)

## Overview

Guía de cumplimiento fiscal con el SAT para **persona física con actividad empresarial** que opera un directorio de salud en línea y factura CFDIs por membresías/suscripciones a proveedores de salud.

**DISCLAIMER:** Esta guía NO constituye asesoría fiscal. Consultar un contador público certificado para validar la estrategia fiscal.

## When to Use

- Configurar o revisar facturación (CFDI 4.0)
- Calcular precios con/sin IVA para membresías
- Evaluar régimen fiscal óptimo (RESICO vs RAEP)
- Preparar declaraciones mensuales o anuales
- Manejar retenciones de IVA/ISR por personas morales
- Crear o actualizar páginas de pricing con tratamiento fiscal correcto
- Evaluar si aplica régimen de plataformas digitales
- Responder a requerimientos del SAT o auditorías

## Quick Reference

### Régimen Fiscal — RESICO vs RAEP

| Aspecto | RESICO | RAEP (Actividad Empresarial) |
|---------|--------|------------------------------|
| Límite de ingresos | \$3,500,000 MXN/año | Sin límite |
| Tasa ISR | 1.00% - 2.50% (sobre ingresos) | 1.92% - 35% (sobre utilidad) |
| Deducciones | NO se deducen gastos | SÍ se deducen gastos |
| Contabilidad | Simplificada | Completa |
| Ideal cuando | Gastos bajos (negocio digital) | Gastos altos (>40% de ingresos) |
| Ejemplo: \$100K/mes ingreso | ~\$2,000 ISR (2.00%) | ~\$23,736 ISR (sin deducciones) |

**Para un directorio digital:** RESICO es significativamente mejor mientras los ingresos estén debajo de \$3.5M MXN/año y los gastos deducibles sean bajos (hosting, dominio, software).

**La opción es por la persona, no por el negocio:** quien opta por RESICO debe hacerlo por la totalidad de sus actividades empresariales, profesionales u otorgamiento del uso o goce temporal de bienes (RMF 2026 regla 3.13.3, verificado 2026-10-23). No se puede tener un negocio en RESICO y otro en RAEP bajo el mismo RFC, así que la evaluación se hace sobre todas las actividades de la persona física.

### Tasas RESICO 2026

| Ingreso mensual | Tasa ISR |
|-----------------|----------|
| Hasta \$25,000 | 1.00% |
| \$25,001 - \$50,000 | 1.10% |
| \$50,001 - \$83,333 | 1.50% |
| \$83,334 - \$208,333 | 2.00% |
| \$208,334 - \$3,500,000 | 2.50% |

### IVA — Reglas para Membresías

| Concepto | Tratamiento |
|----------|-------------|
| Tasa general IVA | **16%** |
| Zona fronteriza (norte **y sur**) | **8%** — estímulo por decreto, ambos vigentes hasta el **31-dic-2026**; verificar prórroga antes de cotizar 2027 |
| Membresías a residentes MX | **16% obligatorio** |
| Exportación de servicios | **0%** (si cliente reside en el extranjero) |
| ¿Exento? | **NO** — servicios de directorio no están exentos |

### Precios con IVA — ejemplo

| Plan | Precio sin IVA | IVA (16%) | Total con IVA |
|------|---------------|-----------|---------------|
| Basic | \$0 | \$0 | \$0 |
| Professional | \$849 MXN | \$135.84 | \$984.84 MXN |
| Featured | \$1,699 MXN | \$271.84 | \$1,970.84 MXN |

**Práctica estándar B2B en México:** Mostrar precios **sin IVA** + leyenda "más IVA" o "IVA no incluido". La factura CFDI desglosa el IVA por separado.

### Retenciones cuando el cliente es Persona Moral

⚠️ **La retención depende del TIPO DE INGRESO, no del tipo de cliente.** Vender membresías/publicidad es **actividad empresarial**, no servicio personal independiente ni servicio profesional.

| Concepto | ¿Aplica a actividad empresarial? | Fundamento |
|----------|----------------------------------|------------|
| Retención IVA 2/3 (10.6667%) | **NO** | LIVA art. 1o.-A fracc. II inciso a) + art. 14 último párrafo: sólo servicios *personales* independientes, y "personal" excluye lo que tenga naturaleza de actividad empresarial. RIVA art. 3 fracc. I. |
| Retención ISR 10% | **NO** | LISR art. 106: sólo cuando se prestan *servicios profesionales* a personas morales. |
| Retención ISR 1.25% (RESICO) | **SÍ** | LISR art. 113-J: aplica a actividades empresariales, profesionales y uso o goce temporal. |

**Ejemplo (Professional \$849, emisor RESICO, cliente persona moral):**

| Concepto | Monto |
|----------|-------|
| Subtotal | \$849.00 |
| IVA 16% | \$135.84 |
| Total facturado | \$984.84 |
| Retención ISR RESICO 1.25% | -\$10.61 |
| **Neto a recibir** | **\$974.23** |

Si el emisor está en RAEP por actividad empresarial, **no hay retención alguna**: recibe los \$984.84 completos.

**IMPORTANTE:** La retención NO es un gasto — se acredita en la declaración mensual. Pero afecta el flujo de efectivo.

## CFDI 4.0 — Configuración para Membresías

### Datos del CFDI

| Campo | Valor recomendado |
|-------|-------------------|
| Versión | **4.0** (vigente) |
| Clave de producto/servicio | **80141601** (Servicios de promoción de ventas) |
| Unidad de medida | **E48** (Unidad de servicio) |
| Uso del CFDI (receptor) | **G03** (Gastos en general) — ⚠️ G03 NO admite régimen receptor **616**; para público en general el uso es **S01** (causa típica de rechazo del PAC; claves G03/616/S01: *verificar antes de usar* en el catálogo c_UsoCFDI del SAT) |
| Método de pago | **PUE** (Pago en una sola exhibición) |
| Forma de pago | Según medio: 01 (efectivo), 03 (transferencia), 04 (tarjeta crédito), 28 (tarjeta débito), 31 (intermediario pagos) |
| Régimen fiscal emisor | **626** (RESICO) o **612** (RAEP) |
| Exportación | **01** (No aplica) |

### CFDI para Público en General (Global Invoice)

Cuando el cliente NO solicita factura con sus datos fiscales:

| Campo | Valor |
|-------|-------|
| RFC receptor | **XAXX010101000** |
| Nombre receptor | **PUBLICO EN GENERAL** |
| Régimen receptor | **616** (Sin obligaciones fiscales) |
| CP receptor | CP del emisor |
| Uso del CFDI | **S01** (Sin efectos fiscales) |
| Periodicidad | **04** (Mensual) — emitir dentro de las **24 horas** siguientes al cierre de las operaciones del periodo (RMF 2026 regla 2.7.1.21; ya NO son los primeros 5 días del mes siguiente; verificado 2026-10-23 contra el texto DOF 28-12-2025) |

**Dos reglas que suelen olvidarse** (RMF 2026 regla 2.7.1.21, verificado 2026-10-23):

- **RESICO:** en el CFDI global por las operaciones del mes se incluye únicamente el monto total de las operaciones del periodo (párrafo primero). Que RESICO no pueda usar periodicidad diaria o semanal no está escrito así en la regla: *verificar antes de usar*.
- **Operaciones menores a \$100.00:** si el cliente no pide comprobante, no hay obligación de expedirlo por operaciones con el público en general de importe inferior a \$100.00. Si lo pide, se expide.

### Cancelación de CFDI (Reglas 2026)

| Plazo | Acción | Multa |
|-------|--------|-------|
| Hasta el mes de la declaración anual del ejercicio de expedición | Cancelación en plazo | \$0 |
| Después de ese plazo | Cancelación extemporánea | **5% - 10%** del monto |
| Requiere motivo | Siempre seleccionar código de cancelación | — |

**CFF art. 29-A (reformado DOF 07-11-2025):** un CFDI emitido en 2026 se puede cancelar hasta abril de 2027 (PF) o marzo de 2027 (PM). La regla anterior ("mismo ejercicio") ya no está vigente.

## Obligaciones Fiscales Mensuales

### Calendario de Declaraciones

| Obligación | Plazo | Frecuencia |
|------------|-------|------------|
| ISR provisional | Día **17** del mes siguiente | Mensual |
| IVA definitiva | Día **17** del mes siguiente | Mensual |
| Retenciones de IVA | Día **17** del mes siguiente | Mensual (si aplica) |
| Declaración anual | **Abril** del año siguiente | Anual |
| DIOT (informativa IVA) | **Durante el mes inmediato posterior** al periodo, a más tardar su último día (RMF 2026 regla 4.5.1, párr. segundo) | Mensual (⚠️ zona gris para RESICO PF — ver referencia) |

> ⚠️ **La DIOT no vence el día 17.** LIVA art. 32 fracc. VIII fija "a más tardar el día 17 del mes inmediato posterior", pero la regla 4.5.1 de la RMF 2026 permite a las personas físicas presentarla durante todo el mes inmediato posterior (verificado 2026-10-23). El día 17 es el plazo de ISR provisional e IVA definitivo.

> **Días adicionales por sexto dígito del RFC** (Decreto DOF 26-12-2013, art. 5.1): 1-2 → +1 día hábil · 3-4 → +2 · 5-6 → +3 · 7-8 → +4 · 9-0 → +5. Aplica automáticamente a personas físicas; no se solicita.

### Recargos por Pago Tardío (2026)

| Concepto | Tasa |
|----------|------|
| Recargos mensuales | **2.07%** (antes 1.47% — aumento del 40%; tasa fijada por el **art. 11 fracc. I de la Ley de Ingresos de la Federación** 2026: prórroga 1.38% × 1.5 = 2.07%, CFF art. 21 — verificar la LIF del ejercicio fiscal vigente antes de calcular) |
| Actualización | Según INPC mensual |

## Plataformas Digitales — NO Aplica

Un directorio de este tipo **NO es plataforma digital** en sentido fiscal porque:

| Criterio SAT | Directorio en línea | Resultado |
|--------------|-----------|-----------|
| Intermediario entre usuarios | NO — vende servicios propios | No aplica |
| Conecta oferta/demanda | NO — es directorio, no marketplace transaccional | No aplica |
| Retiene pago de terceros | NO — cobra por sus propias membresías | No aplica |

**Plataformas digitales** = Uber, Airbnb, Mercado Libre, Rappi (intermediarios transaccionales). Un directorio en línea = negocio propio que factura directamente.

## Exportación de Servicios (Tasa 0% IVA)

Si un proveedor de salud reside **fuera de México** y paga membresía:

| Requisito | Detalle |
|-----------|---------|
| Tasa IVA | **0%** (no 16%) |
| Condición 1 | Servicio aprovechado en el extranjero |
| Condición 2 | Se exporta **en la proporción** en que el servicio sea aprovechado en el extranjero (RIVA art. 59). LIVA art. 29 fracc. IV inciso c) lista "Publicidad" expresamente. |
| Condición 3 | Clave del campo Exportación del CFDI para servicios: *verificar antes de usar* en el catálogo c_Exportacion del Anexo 20. La clave de exportación definitiva que esta fila daba antes no se confirmó en el catálogo, y hay una lectura del SAT en reunión con síndicos (2023-09-07) según la cual a los servicios les corresponde la clave "No aplica" y el campo no condiciona la tasa 0%; esa minuta no se abrió en esta revisión |
| Condición 4 | El servicio debe caber en uno de los incisos de LIVA art. 29 fracc. IV (entre ellos asistencia técnica, publicidad, comisiones y mediaciones y servicios de tecnologías de la información). Un servicio que no está en la lista, como "consultoría" a secas, no se exporta a tasa 0%. El encuadre debe sostenerse en el contrato y en lo que realmente se presta (verificado 2026-10-23) |
| Condición 5 | Prueba del cobro: se entiende, entre otros supuestos, que el servicio se aprovecha en el extranjero cuando lo contrata y paga un residente en el extranjero sin establecimiento en el país, con cheque nominativo o transferencia a cuentas del prestador en instituciones de crédito o casas de bolsa, y el pago proviene de cuentas en instituciones financieras ubicadas en el extranjero (RLIVA art. 58, párr. segundo; verificado 2026-10-23). Si un pago por plataforma de transferencias que llega como transferencia nacional cumple esta condición: *verificar antes de usar* |
| Registro | Conservar comprobante de transferencia internacional. Si el cobro no es en una sola exhibición o se factura antes de cobrar: un CFDI por el valor total al realizarse la operación y un CFDI con complemento para recepción de pagos por cada pago (RMF 2026 regla 2.7.1.32). Tipo de cambio: el de adquisición de la divisa o, sin adquisición, el que Banco de México publica en el DOF el día anterior a aquél en que se causen las contribuciones (CFF art. 20; verificado 2026-10-23) |

**Nota:** Para un directorio de salud en CDMX, la mayoría de los clientes serán proveedores de salud locales (residentes fiscales en México), por lo que la tasa estándar del 16% aplica en casi todos los casos.

## Multas y Sanciones (2026)

| Infracción | Multa (Anexo 5 RMF 2026) |
|------------|--------------------------|
| No emitir CFDI — **RESICO (Secciones II y IV)** | **\$1,910 - \$3,800** por comprobante (CFF art. 84 fracc. IV inciso b) |
| No emitir CFDI — régimen general | **\$22,300 - \$127,530** (CFF art. 84 fracc. IV inciso a) + clausura 3-15 días en reincidencia |
| CFDI sin los complementos que exigen las reglas del SAT (no "errores" en general) | **\$450 - \$670** por comprobante (CFF art. 84 fracc. IV inciso d) |
| Condicionar el CFDI a que exhiban CSF o cédula | **\$21,420 - \$122,440** (CFF 83-IX / 84-VI) |
| Declaración fuera de plazo por medios electrónicos | **\$20,790 - \$41,590** por obligación (CFF art. 82 fracc. I inciso d) + recargos 2.07%/mes |
| No activar Buzón Tributario | Multa \$3,850-\$11,540 diferida a ene-2027, pero el CSD puede restringirse temporalmente si los medios de contacto del buzón no son correctos o auténticos (CFF art. 17-H Bis, fracc. VIII; regla 2.2.7 RMF 2026) |
| Cancelación extemporánea CFDI | **5% - 10%** del monto del comprobante |
| No presentar DIOT | **\$14,880 - \$29,750** (CFF art. 82 fracc. XXVI; +100% por reincidencia) |

Fundamentos de los arts. 82 y 84 verificados 2026-10-23 contra el CFF vigente (LeyesBiblio).

## Checklist de Compliance

### Prioridad Alta (implementar primero)

- [ ] Verificar régimen fiscal actual (¿RESICO o RAEP?)
- [ ] Si aplica, presentar aviso de actualización (ficha 28/CFF) para tributar en RESICO; una vez elegida la opción no se puede variar en el mismo ejercicio (regla 3.13.2 RMF 2026)
- [ ] Configurar CFDI con clave 80141601 y datos correctos
- [ ] Definir precios en página /join: mostrar sin IVA + leyenda "más IVA"
- [ ] Activar Buzón Tributario (si no está activo)
- [ ] Verificar vigencia de e.firma y CSD
- [ ] Declaraciones mensuales al día (ISR + IVA antes del día 17)

### Prioridad Media

- [ ] Proceso para manejar retenciones de personas morales
- [ ] Template de CFDI global para clientes que no piden factura
- [ ] Proceso de cancelación de CFDI documentado
- [ ] Respaldo digital de todos los CFDIs emitidos (5 años mínimo)
- [ ] Calcular flujo de efectivo neto considerando retenciones

### Prioridad Baja (monitoreo)

- [ ] Monitorear Miscelánea Fiscal 2027 (publicación dic 2026)
- [ ] Evaluar cambio de régimen si ingresos superan \$3.5M MXN/año
- [ ] Consultar contador para optimización fiscal anual
- [ ] Revisar si nuevas claves de productos/servicios del SAT son más específicas

## Pricing Page — Implementación Recomendada

### Opción recomendada: Precio + IVA (B2B estándar)

```
Professional Plan
\$849 MXN/mes + IVA
(\$984.84 MXN total con IVA)
```

### Elementos legales en página de pricing

1. Leyenda visible: "Todos los precios están en MXN y no incluyen IVA (16%)"
2. Al checkout: mostrar desglose (subtotal + IVA + total)
3. En términos y condiciones: "Se emitirá CFDI por cada pago recibido"
4. Nota sobre facturación: "Para facturación, proporcione su RFC y datos fiscales"

## Common Mistakes

| Error | Consecuencia | Corrección |
|-------|-------------|------------|
| Incluir IVA en precio listado sin indicarlo | Confusión al facturar; margen reducido | Listar sin IVA + leyenda "más IVA" |
| No emitir CFDI por cada cobro | Multa \$1,910-\$3,800 por comprobante en RESICO; \$22,300-\$127,530 en régimen general | Facturar todo, incluso público en general |
| Ignorar retenciones de personas morales | Flujo de efectivo menor al esperado | Calcular neto real al proyectar ingresos |
| Declarar tarde | Recargos 2.07% mensual (antes 1.47%) | Calendario de alertas día 15 de cada mes |
| Estar en RAEP con gastos bajos | Pagar hasta 10x más ISR del necesario | Evaluar cambio a RESICO |
| Cancelar fuera del plazo del art. 29-A | Multa 5-10% del monto | Cancelar antes del mes de la anual del ejercicio de expedición |
| No activar Buzón Tributario | Multa (prorrogada a ene 2027) | Activar ya con e.firma |

## Referencia Detallada

Para el análisis completo con tasas, tablas ISR, fuentes y recomendaciones específicas, ver:
`./sat-2026-reference.md`

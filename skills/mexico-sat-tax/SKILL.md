---
name: mexico-sat-tax
description: Use when creating invoices, configuring CFDI, pricing with IVA, handling tax obligations, or evaluating compliance with Mexican tax law (SAT) for persona física con actividad empresarial. Also use when adjusting pricing pages, membership fees, or B2B billing for Mexican clients.
version: 1.1.0
last-verified: 2026-08-19
review-by: 2026-09-30
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
| Uso del CFDI (receptor) | **G03** (Gastos en general) — ⚠️ G03 NO admite régimen receptor **616**; para público en general el uso es **S01** (causa típica de rechazo del PAC) |
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
| Periodicidad | **04** (Mensual) — emitir dentro de las **24 horas** siguientes al cierre del periodo (RMF 2026 regla 2.7.1.21; ya NO son 5 días) |

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
| DIOT (informativa IVA) | Día **17** del mes siguiente | Mensual (⚠️ zona gris para RESICO PF — ver referencia) |

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
| Condición 3 | CFDI con Exportación = **04** (Definitiva con clave distinta a A1 o cuando no existe enajenación en términos de la Ley Aduanera) — la clave 02 es para mercancías con pedimento A1, NO para servicios |
| Registro | Conservar comprobante de transferencia internacional |

**Nota:** Para un directorio de salud en CDMX, la mayoría de los clientes serán proveedores de salud locales (residentes fiscales en México), por lo que la tasa estándar del 16% aplica en casi todos los casos.

## Multas y Sanciones (2026)

| Infracción | Multa (Anexo 5 RMF 2026) |
|------------|--------------------------|
| No emitir CFDI — **RESICO (Secciones II y IV)** | **\$1,910 - \$3,800** por comprobante |
| No emitir CFDI — régimen general | **\$22,300 - \$127,530** + clausura 3-15 días en reincidencia |
| CFDI sin complementos | **\$450 - \$670** por documento |
| Condicionar el CFDI a que exhiban CSF o cédula | **\$21,420 - \$122,440** (CFF 83-IX / 84-VI) |
| Declaración fuera de plazo por medios electrónicos | **\$20,790 - \$41,590** por obligación + recargos 2.07%/mes |
| No activar Buzón Tributario | Multa \$3,850-\$11,540 diferida a ene-2027, **pero el CSD sí puede restringirse hoy** (regla 2.2.4 fracc. VII) |
| Cancelación extemporánea CFDI | **5% - 10%** del monto del comprobante |
| No presentar DIOT | **\$14,880 - \$29,750** (+100% por reincidencia) |

## Checklist de Compliance

### Prioridad Alta (implementar primero)

- [ ] Verificar régimen fiscal actual (¿RESICO o RAEP?)
- [ ] Si aplica, solicitar cambio a RESICO (enero de cada ejercicio)
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

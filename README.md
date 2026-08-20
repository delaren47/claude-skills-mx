# claude-skills-mx

Cinco skills de [Claude Code](https://docs.claude.com/en/docs/claude-code) que codifican dominios regulatorios mexicanos: impuestos (SAT), protección de datos (LFPDPPP), marcas (IMPI), protección al consumidor (PROFECO) y contratos digitales. Escritos en español, con referencias a artículos de ley, tasas y plazos verificados a la fecha que indica cada `SKILL.md`.

Cada skill se activa sola cuando la conversación toca su tema (por ejemplo, redactar un aviso de privacidad o calcular IVA), o puedes invocarla a mano.

> **Lee primero el [DISCLAIMER](DISCLAIMER.md).** Estas skills son herramientas informativas. NO son asesoría legal, fiscal ni profesional. Las leyes cambian. Valida siempre con un contador o abogado con licencia.

## Las 5 skills

| Skill | Qué cubre |
|-------|-----------|
| **mexico-sat-tax** | Facturación CFDI 4.0, cálculo de IVA/ISR, régimen RESICO vs actividad empresarial, retenciones, declaraciones y plazos ante el SAT para persona física con actividad empresarial. |
| **mexico-privacy-law** | Cumplimiento con la LFPDPPP 2025 (nueva ley, autoridad SABG): avisos de privacidad, consentimiento, datos sensibles, derechos ARCO, transferencias internacionales, cookies. |
| **mexico-impi-trademark** | Registro de marcas ante el IMPI bajo la LFPPI: búsqueda en MARCANET, distintividad, oposiciones, declaración de uso, disputas de dominio (UDRP/LDRP), regla first-to-file. |
| **mexico-profeco-consumer** | Protección al consumidor bajo la LFPC: legalidad de claims publicitarios, reforma de suscripciones (Art. 76 Bis, dic 2025), cláusulas abusivas, responsabilidad de plataformas, multas. |
| **mexico-digital-contracts** | Términos y condiciones, acuerdos de membresía y contratos de adhesión bajo la LFPC y el Código de Comercio: cláusulas nulas, clickwrap, contenido de usuarios, jurisdicción, conservación (NOM-151). |

Cada carpeta contiene un `SKILL.md` (referencia rápida que Claude carga primero) y un archivo de referencia detallada con artículos, tablas, fuentes y URLs.

## Instalación (Claude Code)

Copia las carpetas de skills a tu directorio de skills de Claude Code:

```bash
cp -R skills/* ~/.claude/skills/
```

Después de copiarlas, Claude Code las detecta al iniciar. Se activan de dos maneras:

- **Automática:** cuando tu conversación coincide con la descripción de la skill (por ejemplo, "escribe un aviso de privacidad para un sitio mexicano" activa `mexico-privacy-law`).
- **Manual:** con la herramienta Skill, pidiendo la skill por su nombre.

Para instalar una sola:

```bash
cp -R skills/mexico-sat-tax ~/.claude/skills/
```

## Quién lo mantiene

Mantenido por Alfredo del Arenal — [Delaren Consulting](https://delaren.com), Ciudad de México. Delaren construye automatización de IA para negocios en México con una ventaja regulatoria local y en español nativo.

## Por qué existe

El conocimiento regulatorio mexicano suele estar disperso en PDFs de leyes, boletines de despachos y notas de prensa, casi siempre pensado para el mercado de EE. UU. Estas skills concentran ese criterio en un formato que Claude Code puede usar directamente al construir o revisar productos digitales que operan en México. Se actualizan conforme la ley se mueve; cada `SKILL.md` incluye una fecha de última verificación y una fecha de revisión.

---

## English (condensed)

Five [Claude Code](https://docs.claude.com/en/docs/claude-code) skills encoding Mexican regulatory domains: tax (SAT), data protection (LFPDPPP), trademarks (IMPI), consumer protection (PROFECO), and digital contracts. Written in Spanish, with article references, rates and deadlines verified as of the date shown in each `SKILL.md`.

> **Read the [DISCLAIMER](DISCLAIMER.md) first.** These skills are informational tooling. They are NOT legal, tax, or professional advice. Laws change. Always verify with a licensed accountant or lawyer.

| Skill | What it covers |
|-------|----------------|
| **mexico-sat-tax** | CFDI 4.0 invoicing, IVA/ISR calculation, RESICO vs business-activity regime, withholdings, filings and SAT deadlines. |
| **mexico-privacy-law** | LFPDPPP 2025 compliance (new law, SABG authority): privacy notices, consent, sensitive data, ARCO rights, cross-border transfers, cookies. |
| **mexico-impi-trademark** | IMPI trademark registration under LFPPI: MARCANET search, distinctiveness, oppositions, use declarations, domain disputes (UDRP/LDRP), first-to-file. |
| **mexico-profeco-consumer** | LFPC consumer protection: advertising-claim legality, subscription reform (Art. 76 Bis, Dec 2025), abusive clauses, platform liability, penalties. |
| **mexico-digital-contracts** | Terms & conditions, membership and adhesion contracts under the LFPC and Commercial Code: void clauses, clickwrap, user content, jurisdiction, retention (NOM-151). |

**Install:** copy the skill folders into your Claude Code skills directory, then invoke them automatically or by name.

```bash
cp -R skills/* ~/.claude/skills/
```

Maintained by Alfredo del Arenal — [Delaren Consulting](https://delaren.com), Mexico City. Contributions welcome: see [CONTRIBUTING](CONTRIBUTING.md). Licensed under [MIT](LICENSE).

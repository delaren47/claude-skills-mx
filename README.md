# claude-skills-mx

> **Lee primero el [DISCLAIMER](DISCLAIMER.md).** Estas skills son herramientas informativas. NO son asesoría legal, fiscal ni profesional. Las leyes cambian. Valida siempre con un contador o abogado con licencia.

Las skills de la tabla son skills de [Claude Code](https://docs.claude.com/en/docs/claude-code) que codifican dominios regulatorios mexicanos. Están escritas en español, con referencias a artículos de ley, tasas y plazos. Cada una lleva una fecha `last-verified` y una fecha `review-by`, y se vuelve a auditar contra fuentes primarias cada 90 días.

Cada skill se activa sola cuando la conversación toca su tema (por ejemplo, redactar un aviso de privacidad o calcular IVA), o puedes invocarla a mano.

## Las skills

<!-- vigency:start -->
| Skill | Cubre | Verificada | Revisar antes de |
|-------|-------|------------|------------------|
| **mexico-cofepris** | Publicidad sanitaria (permiso, aviso y claims prohibidos), licencia sanitaria y aviso de funcionamiento de establecimientos de salud, deberes de anunciante, agencia y medio de difusión, y sanciones de COFEPRIS en México. | 2026-10-23 | 2027-01-21 |
| **mexico-digital-contracts** | Términos y condiciones, acuerdos de membresía y contratos de adhesión bajo la LFPC y el Código de Comercio: cláusulas nulas, clickwrap, contenido de usuarios, jurisdicción, conservación (NOM-151). | 2026-10-23 | 2027-01-21 |
| **mexico-impi-trademark** | Registro de marcas ante el IMPI bajo la LFPPI: búsqueda en MARCANET, distintividad, oposiciones, declaración de uso, disputas de dominio (UDRP/LDRP), regla first-to-file. | 2026-10-23 | 2027-01-21 |
| **mexico-imss** | Obligaciones ante el IMSS de quien contrata a su primer empleado, el aseguramiento voluntario de la persona trabajadora independiente (LSS art. 13 fracc. I) y el estado vigente de la continuación voluntaria (Modalidad 40) tras el acuerdo del Consejo Técnico publicado en el DOF el 21-10-2026; y el régimen obligatorio de las personas trabajadoras del hogar (art. 12 fracc. IV). | 2026-10-23 | 2027-01-21 |
| **mexico-legal-vigency** | Método para verificar cualquier afirmación jurídica, fiscal o regulatoria mexicana contra la fuente primaria antes de afirmarla: dónde vive cada tipo de norma, cómo distinguir lo publicado de lo aprobado, la iniciativa y el criterio, cómo citar y fechar, y cuándo escribir no verificable. | 2026-10-23 | 2027-01-21 |
| **mexico-privacy-law** | Cumplimiento con la LFPDPPP 2025 (nueva ley; autoridad: Secretaría Anticorrupción y Buen Gobierno, SABG): avisos de privacidad, consentimiento, datos sensibles, derechos ARCO, transferencias internacionales, cookies. | 2026-10-23 | 2027-01-21 |
| **mexico-profeco-consumer** | Protección al consumidor bajo la LFPC: legalidad de claims publicitarios, reforma de suscripciones (Art. 76 Bis, dic 2025), cláusulas abusivas, responsabilidad de plataformas, multas. | 2026-10-23 | 2027-01-21 |
| **mexico-sat-tax** | Facturación CFDI 4.0, cálculo de IVA/ISR, régimen RESICO vs actividad empresarial, retenciones, declaraciones y plazos ante el SAT para persona física con actividad empresarial. | 2026-10-23 | 2027-01-21 |
<!-- vigency:end -->

Cada carpeta contiene un `SKILL.md` (referencia rápida que Claude carga primero) y un archivo de referencia detallada con artículos, tablas, fuentes y URLs.

## Instalación

Hay tres caminos. Usa el primero que tengas disponible.

**1. Con el CLI `skills`** (requiere Node.js 22.20 o posterior):

```bash
npx skills add delaren47/claude-skills-mx
```

Para instalar una sola skill, agrega `--skill <nombre>`, por ejemplo `--skill mexico-sat-tax`.

**2. Como plugin de Claude Code**, dentro de una sesión:

```
/plugin marketplace add delaren47/claude-skills-mx
/plugin install mexico-legal-skills@claude-skills-mx
```

En Claude Code 2.1.275 o posterior también funciona en un solo paso:

```
/plugin install mexico-legal-skills --marketplace delaren47/claude-skills-mx
```

Instaladas como plugin, las skills quedan bajo el prefijo `/mexico-legal-skills:<skill>`.

**3. Sin herramientas:** clona el repositorio y copia las carpetas a tu directorio de skills.

```bash
cp -R skills/* ~/.claude/skills/
```

Claude Code detecta las skills al iniciar. Se activan de dos maneras:

- **Automática:** cuando tu conversación coincide con la descripción de la skill (por ejemplo, "escribe un aviso de privacidad para un sitio mexicano" activa `mexico-privacy-law`).
- **Manual:** con la herramienta Skill, pidiendo la skill por su nombre.

## Vigencia

Cada `SKILL.md` declara dos fechas en su frontmatter, y la tabla de arriba se genera a partir de ellas:

- **`last-verified`** es el día en que la skill pasó su última auditoría completa.
- **`review-by`** es esa fecha más 90 días. Si hoy es posterior a `review-by`, trata las cifras de la skill como no verificadas hasta la siguiente auditoría.

La auditoría revisa la skill afirmación por afirmación (artículos, fracciones, montos, tasas, plazos y fechas) contra fuentes primarias: el DOF, LeyesBiblio de la Cámara de Diputados, el SAT, el IMSS, el IMPI, la PROFECO y la SCJN. Una afirmación que no se puede confirmar en una fuente primaria queda escrita como *verificar antes de usar*, no como una cifra precisa.

Entre auditorías, un vigilante del DOF en [`tools/dof-watch/`](tools/dof-watch/README.md) corre dos veces al día de lunes a viernes en GitHub Actions. No usa ningún modelo de lenguaje: lee las notas del día, compara cada título con una lista de patrones por skill, escribe un resumen diario en la rama [`digests`](https://github.com/delaren47/claude-skills-mx/tree/digests) y abre un issue con la etiqueta `dof-hit` por cada nota que puede tocar una skill. Un `dof-hit` indica qué leer; no significa que la skill esté mal. El [README del vigilante](tools/dof-watch/README.md) explica cómo funciona y cómo adaptarlo a tus propias skills.

## Para leer el texto completo de una nota del DOF

Dentro de Claude Code, el servidor MCP [`amatiasdev/dof-mcp`](https://github.com/amatiasdev/dof-mcp) da acceso a las publicaciones del DOF y a los indicadores FIX, UDIS y TIIE. El vigilante te dice qué nota leer; dof-mcp te permite leerla en la misma sesión. Es un proyecto de otro autor y no se mantiene en este repositorio.

## Quién lo mantiene

Mantenido por Alfredo del Arenal, [Delaren Consulting](https://delaren.com), Ciudad de México. Delaren construye automatización de IA para negocios en México con una ventaja regulatoria local y en español nativo.

## Por qué existe

El conocimiento regulatorio mexicano suele estar disperso en PDFs de leyes, boletines de despachos y notas de prensa, casi siempre pensado para el mercado de EE. UU. Estas skills concentran ese criterio en un formato que Claude Code puede usar directamente al construir o revisar productos digitales que operan en México. Sus cifras están verificadas a la fecha que indica cada `SKILL.md`.

---

## English (condensed)

> **Read the [DISCLAIMER](DISCLAIMER.md) first.** These skills are informational tooling. They are NOT legal, tax, or professional advice. Laws change. Always verify with a licensed accountant or lawyer.

The skills in the table above are [Claude Code](https://docs.claude.com/en/docs/claude-code) skills encoding Mexican regulatory domains, written in Spanish, with article references, rates and deadlines. Each one carries a `last-verified` and a `review-by` date, and is re-audited against primary sources every 90 days.

**Install** (pick one):

```bash
npx skills add delaren47/claude-skills-mx          # Node.js 22.20+; add --skill <name> for one skill
```

```
/plugin marketplace add delaren47/claude-skills-mx
/plugin install mexico-legal-skills@claude-skills-mx
# or, on Claude Code 2.1.275+, in one step:
/plugin install mexico-legal-skills --marketplace delaren47/claude-skills-mx
```

Installed as a plugin, the skills are namespaced as `/mexico-legal-skills:<skill>`.

```bash
cp -R skills/* ~/.claude/skills/                   # no tooling
```

**Vigency:** `last-verified` is the date of a skill's last claim-by-claim audit against primary sources (DOF, LeyesBiblio, SAT, IMSS, IMPI, PROFECO, SCJN); `review-by` is that date plus 90 days. Between audits, the DOF watcher in [`tools/dof-watch/`](tools/dof-watch/README.md) runs on GitHub Actions twice a day on weekdays with no LLM, writes daily digests to the [`digests`](https://github.com/delaren47/claude-skills-mx/tree/digests) branch and opens an issue labelled `dof-hit` for each note that may touch a skill. To read a note's full text inside Claude Code, use the [`amatiasdev/dof-mcp`](https://github.com/amatiasdev/dof-mcp) MCP server.

Maintained by Alfredo del Arenal, [Delaren Consulting](https://delaren.com), Mexico City. Contributions welcome: see [CONTRIBUTING](CONTRIBUTING.md). Licensed under [MIT](LICENSE).

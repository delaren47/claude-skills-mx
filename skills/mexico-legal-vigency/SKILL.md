---
name: mexico-legal-vigency
description: "Method for verifying any Mexican legal, tax or regulatory claim against primary sources before asserting it. Use before stating an article number, fraction, amount, rate, deadline or date from Mexican law; when you must tell published law (DOF) apart from approved-but-unpublished texts, initiatives, SAT anticipated versions, administrative agreements and authority criteria; when citing and dating a claim; when auditing or updating any mexico-* skill; and when reading a DOF hit (SIDOF note) to decide whether it changes anything. Gives the source for each type of norm, the SIDOF endpoints, citation and dating formats, the rule for writing unverifiable instead of inventing precision, and a worked example (IMSS Modalidad 40 agreement, DOF 21-10-2026)."
license: MIT
metadata:
  version: "1.0"
  last-verified: "2026-10-23"
  review-by: "2027-01-21"
  cubre: "Método para verificar cualquier afirmación jurídica, fiscal o regulatoria mexicana contra la fuente primaria antes de afirmarla: dónde vive cada tipo de norma, cómo distinguir lo publicado de lo aprobado, la iniciativa y el criterio, cómo citar y fechar, y cuándo escribir no verificable."
---

# Vigencia de normas mexicanas: método de verificación

Esta skill no trae reglas de ninguna materia. Trae el procedimiento para comprobar una afirmación antes de escribirla. Las fallas que previene son dos: números de artículo, fracciones o tarifas inventados, y cifras viejas que nadie volvió a derivar. Que la ley haya cambiado es el caso menos frecuente.

**Regla base:** una cifra, un artículo o una fecha se afirman sólo si abriste hoy la fuente primaria y la leíste ahí. La prensa y los despachos sirven para saber dónde buscar, nunca como cita.

**DISCLAIMER:** Esta guía NO constituye asesoría legal.

## Tipos de norma y dónde vive el texto vigente

| Tipo de norma | Fuente primaria | Qué te da |
|---|---|---|
| Ley federal y Constitución | Cámara de Diputados, LeyesBiblio: https://www.diputados.gob.mx/LeyesBiblio/index.htm | Texto vigente compilado (PDF y DOC), con la fecha de la última reforma y la nota de reforma al pie de cada párrafo |
| Reglamento, decreto, acuerdo, RMF, NOM | DOF, consultado vía SIDOF | La publicación oficial, con fecha y código de nota |
| Resolución Miscelánea, anexos, criterios del SAT | SAT, minisitio de normatividad (ver Endpoints) | PDF de la RMF publicada en DOF, sus modificaciones, anexos (criterios normativos en el Anexo 7) y versiones anticipadas |
| Acuerdos del H. Consejo Técnico del IMSS | DOF vía SIDOF | El acuerdo con sus resolutivos y su regla de entrada en vigor |
| Jurisprudencia y tesis | Semanario Judicial de la Federación (SJF) de la SCJN | Tesis por registro digital; hoy sólo se abre en navegador (ver Endpoints) |
| UMA | INEGI la calcula y la publica en el DOF cada enero | Valores diario, mensual y anual con su fecha de vigencia |
| Tarifas IMPI, derechos COFEPRIS | DOF: acuerdos de tarifas (IMPI); para derechos, la Ley Federal de Derechos en LeyesBiblio y el Anexo 4 de la RMF (cantidades actualizadas de la LFD) | El monto vigente y desde cuándo |

Compilaciones privadas, blogs de despachos y notas de prensa no están en esta tabla. Úsalos para encontrar el número de DOF o el artículo; luego abre la fuente primaria.

Según el aviso legal del SIDOF, desde la edición del 5 de julio de 2012 el PDF del DOF tiene carácter oficial y auténtico (firma electrónica avanzada); las ediciones anteriores en el sitio son informativas. El HTML de una nota sirve para leer y citar el texto; si hay duda de una coma, manda el PDF.

## Publicado, aprobado, iniciativa o criterio

Antes de escribir "la ley dice", clasifica el texto que tienes enfrente:

1. **Publicado en el DOF.** Obliga desde su entrada en vigor, que puede no ser el día de la publicación. Lee el transitorio o el resolutivo de vigencia. Puedes afirmar: "vigente desde DD-MM-YYYY (DOF DD-MM-YYYY)".
2. **Aprobado pero no publicado.** Un decreto que ya votó el Congreso, un acuerdo que ya dictó un órgano de gobierno, una versión anticipada de la RMF en el sitio del SAT. Existe, pero no obliga. Puedes afirmar: "aprobado el DD-MM-YYYY por X; al YYYY-MM-DD no está publicado en el DOF". Ejemplo real: al 2026-10-23 la página de normatividad del SAT lista la Cuarta Resolución de Modificaciones a la RMF para 2026 sólo como versiones anticipadas (la tercera, del 22-10-2026); la Tercera sí aparece con fecha DOF 02-10-2026.
3. **Iniciativa.** Una propuesta presentada en una cámara. No cambia nada. Puedes afirmar sólo que existe, quién la presentó y en qué fecha, con la Gaceta Parlamentaria como fuente (ruta no verificada 2026-10-23).
4. **Criterio.** La lectura de la autoridad (criterios normativos del SAT, Anexo 7 de la RMF) o de un tribunal (tesis y jurisprudencia). Te dice cómo se interpreta una norma; no es la norma. Cítalo como criterio, con su número y fuente.

Cómo lo confunde la prensa: llama "reforma" a cualquier cambio, aunque sea un acuerdo administrativo o una regla de la RMF; escribe "ya es ley" cuando hay un dictamen aprobado sin publicar; presenta una versión anticipada como "el SAT ya obliga". Tu prueba es una sola: ¿está en el DOF y ya entró en vigor? Si la prensa dice "reforma", busca el decreto que modifica la ley en LeyesBiblio; si no hay nota de reforma al pie del artículo, no hubo reforma a esa ley.

## Cómo citar

Orden: ordenamiento, artículo, fracción, inciso, párrafo, fecha DOF, nota SIDOF cuando la hay, y la fecha en que lo verificaste.

- Ley con artículo y párrafo: `LSS, art. 218, párr. primero (texto vigente, última reforma DOF 15-01-2026; verificado 2026-10-23)`
- Fracción: `LSS, art. 220, fracc. II`
- Párrafo sin número: `LSS, art. 220, último párrafo`
- Acuerdo publicado: `Acuerdo ACDO.AS2.HCT.101026/302.P.DG del H. Consejo Técnico del IMSS, resolutivo Cuarto, DOF 21-10-2026, nota SIDOF 5801708`
- Disposición fiscal: `Resolución Miscelánea Fiscal para 2026, DOF 28-12-2025`
- Cifra publicada: `UMA 2026, valor diario \$117.31, vigente desde el 01-02-2026 (INEGI, DOF 09-01-2026, nota SIDOF 5778072)`
- Tesis: registro digital del SJF, instancia y rubro; verifica en navegador.

Formato largo que pide el aviso legal del SIDOF para citar el DOF: título (sumario) del documento, autoridad emisora, lugar de publicación, DOF, fecha de publicación, `[citado dd-mm-aaaa]`, formato y URL. Ejemplo:

`Acuerdo ACDO.AS2.HCT.101026/302.P.DG [...], Instituto Mexicano del Seguro Social; Estados Unidos Mexicanos; DOF 21/10/2026; [citado 23-10-2026]; disponible en HTML en internet: https://dof.gob.mx/nota_detalle.php?codigo=5801708&fecha=21/10/2026`

Las fechas DOF van `DD-MM-YYYY`, como las usa el propio SIDOF. Las fechas de verificación van ISO `YYYY-MM-DD`.

## Cómo fechar un claim

- Cada afirmación verificable lleva su marca: `(verificado YYYY-MM-DD, <fuente>)`. La fecha es el día en que abriste la fuente primaria, no la fecha de la norma ni la del artículo de prensa.
- En una skill, `metadata.last-verified` es el día en que pasó la verificación completa y `metadata.review-by` es esa fecha más 90 días. Pasado `review-by`, el contenido se trata como no verificado hasta repetir la revisión.
- Cada archivo de referencia lleva su propia primera línea `Verified YYYY-MM-DD`. Se fecha aparte porque se actualiza en otro momento que el SKILL.md.
- Las cifras que cambian por calendario (UMA, salario mínimo, tarifas, cantidades actualizadas) llevan además el periodo de vigencia: "vigente desde el 01-02-2026".

## Cuándo escribir "no verificable"

Si no puedes abrir la cifra o el artículo en una fuente primaria, no lo escribas como dato. Escribe *verificar antes de usar* y lo que sí encontraste: "la prensa reporta X; no está en el texto publicado en DOF DD-MM-YYYY" o "el SJF no abrió por script el YYYY-MM-DD; tesis sin confirmar".

Nunca completes una fracción, un monto o un plazo de memoria. Una cifra redonda sin fuente es peor que un hueco declarado. En una auditoría, el veredicto de cada claim es uno de cuatro: `confirmed`, `corrected`, `unverifiable`, `obsolete`, y cada `confirmed` lleva la URL primaria y la fecha del fetch.

## Endpoints y rutas

Probados el 2026-10-23; el detalle de cada fetch está en la referencia.

- SIDOF, notas de un día (JSON): `GET https://sidof.segob.gob.mx/dof/sidof/notas/DD-MM-YYYY`. Con `YYYY-MM-DD` responde 400. Trae `NotasMatutinas`, `NotasVespertinas` y `NotasExtraordinarias`; algunas notas vienen sin `titulo`, así que filtra también por `codOrgaDos` (organismo).
- SIDOF, una nota (JSON): `GET https://sidof.segob.gob.mx/dof/sidof/notas/nota/<codNota>`. El texto está en `Nota.cadenaContenido` como HTML: quita `<style>` y etiquetas antes de leer.
- SIDOF, ediciones de un día: `GET https://sidof.segob.gob.mx/dof/sidof/diarios/porFecha/DD-MM-YYYY` (matutina, vespertina, extraordinaria, con páginas).
- DOF, sumario del día (RSS, ISO-8859-1): https://dof.gob.mx/sumario.xml
- DOF, página de una nota: `https://dof.gob.mx/nota_detalle.php?codigo=<codNota>&fecha=DD/MM/YYYY`
- SIDOF, aviso legal (carácter oficial y formato de cita): https://sidof.segob.gob.mx/avisoLegal
- LeyesBiblio: índice en https://www.diputados.gob.mx/LeyesBiblio/index.htm (la raíz `/LeyesBiblio/` da 403). Texto vigente de una ley: `https://www.diputados.gob.mx/LeyesBiblio/pdf/<SIGLA>.pdf` y `.../doc/<SIGLA>.doc`; historial de reformas: `https://www.diputados.gob.mx/LeyesBiblio/ref/<sigla>.htm`. La sigla se toma del índice.
- SAT normatividad: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce2026.html (la RMF del año, modificaciones, anexos y anticipadas). El portal principal (https://www.sat.gob.mx/portal/public/normatividad) entrega a un script la misma página vacía que la portada: no verificado 2026-10-23.
- SJF: https://sjf2.scjn.gob.mx/ responde con un reto anti-bot; sin contenido por script (no verificado 2026-10-23).
- INEGI UMA: https://www.inegi.org.mx/temas/uma/ carga los valores con JavaScript; la cifra se toma de la nota del DOF.
- IMSS: https://www.imss.gob.mx/prensa da comunicados; sirven de pista, no de cita. Los acuerdos del Consejo Técnico se citan del DOF.

## Ejemplo trabajado: Modalidad 40, octubre de 2026

**El hecho.** El miércoles 21-10-2026 el DOF publicó (nota SIDOF 5801708, edición matutina, página 51) el Acuerdo ACDO.AS2.HCT.101026/302.P.DG del H. Consejo Técnico del IMSS, dictado en sesión extraordinaria del 10-10-2026, sobre la Continuación Voluntaria en el Régimen Obligatorio. "Modalidad 40" es el nombre de uso común; no aparece en el texto. Fuente: https://sidof.segob.gob.mx/dof/sidof/notas/nota/5801708 (fetch 2026-10-23, HTTP 200).

**Resolutivos citados textualmente** (de `Nota.cadenaContenido`, HTML retirado):

> "Segundo.- Se instruye a la Dirección de Finanzas para que, por conducto de la Unidad de Riesgos Financieros y Actuariales [...], realice un análisis del efecto de la Continuación Voluntaria en la situación financiera del Instituto Mexicano del Seguro Social, a más tardar en el plazo de 6 meses a partir de la emisión del presente acuerdo."

> "Tercero.- Se instruye a la Dirección Jurídica para que, en un plazo no mayor a 6 meses contados a partir de la recepción de los resultados del análisis señalado en el punto anterior, coordine la elaboración de una propuesta de modificación a las disposiciones normativas correspondientes que atienda las áreas de oportunidad que se detecten, con el fin de que la Continuación Voluntaria en el Régimen Obligatorio constituya una modalidad viable en el mediano y largo plazos. [...]"

> "Cuarto.- Como medida temporal, y hasta que se cuente con el análisis a que se refiere el punto segundo del presente Acuerdo, mismo que será hecho del conocimiento de este Órgano de Gobierno para determinar la continuidad de la medida establecida en este punto, las personas que, a la fecha de entrada en vigor del presente Acuerdo, se encuentren inscritas en la Continuación Voluntaria en el Régimen Obligatorio, permanecerán en dicha modalidad, en las condiciones actuales, hasta la conclusión del periodo que tengan contratado. Las personas que concluyan el periodo contratado de su aseguramiento en dicha modalidad, así como aquellas que deseen conservar sus derechos en materia de seguridad social para efectos pensionarios, podrán optar por incorporarse a la Continuación Voluntaria, a partir de la solicitud que formulen al Instituto, a razón del último salario base de cotización registrado al momento de causar baja en el régimen obligatorio o hasta el importe de éste, más una Unidad de Medida y Actualización, importe que en ningún caso podrá ser inferior a un salario mínimo general vigente para el resto del país. Los nuevos aseguramientos a la Continuación Voluntaria se realizarán exclusivamente a partir de la fecha de la solicitud. [...] Las personas que se encuentren o incorporen a la modalidad a la que se refiere la fracción I del artículo 13 de la Ley del Seguro Social, no podrán contratar la Continuación Voluntaria en el régimen obligatorio; [...]"

> "Séptimo.- El presente Acuerdo entrará en vigor el día hábil siguiente al de su publicación en el Diario Oficial de la Federación. Los asegurados que a la entrada en vigor del presente instrumento se encuentren inscritos en la continuación voluntaria del régimen obligatorio en términos de la legislación aplicable, conservarán el reconocimiento de las semanas y salarios cotizados efectivamente pagados, los cuales surtirán plenos efectos para el cálculo de sus derechos pensionarios futuros."

**Paso 1: clasificar.** Es un *acuerdo administrativo* del Consejo Técnico, fundado en los arts. 251, 263 y 264 de la LSS (lo dice su proemio). No es una *reforma* a la LSS. Prueba: el texto vigente de la LSS en LeyesBiblio marca última reforma DOF 15-01-2026, anterior al acuerdo, y al pie de los arts. 218 a 220 (capítulo VIII, de la continuación voluntaria) las notas de reforma más recientes son DOF 20-12-2001 y DOF 16-12-2020. La ley no cambió; cambió cómo la aplica el IMSS.

**Paso 2: lo que se puede afirmar hoy.**
- Está vigente desde el jueves 22-10-2026: el Séptimo fija el día hábil siguiente a la publicación del miércoles 21-10-2026 (fecha derivada).
- Quien ya estaba inscrito sigue en las condiciones actuales hasta terminar el periodo contratado, y conserva las semanas y salarios efectivamente pagados (Cuarto y Séptimo).
- Las nuevas incorporaciones son a partir de la fecha de la solicitud, con el salario de registro que fija el Cuarto, nunca debajo de un salario mínimo general.
- Quien está o entra a la modalidad del art. 13, fracc. I, de la LSS no puede contratar la Continuación Voluntaria.

**Paso 3: lo que es temporal.** El Cuarto se declara "medida temporal" y dura "hasta que se cuente con el análisis" del Segundo; su continuidad la decide el Consejo Técnico. Hay dos ventanas de seis meses: el análisis financiero (Segundo, desde la emisión del acuerdo) y, después de recibido, la propuesta de modificación normativa (Tercero). El texto no fija una fecha de término para la medida. Cuánto vale en pesos el salario de registro del Cuarto para un caso concreto: *verificar antes de usar*.

**Paso 4: lo que la prensa dijo mal.** "Reforma": no aparece en el acuerdo y la LSS no tiene nota de reforma posterior al 15-01-2026. "12 meses": ni "12 meses" ni "doce meses" aparecen en el texto; los plazos son de 6 meses cada uno. En el peor caso, sumar las dos ventanas da hasta doce meses para que exista una *propuesta*, no doce meses de vigencia de nada.

**Paso 5: cómo re-verificar.**
1. `GET https://sidof.segob.gob.mx/dof/sidof/notas/nota/5801708`, quitar el HTML de `Nota.cadenaContenido` y releer los resolutivos.
2. Abrir https://www.diputados.gob.mx/LeyesBiblio/ref/lss.htm y https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf: si la última reforma es posterior a DOF 15-01-2026, revisar las notas al pie de los arts. 218 a 220.
3. Revisar en SIDOF, por fecha, si el Consejo Técnico publicó otro acuerdo sobre la continuidad del Cuarto (filtra `codOrgaDos` = INSTITUTO MEXICANO DEL SEGURO SOCIAL).

## Referencia

Tabla por familia de fuentes con patrón de URL, formato, autenticación, qué entrega y el fetch del 2026-10-23 con su estatus HTTP: `references/sources-and-endpoints.md`.

Verified 2026-10-23

# COFEPRIS — Referencia detallada (verificada ago 2026; re-verificada 2026-10-23)

Complemento de `SKILL.md`. Aquí viven los textos primarios citados, con su localización exacta, para no tener que reabrir los PDF. Todo lo de abajo fue leído del texto vigente en `diputados.gob.mx/LeyesBiblio/`, no reconstruido de memoria.

**Versiones leídas el 19-ago-2026, releídas el 2026-10-23 sin cambio de versión:**
- LGS — última reforma **DOF 15-01-2026** · `https://www.diputados.gob.mx/LeyesBiblio/pdf/LGS.pdf`
- RLGSMP — DOF 04-05-2000, última reforma **DOF 08-09-2022** · `https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf`
- LFD — última reforma **DOF 07-11-2025** · `https://www.diputados.gob.mx/LeyesBiblio/pdf/LFD.pdf`
- UMA — INEGI, DOF 09-01-2026, nota SIDOF 5778072 · `https://sidof.segob.gob.mx/dof/sidof/notas/nota/5778072`

**Gotcha de fetch:** las páginas HTML de `gob.mx` responden con un reto de JavaScript, pero los PDF bajo `gob.mx/cms/uploads/` sí bajan con `curl` (HTTP 200, probado 2026-10-23), y las notas del DOF se leen por SIDOF (`sidof.segob.gob.mx/dof/sidof/notas/…`). Los PDF de `diputados.gob.mx` sí bajan con `curl -sL -A "<UA de navegador>"`. Convertir con `pdftotext -layout`.

---

## 1. Estructura del RLGSMP (mapa para navegarlo)

| Título | Materia |
|---|---|
| I | Disposiciones generales (arts. 1–15) |
| **II** | **Publicidad de la prestación de servicios de salud (arts. 16–19)** |
| III | Alimentos, suplementos alimenticios y bebidas no alcohólicas (20–…) |
| IV | Bebidas alcohólicas y tabaco (Cap. III Tabaco derogado DOF 31-05-2009) |
| V | Insumos para la salud — medicamentos, remedios herbolarios, equipos médicos |
| VI | Productos de aseo |
| VII | Productos de perfumería y belleza |
| **VIII** | **Servicios y procedimientos de embellecimiento (63–65)** |
| IX | Plaguicidas, nutrientes vegetales, sustancias tóxicas |
| X | Productos biotecnológicos |
| **XI** | **Autorizaciones y avisos — Cap. I comunes (72–78), Cap. II permisos (79–85), Cap. III avisos (86–88)** |
| XII | Terceros autorizados (89–…) |
| XIII | Códigos de ética (99–100) |
| XIV | Consejo Consultivo de la Publicidad |
| **XV** | **Vigilancia (106–107), medidas de seguridad (108), acción popular (109), sanciones (110–112)** |

---

## 2. Definiciones — RLGSMP art. 2 (texto)

> **I. Agencia de publicidad**, a quien tenga como actividad principal la creación, diseño, planificación y ejecución de campañas publicitarias, así como la contratación, por cuenta y orden de anunciantes, de espacios para difusión a través de los distintos medios de comunicación;
>
> **II. Anunciante**, a quien utiliza la publicidad para dar a conocer las características o beneficios de sus productos y servicios;
>
> **III. Anuncio publicitario**, al mensaje dirigido al público o a un segmento del mismo, con el propósito de informar sobre la existencia o las características de un producto, servicio o actividad para su comercialización y venta o para motivar una conducta;
>
> **VII. Medio de difusión**, al que se utiliza para difundir los anuncios publicitarios a la población en general y que incluye a la televisión, cine, radio, espectacular, laterales de transporte, anuncios luminosos, carteles, prensa, revistas, correo directo, catálogos, folletos, volantes, material de punto de venta, así como a cualquier otro medio de comunicación, sea impreso, electrónico, telefónico, informático, de telecomunicaciones o mediante otras tecnologías;
>
> **IX. Publicidad**, a la actividad que comprende todo proceso de creación, planificación, ejecución y difusión de anuncios publicitarios en los medios de comunicación con el fin de promover la venta o consumo de productos y servicios.

También: **IV** artículo promocional · **V** campaña publicitaria · **VIII** patrocinio (respaldo económico para la promoción de una persona o para la realización de una actividad o evento).

**Por qué importan las tres marcadas:** son las que deciden si una ficha de directorio es o no un "anuncio publicitario" (III), si un sitio web es "medio de difusión" (VII — lo es, sin discusión: el texto dice *informático*), y si la actividad de la plataforma es "publicidad" (IX — depende del fin de promover venta o consumo).

---

## 3. Título Segundo RLGSMP — servicios de salud (texto íntegro)

> **ARTÍCULO 16.** La publicidad de la prestación de servicios de salud informará al público sobre el tipo, características y finalidades de los servicios de que se trate y las modalidades generales de acceso a los mismos.
>
> **ARTÍCULO 17.** La publicidad a la que se refiere este título no podrá ofrecer técnicas y tratamientos preventivos, curativos o rehabilitatorios de carácter médico o paramédico por correspondencia o mediante folletos, instructivos, manuales u otros medios informativos, salvo en aquellos casos en que se cuente con autorización de la Secretaría.
>
> **ARTÍCULO 18.** No se autorizará la publicidad de la prestación de servicios de salud cuando:
> I. Desvirtúe o contravenga la normatividad aplicable en materia de prevención, tratamiento o rehabilitación de enfermedades;
> II. Ofrezca tratamientos preventivos, curativos o rehabilitatorios de naturaleza médica o paramédica cuya eficacia no haya sido comprobada científicamente, o
> III. No se acredite que el establecimiento o persona que preste el servicio cuente con el personal capacitado, los recursos técnicos y materiales adecuados, y con los demás elementos que al respecto exijan las disposiciones aplicables.
>
> **ARTÍCULO 19.** Quienes ejerzan las actividades profesionales, técnicas y auxiliares y las especialidades a que se refiere el Capítulo I del Título Cuarto de la Ley, deberán expresar en la publicidad que realicen al respecto, cualquiera que sea el medio publicitario de que se trate, la institución educativa que les expidió el título, diploma o certificado correspondiente y, en su caso, el número de cédula profesional.

Nota: sólo son **cuatro artículos**. Todo lo demás que se le aplica a un anuncio de clínica viene del Título I (generales) y del Título XI (permisos/avisos).

---

## 4. Cadena de responsabilidad — textos

**LGS art. 305:**
> Los responsables de la publicidad, anunciantes, agencias de publicidad y medios difusores, se ajustarán a las normas de este título.

**RLGSMP art. 76:**
> Los anunciantes deberán obtener, en su caso, la autorización o el aviso sellado por la Secretaría, según el producto o servicio que se anuncie.

**RLGSMP art. 77:**
> Las agencias de publicidad deberán apegarse a los términos de la autorización o del aviso, en su caso, para la elaboración de los materiales publicitarios.

**RLGSMP art. 78** (reformado DOF 19-01-2012):
> Los medios de difusión se asegurarán de que la publicidad que trasmitan cuente con el permiso correspondiente o se haya presentado aviso ante la Secretaría, conforme a lo establecido en este Reglamento.
>
> Para efectos del párrafo anterior, el anunciante que pretenda publicitar un producto o servicio sujeto a control sanitario por parte de la Secretaría, deberá presentar al medio de difusión cuyos servicios utilice, ya sea por sí mismo o a través de una agencia de publicidad, copia certificada de la carátula del registro sanitario vigente, en caso de tratarse de un producto sujeto a esta autorización sanitaria y del permiso o aviso presentado ante la Secretaría.

**RLGSMP art. 108** (reformado DOF 19-01-2012) — orden de suspensión:
> La Secretaría ordenará a los medios de difusión la suspensión de la publicidad de remedios herbolarios, suplementos alimenticios o productos cosméticos que se publiciten, promuevan o comercialicen como medicamentos o productos a los cuales se les hubieran atribuido cualidades o efectos terapéuticos […] así como de aquellos productos que no cumplan con lo establecido en el artículo 6 de este Reglamento.
>
> Para efectos del párrafo anterior los medios de difusión suspenderán el anuncio publicitario de que se trate dentro de las veinticuatro horas siguientes al momento de la notificación de la orden que al efecto emita la Secretaría.

⚠️ **Matiz del art. 108 que hay que leer bien:** el mandato de suspensión está redactado para *remedios herbolarios, suplementos y cosméticos* con claims terapéuticos, más lo que viole el art. 6. No está redactado como una facultad general de suspensión de publicidad de *servicios de salud*. La facultad general de verificar en cualquier momento sí está (art. 107), y las medidas de seguridad de la LGS (Título Decimoséptimo) operan aparte. **No sobre-afirmar que el art. 108 cubre todo.**

---

## 5. Permisos y avisos — textos operativos

### Art. 79 — catálogo de permiso (lista completa)

I. Prestación de servicios de salud, **salvo cuando se trate de servicios otorgados en forma individual**
II. Suplementos alimenticios y productos biotecnológicos
III. Bebidas alcohólicas y tabaco (incluida la del art. 31)
IV. Medicamentos y remedios herbolarios
V. Equipos médicos, prótesis, órtesis, ayudas funcionales, agentes de diagnóstico, insumos de uso odontológico, materiales quirúrgico y de curación, y productos higiénicos
VI. Servicios y procedimientos de embellecimiento
VII. Plaguicidas, excepto información técnica
VIII. Nutrientes vegetales con características tóxicas conforme a NOM
IX. Sustancias tóxicas o peligrosas sujetas a control sanitario (LGS 278)
X. Alimentos y bebidas no alcohólicas difundidos por TV abierta, TV restringida, salas de cine, **internet y demás plataformas digitales**, cuando no se ajusten a los lineamientos del art. 22 Bis, 2º párrafo

Salvedades del propio art. 79: para IV, V y IX sólo aplica cuando la publicidad se dirija a población en general; VIII y IX no requieren permiso cuando se usen como materias primas; VII tampoco, bajo la condición que ahí se describe.

### Art. 80 — requisitos de la solicitud de permiso

I. Nombre del producto o servicio · II. Número de registro sanitario, en su caso · **III. Número de la licencia sanitaria o aviso de funcionamiento, en su caso** · IV. Características de la difusión (medio, duración, número de versiones, título, agencia) · V. Proyecto de publicidad en dos tantos · **VI. Documentación que dé sustento a las afirmaciones** · VII. Autorización sanitaria del producto y marbete (insumos para la salud) · VIII. Etiqueta (alimentos/bebidas preenvasados y suplementos).

Plazos del mismo artículo:
> La Secretaría tendrá **cinco días** para resolver la solicitud, en los casos en que se presente dictamen por parte de un tercero autorizado […] o se trate de interesados que hayan suscrito los códigos de ética y convenios a que se refieren los artículos 99 y 100 de este Reglamento, y **veinte días** en los demás casos.
>
> Una vez transcurrido el plazo correspondiente, sin que la Secretaría emita una resolución, **el permiso se tendrá por otorgado**.
>
> Tratándose de las solicitudes de publicidad de los productos a que se refiere la fracción X del artículo 79 […] el permiso se tendrá por **negado**.

### Arts. 81–85 — reglas del permiso

- **81:** si hay motivos para suponer falsedad, ambigüedad o inducción a error, la Secretaría puede requerir el material elaborado (grabado, filmado o impreso) en un tercio del plazo oficial; si el solicitante no lo presenta en 30 días naturales, la solicitud se tiene por no presentada.
- **82:** permisos por **tiempo indeterminado**, vigencia desde la fecha de expedición.
- **83:** prohibido introducir modificaciones que hagan variar las características que sirvieron de base al permiso.
- **84:** el permiso se entiende concedido al titular de la autorización sanitaria o, en su caso, al distribuidor, al **anunciante**, o al **prestador del servicio**.
- **85:** revocado un permiso, se notifica al titular, a los medios donde se difunda, a otras dependencias competentes en publicidad, y a las de orientación y protección al consumidor (→ el expediente llega a PROFECO).

### Art. 86 — catálogo de aviso (estado vigente)

I. **Actividades profesionales, técnicas, auxiliares y las especialidades** del Cap. I del Título Cuarto de la LGS
II. *Derogada* (DOF 06-04-2006)
III. *Derogada* (DOF 14-02-2014)
IV. **Insumos para la salud, cuando se dirija a profesionales de la salud**
V. *Derogada* (DOF 06-04-2006)
VI. *Derogada* (DOF 08-09-2022)

→ Sólo quedan **dos supuestos vivos de aviso**. Cuidado con guías de agencias que siguen citando fracciones derogadas.

### Art. 87 — cuándo y con qué se presenta el aviso

Regla general: por escrito, en formato oficial, **dentro de los cinco días posteriores** al inicio de la difusión, con: nombre del producto o servicio · registro sanitario en su caso · **número de licencia sanitaria o aviso de funcionamiento en su caso** · características de la difusión · proyecto de publicidad en dos tantos · documentos que sustenten las afirmaciones categóricas.

Último párrafo (la excepción que importa):
> El aviso de publicidad de las actividades profesionales, técnicas, auxiliares y las especialidades a que se refiere el Capítulo I del Título Cuarto de la Ley deberá presentarse **dentro de los cinco días previos al inicio de la difusión**, en los términos de este artículo.

### Arts. 99–100 — la vía rápida por código de ética

La Secretaría promueve que colegios y asociaciones formulen códigos de ética; si esos códigos **amplían** los requisitos del art. 306 LGS, la Secretaría puede celebrar convenios con anunciantes, agencias y medios suscriptores para darles facilidades — entre ellas el **plazo de 5 días** del art. 80, o la **exención del aviso** en los supuestos de las fracciones II, III y V del art. 86 (hoy derogadas, así que en la práctica lo que queda vivo de este beneficio es el plazo corto).

---

## 6. LGS — profesionales (Título Cuarto, Cap. I)

**Art. 79, 1er párrafo** — profesiones que requieren título registrado ante autoridad educativa:
> medicina, farmacia, odontología, veterinaria, biología, bacteriología, enfermería, partería profesional, terapia física, trabajo social, química, psicología, optometría, ingeniería sanitaria, nutrición, dietología, patología y sus ramas, **y las demás que establezcan otras disposiciones legales aplicables**

(Párrafo reformado DOF 08-12-2017, 24-01-2020, **26-03-2024**. **La quiropráctica no aparece nombrada.**)

**Art. 79, 2º párrafo** — actividades técnicas y auxiliares que requieren diploma registrado: atención médica prehospitalaria, medicina, odontología, veterinaria, enfermería, laboratorio clínico, radiología, optometría, terapia física, terapia ocupacional, terapia del lenguaje, prótesis y órtesis, trabajo social, nutrición, citotecnología, patología, bioestadística, codificación clínica, bioterios, farmacia, saneamiento, histopatología y embalsamiento y sus ramas.

**Art. 83** (reformado DOF 01-09-2011) — la obligación más incumplida:
> Quienes ejerzan las actividades profesionales, técnicas y auxiliares y las especialidades médicas, deberán poner a la vista del público un anuncio que indique la institución que les expidió el Título, Diploma, número de su correspondiente cédula profesional y, en su caso, el Certificado de Especialidad vigente. Iguales menciones deberán consignarse en los documentos y papelería que utilicen en el ejercicio de tales actividades **y en la publicidad que realicen al respecto**.

Sancionado en **LGS 419** (hasta 2,000 UMA).

---

## 7. LGS — establecimientos

**Art. 198** — catálogo cerrado de autorización sanitaria: I estupefacientes/psicotrópicos, vacunas, toxoides, sueros y antitoxinas de origen animal, hemoderivados · II elaboración/fabricación de medicamentos, plaguicidas, nutrientes vegetales o sustancias tóxicas · III aplicación de plaguicidas · **IV fuentes de radiación para fines médicos o de diagnóstico** · **V actos quirúrgicos u obstétricos y hemodiálisis** (reformada DOF 21-06-2018) · VI centros de mezcla.
> La solicitud de autorización sanitaria deberá presentarse ante la autoridad sanitaria, **previamente al inicio de sus actividades**.

**Art. 200** — la Secretaría determina, con base en el riesgo, cuáles de los establecimientos del 198 requieren: I contar con un **responsable** que reúna los requisitos de la ley y reglamentos · III usar la última edición de la Farmacopea. (La fracción II fue derogada DOF 07-05-1997.)

**Art. 200 Bis** — aviso de funcionamiento:
> Deberán dar aviso de funcionamiento los establecimientos que no requieran de autorización sanitaria y que, mediante **acuerdo**, determine la Secretaría de Salud. […] El aviso […] deberá presentarse por escrito a la Secretaría de Salud o a los gobiernos de las entidades federativas, **por lo menos treinta días anteriores** a aquel en que se pretendan iniciar operaciones

Contenido: I propietario · II domicilio del establecimiento y fecha de inicio · III procesos y líneas de productos · IV declaración bajo protesta de decir verdad de cumplimiento · V clave de actividad · **VI número de cédula profesional, en su caso, del responsable sanitario**.

⚠️ El **acuerdo** que clasifica los establecimientos obligados al aviso se publica en el DOF y **no fue verificado en esta versión** (el DOF bloquea fetch). Es el documento que resuelve, en definitiva, si una residencia de adultos mayores o un consultorio de quiropráctica están en la lista de aviso. Verificarlo antes de instruir a un cliente.

---

## 8. LGS — sanciones (textos de rango)

- **417:** amonestación con apercibimiento · multa · **clausura temporal o definitiva, parcial o total** · **arresto hasta por treinta y seis horas**.
- **418** (individualización): daños producidos o que puedan producirse · gravedad · condiciones socioeconómicas del infractor · reincidencia · **el beneficio obtenido por el infractor como resultado de la infracción** (fracción V, adicionada DOF 07-05-1997).
- **419:** hasta **2,000 UMA** — incluye arts. 55, 56, **83**, 103, 107, 137, 138, 139, 161, **200 Bis**, 202, 263, 268 Bis 1, 282 Bis 1, 346, 348, 348 Bis, 348 Bis 1, 350 Bis 6, 391, 392.
- **420:** **2,000 a 6,000 UMA** — incluye arts. 75, 121, 142, 147, 153, 157 Bis 10, **198**, **200**, 204, 241, 259, 260, 265, 267, **304**, **307**, 341, 348 (2º y 3er párrafo), 349, 350 Bis, 350 Bis 2, 350 Bis 3, 373.
- **421:** **6,000 a 12,000** — incluye 67, 101, 125, 127, 149, 193, 210, 212, 213, 218, 220, 230, 232, 233, 237, 238, 240, 242, 243, 247, 248, 251, 252, 255, 256, 258, 266, **306**, **308**, **309**, 315, 317, 330–336, 338 último párrafo, 342, 348 primer párrafo, 350 bis 1, 365, 367, 375, 376, 400, 411, 413.
- **421 Bis:** **15,000 a 20,000 UMA** — arts. 36, 100, 122, 126, 146, 166 Bis 19, 166 Bis 20, 205, 235, 254, 264, 271 Bis, 281, 289, 293, 298, 325, 327, 333.
- **421 Ter:** **12,000 a 16,000** + inhabilitación 7–10 años — Título Quinto Bis.
- **422:** hasta **16,000** — infracciones no previstas en el capítulo, con las reglas de calificación del 418.
- **423:** **reincidencia duplica** la multa. Reincidencia = misma violación dos o más veces dentro de un año desde la notificación de la sanción anterior.
- **425-I:** procede clausura cuando los establecimientos del art. 373 carezcan de licencia sanitaria.

**Nota de redacción legal:** 421, 421 Ter y 422 aún dicen "salario mínimo general diario vigente en la zona económica"; 419, 420 y 421 Bis ya dicen UMA. Por el transitorio Tercero del decreto de desindexación (DOF 27-01-2016, nota SIDOF 5423663: las menciones al salario mínimo como unidad de cuenta en leyes federales "*y en cualquier disposición jurídica que emane*" de ellas "*se entenderán referidas a la Unidad de Medida y Actualización*") se leen todas como UMA — pero al **citar** el texto, citar lo que dice.

---

## 9. RLGSMP — sanciones (textos de rango)

- **110:** 2,000 a 4,000 — arts. 21, 22 y 23 del Reglamento.
- **111:** **6,000 a 8,000** — arts. 7, 8, 10, **18**, 32, 33, 34, 35, 44, 55, 56, 68, 69, **77**, **78**, 83.
- **112:** hasta 16,000 — violaciones no previstas en el capítulo.

**111 es el artículo que le importa a una agencia y a una plataforma:** contiene el 77 (agencia) y el 78 (medio de difusión), y también el 18 (causales de no autorización de publicidad de servicios de salud) y el 7, 8 y 10 (contenido orientador, dignidad, leyendas).

---

## 10. LFD art. 195-I — cuotas del permiso de publicidad

Cuota **por cada producto o servicio y por cada tipo de mensaje**, según el medio. Montos **as of enero 2026** — RMF 2026 Anexo 4, "Cantidades actualizadas establecidas en la LFD para 2026" (**DOF 28-12-2025**), fuente primaria; la Tarifas de Pagos COFEPRIS 2026 (gob.mx) es su reexpresión. Consistentes con el texto vigente de la LFD art. 195-I (última reforma DOF 07-11-2025). Se paga el monto redondeado ("Con ajuste" en el Anexo 4; "Redondeado" en las Tarifas):

| Inciso | Medio | Cuota | Monto a pagar (redondeado) | Nota de reforma |
|---|---|---|---|---|
| a) | **Televisión e Internet** | **\$44,252.23** | **\$44,252** | reformado DOF 13-11-2008 y **07-11-2025** |
| b) | Cine, video en lugares públicos cerrados y en medios de transporte público | \$4,905.39 | \$4,905 | reformado DOF 13-11-2008 |
| c) | Radio | \$3,485.40 | \$3,485 | |
| d) | Prensa | \$1,161.80 | \$1,162 | |
| e) | Folletos, catálogos, carteles y otros medios similares | \$800.35 | \$800 | reformado DOF 13-11-2008 |
| f) | Anuncios en exteriores | \$6,196.26 | \$6,196 | |

Reglas del mismo artículo:
- Se paga **por cada tipo de mensaje** que comprenda la autorización, **según el medio** de los incisos.
- **Doble** cuota: bebidas alcohólicas, tabaco, sustancias tóxicas, plaguicidas, alimentos de bajo valor nutritivo.
- **+50%**: suplementos alimenticios.
- **No pagan**: Federación, CDMX, Estados y Municipios, por publicidad de programas o campañas de prevención de riesgos en materia de salud.

**Forma de pago:** **clave de pago 400107**, por el esquema **e5cinco** (pago electrónico de derechos, productos y aprovechamientos; *verificar antes de usar*: "e5cinco" no aparece en el PDF de tarifas).

**Actualización (LFD art. 1o):** las cuotas de la LFD **se actualizan anualmente el 1 de enero**. Los montos de arriba son los del RMF 2026 Anexo 4 (DOF 28-12-2025) — **re-derivarlos del Anexo 4 del año en curso antes de cotizarle a un cliente**, no hardcodearlos.

✅ **El aviso de publicidad es gratuito — verificado en fuente oficial.** La LFD art. 195-I no establece cuota para el aviso, y la ficha oficial del trámite `COFEPRIS-02-002-A` lo confirma expresamente: **"No requiere de pago"**, y **"Ficta del trámite: No aplica"**. Fundamento legal citado por la propia ficha: **LGS art. 301 Bis + RLGSMP art. 86 fracción I**. Ya no es derivación de la ausencia de cuota.

---

## 11. Trámites — lo que se pudo y no se pudo confirmar

| Homoclave | Trámite | Estado de verificación |
|---|---|---|
| `COFEPRIS-02-001-A` | Permiso de publicidad, modalidad A — productos y servicios (incluye **servicios de salud**, bebidas alcohólicas, suplementos, plaguicidas, nutrientes vegetales, sustancias tóxicas) | Aparece en guías de COEPRIS estatales y en el portal RETYS de Baja California. **No confirmado en el sitio de COFEPRIS.** La ficha de RETYS estaba marcada como "no publicada". |
| `COFEPRIS-02-001-B` | Permiso de publicidad, modalidad B — insumos para la salud | Igual |
| `COFEPRIS-02-001-C` | Permiso de publicidad, modalidad C — alimentos y bebidas no alcohólicas | Igual |
| `COFEPRIS-02-002-A` | **Aviso de publicidad, modalidad A — actividades profesionales, técnicas, auxiliares y especialidades** | ✅ **VERIFICADA — ficha oficial obtenida.** Ver el desglose abajo. Es el trámite del profesional individual. |
| `COFEPRIS-02-002-B/C/D/E` | Aviso — alimentos y bebidas (B, E), insumos a profesionales de la salud (C), **responsable de publicidad de cosméticos por marca (D)** | Igual (no confirmadas) |
| — | Canal de presentación | **DIGIPRIS** — `https://digipris.cofepris.gob.mx/`. Confirmado por la ficha de 02-002-A ("Esta homoclave DEBE ser ingresada a través de la plataforma de trámites DIGIPRIS"). |

### Ficha oficial `COFEPRIS-02-002-A` — contenido verificado

| Campo | Valor |
|---|---|
| Nombre y modalidad | Aviso de publicidad · Modalidad A — Actividades profesionales, técnicas, auxiliares y especialidades |
| **Pago asociado** | **No requiere de pago** |
| **Ficta del trámite** | **No aplica** |
| **Fundamento legal** | **Artículo 301 Bis de la LGS y artículo 86 fracción I del RLGSMP** |
| Modo de ingreso | Plataforma de Trámites Autogestivos — **DIGIPRIS** |

**Requisitos documentales (textuales de la ficha):**
- **Contar con Aviso de funcionamiento o licencia sanitaria** ← ver el gap del §1 de `SKILL.md`: este requisito contradice el corte limpio establecimiento/individual
- Proyecto de publicidad en formato **PDF o JPG no mayor a 15 MB**
- Referencias bibliográficas en PDF o JPG ≤15 MB (campo **no obligatorio**)
- Si aplica, Licencia Sanitaria en PDF o JPG de hasta 7 MB
- URL soporte (no obligatorio)

**e.firmas vigentes y actualizadas que exige la plataforma:** de la persona moral (si aplica) · del **representante legal** · del **responsable sanitario** · de los administradores de la cuenta (si aplica). Además, domicilio completo del establecimiento.

⚠️ **Lo que esta ficha NO resuelve:** no define "servicios otorgados en forma individual" ni traza la frontera con el permiso 02-001-A. Al contrario — al exigir aviso de funcionamiento o licencia, la deja más borrosa.

⚠️ Las modalidades listadas en las guías estatales incluyen fracciones del art. 86 que ya están **derogadas** (cosméticos, alimentos). Eso sugiere que los catálogos estatales están desactualizados respecto de la reforma DOF 08-09-2022 — un motivo más para verificar en DIGIPRIS antes de instruir a un cliente.

---

## 12. Enforcement — VIGIMED 2026

Programa **Vigilancia en Medios Digitales (VIGIMED)**, cifras del año corriente reportadas el 4–5 de agosto de 2026:

- Anuncios monitoreados: **36,973**
- Anuncios suspendidos: **31,155**

| Categoría | Suspendidos |
|---|---|
| Medicamentos | 16,819 |
| Suplementos alimenticios | 7,090 |
| Servicios de salud | 3,428 |
| Servicios de embellecimiento | 2,622 |
| Productos "milagro" / engaño | 2,376 |
| Dispositivos médicos | 2,272 |

| Plataforma | Suspendidos |
|---|---|
| Facebook | >24,000 |
| Instagram | 5,117 |
| TikTok | 2,500 |
| Mercado Libre | 1,263 |

Productos con más publicaciones ilícitas detectadas: Wegovy (159), bótox (115), tirzepatida (86), Lantus (83), testosterona (81), Mytocel (68), Forxiga (63), Ozempic (60), metformina (60).

Retiros ejecutados con apoyo de la SSPC y la SSC de la Ciudad de México.

**Fuentes:** La Jornada, 05-ago-2026, p. 8 (`https://www.jornada.com.mx/2026/08/05/politica/008n2pol`); Milenio, 04-ago-2026 (`https://www.milenio.com/policia/cofepris-suspende-mas-de-31-mil-anuncios-en-redes-sociales`). Ambos citan a COFEPRIS. **El boletín oficial no pudo recuperarse** (gob.mx responde con reto de JavaScript); la cifra está corroborada por dos medios independientes, no leída de la fuente primaria.

---

## 13. Quiropráctica — estado regulatorio (caso: una clínica quiropráctica)

**Verificado leyendo el texto vigente:** la quiropráctica **no está nombrada** en el catálogo de profesiones del art. 79 LGS, cuyo primer párrafo fue reformado por última vez el **26-03-2024**. El artículo cierra con la cláusula abierta "*y las demás que establezcan otras disposiciones legales aplicables*".

**De fuentes secundarias (⚠️ no primarias):** existe **licenciatura en quiropráctica** en universidades públicas — UNEVE (Universidad Estatal del Valle de Ecatepec, pionera), UNEVT (Universidad Estatal del Valle de Toluca) y Universidad Veracruzana — cuyos egresados registran título ante la Dirección General de Profesiones de la SEP y obtienen **cédula profesional**. Se presentó una **iniciativa de reforma al art. 79 LGS** para nombrar expresamente a la quiropráctica el **18-feb-2020** (`sil.gobernacion.gob.mx`, asunto 4001555); **no se refleja en el texto vigente a agosto 2026** — esto último sí es verificable por lectura directa del artículo.

**Conclusión operativa:** si el quiropráctico tiene cédula profesional, la ruta defendible es tratarlo como profesional del Título Cuarto → **aviso** (RLGSMP 86-I), presentado **5 días antes** de difundir, con institución y cédula en el creativo (LGS 83, RLGSMP 19). Si anuncia como *establecimiento* con nombre comercial, cae en **permiso** (79-I) y en la cuota de \$44,252 (monto redondeado a pagar) por tipo de mensaje en internet.

---

## 14. Qué falta verificar (deuda explícita de esta versión)

1. **Acuerdo del art. 200 Bis** que clasifica los establecimientos obligados a dar aviso de funcionamiento (DOF). Determina el estatus de un consultorio y de una residencia de adultos mayores.
2. **NOM de asistencia social para personas adultas mayores** — número, año y título exactos; requisitos concretos para una residencia. **No citar de memoria.**
3. **Capa estatal/CDMX** para establecimientos de asistencia social: autoridad competente y trámite.
4. **NOM-004-SSA3** (expediente clínico) y **NOM-024-SSA3** — número, año y vigencia a 2026.
5. **NOM de infraestructura y equipamiento** de establecimientos para atención médica ambulatoria.
6. Fichas oficiales de los trámites en **DIGIPRIS**. **Parcialmente cerrada:** `COFEPRIS-02-002-A` verificada (ver §11), incluida la gratuidad del aviso. Siguen pendientes `COFEPRIS-02-001-A` (permiso — el que trae la cuota de \$44K) y las demás modalidades.
7. **Criterio público de COFEPRIS sobre plataformas/directorios de terceros** — no se localizó ninguno. Todo el §4 de `SKILL.md` (ver caso-plataforma-directorio.md, en esta misma carpeta) es derivación normativa, no aplicación de criterio publicado.
8. **Definición de "servicios otorgados en forma individual" (RLGSMP 79-I)** — no existe en el Reglamento, y la ficha del aviso 02-002-A exige aviso de funcionamiento o licencia, lo que contradice el corte establecimiento/individual. **UNRESOLVED**, y es el gap de mayor impacto comercial: decide si un consultorio paga \$44,252 o cero.
9. ✅ **Cerrada (2026-10-23): remisión del RLGSMP art. 62 Bis al LGS art. 270** (aviso de responsable de publicidad de cosméticos, por marca). El último párrafo del 270 sí crea el aviso: "*Los responsables de la publicidad de productos cosméticos deberán presentar aviso a la Secretaría para publicitar sus productos; el aviso se dará por marca de producto…*"; el 62 Bis (adicionado DOF 19-01-2012) lo reglamenta. Sigue pendiente sólo la homoclave `COFEPRIS-02-002-D` (ver §11).
10. ✅ **Cerrada (2026-10-23): régimen transitorio de la desindexación** aplicado a los artículos que aún dicen "salario mínimo" (LGS 421, 421 Ter, 422; RLGSMP 110–112). El transitorio Tercero del decreto DOF 27-01-2016 (nota SIDOF 5423663) manda leer esas menciones como UMA, incluidas las de "*cualquier disposición jurídica que emane*" de las leyes federales; las conversiones a pesos de `SKILL.md` §6 (ver sanciones.md, en esta misma carpeta) ya no llevan marca UNVERIFIED.

**Cómo cerrarlas:** los textos de ley bajan de `diputados.gob.mx/LeyesBiblio/` con `curl -A` de navegador. Las NOM viven en el DOF (el HTML de `dof.gob.mx` puede dar reto; leer la nota por SIDOF, probar `curl -sL -A "<UA>"` o el buscador de NOM de la Secretaría de Economía). Los trámites, en DIGIPRIS con sesión de navegador. **Si un camino falla, probar otro antes de declarar el dato inexistente.**

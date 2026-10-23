---
name: mexico-cofepris
description: Use when reviewing health-service advertising, clinic/establishment licensing, COFEPRIS permits, health claims in ads or platform listings for Mexican health providers. Also use when writing or auditing Meta/Google Ads copy for clinics, doctors, chiropractors, aesthetic or elder-care services in Mexico; when deciding whether a permiso or aviso de publicidad is required; or when assessing whether a directory/platform that lists health providers is itself doing regulated advertising.
license: MIT
metadata:
  version: "1.0.1"
  last-verified: "2026-10-23"
  review-by: "2027-01-21"
  cubre: "Publicidad sanitaria (permiso, aviso y claims prohibidos), licencia sanitaria y aviso de funcionamiento de establecimientos de salud, deberes de anunciante, agencia y medio de difusión, y sanciones de COFEPRIS en México."
---

# Mexico COFEPRIS — Publicidad Sanitaria y Establecimientos de Salud

## Overview

Guía de cumplimiento con el **control sanitario de la publicidad** y con la **autorización de establecimientos de salud** en México. Autoridad: **COFEPRIS** (órgano desconcentrado de la Secretaría de Salud), con coadyuvancia de las COEPRIS estatales.

Marco primario:
- **Ley General de Salud (LGS)** — Título Cuarto Cap. I (profesionales), Título Décimo Tercero (Publicidad, arts. 300–312), Título Décimo Segundo, Cap. I (establecimientos, arts. 198–200 Bis) y Título Décimo Sexto (autorizaciones y licencias, arts. 368 y ss.; licencia, art. 373), Título Décimo Octavo (sanciones, arts. 416–427). Texto vigente: última reforma **DOF 15-01-2026** (verificado 2026-10-23).
- **Reglamento de la LGS en Materia de Publicidad (RLGSMP)** — DOF 04-05-2000, última reforma **DOF 08-09-2022**.
- **Ley Federal de Derechos (LFD)** art. 195 — cuotas de los trámites. Última reforma **DOF 07-11-2025**.

**DISCLAIMER:** Esta guía NO constituye asesoría legal. Para un trámite real o una contingencia abierta, consultar a un abogado sanitario o a un gestor especializado en COFEPRIS.

## When to Use

- Revisar copy de anuncios (Meta Ads, Google Ads, sitio, folletos) de una clínica, consultorio o profesional de la salud
- Decidir si un cliente necesita **permiso**, **aviso**, o nada, antes de lanzar campaña
- Auditar claims de salud ("cura", "garantizado", "sin dolor", antes/después, testimonios)
- Evaluar si una **plataforma o directorio** que lista proveedores de salud está haciendo publicidad regulada
- Revisar licencia sanitaria / aviso de funcionamiento / responsable sanitario de un establecimiento
- Evaluar un establecimiento de **asistencia social para adultos mayores** (residencia, estancia, casa de reposo)
- Estimar exposición a multa o a suspensión de anuncios
- Deslindar qué corresponde a COFEPRIS y qué a PROFECO o a protección de datos

## Deslinde de autoridades (leer esto primero)

| Autoridad | Qué regula | Skill hermana |
|---|---|---|
| **COFEPRIS** | Riesgo sanitario: publicidad de productos/servicios de salud, establecimientos, insumos, NOMs | esta |
| **PROFECO** | Relación proveedor–consumidor: publicidad engañosa, precios, suscripciones, contratos de adhesión, e-commerce | `mexico-profeco-consumer` |
| **SABG** | Datos personales (incl. datos de salud, que son sensibles) | `mexico-privacy-law` |
| **SEP / DGP** | Registro de títulos y cédulas profesionales (fuente de verificación) | — |
| **IMPI** | Marcas y nombres comerciales | `mexico-impi-trademark` |

**Regla de deslinde práctica:** un mismo anuncio puede violar las dos leyes por razones distintas. "Curamos la hernia discal" es **COFEPRIS** (atribuye propiedades curativas no comprobadas, LGS 306-I / RLGSMP 6-I). "El único quiropráctico certificado de la CDMX" es **PROFECO** (superlativo sin sustento, LFPC 32). Un claim puede ser sanitariamente correcto y aun así engañoso al consumidor, y viceversa. **Correr siempre las dos pasadas.**

**Tres reglas de PROFECO que se confunden con reglas de COFEPRIS.** Son las que más seguido se citan mal en guías de agencia — no existen como prohibición nominada en la LGS ni en el RLGSMP:

| Regla | Texto | Autoridad |
|---|---|---|
| **LFPC 32 ¶1–2** | La publicidad debe ser veraz, comprobable y clara; es engañosa o abusiva la que induce a error por presentación **inexacta, falsa, exagerada, parcial, artificiosa o tendenciosa**. Aquí caen los superlativos ("el único", "el mejor", "#1") | **PROFECO** |
| **LFPC 32 ¶3** | La publicidad que **compare** productos o servicios, de la misma marca o de distinta, no puede ser engañosa ni abusiva. Aquí cae la comparación denigratoria con otra clínica o técnica | **PROFECO** |
| **LFPC 32 ¶4** (adicionado DOF 11-01-2018) | Prohibido incluir leyenda o información que indique que el producto o servicio ha sido "**avalado, aprobado, recomendado o certificado** por sociedades o asociaciones profesionales" cuando éstas carezcan de documentación que lo soporte con **evidencia científica, objetiva y fehaciente** | **PROFECO** |

→ El ¶4 es el que muerde el sello de colegio o asociación en el creativo de una clínica. Ojo con no confundirlo con el RLGSMP 6-I Bis (sellos de recomendación de asociaciones), que existe pero **sólo aplica a alimentos y bebidas**, no a servicios de salud.

Deslinde inverso que la skill de PROFECO dejaba corto: aquella nota decía que COFEPRIS "NO aplica a un directorio". Eso es **verdad sólo en su lectura estrecha** (el directorio no presta servicios de salud). No es verdad respecto de la publicidad: el RLGSMP alcanza al **medio de difusión**, y "medio de difusión" incluye expresamente lo informático. Ver §4 (ver references/caso-plataforma-directorio.md).

---

## §1. Árbol de decisión: ¿permiso, aviso o nada?

Empieza aquí. Todo lo demás cuelga de esta pregunta.

```
¿El mensaje promueve un producto/servicio regulado por la LGS?
├── NO (ej. una agencia, una app de agenda, un gym sin claims de salud)
│    └── Fuera del RLGSMP. Sólo aplica PROFECO.
└── SÍ
     ├── ¿Es publicidad SÓLO de precio/oferta comercial? (RLGSMP art. 5)
     │    └── No sujeta al Reglamento — pero si nombra el producto o la marca,
     │        debe llevar la leyenda que corresponda.
     ├── ¿Servicio de salud prestado por un ESTABLECIMIENTO (clínica, hospital,
     │   grupo de médicos, residencia)?                → **PERMISO** (art. 79-I) ⚠️
     ├── ¿Servicio de salud otorgado en FORMA INDIVIDUAL
     │   (un profesional, su propia práctica)?          → **AVISO** (art. 86-I) ⚠️
     │   ⚠️ Este split NO es textual — es lectura de práctica. Leer la nota
     │      de la bisagra abajo ANTES de aconsejar a un cliente.
     ├── ¿Servicio o procedimiento de EMBELLECIMIENTO?  → **PERMISO** (art. 79-VI)
     ├── ¿Suplemento alimenticio / producto biotecnológico? → **PERMISO** (79-II)
     ├── ¿Medicamento, remedio herbolario?              → **PERMISO** (79-IV)
     ├── ¿Equipo médico, prótesis, órtesis, insumo odontológico,
     │   material quirúrgico y de curación, producto higiénico?
     │        · dirigido a población general            → **PERMISO** (79-V)
     │        · dirigido a profesionales de la salud    → **AVISO** (86-IV)
     └── ¿Alimentos y bebidas no alcohólicas que NO cumplan
         los lineamientos del art. 22 Bis, difundidos en TV, cine,
         internet y demás plataformas digitales?        → **PERMISO** (79-X)
```

### La bisagra que decide casi todos los casos de práctica

**RLGSMP art. 79-I:** requiere permiso la publicidad relativa a "*Prestación de servicios de salud, **salvo cuando se trate de servicios otorgados en forma individual***".

**RLGSMP art. 86-I:** requiere aviso la publicidad relativa a "*Actividades profesionales, técnicas, auxiliares y las especialidades a que se refiere el Capítulo I del Título Cuarto de la Ley*" (LGS arts. 78–83).

⚠️ **El split establecimiento → permiso / individual → aviso es lectura de práctica, NO texto de ley. UNRESOLVED.** Dos razones concretas:

1. **"Servicios otorgados en forma individual" no tiene definición legal.** El grep completo del RLGSMP arroja cero definiciones de la frase — ni en el art. 2 (definiciones) ni en ningún otro artículo. Quien decide si un consultorio de un solo profesional es "individual" es el evaluador, no el texto.
2. **La ficha oficial del aviso contradice el corte limpio.** `COFEPRIS-02-002-A` (aviso, actividades profesionales) lista entre sus requisitos documentales *"Contar con Aviso de funcionamiento o licencia sanitaria"* — es decir, la vía del "profesional individual" **presupone un establecimiento con estatus resuelto**. Si el aviso exige establecimiento, la línea que separa el 79-I del 86-I no es "hay establecimiento o no".

**Cómo operar mientras no se resuelva:** un consultorio quiropráctico (o cualquier práctica de un solo profesional con local) puede recibir **cualquiera de las dos respuestas** de COFEPRIS. Presentar la ruta del aviso como *defendible*, nunca como *segura*; documentar el criterio con el que se eligió; y no prometerle al cliente el ahorro de \$44K como si estuviera cerrado. Para un cliente con campaña viva y presupuesto, vale la consulta formal antes de escalar. Ver la fila correspondiente en "Verificación pendiente".

Traducción operativa (bajo la reserva anterior):

| Quién anuncia | Instrumento | Costo | Cuándo se presenta |
|---|---|---|---|
| Un profesional, su práctica individual | **Aviso** | **Gratuito** — ficha oficial 02-002-A: "No requiere de pago" | **5 días hábiles ANTES** de iniciar la difusión (art. 87, último párrafo) |
| Clínica, hospital, grupo de médicos, establecimiento | **Permiso** | Sí, por medio y por tipo de mensaje (LFD 195-I) | Antes de difundir; resolución en 5 o 20 **días hábiles** (art. 80) |

⚠️ **La asimetría de plazo es una trampa real:** los demás avisos se presentan *dentro de los cinco días posteriores* al inicio de la difusión; el aviso de actividades profesionales se presenta *dentro de los cinco días previos*. Si un cliente prende una campaña de Meta y presenta el aviso al día siguiente, cumplió el plazo equivocado.

**Todos los plazos de esta sección son en días HÁBILES** (LFPA art. 28: en los plazos fijados en días no se cuentan los inhábiles, salvo disposición expresa en contrario). Cinco días hábiles antes de prender la campaña son, en la práctica, entre 7 y 9 días naturales según caiga la semana. Excepciones expresas: art. 81 (**30 días naturales** para atender un requerimiento de material) y art. 75 (**15 días naturales** para manifestar lo que convenga tras la revisión de una autorización).

### Plazos, vigencia y afirmativa ficta

| Regla | Detalle | Fuente |
|---|---|---|
| Resolución del permiso | **5 días hábiles** si hay dictamen de tercero autorizado o el interesado suscribió código de ética (arts. 99–100); **20 días hábiles** en los demás casos | RLGSMP 80 + LFPA 28 |
| Requerimiento de material (art. 81) | La Secretaría puede pedirlo dentro de **un tercio** del plazo; el solicitante tiene **30 días naturales** o la solicitud se tiene por no presentada | RLGSMP 81 |
| Plazo genérico si el Reglamento no fija uno | 40 días hábiles | RLGSMP 72 + LFPA 28 |
| **Afirmativa ficta** | Transcurrido el plazo sin resolución, **el permiso se tiene por otorgado** | RLGSMP 80 |
| Excepción — **negativa ficta** | Para alimentos y bebidas no alcohólicas del art. 79-X, el silencio se tiene por **negado** | RLGSMP 80, párrafo adicionado DOF 14-02-2014 |
| Vigencia del permiso | **Tiempo indeterminado**, desde la fecha de expedición | RLGSMP 82 |
| Modificar el material autorizado | Prohibido si varía las características que sirvieron de base; requiere trámite nuevo | RLGSMP 83 |
| Clave de autorización en el material | Debe **aparecer en el material publicitario impreso**, sin formar parte de la leyenda precautoria | LGS 304 |
| Uso comercial de la resolución | Prohibido usar la autorización con fines publicitarios ("aprobado por COFEPRIS") | LGS 304, 2º párrafo |

**No presumir la afirmativa ficta sin evidencia del acuse.** Sirve como defensa sólo si existe el acuse de recepción fechado y el cómputo del plazo; sin acuse no hay nada que invocar.

### ¿Federal o estatal? La pregunta que decide ante quién se presenta

- **LGS 302:** los gobiernos de las entidades federativas "*coadyuvarán*" con la Secretaría de Salud en las actividades del art. 301, en sus respectivas jurisdicciones territoriales.
- **RLGSMP 3:** la aplicación del Reglamento corresponde a la Secretaría y a las entidades federativas "*de conformidad con los acuerdos de coordinación que, en su caso, se suscriban*".

La competencia estatal depende del acuerdo de coordinación de cada entidad (RLGSMP 3); el corte por alcance territorial es lectura de práctica, no texto. Verificar con la COEPRIS antes de elegir ventanilla. Ni la LGS ni el RLGSMP mencionan la geo-segmentación de una campaña: no usarla como regla de ventanilla.

### Mecánica del trámite

El aviso (02-002-A) se presenta por **DIGIPRIS** (`digipris.cofepris.gob.mx`), con **e.firma vigente** del representante legal y del responsable sanitario (más la de la persona moral y la de los administradores de cuenta, si aplican), domicilio completo del establecimiento, y el **proyecto de publicidad en PDF o JPG de no más de 15 MB**; para el permiso, verificar la ficha 02-001-A (no leída). Una e.firma vencida detiene el trámite antes de que empiece: verificarla la misma semana en que se decide la campaña.

### Dos casos especiales que rompen el árbol

- **Cosméticos y productos de belleza:** no requieren permiso ni aviso *del anuncio*, pero la ley exige un aviso de **responsable de la publicidad, por cada marca**: **LGS art. 270, último párrafo** ("*Los responsables de la publicidad de productos cosméticos deberán presentar aviso a la Secretaría para publicitar sus productos; el aviso se dará por marca de producto…*") + **RLGSMP art. 62 Bis**, que lo reglamenta (homoclave `COFEPRIS-02-002-D`, sin verificar). Es un aviso de persona, no de creativo — se presenta una vez por marca, no por campaña.
- **Tabaco:** el art. 79-III todavía lo lista como supuesto de permiso, pero la **Ley General para el Control del Tabaco art. 23** (reforma DOF 17-02-2022) prohíbe **toda** publicidad, promoción y patrocinio de productos de tabaco. La vía del permiso quedó como letra muerta: no hay permiso que tramitar porque no hay publicidad lícita que amparar. No cotizarlo ni ofrecerlo.

### Costos — Ley Federal de Derechos art. 195-I

Cuota **por cada producto o servicio y por cada tipo de mensaje**, según el medio:

| Medio | Cuota | Monto a pagar (redondeado) |
|---|---|---|
| **Televisión e Internet** | **\$44,252.23** | **\$44,252** |
| Anuncios en exteriores | \$6,196.26 | \$6,196 |
| Cine, video en lugares públicos cerrados y transporte público | \$4,905.39 | \$4,905 |
| Radio | \$3,485.40 | \$3,485 |
| Prensa | \$1,161.80 | \$1,162 |
| Folletos, catálogos, carteles y similares | \$800.35 | \$800 |

*Montos **as of enero 2026** — RMF 2026 Anexo 4, "Cantidades actualizadas establecidas en la LFD para 2026" (DOF 28-12-2025), fuente primaria; la Tarifas de Pagos COFEPRIS 2026 (gob.mx) es su reexpresión. Consistentes con el texto vigente de la LFD art. 195-I (última reforma DOF 07-11-2025). Se paga el monto redondeado ("Con ajuste" en el Anexo 4; "Redondeado" en las Tarifas). **Clave de pago 400107**, se paga por el esquema **e5cinco** (*verificar antes de usar*: no aparece en el PDF de tarifas). Las cuotas de la LFD **se actualizan cada 1 de enero** (LFD art. 1o): re-derivarlas del PDF de tarifas del año en curso antes de cotizar — no hardcodearlas.*

Recargos sobre estas cuotas: **doble** para bebidas alcohólicas, tabaco, sustancias tóxicas, plaguicidas y alimentos de bajo valor nutritivo; **+50%** para suplementos alimenticios.

**Consecuencia comercial que hay que decirle al cliente en la primera junta:** una clínica que quiera anunciarse en internet paga ~\$44K por tipo de mensaje. Un profesional individual paga cero. La diferencia entre "Clínica X" y "Dr. Y" en el creativo no es de branding, es de \$44K y de trámite. Decidir la figura ANTES de producir creativos.

---

## §2. Qué no se puede decir — claims prohibidos

### Reglas generales (aplican a toda publicidad sanitaria)

| Regla | Fuente |
|---|---|
| Atribuir cualidades **preventivas, terapéuticas, rehabilitatorias, nutritivas o estimulantes** que no correspondan a su función o uso autorizado | RLGSMP 6-I |
| Indicar o sugerir que el uso del producto o la prestación del servicio es **factor determinante para modificar la conducta** de las personas | RLGSMP 6-II |
| Inducir a creer, explícita o implícitamente, que el producto tiene propiedades **de las que carece** | RLGSMP 6-III |
| Publicidad que **atente o ponga en riesgo** la seguridad, integridad física o mental, o la **dignidad** de las personas | RLGSMP 8; LGS 306-IV |
| **Inducir al error** | RLGSMP 9-I |
| **Ocultar contraindicaciones** necesarias | RLGSMP 9-II |
| **Exagerar** características o propiedades | RLGSMP 9-III |
| Sugerir que el servicio determina características **físicas, intelectuales o sexuales** sin pruebas fehacientes | RLGSMP 9-IV |
| **Comparaciones** entre productos de ingredientes distintos cuando generen riesgo | RLGSMP 9-V |
| **Mensajes subliminales** — causal expresa de no autorización o de suspensión | RLGSMP 14 |
| La información sobre calidad, origen, pureza, propiedades y beneficios debe ser **comprobable** | LGS 306-I |
| El mensaje debe tener contenido **orientador y educativo** | LGS 306-II; RLGSMP 7 |
| El mensaje no debe **desvirtuar ni contravenir** lo que la Secretaría establezca en prevención, tratamiento o rehabilitación | LGS 306-V |

**Por qué la columna dice "Regla" y no "Prohibición":** el **LGS art. 306 es una lista de seis requisitos** que toda publicidad sanitaria debe cumplir (comprobable · orientadora y educativa · correspondiente a la autorización sanitaria · que no induzca conductas nocivas · que no desvirtúe lo que fije la Secretaría · conforme a derecho), no un catálogo de conductas prohibidas. Las prohibiciones propiamente dichas viven en el **RLGSMP** (arts. 6, 8, 9, 14) y en los títulos por producto. La distinción importa al redactar un dictamen: un incumplimiento del 306 se argumenta como *requisito no satisfecho*, y la carga de satisfacerlo es del anunciante.

**Carga de la prueba invertida (RLGSMP 11):** el anunciante debe **comprobar ante la Secretaría, cuando ésta lo requiera**, las aseveraciones que haga sobre calidad, origen, pureza, conservación, propiedades y beneficios, presentando la información técnica y científica que se le solicite, **y señalar el grupo objetivo** al que dirige la publicidad. No es COFEPRIS quien tiene que probar que el claim es falso; es el anunciante quien tiene que probar que es cierto, en el momento en que se lo pidan.

→ Implicación operativa: **cada claim vive con su carpeta de sustento**. Si el copy dice "reduce el dolor lumbar en 3 sesiones", esa afirmación necesita la referencia técnica archivada el día que se publica, no el día que llega el requerimiento.

### Específicas de servicios de salud (RLGSMP Título Segundo, arts. 16–19)

| Regla | Detalle |
|---|---|
| **Art. 16** | La publicidad **informará** sobre tipo, características y finalidades del servicio y las modalidades generales de acceso. Ése es el alcance permitido. |
| **Art. 17** | **No** se pueden ofrecer técnicas ni tratamientos preventivos, curativos o rehabilitatorios de carácter médico o paramédico **por correspondencia o mediante folletos, instructivos, manuales u otros medios informativos**, salvo con autorización. Un lead magnet tipo "guía para curar tu ciática en casa" cae aquí. |
| **Art. 18-I** | No se autoriza si **desvirtúa o contraviene** la normatividad de prevención, tratamiento o rehabilitación. |
| **Art. 18-II** | No se autoriza si ofrece tratamientos **cuya eficacia no haya sido comprobada científicamente**. |
| **Art. 18-III** | No se autoriza si **no se acredita** que el establecimiento o la persona cuenta con personal capacitado, recursos técnicos y materiales adecuados. |

### La obligación de la cédula (la más incumplida, y es barata de arreglar)

**LGS art. 83:** quienes ejerzan actividades profesionales, técnicas, auxiliares y especialidades médicas deberán **poner a la vista del público** un anuncio con la institución que expidió el título, el diploma, el **número de cédula profesional** y, en su caso, el certificado de especialidad vigente. *"Iguales menciones deberán consignarse en los documentos y papelería que utilicen en el ejercicio de tales actividades **y en la publicidad que realicen al respecto**."*

**RLGSMP art. 19** repite la obligación para la publicidad, "cualquiera que sea el medio publicitario de que se trate": institución educativa que expidió el título + número de cédula profesional.

Sanción: **hasta 2,000 UMA** (LGS art. 419 lista expresamente el art. 83).

→ Un anuncio de Meta de un consultorio **sin cédula visible** es una infracción constatable desde el celular de un verificador, sin peritaje. Es el hallazgo más fácil de levantar y el más fácil de corregir: cabe en la última línea del creativo o en el primer renglón del texto primario.

### Servicios y procedimientos de embellecimiento (Título Octavo, arts. 63–65)

Definición (art. 63): los que **modifican las características del cuerpo humano** mediante técnicas físicas, aparatos o equipos, o aplicación de productos y métodos. *"En ningún caso se podrán atribuir a este tipo de servicios o productos cualidades preventivas, rehabilitatorias o terapéuticas."*

Requieren **permiso** (art. 79-VI) y la publicidad sólo se autoriza cuando (art. 65):
1. Se acrediten las afirmaciones con **pruebas de plena validez científica**
2. Se manifiesten los **riesgos** derivados de su aplicación
3. Se señalen de manera clara **contraindicaciones y efectos secundarios**
4. Se acredite que el anunciante cuenta con **recursos técnicos, humanos y materiales** adecuados

Art. 64: la publicidad debe limitarse a los **resultados reales** en la apariencia física, comprobados técnica y científicamente ante la Secretaría.

⚠️ **Frontera peligrosa:** un servicio que se vende como "estético" pero se anuncia con lenguaje terapéutico ("corrige tu postura", "alivia") cruza de embellecimiento a servicio de salud, y arrastra las reglas de los dos títulos a la vez. Elegir un lado y sostenerlo en todo el copy.

---

## §3. Quién responde: anunciante, agencia y medio

Ésta es la sección que hace la diferencia para una agencia y para una plataforma.

**LGS art. 305:** "*Los responsables de la publicidad, **anunciantes, agencias de publicidad y medios difusores**, se ajustarán a las normas de este título.*" La ley reparte el deber a los tres, no sólo al anunciante.

Definiciones del RLGSMP art. 2:

| Figura | Definición | Fracción |
|---|---|---|
| **Anunciante** | Quien utiliza la publicidad para dar a conocer las características o beneficios **de sus** productos y servicios | 2-II |
| **Agencia de publicidad** | Quien tiene como actividad principal la creación, diseño, planificación y ejecución de campañas, así como la contratación **por cuenta y orden de anunciantes** de espacios de difusión | 2-I |
| **Medio de difusión** | El que se utiliza para difundir anuncios a la población, incluye TV, cine, radio, espectacular, prensa, revistas, correo directo, catálogos, folletos, volantes, material de punto de venta, *"así como a cualquier otro medio de comunicación, sea impreso, **electrónico, telefónico, informático, de telecomunicaciones o mediante otras tecnologías**"* | 2-VII |

Deberes específicos:

| Sujeto | Deber | Artículo |
|---|---|---|
| Anunciante | Obtener la autorización o el aviso sellado según el producto o servicio | RLGSMP 76 |
| **Agencia** | **Apegarse a los términos de la autorización o del aviso** al elaborar los materiales | RLGSMP 77 |
| **Medio de difusión** | **Asegurarse de que la publicidad que transmita cuente con el permiso correspondiente o tenga aviso presentado** | RLGSMP 78 |
| Anunciante → medio | Entregar al medio copia certificada de la carátula del registro sanitario vigente (si aplica) **y del permiso o aviso presentado** | RLGSMP 78, 2º párrafo |
| Medio de difusión | **Suspender el anuncio dentro de las 24 horas** siguientes a la notificación de la orden de la Secretaría | RLGSMP 108 |

**Sanción para agencia y medio:** las violaciones a los arts. **77 y 78** están listadas expresamente en **RLGSMP art. 111** — multa de **6,000 a 8,000** veces la unidad de cuenta. No es responsabilidad refleja del anunciante: es infracción propia.

→ **Para una agencia:** el art. 77 la obliga directamente a que el material que monta se apegue a los términos del permiso o aviso del cliente. La agencia no es un tercero neutral que "sólo sube el creativo". Es la traducción sanitaria de una regla útil sobre claims de cliente: *el derecho se ejerce sobre lo que firmas tú*.

---

## §4. El caso plataforma / directorio en línea de proveedores de salud

Detalle completo en [references/caso-plataforma-directorio.md](references/caso-plataforma-directorio.md) (anclajes normativos, matriz de riesgo por tipo de listado, zona gris, recomendaciones).

---

## §5. Establecimientos: licencia sanitaria, aviso de funcionamiento y responsable sanitario

### La regla base

| Instrumento | Cuándo | Fuente |
|---|---|---|
| **Autorización / licencia sanitaria** | Sólo para los establecimientos del catálogo cerrado del art. 198 LGS. Se solicita **previamente al inicio de actividades** | LGS 198 |
| **Aviso de funcionamiento** | Para los establecimientos que **no** requieren autorización sanitaria y que la Secretaría determine por acuerdo publicado en el DOF. Se presenta **por lo menos 30 días antes** de iniciar operaciones | LGS 200 Bis |

**LGS art. 198 — requieren autorización sanitaria los establecimientos dedicados a:**

| Fracción | Actividad |
|---|---|
| I | Proceso de medicamentos con estupefacientes y psicotrópicos; vacunas; toxoides; sueros y antitoxinas de origen animal; hemoderivados |
| II | Elaboración, fabricación o preparación de medicamentos, plaguicidas, nutrientes vegetales o sustancias tóxicas o peligrosas |
| III | Aplicación de plaguicidas |
| IV | **Utilización de fuentes de radiación para fines médicos o de diagnóstico** (rayos X, imagenología) |
| V | **Establecimientos en que se practiquen actos quirúrgicos u obstétricos** y los que presten **servicios de hemodiálisis** |
| VI | Centros de mezcla para mezclas parenterales nutricionales y medicamentosas |

**Lectura contraintuitiva que hay que entender bien:** un **consultorio médico o de quiropráctica que no practica actos quirúrgicos ni usa fuentes de radiación NO está en el art. 198**, y por lo tanto **no requiere licencia sanitaria** — le corresponde el **aviso de funcionamiento** del art. 200 Bis, si el acuerdo del 200 Bis lo incluye (no verificado). El error frecuente es al revés: creer que todo lo que huele a salud necesita licencia. Lo que necesita licencia es lo que está en la lista; lo demás avisa.

**Contenido del aviso de funcionamiento (LGS 200 Bis):** nombre y domicilio del propietario; domicilio del establecimiento y fecha de inicio de operaciones; procesos y líneas de productos; declaración bajo protesta de decir verdad de que se cumplen los requisitos; clave de la actividad; y **número de cédula profesional del responsable sanitario, en su caso**.

**Responsable sanitario:** la LGS art. 200 faculta a la Secretaría a determinar, con base en el riesgo, qué establecimientos del art. 198 requieren contar con un **responsable** que reúna los requisitos de ley y reglamentos. El dato de su cédula es campo del propio aviso de funcionamiento (200 Bis-VI).

**Sanciones asociadas:** violar el art. 198 (operar sin autorización) se sanciona con **2,000 a 6,000 UMA** (LGS 420); violar el art. 200 Bis (no dar aviso) con **hasta 2,000 UMA** (LGS 419). Procede además **clausura** temporal o definitiva, parcial o total, cuando el establecimiento carezca de la licencia correspondiente — pero **LGS 425-I sólo alcanza a los establecimientos del art. 373**, es decir, a los que sí requieren licencia sanitaria. Un consultorio que opera con aviso de funcionamiento no es clausurable por esa vía: su incumplimiento es del 200 Bis y se sanciona con multa (419). No amenazar a un cliente con clausura por la fracción I, que no le aplica; la clausura sigue disponible por las fracciones II y IV del 425 (violación reiterada o rebeldía; peligro para la salud pública), que alcanzan a cualquier establecimiento.

### El enlace publicidad ↔ establecimiento (fácil de pasar por alto)

Tanto la solicitud de **permiso** (RLGSMP 80-III) como la de **aviso** (RLGSMP 87-III) piden **el número de la licencia sanitaria o del aviso de funcionamiento**. No se puede tramitar publicidad de un establecimiento que no tiene resuelto su estatus de funcionamiento. **El orden es: establecimiento primero, publicidad después.** Un cliente que llega pidiendo "arréglame el aviso de publicidad" y no tiene aviso de funcionamiento tiene un problema anterior al que cree.

---

## §6. Sanciones

Detalle completo en [references/sanciones.md](references/sanciones.md) (unidad de cuenta, multas LGS y RLGSMP, sanciones no monetarias, enforcement real agosto 2026).

---

## §7. Red flags — checklist de revisión de copy

Correr esto sobre cada creativo, anuncio, landing y post de cliente de salud **antes** de publicar. Un ❌ es bloqueante.

### Bloque A — habilitación (antes de mirar el copy)

- [ ] ¿El cliente tiene **aviso de funcionamiento** o **licencia sanitaria**, según corresponda? (§5)
- [ ] ¿Está definido si anuncia como **individuo** (aviso) o como **establecimiento** (permiso)? (§1)
- [ ] ¿Existe el **acuse** del aviso o el **permiso** vigente, en archivo, con fecha?
- [ ] Si es aviso de actividades profesionales: ¿se presentó **5 días antes** de prender la campaña?
- [ ] Si cambió el creativo respecto del material autorizado: ¿varía las características que sirvieron de base al permiso? (RLGSMP 83)

### Bloque B — claims prohibidos (buscar literalmente estas palabras)

| ❌ Bandera roja en el copy | Por qué | Artículo |
|---|---|---|
| "cura", "curamos", "curación" | Atribuye cualidad terapéutica no comprobada | RLGSMP 6-I; LGS 306-I |
| "garantizado", "resultados garantizados", "100% efectivo" | No comprobable + exageración | RLGSMP 9-III, 11 |
| "el único", "el mejor", "líder", "#1" | Superlativo sin sustento — es primero un problema de consumidor. **No existe prohibición nominada de "único" en la LGS ni en el RLGSMP** | **LFPC 32 (PROFECO)**; derivadamente RLGSMP 9-III por exageración |
| "sin efectos secundarios", "sin riesgos" | Oculta contraindicaciones | RLGSMP 9-II |
| "elimina el dolor para siempre", "definitivo" | Promesa de resultado no comprobable | RLGSMP 9-I, 9-III |
| "tratamiento natural, por eso es seguro" | Induce al error | RLGSMP 9-I |
| Testimonio de paciente con resultado clínico | No comprobable; requiere sustento | RLGSMP 11; LGS 306-I |
| Fotos **antes/después** de un tratamiento | **DERIVADA — no existe regla nominada de "antes/después"** en el RLGSMP ni en la LGS (grep de "antes y después", "fotograf", "imágenes": nada). Se ataca como afirmación no comprobable y exagerada, y en servicios de salud por el gate del 18-II. Sólo cuando el servicio es de **embellecimiento** entran los requisitos duros de los arts. 64–65 (resultados reales comprobados ante la Secretaría + riesgos + contraindicaciones) | RLGSMP 9-III + 11; 18-II si es servicio de salud; 64–65 **sólo si es embellecimiento** |
| "aprobado por COFEPRIS", "autorizado por la Secretaría de Salud" | Prohibido usar la resolución con fines publicitarios | LGS 304, 2º párrafo |
| Diagnóstico o tratamiento ofrecido en el propio material (guía, e-book, "haz esto en casa") | Ofrecer técnicas/tratamientos por medios informativos sin autorización | RLGSMP 17 |
| Comparación denigratoria con otra clínica o técnica | **No es COFEPRIS.** El RLGSMP 9-V cubre únicamente comparaciones **producto vs. producto por ingredientes distintos que generen riesgo sanitario** — no la comparación entre prestadores de servicios. Denigrar a otra clínica es materia de consumidor | **PROFECO — LFPC 32 ¶3** (la publicidad comparativa no puede ser engañosa ni abusiva) |
| Miedo, urgencia sobre la salud, imágenes de deterioro | **DERIVADA — no existe una regla de "publicidad de miedo"** en la LGS ni en el RLGSMP. Sólo muerde por la vía del art. 8 y sólo si el mensaje efectivamente **atenta o pone en riesgo la seguridad, integridad física o mental, o la dignidad** de las personas. El susto comercial ordinario ("no dejes que empeore") no basta para acreditarlo — no lo levantes como bloqueante sin argumentar el 8 | RLGSMP 8; LGS 306-IV |
| Servicio estético descrito con verbos terapéuticos ("corrige", "sana", "trata") | Cruza de embellecimiento a servicio de salud | RLGSMP 63 |
| Dirigido a menores, o con menores en el mensaje, para servicios de salud | Revisar caso a caso; carga probatoria alta | RLGSMP 8 |

### Bloque C — lo que DEBE estar y casi nunca está

- [ ] **Número de cédula profesional** del profesional que presta el servicio (LGS 83; RLGSMP 19)
- [ ] **Institución educativa** que expidió el título (LGS 83; RLGSMP 19)
- [ ] Certificado de especialidad vigente, si se anuncia una especialidad (LGS 83)
- [ ] **Clave de autorización** en el material impreso, si hay permiso, fuera de la leyenda precautoria (LGS 304)
- [ ] Leyendas precautorias aplicables, con el tamaño/duración del RLGSMP 10 (¼ de la duración del anuncio en video; ≥20 puntos en impresos)
- [ ] Riesgos y contraindicaciones, si es embellecimiento (RLGSMP 65-II, 65-III)
- [ ] Todo en **español**, en términos claros y comprensibles para el público destinatario (RLGSMP 7-I) — relevante para copy bilingüe: la versión en inglés no sustituye el requisito

### Bloque D — sustento archivado

- [ ] Cada afirmación categórica tiene su **documento de sustento** guardado y localizable (RLGSMP 11, 80-VI, 87-VI)
- [ ] Está declarado el **grupo objetivo** al que se dirige la publicidad (RLGSMP 11)
- [ ] Existe procedimiento y dueño para **bajar el anuncio en 24 horas** si llega orden de suspensión (RLGSMP 108 — supuestos acotados: herbolarios, suplementos y cosméticos con claims terapéuticos + violaciones al art. 6; la facultad general de verificación es el 107)

### Bloque E — segunda pasada, PROFECO

- [ ] Correr el mismo copy contra `mexico-profeco-consumer` (veracidad, comprobabilidad, superlativos, cláusulas). Un copy sanitariamente limpio puede seguir siendo engañoso al consumidor.

---

## Aplicación a casos tipo

### Un directorio en línea de proveedores de salud
Riesgo primario: pasar de **padrón** a **anunciante** sin darse cuenta, vía copy editorial valorativo o featured pagado. Riesgo secundario, casi siempre no modelado: el deber propio del **medio de difusión** (RLGSMP 78), con multa propia de 6,000–8,000 (RLGSMP 111). Acciones en §4 (ver references/caso-plataforma-directorio.md). La verificación de cédula sigue siendo la respuesta a PROFECO, no a COFEPRIS: hay que decir explícitamente que **verificar cédula no equivale a autorización sanitaria**.

---

## Verificación pendiente ⚠️

Marcado explícito de lo que esta versión NO verificó en fuente oficial. No asesorar sobre estos puntos sin cerrarlos primero.

| Tema | Estado |
|---|---|
| NOM aplicable a asistencia social para personas adultas mayores (número, año, título exacto, requisitos) | ⚠️ **No verificado en DOF.** No citar número de NOM de memoria. |
| Autorización estatal / CDMX para residencias de adultos mayores; autoridad competente | ⚠️ **No verificado.** El reparto federal-estatal es real y determina a quién se le tramita. |
| NOM-004-SSA3 (expediente clínico) y NOM-024-SSA3 — vigencia y número exacto a 2026 | ⚠️ **No verificado en DOF en esta versión.** Aplican a establecimientos de atención médica, no a un directorio. |
| NOM de infraestructura mínima de establecimientos para atención médica ambulatoria | ⚠️ **No verificado.** |
| **Corte entre RLGSMP 79-I (permiso) y 86-I (aviso) para una práctica individual con local** | ⚠️ **UNRESOLVED — es el gap de mayor impacto comercial de esta skill.** "Servicios otorgados en forma individual" no está definido en ninguna parte del RLGSMP, y la ficha oficial del aviso 02-002-A exige *"Contar con Aviso de funcionamiento o licencia sanitaria"*, lo que rompe el corte limpio establecimiento/individual. Un consultorio puede recibir cualquiera de las dos respuestas. Cerrarlo con consulta formal a COFEPRIS o con abogado sanitario antes de comprometerle a un cliente el ahorro de la cuota. Ver §1. |
| Homoclave `COFEPRIS-02-002-A` (aviso, actividades profesionales) | ✅ **Verificada.** Ficha oficial obtenida: sin pago, sin ficta, fundamento LGS 301 Bis + RLGSMP 86-I, ingreso por DIGIPRIS, requisitos documentales confirmados. |
| Homoclave `COFEPRIS-02-001-A` (permiso) y demás modalidades `02-001-*` / `02-002-B…E` | ⚠️ **Pendientes.** Aparecen en guías de COEPRIS estatales y en RETYS Baja California; **no confirmadas contra ficha oficial de COFEPRIS**. Verificar en digipris.cofepris.gob.mx antes de instruir a un cliente. |
| RLGSMP art. 62 Bis (aviso de responsable de publicidad de cosméticos, por marca) → su remisión al **LGS art. 270** | ✅ **Conciliada (2026-10-23).** LGS 270, último párrafo, crea el aviso por marca; 62 Bis lo reglamenta. Homoclave `02-002-D` sin verificar. |
| Criterio de COFEPRIS sobre directorios/plataformas de terceros | ⚠️ **No existe uno público localizado.** Todo §4 es derivación normativa. |

**Gotcha de investigación para futuras actualizaciones:** las páginas HTML de `gob.mx` responden con un reto de JavaScript, pero los PDF bajo `gob.mx/cms/uploads/` sí bajan con `curl` (HTTP 200, probado 2026-10-23), y las notas del DOF se leen por SIDOF (`sidof.segob.gob.mx/dof/sidof/notas/…`). Los textos de ley sí se obtienen de `diputados.gob.mx/LeyesBiblio/` con `curl -A` de navegador; las guías de las COEPRIS estatales sirven como espejo de homoclaves. No declarar un dato inexistente porque falló el primer camino.

## Common Mistakes

| Error | Consecuencia | Corrección |
|---|---|---|
| Asumir que todo establecimiento de salud necesita **licencia sanitaria** | Trámite equivocado, meses perdidos | Sólo el catálogo del art. 198 LGS; lo demás es **aviso de funcionamiento** (200 Bis), si el acuerdo del 200 Bis lo incluye (no verificado) |
| Asumir que un consultorio necesita **permiso** de publicidad | Cotizar \$44K que no se debían | Servicio individual → **aviso** (RLGSMP 86-I). Establecimiento → permiso (79-I). ⚠️ El corte no es textual y está UNRESOLVED (§1): presentar la ruta del aviso como criterio defendible, no como certeza |
| Presentar el aviso de actividades profesionales **después** de prender la campaña | Incumplimiento del plazo | Se presenta **5 días hábiles ANTES** (RLGSMP 87, último párrafo; días hábiles por LFPA 28) — al revés que los demás avisos |
| Tramitar publicidad antes de resolver el estatus del establecimiento | La solicitud pide el número de licencia o aviso de funcionamiento | Establecimiento primero, publicidad después (RLGSMP 80-III, 87-III) |
| Omitir la **cédula profesional** en el anuncio | Multa hasta 2,000 UMA; infracción constatable sin peritaje | Cédula + institución en todo material publicitario (LGS 83; RLGSMP 19) |
| Poner "aprobado por COFEPRIS" como sello de confianza | Prohibido expresamente | LGS 304, 2º párrafo — la resolución no se usa con fines publicitarios |
| Creer que la agencia sólo ejecuta y no responde | La agencia tiene infracción propia de 6,000–8,000 | RLGSMP 77 + 111 — apegarse a los términos del permiso o aviso |
| Creer que una plataforma que aloja fichas de terceros está exenta | El medio de difusión tiene deber propio (art. 78), sancionado en el 111 | Exigir permiso/aviso al proveedor en el onboarding; procedimiento de retiro rápido (el plazo de 24 h del art. 108 aplica a sus supuestos acotados; la verificación general es el 107) |
| Usar el T-MEC 19.17 como defensa sanitaria | Protege frente a contenido de terceros, no exime el deber propio del art. 78 | Son planos distintos: uno responde a PROFECO, otro a COFEPRIS |
| Marketear un servicio estético con verbos terapéuticos | Cruza a servicio de salud y arrastra dos regímenes | Elegir un lado y sostenerlo en todo el copy (RLGSMP 63) |
| Guardar el sustento del claim "por si acaso" en el correo de alguien | La carga de la prueba es del anunciante y el plazo corre | Carpeta de sustento por claim, el día de la publicación (RLGSMP 11) |
| Suponer afirmativa ficta sin acuse | No hay nada que invocar | El acuse fechado ES la defensa (RLGSMP 80) |
| Dar por bueno un monto de la LFD del año pasado | Las cuotas se actualizan cada 1 de enero | Recomputar; los números nacen fechados (LFD art. 1o) |
| Correr sólo la pasada de COFEPRIS | Un copy sanitariamente limpio puede ser engañoso al consumidor | Segunda pasada con `mexico-profeco-consumer` |

## Fuentes primarias

Texto verbatim de LGS / RLGSMP y notas de verificación: [references/cofepris-2026-reference.md](references/cofepris-2026-reference.md) (335 líneas; cargar sólo cuando se cite un artículo).

| Documento | Versión leída | URL |
|---|---|---|
| Ley General de Salud | Última reforma DOF 15-01-2026 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LGS.pdf |
| Reglamento de la LGS en Materia de Publicidad | DOF 04-05-2000, última reforma DOF 08-09-2022 | https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf |
| Ley Federal de Derechos (art. 195) | Última reforma DOF 07-11-2025 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFD.pdf |
| **RMF 2026 Anexo 4** (cantidades actualizadas de la LFD, art. 195-I) | DOF 28-12-2025 (as of enero 2026) | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-4-RMF-2026_DOF-28122025.pdf |
| COFEPRIS — Tarifas de Pagos 2026 (reexpresión del Anexo 4) | Publicada en gob.mx (as of enero 2026) | https://www.gob.mx/cms/uploads/attachment/file/1049620/TarifasDePagos2026.pdf |
| **Ficha del trámite COFEPRIS-02-002-A** (aviso, actividades profesionales) | Obtenida ago 2026 | https://www.gob.mx/cms/uploads/attachment/file/997041/COFEPRIS-02-002-A.pdf |
| Ley Federal de Procedimiento Administrativo (art. 28 — días hábiles) | Última reforma DOF 14-11-2025 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPA.pdf |
| Ley Federal de Protección al Consumidor (art. 32) | Última reforma DOF 12-12-2025 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf |
| Ley General para el Control del Tabaco (art. 23) | Última reforma DOF 17-02-2022 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LGCT.pdf |
| COFEPRIS — trámites y DIGIPRIS | Consultado ago 2026 (reto JS) | https://digipris.cofepris.gob.mx/ · https://www.gob.mx/cofepris |
| VIGIMED — cifras 2026 | La Jornada 05-ago-2026; Milenio 04-ago-2026 | https://www.jornada.com.mx/2026/08/05/politica/008n2pol |

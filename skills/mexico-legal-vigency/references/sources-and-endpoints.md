Verified 2026-10-23

# Fuentes primarias y endpoints

Cada fila registra un fetch hecho el 2026-10-23 con `curl` (sin sesión, sin cookies). "Auth" es lo que pidió el servidor a ese cliente. Una ruta que no entregó contenido por script se marca *no verificado 2026-10-23*; en ese caso abre la página en un navegador y anota lo que viste.

## SIDOF (Secretaría de Gobernación, API del DOF)

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| `GET https://sidof.segob.gob.mx/dof/sidof/notas/DD-MM-YYYY` | JSON UTF-8 | Ninguna | `NotasMatutinas`, `NotasVespertinas`, `NotasExtraordinarias`; cada nota con `codNota`, `titulo`, `fecha`, `codDiario`, `pagina`, `codOrgaUno`, `codOrgaDos`, `existePdf` | `.../notas/21-10-2026` → 200 (121 matutinas, 2 vespertinas, 0 extraordinarias) |
| La misma ruta con fecha ISO | JSON | Ninguna | Error | `.../notas/2026-10-21` → 400 `{"messageCode":400,"response":"BAD_REQUEST"}` |
| `GET https://sidof.segob.gob.mx/dof/sidof/notas/nota/<codNota>` | JSON UTF-8 | Ninguna | `Nota.titulo`, `Nota.fecha`, `Nota.pagina`, `Nota.codEdicion` (MAT, VES), `Nota.cadenaContenido` (documento HTML completo con `<style>`) | `.../notas/nota/5801708` → 200; `.../notas/nota/5778072` → 200 |
| `GET https://sidof.segob.gob.mx/dof/sidof/diarios/porFecha/DD-MM-YYYY` | JSON | Ninguna | Ediciones del día (`Matutina`, `Vespertina`, `Extraordinaria`) con `codDiario` y rango de páginas | `.../diarios/porFecha/21-10-2026` → 200 (matutina `codDiario` 330345, páginas 1 a 552; vespertina 330365) |
| https://sidof.segob.gob.mx/avisoLegal | HTML | Ninguna | Carácter oficial del PDF desde la edición del 05-07-2012 y formato de cita del DOF | → 200 |

Notas de uso:
- Fechas siempre `DD-MM-YYYY` en la ruta.
- En las listas por fecha, algunas notas llegan sin `titulo` (21-10-2026: el primer elemento de `NotasMatutinas` no lo trae). Filtra también por `codOrgaDos`.
- Los títulos pueden ser genéricos y en minúsculas: la UMA 2026 se publicó como "Unidad de medida y actualización." Busca sin distinguir mayúsculas.
- Para leer `cadenaContenido`: quita los bloques `<style>` y `<script>`, cambia `<br>` y `</p>` por saltos de línea, quita etiquetas y decodifica entidades HTML.
- Sábados y domingos sin edición devuelven listas vacías: `.../notas/10-01-2026` → 200 con 0 notas.

## DOF (dof.gob.mx)

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| https://dof.gob.mx/sumario.xml | RSS 2.0, ISO-8859-1 | Ninguna | Sumario de la edición más reciente; cada `<item>` con título de sección, `link` a `nota_detalle.php` y descripción con entidades HTML | → 200, 16 items, todos con `fecha=23/10/2026` |
| `https://dof.gob.mx/nota_detalle.php?codigo=<codNota>&fecha=DD/MM/YYYY` | HTML UTF-8 | Ninguna | La nota en HTML para lectura humana | `?codigo=5801708&fecha=21/10/2026` → 200; contiene el acuerdo y sus resolutivos |
| `https://dof.gob.mx/abrirPDF.php?archivo=DDMMYYYY-MAT.pdf&anio=YYYY&repo=repositorio/` | PDF | Ninguna | La edición matutina completa del día en PDF, con índice; ahí se leen las notas que SIDOF sólo da como imagen y PDF | `?archivo=21102026-MAT.pdf&anio=2026&repo=repositorio/` → 200; con el host `www.dof.gob.mx` la conexión falla en TLS |

El RSS no trae el texto de las notas. Para el texto, toma el `codigo` del `link` y pide la nota a SIDOF. Decodifica el RSS como ISO-8859-1, no como UTF-8. Para el PDF de la edición completa usa la ruta `abrirPDF.php` de la tabla (índice incluido; ahí se leen las notas que SIDOF sólo da como imagen y PDF). En la página `nota_detalle.php` no encontré un enlace directo al PDF de una nota suelta: esa ruta sigue sin confirmar.

## Cámara de Diputados, LeyesBiblio (leyes federales vigentes)

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| https://www.diputados.gob.mx/LeyesBiblio/index.htm | HTML ISO-8859-1 | Ninguna | Índice de leyes vigentes con la fecha de última reforma y enlaces `pdf/<SIGLA>.pdf` y `doc/<SIGLA>.doc` | → 200 (fila de la LSS: "DOF 15/01/2026") |
| https://www.diputados.gob.mx/LeyesBiblio/ | HTML | — | Nada | → 403; usa `index.htm` |
| `https://www.diputados.gob.mx/LeyesBiblio/pdf/<SIGLA>.pdf` | PDF | Ninguna | Texto vigente compilado; encabezado "Última Reforma DOF DD-MM-YYYY" y nota de reforma al pie de cada párrafo | `.../pdf/LSS.pdf` → 200, 181 páginas, "Última Reforma DOF 15-01-2026" |
| `https://www.diputados.gob.mx/LeyesBiblio/doc/<SIGLA>.doc` | Word 97-2003 | Ninguna | El mismo texto en DOC | `.../doc/LSS.doc` → 200 |
| `https://www.diputados.gob.mx/LeyesBiblio/ref/<sigla>.htm` | HTML ISO-8859-1 | Ninguna | Publicación original, aclaraciones y lista de decretos de reforma con fecha DOF | `.../ref/lss.htm` → 200 (original DOF 21-12-1995; 43 decretos de reforma listados) |

La sigla se toma del índice; no la adivines. LeyesBiblio es una compilación de la Cámara: para el texto oficial de un decreto de reforma, ve al DOF de la fecha que indica la nota al pie.

## SAT, normatividad

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/index.html | HTML | Ninguna | Redirección (meta refresh) a la página del año en curso | → 200, redirige a `normatividad_rmf_rgce2026.html` |
| `https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce<AAAA>.html` | HTML | Ninguna | RMF del año, resoluciones de modificación, anexos, versiones anticipadas, compilados, RGCE y RFA, con enlaces PDF | `...rgce2026.html` → 200; lista enlaces a 2025, 2024 y 2023 |
| `https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos<AAAA>/rmf/...` | PDF | Ninguna | Los documentos enlazados desde la página del año | `documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf` → 200 (página 1: "Domingo 28 de diciembre de 2025"); `documentos2026/rmf/anticipadas/4aRM_RMF2026-Tercera_version_anticipada_22102026.pdf` → 200 (encabezado "TERCERA VERSIÓN ANTICIPADA"); `documentos2026/rmf/anexos/Anexo_7_RMF2026-09012026.pdf` → 200 |
| https://www.sat.gob.mx/portal/public/normatividad | HTML (aplicación JavaScript) | — | A un script le entrega la misma página vacía de 1,477 bytes que la portada | → 200 sin contenido; *no verificado 2026-10-23* |

Lo que muestra la página de 2026: Anexo 3 es la compilación de criterios sobre prácticas fiscales indebidas, Anexo 7 la de criterios normativos fiscales, y Anexo 4 las cantidades actualizadas de la Ley Federal de Derechos. Las versiones anticipadas no son DOF; la página distingue "Resolución de Modificaciones" (con fecha DOF en el nombre del archivo) de "Versión Anticipada".

## SCJN, Semanario Judicial de la Federación

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| https://sjf2.scjn.gob.mx/ | HTML | Reto anti-bot (Incapsula) | Una página de 212 bytes con un script de verificación, sin contenido | → 200 sin contenido; un segundo intento con cookies → 403 `{"error": "Acceso denegado: Formato inválido."}` |
| https://sjf2.scjn.gob.mx/busqueda-principal-tesis | HTML | Igual | La misma página de reto | → 200 sin contenido |
| `https://sjf2.scjn.gob.mx/detalle/tesis/<registro>` | HTML | Igual | La misma página de reto | `.../detalle/tesis/2023000` → 200 sin contenido; patrón *no verificado 2026-10-23* |

Por script no hay acceso. Una tesis se verifica abriendo el SJF en un navegador y anotando registro digital, instancia, rubro y fecha de consulta.

## INEGI, UMA

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| https://www.inegi.org.mx/temas/uma/ | HTML con componentes JavaScript | Ninguna | La página del tema; los valores se cargan en el navegador y no vienen en el HTML | → 200; sin cifras en el HTML |
| Nota del DOF de enero, vía SIDOF | JSON | Ninguna | Los valores oficiales y su vigencia | `.../notas/09-01-2026` → 200, nota 5778072 de INEGI; `.../notas/nota/5778072` → 200 |

UMA 2026 según DOF 09-01-2026, nota SIDOF 5778072: valor diario \$117.31, mensual \$3,566.22, anual \$42,794.64, vigentes a partir del 1 de febrero de 2026. Método del propio texto: diario del año anterior por (1 + variación interanual del INPC de diciembre); mensual = diario × 30.4; anual = mensual × 12. En enero de cada año repite la búsqueda por fecha en SIDOF filtrando `codOrgaDos` = INSTITUTO NACIONAL DE ESTADISTICA Y GEOGRAFIA.

## IMSS

| Patrón | Formato | Auth | Qué entrega | Fetch 2026-10-23 |
|---|---|---|---|---|
| https://www.imss.gob.mx/ | HTML | Ninguna | Portada con enlaces a trámites (`/tramites`, `/patrones/idse`, `/patrones/sua`) y comunicados | → 200 |
| https://www.imss.gob.mx/prensa | HTML | Ninguna | Lista de comunicados | → 200 |
| `https://www.imss.gob.mx/prensa/archivo/<AAAAMM>/<número>` | HTML | Ninguna | Un comunicado ("No. 550/2026") | `.../prensa/archivo/202610/550` → 200 |
| https://www.imss.gob.mx/conoce-al-imss/marco-juridico | HTML | — | No existe | → 404 |

Los comunicados del IMSS son una pista, no una cita. Los acuerdos del H. Consejo Técnico se citan del DOF (SIDOF por fecha, filtrando `codOrgaDos` = INSTITUTO MEXICANO DEL SEGURO SOCIAL). No encontré en imss.gob.mx una ruta con el compendio de acuerdos: *no verificado 2026-10-23*.

## Fuentes sin ruta verificada hoy

Gaceta Parlamentaria (iniciativas y dictámenes), IMPI, COFEPRIS y Senado no se consultaron el 2026-10-23. Antes de citar una ruta de esas fuentes, haz el fetch y agrega aquí la fila con su estatus.

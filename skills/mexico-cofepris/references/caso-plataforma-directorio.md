Verified 2026-10-23

# §4. El caso plataforma / directorio en línea de proveedores de salud — mexico-cofepris reference (moved verbatim from SKILL.md, 2026-09-06)

## §4. El caso plataforma / directorio en línea de proveedores de salud

**Pregunta:** ¿un directorio que lista médicos y clínicas está haciendo publicidad regulada por COFEPRIS?

**Respuesta corta:** *depende de la función del listado, no del hecho de listar.* Hay un tramo claramente fuera, un tramo claramente dentro, y una zona gris que se decide por tres variables: **promoción, dinero y control editorial**. Y aun en el tramo "fuera", queda el deber del art. 78 como **medio de difusión**, que es el riesgo que casi nadie modela.

### Los cuatro anclajes normativos

1. **RLGSMP 2-III — qué es un anuncio publicitario:** "*el mensaje dirigido al público o a un segmento del mismo, con el propósito de informar sobre la existencia o las características de un producto, servicio o actividad **para su comercialización y venta o para motivar una conducta***". El elemento distintivo no es "informar", es la **finalidad de comercialización o de motivar conducta**.
2. **RLGSMP 2-IX — qué es publicidad:** el proceso de creación, planificación, ejecución y difusión de anuncios **"con el fin de promover la venta o consumo"**.
3. **RLGSMP 2-VII — qué es medio de difusión:** incluye expresamente lo **informático y de telecomunicaciones**. Un sitio web es medio de difusión sin discusión posible.
4. **RLGSMP 78 + LGS 305 — el deber del medio:** el medio debe asegurarse de que lo que difunde tenga permiso o aviso, y el anunciante debe entregarle copia. Sanción propia de 6,000–8,000 (RLGSMP 111).

### Matriz de riesgo por tipo de listado

| Modalidad del listado | ¿Es publicidad del proveedor? | ¿La plataforma es medio de difusión? | Riesgo |
|---|---|---|---|
| Ficha **puramente factual** — nombre, especialidad, cédula, dirección, idiomas, teléfono; sin adjetivos ni claims; sin pago | Débil. La finalidad es informativa/referencial, no de comercialización de un servicio propio | Discutible; no hay "anuncio" que difundir | **BAJO** |
| Ficha factual + **botón de contacto / agendar** | Empieza a "motivar una conducta" (2-III) | Sí | **BAJO-MEDIO** |
| Ficha con **copy descriptivo escrito por la plataforma** ("excelente trato", "especialista en…") | Sí. Es contenido editorial propio que promueve | Sí, y además es contenido propio, no de tercero | **MEDIO** |
| **Featured / destacado pagado**, ranking pagado, banner del proveedor | Sí, inequívocamente. Hay contraprestación por promoción | **Sí** — aquí el art. 78 muerde de lleno | **ALTO** |
| Contenido editorial de salud (artículos "cómo tratar X") que recomienda tratamientos | Puede caer en **RLGSMP 17** (ofrecer técnicas/tratamientos por medios informativos) | — | **MEDIO-ALTO** |
| Reseñas de usuarios sobre resultados de tratamiento | Contenido de tercero; pero si la plataforma lo cura o lo destaca, se apropia | — | **MEDIO** |

### La distinción que hay que sostener

**Listar no es anunciar; promover sí.** Un directorio que se limita a reproducir hechos verificables sobre la existencia y credenciales de un proveedor está más cerca de un padrón que de un anuncio. En el momento en que la plataforma (a) escribe copy valorativo, (b) cobra por posición o visibilidad, o (c) atribuye al proveedor cualidades terapéuticas, deja de ser padrón: es publicidad, con la plataforma como anunciante o cuando menos como medio.

**El pago es la variable que más rápido mueve la clasificación.** Es también la variable que un modelo de negocio de directorio inevitablemente activa. Modelarlo desde ahora, no cuando ya haya facturación.

### Zona gris honesta — lo que NO está resuelto

⚠️ **No localicé un criterio, acuerdo o precedente público de COFEPRIS que resuelva expresamente el estatus de un directorio o plataforma de terceros.** El análisis anterior es derivación de los textos vigentes, no aplicación de un criterio publicado. Tratarlo como hipótesis defendible, no como certeza. Si el modelo de negocio se va a apoyar en esta lectura, vale una consulta formal (COFEPRIS admite consultas) o una opinión de abogado sanitario antes de escalar el featured pagado.

⚠️ Tampoco hay en México un puerto seguro sanitario para intermediarios equivalente al del T-MEC art. 19.17 para contenido de terceros. El T-MEC protege frente a responsabilidad por **contenido de terceros**; no exime del deber **propio y directo** que el art. 78 impone al medio. Son planos distintos y conviene no confundirlos: la defensa "yo sólo alojo lo que el doctor escribió" responde a la pregunta de PROFECO, no a la del RLGSMP 78.

### Recomendaciones accionables para un directorio en línea de proveedores de salud

- [ ] **Separar visualmente y contractualmente** lo factual de lo promocional. Ficha base = campos cerrados y verificables. Cualquier texto libre del proveedor, marcado como tal ("Información proporcionada por el proveedor").
- [ ] **Nunca** escribir en copy propio de plataforma adjetivos terapéuticos sobre un proveedor ("el mejor para", "resuelve", "cura").
- [ ] Publicar **quién escribió qué** en cada ficha (autoría) — es lo que separa medio de anunciante.
- [ ] Si se lanza **featured pagado**: exigir al proveedor, como requisito de alta, copia de su **permiso o aviso de publicidad** vigente. Esto es literalmente lo que el art. 78, 2º párrafo, ordena al anunciante entregar al medio. Convertirlo en campo obligatorio del onboarding, no en trámite ocasional.
- [ ] **Procedimiento de retiro en 24 horas** documentado, con dueño y canal designado — cuando aplique el art. 108, el plazo corre desde la notificación y no admite negociación. ⚠️ El art. 108 está redactado para remedios herbolarios, suplementos y cosméticos con claims terapéuticos, más lo que viole el art. 6; no es una facultad general de suspensión sobre servicios de salud (ésa se apoya en el art. 107 y en las medidas de seguridad de la LGS). Aun así, el procedimiento de retiro rápido se construye igual: la plataforma no gana nada por discutir el encuadre mientras el anuncio sigue arriba.
- [ ] El contenido editorial de salud se escribe en modo **informativo-educativo**, nunca en modo prescriptivo ("consulta a un profesional" en vez de "haz X para curar Y"), por RLGSMP 17.
- [ ] Coordinar con el disclaimer de verificación ya definido en `mexico-profeco-consumer`: la verificación de cédula responde a PROFECO; añadir que **no implica autorización sanitaria ni endoso de COFEPRIS**.

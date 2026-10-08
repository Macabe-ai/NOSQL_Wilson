# Consultas y Reglas del Caso — Unidad de Emprendimiento SENA

## Reglas del Ejercicio
1. **Códigos únicos:** Emprendedores, iniciativas y asesorías deben contar con códigos únicos (ej. `INI-001`, `ASE-001`).
2. **Relación de iniciativa:** Cada iniciativa tiene un emprendedor responsable existente; una persona puede representar varias iniciativas.
3. **Asesorías:** Cada asesoría se vincula con una iniciativa existente y registra el código ficticio del asesor que la atiende.
4. **Sectores de ejemplo:** Tecnología, alimentos y economía_circular.
5. **Etapas didácticas:** Idea, validación y puesta_en_marcha.
6. **Estados:** Iniciativa (`activa` o `archivada`); Asesoría (`programada`, `realizada` o `cancelada`).
7. **Fechas:** Se registra `fecha_programada` y `fecha_realizacion` (esta última es nula si aún no se efectúa).
8. **Concurrencia:** No programar dos asesorías para el mismo asesor en la misma franja horaria.
9. **Historial:** Archivar una iniciativa no elimina automáticamente su historial de asesorías.

## Definición de las 6 Consultas (Q01 — Q06)
- **Q01:** Iniciativas activas por sector y etapa didáctica (Filtra por estado `activa`, agrupa o lista por sector y etapa).
- **Q02:** Detalle de una iniciativa con su propuesta de valor y atributos específicos según el sector (alimentos o tecnología).
- **Q03:** Iniciativas de un emprendedor responsable filtradas por su estado (`activa` / `archivada`).
- **Q04:** Asesorías programadas pendientes por rango de fechas y modalidad (`virtual` o `presencial`).
- **Q05:** Historial completo de asesorías asociadas a una iniciativa específica mediante su código.
- **Q06:** Cantidad de asesorías realizadas agrupadas por sector de la iniciativa y mes.
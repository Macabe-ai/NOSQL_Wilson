# Diagnóstico Teórico A1 — Respuestas (Parte A)

### 1. ¿Qué representan una tabla, una fila y una clave primaria? Utiliza un ejemplo relacionado con las iniciativas de emprendimiento.
* **Tabla:** Es la estructura o entidad principal que agrupa un conjunto de registros del mismo tipo (ej. la tabla `iniciativas`).
* **Fila (o registro):** Representa un elemento individual dentro de la tabla con sus datos específicos (ej. la fila correspondiente a la iniciativa `"EcoEmpaque"`).
* **Clave primaria (Primary Key):** Es el identificador único e irrepetible de cada fila en la tabla para garantizar que no existan duplicados (ej. `id_iniciativa = "INI-001"`).

---

### 2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una iniciativa que referencia a un emprendedor inexistente?
* **Clave foránea (Foreign Key):** Es un campo en una tabla que hace referencia a la clave primaria de otra tabla, permitiendo establecer una relación formal entre ambas.
* **Problema:** Si una iniciativa referencia a un ID de emprendedor que no existe, se rompe la **integridad referencial** de la base de datos. Esto genera datos huérfanos e inconsistencias al intentar consultar quién es la persona responsable del proyecto.

---

### 3. Explica qué devuelve `SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';`. ¿Modifica registros?
* **Qué devuelve:** Retorna una lista únicamente con los valores de la columna `codigo` de todas las filas en la tabla `iniciativas` cuyo campo `sector` sea exactamente `'tecnologia'`.
* **Modificación:** **No modifica ningún registro**. Es una instrucción DQL (*Data Query Language*) de solo lectura.

---

### 4. Diferencia una lista y un diccionario en Python. ¿Qué estructura utilizarías para una iniciativa y para varias iniciativas?
* **Diferencia:** Una **lista** (`[...]`) es una colección ordenada e indexada por posición numérica. Un **diccionario** (`{...}`) es una estructura que almacena datos en pares `clave: valor`.
* **Uso:** 
  * Para **una sola iniciativa**: Se utiliza un **diccionario** (ej. `{"codigo": "INI-001", "sector": "alimentos"}`).
  * Para **varias iniciativas**: Se utiliza una **lista de diccionarios** (ej. `[iniciativa1, iniciativa2, ...]`).

---

### 5. ¿Son equivalentes `false` y `"false"` en JSON? Explica el tipo de cada valor.
* **No son equivalentes**.
* **`false`:** Es un valor de tipo **booleano** (`boolean`) nativo en JSON.
* **`"false"`:** Es un valor de tipo **cadena de texto** (`string`) debido a las comillas dobles.

---

### 6. Diferencia un campo ausente, un campo con `null` y un campo con una cadena vacía. Propón un ejemplo.
* **Campo ausente:** La clave no existe dentro de la estructura del documento/diccionario.
* **Campo con `null`:** La clave existe explícitamente pero su valor es nulo o indefinido.
* **Campo con cadena vacía (`""`):** La clave existe y su valor es un texto de longitud cero.
* **Ejemplo:**
  ```json
  // Documento A (ausente): {"codigo": "INI-001"}  --> 'fecha_realizacion' no existe
  // Documento B (null):     {"codigo": "INI-001", "fecha_realizacion": null}
  // Documento C (cadena):   {"codigo": "INI-001", "fecha_realizacion": ""}

  ### Autoevaluación DGN-01
- **Puedo realizar:** La manipulación básica de listas/diccionarios en Python y consultas SQL relacionales.
- **Necesito reforzar:** La identificación precisa de tipos BSON en MongoDB y el manejo de fechas con zona horaria.
- **Mi primera acción de mejora será:** Practicar scripts de manipulación de documentos en mongosh.
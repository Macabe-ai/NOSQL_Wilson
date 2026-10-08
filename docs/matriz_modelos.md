# Matriz de Selección de Modelos NoSQL

| Caso | Modelo propuesto | Razón vinculada a una consulta | Límite o costo | Alternativa |
| :--- | :--- | :--- | :--- | :--- |
| **Iniciativas de varios sectores** | Documental (MongoDB) | Permite atributos variables por sector (ej. alimentos vs. software) sin romper el esquema general. | Consultas complejas en múltiples niveles anidados si mal se diseña. | Relacional (SQL) con tablas normalizadas. |
| **Sesiones temporales** | Clave-Valor (Redis) | Acceso ultrarrápido por clave y expiración automática de tokens de sesión. | No apto para consultas relacionales complejas o filtros cruzados. | Base documental con índices de expiración (TTL). |
| **Recorridos de relaciones** | Grafos (Neo4j) | Optimizado para consultas de interconexión profunda entre emprendedores, mentores y habilidades. | Curva de aprendizaje alta y consumo elevado de memoria. | Relacional con múltiples tablas de unión (*joins*). |
| **Lecturas por dispositivo/periodo** | Familias de columnas (Cassandra) | Escritura masiva y eficiente para series temporales de sensores a gran escala. | Flexibilidad limitada en consultas *ad-hoc* que no sigan la clave de partición. | MongoDB con colecciones estructuradas por rangos de tiempo. |
import json

# Texto JSON corregido (en JSON los booleanos van en minúscula: true/false y sin comas sobrantes)
texto = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

# 1. Cargar el texto usando json.loads
datos = json.loads(texto)

# 3. Mostrar código, activa y los tipos de ambos valores
print("Datos cargados:", datos)
print("Código:", datos["codigo"], "-> Tipo:", type(datos["codigo"]).__name__)
print("Activa:", datos["activa"], "-> Tipo:", type(datos["activa"]).__name__)
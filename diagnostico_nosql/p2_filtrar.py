iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"} # Campo ausente a propósito
]

def seleccionar_pendientes(registros, sector):
    codigos_filtrados = []
    for reg in registros:
        if reg.get("sector") == sector and reg.get("pendiente") is True:
            codigos_filtrados.append(reg["codigo"])
    return codigos_filtrados

# Pruebas solicitadas
print("Prueba con resultados (tecnologia):", seleccionar_pendientes(iniciativas, "tecnologia"))
print("Prueba sin resultados (economia_circular):", seleccionar_pendientes(iniciativas, "economia_circular"))
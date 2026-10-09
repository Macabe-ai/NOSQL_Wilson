# Registro de Entorno y Exploración (Evidencia A4)

## 1. Información del Sistema y Herramientas

* **Sistema Operativo:** Windows (Git Bash / MINGW64)
* **Python:** 3.14.7 (`py --version`)
* **Git:** 2.55.0.windows.5 (`git --version`)
* **MongoDB Shell (`mongosh`):** No detectado / Pendiente de instalación (`bash: mongosh: command not found`)

---

## 2. Diagnóstico de la conexión e Incidencia

### Estado de `mongosh`
Al intentar verificar la versión del cliente MongoDB Shell en la terminal con `mongosh --version`, se obtuvo la siguiente respuesta:
```bash
Sena@DESKTOP-CJ6BHF3 MINGW64 ~/Documents/NOSQL Wilson (main)
$ mongosh --version
bash: mongosh: command not found


Sena@DESKTOP-CJ6BHF3 MINGW64 ~/Documents/NOSQL Wilson (main)
$ ./mongosh.exe "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" --file scripts/01_explorar.js
{
  _id: 'ASE-DEMO-001',
  emprendedor_alias: 'Emprendedor ficticio 01',
  iniciativa: {
    codigo: 'INI-DEMO-001',
    nombre: 'EcoEmpaque',
    sector: 'economia_circular'
  },
  temas: [
    'propuesta de valor',
    'validacion de clientes'
  ],
  modalidad: 'virtual',
  estado: 'programada',
  requiere_seguimiento: true,
  fecha_programada: ISODate('2026-10-08T13:00:00.000Z'),
  fecha_realizacion: null
}
Conteo de documentos: 1
¿La fecha_programada es tipo Date? true

Sena@DESKTOP-CJ6BHF3 MINGW64 ~/Documents/NOSQL Wilson (main)
$ 
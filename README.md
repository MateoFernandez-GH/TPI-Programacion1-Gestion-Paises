# Trabajo Práctico Integrador – Programación 1

# Gestión de Datos de Países en Python: Filtros, Ordenamientos y Estadísticas

## Universidad Tecnológica Nacional

**Tecnicatura Universitaria en Programación**

**Materia:** Programación 1

**Grupo:** 17

### Integrantes

* Mate Fernández
* Nayla Benitez

---

# Descripción del Proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia Programación 1.

La aplicación consiste en un sistema de gestión de países desarrollado en Python que permite almacenar, consultar, modificar y analizar información geográfica y demográfica mediante el uso de archivos CSV.

El sistema implementa estructuras de datos fundamentales como listas y diccionarios, así como funciones, validaciones, manejo de excepciones, procesamiento de archivos y algoritmos de ordenamiento.

---

# Objetivos Académicos

Mediante este proyecto se aplicaron los conceptos vistos durante la cursada:

* Listas
* Diccionarios
* Funciones
* Estructuras condicionales
* Estructuras repetitivas
* Manejo de excepciones
* Lectura y escritura de archivos CSV
* Búsquedas y filtrados
* Ordenamientos
* Estadísticas básicas
* Modularización de código

---

# Estructura de Datos Utilizada

Cada país se representa mediante un diccionario con los siguientes campos:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}
```

Todos los países se almacenan dentro de una lista principal cargada desde un archivo CSV.

---

# Funcionalidades Implementadas

## Gestión de Países

* Mostrar países registrados.
* Agregar nuevos países.
* Actualizar población y superficie de un país existente.

## Búsquedas

* Búsqueda parcial por nombre.
* Búsqueda sin distinción entre mayúsculas y minúsculas.

## Filtros

* Filtrado por continente.
* Filtrado por rango de población.
* Filtrado por rango de superficie.

## Ordenamientos

* Ordenamiento por nombre.
* Ordenamiento por población.
* Ordenamiento por superficie ascendente.
* Ordenamiento por superficie descendente.

## Estadísticas

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

## Persistencia de Datos

* Lectura inicial desde archivo CSV.
* Actualización automática del archivo CSV luego de modificaciones.

---

# Tecnologías Utilizadas

* Python 3
* Módulo csv
* Módulo os
* Git
* GitHub

---

# Organización del Proyecto

```text
TPI-Programacion1
│
├── src/
│   └── TPI.py
│
├── data/
│   └── paises.csv
│
├── docs/
│   ├── Documentacion_Tecnica_Academica.pdf
│   └── Documentacion_Tecnica_Academica.docx
│
├── capturas/
│
└── README.md
```

---

# Instrucciones de Ejecución

1. Clonar el repositorio:

```bash
git clone [URL_DEL_REPOSITORIO]
```

2. Acceder al proyecto:

```bash
cd TPI-Programacion1
```

3. Ejecutar el programa:

```bash
python src/TPI.py
```

---

# Aspectos Técnicos Destacados

* Utilización de rutas dinámicas mediante el módulo `os`.
* Implementación de validaciones para evitar entradas inválidas.
* Manejo de errores mediante bloques `try/except`.
* Persistencia de datos utilizando archivos CSV.
* Normalización de continentes para mejorar búsquedas y estadísticas.
* Implementación manual del algoritmo de ordenamiento Burbuja.
* Uso de estructuras de control `match-case` para el menú principal.

---

# Participación de los Integrantes

El trabajo fue desarrollado de manera colaborativa por ambos integrantes.

Tanto el desarrollo del código fuente como la elaboración de la documentación académica y técnica fueron realizados conjuntamente, participando ambos miembros en las tareas de análisis, diseño, implementación, pruebas y documentación del sistema.

---

# Documentación Académica y Técnica

Documento PDF:

[PEGAR LINK AL PDF EN EL REPOSITORIO]

---

# Video Demostrativo

Video de presentación y funcionamiento del sistema:

https://drive.google.com/file/d/1sGPDtA4HOGy9rDHdDAwhimALPVSrxKuF/view?usp=drive_link
---

# Repositorio GitHub

https://github.com/MateoFernandez-GH/TPI-Programacion1-Gestion-Paises.git
---

# Bibliografía Principal

* Downey, Allen B. (2015). Pensar en Python: Aprende a pensar como un informático.
* Python Documentation: https://docs.python.org/3/
* Git Documentation: https://git-scm.com/doc
* GitHub Documentation: https://docs.github.com/

---

Proyecto desarrollado para Programación 1 – Tecnicatura Universitaria en Programación – Universidad Tecnológica Nacional.

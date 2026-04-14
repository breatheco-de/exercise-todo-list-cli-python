# Lista de tareas CLI en Python

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros colaboradores](https://github.com/4GeeksAcademy/exercise-todo-list-cli-python/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Te has unido al equipo de herramientas internas de una empresa pequeña de logistica. Hoy, los coordinadores operativos anotan tareas pendientes entre mensajes de chat y notas sueltas, y eso provoca que se pierdan seguimientos importantes entre turnos. Tu product manager te ha pedido una herramienta ligera de terminal para que cualquier persona pueda gestionar tareas rapidamente desde la linea de comandos.

La aplicacion debe permitir registrar nuevas tareas cuando llegan, consultar toda la lista en cualquier momento y eliminar tareas completadas indicando su posicion numerica. Como el equipo cierra y abre terminales durante el dia, tambien necesita guardar tareas en un archivo local y volver a cargarlas despues sin perder progreso.

> Tu product manager compartio este brief funcional:
>
> ### Comportamiento requerido
>
> - Agregar una nueva tarea por titulo
> - Mostrar todas las tareas pendientes con su posicion numerica
> - Eliminar una tarea por su posicion en la lista
> - Guardar tareas en un archivo `todos.csv`
> - Cargar nuevamente las tareas desde `todos.csv`
> - No hace falta editar tareas en esta version; el flujo esperado es eliminar y volver a crear

Construye esta primera version funcional para que el equipo de operaciones la pruebe esta semana.

---

## 🌱 Cómo iniciar el proyecto

- Abre este enlace en tu navegador usando [Codespaces](https://4geeks.com/es/lesson/tutorial-de-github-codespaces) (recomendado): `https://github.com/codespaces/new/?repo=4GeeksAcademy/python-hello`
- O clona la plantilla localmente:

```bash
git clone https://github.com/4GeeksAcademy/python-hello
```

- Si trabajas en local, asegurate de tener Python [instalado](https://4geeks.com/es/how-to/como-instalar-python)
- Ejecuta `python3 app.py` para verificar que el entorno funciona
- Ejecuta `python3 test.py` para correr las pruebas
- Crea tu propio repositorio en GitHub para la entrega y actualiza el remote con `git remote set-url origin <tu-nueva-url>`
- Revisa la guia completa de inicio aqui: [como iniciar un proyecto](https://4geeks.com/es/lesson/how-to-start-a-project)

---

## 💻 Qué debes hacer

- [ ] Implementar `add_one_task(title)` para agregar una nueva tarea a la lista en memoria
- [ ] Implementar `print_list()` para mostrar todas las tareas con posiciones numericas claras
- [ ] Implementar `delete_task(number_to_delete)` para eliminar una tarea usando su posicion
- [ ] Implementar `save_todos()` para persistir las tareas en `todos.csv`
- [ ] Implementar `load_todos()` para cargar tareas desde `todos.csv` hacia memoria
- [ ] Asegurar que el usuario pueda agregar tantas tareas como necesite en la misma ejecucion
- [ ] Asegurar que toda la experiencia funcione desde la linea de comandos y coincida con la referencia visual

⚠️ **IMPORTANTE:** En esta version del proyecto usa solo herramientas de la libreria estandar de Python para entrada/salida de archivos y manejo de CLI.

---

## ✅ Qué vamos a evaluar

- [ ] `add_one_task(title)` agrega correctamente nuevas tareas a la lista activa
- [ ] `print_list()` muestra las tareas en orden con posiciones que el usuario pueda referenciar
- [ ] `delete_task(number_to_delete)` elimina la tarea correcta y actualiza bien la lista resultante
- [ ] `save_todos()` guarda las tareas actuales en `todos.csv` con un formato reutilizable
- [ ] `load_todos()` reconstruye correctamente las tareas desde `todos.csv`
- [ ] El flujo CLI se comporta de forma consistente: crear, listar, eliminar, guardar y cargar

> Nota: La edicion de tareas (actualizacion en sitio) queda fuera del alcance de este ejercicio.

---

## 📦 Cómo entregar

Sube tu solucion a tu propio repositorio en GitHub y comparte la URL del repositorio segun las instrucciones de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).

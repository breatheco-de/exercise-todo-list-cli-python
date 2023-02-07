<!--hide-->
# Lista de tareas pendientes CLI (interfaz de línea de comandos)
<!--endhide-->

<p align="center">
  <img height="200" src="https://github.com/breatheco-de/exercise-todo-list-cli-python/blob/master/preview.gif?raw=true" />
</p>

Crea una aplicación de lista de tareas o de todos que le permita a los usuarios añadir y eliminar tareas desde la terminal.

## 🌱  Cómo iniciar este proyecto

1. Este proyecto viene con los archivos necesarios para empezar a trabajar, pero tienes dos opciones para empezar:

a) Abrir este link con Gitpod (recomendada) en tu navegador: https://gitpod.io#https://github.com/breatheco-de/exercise-todo-list-cli

b) Clonar este repositorio localmente en tu computador:
```sh
$ git clone https://github.com/breatheco-de/exercise-todo-list-cli
```
2. Puedes probar tu código escribiendo en la terminal: `$ python3 test.py`

3. Puedes ejecutar tu código escribiendo en la terminal: `$ python3 app.py`.



💡 Importante: Recuerda actualizar el `remote` del proyecto con el de tu repositorio usando `git remote set-url origin <your new url>`, y luego guardar tu código en tu nuevo repositorio usando `add`, `commit` y `push`.

## 📝 Instrucciones

Estas son las funciones que tendrás que implementar:

```python
def add_one_task(title):
def print_list():
def delete_task(number_to_delete):
def save_todos():
def load_todos():
````

- Tu aplicación debe funcionar desde la terminal [como esta] (https://projects.breatheco.de/json?slug=todo-list-cli&preview).
- El usuario puede agregar nuevas tareas
- El usuario puede agregar tantas tareas como quiera.
- El usuario puede eliminar tareas especificando la posición de la tarea en la lista.
- El usuario puede guardar los todos en un archivo `todos.csv`
- El usuario puede recuperar los todos de un archivo `todos.csv`
- No hay forma de actualizar una tarea, el usuario deberá borrar y crear nuevamente.

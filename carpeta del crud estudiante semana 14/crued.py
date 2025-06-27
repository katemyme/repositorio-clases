import os
import getpass
import pwinput

# Se importa el módulo os para usar la función: os.path.exists(ruta)

ARCHIVO = "estudiantes.txt"
CLAVE = 'Sergioguei123'

def validar_contra(contra, valida):
    for i in range(3):
        if contra == valida:
            print("Contraseña correcta")
            return True
        else:
            print("Contraseña incorrecta, intente nuevamente")
            contra = input("Ingrese la contraseña: ")
            if i == 2:
                print("Número máximo de intentos alcanzado")
                return False
          
def inicio():
    """Permite hasta 3 intentos de autenticación. Devuelve True/False."""
    usuarios = cargar_usuarios()
    for intento in range(1, 4):
        usuario = input("Usuario: ")
        clave   = pwinput.pwinput("Contraseña: ", mask="*")
        if usuario in usuarios and usuarios[usuario] == clave:
            print("  Acceso concedido\n")
            return True
        else:
            print(f"  Credenciales incorrectas (intento {intento}/3)\n")
    print("Número máximo de intentos alcanzado.\n")
    return False


def cargar_usuarios():
    usuarios={}
    if os.path.exists("crud_estudiante.txt"):
        with open("crud_estudiante.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(',')
                usuarios[usuario]=clave
    return usuarios

def cargar_estudiantes():
    estudiantes = []
    # La función os.path.exists() verifica si un archivo o carpeta existe en una ruta determinada
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")
                # linea.strip() Elimina espacios y saltos de línea (\n) al principio o al final.
                # split(",") Divide la cadena en una lista de partes, usando la coma como separador.
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w") as archivo:
        for est in estudiantes:
            linea = f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)

def crear_estudiante(estudiantes):
    codigo = input("Código del estudiante: ")
    # Verificar si el código ya existe
    # La función any() devuelve True si al menos un elemento de un iterable es verdadero.
    if any(est["codigo"] == codigo for est in estudiantes):
        print("El código ya existe\n")
        return

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })

    guardar_estudiantes(estudiantes)
    print("Estudiante agregado correctamente.\n")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    print("\nLista de estudiantes:")
    for est in estudiantes:
        print(f"Código: {est['codigo']}, Nombre: {est['nombre']} {est['apellido']}, Carrera: {est['carrera']}")
    print()

def actualizar_estudiante(estudiantes):
    codigo = input("Ingresa el código del estudiante a actualizar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            est["nombre"] = input(f"Nuevo nombre (actual: {est['nombre']}): ") or est["nombre"]
            est["apellido"] = input(f"Nuevo apellido (actual: {est['apellido']}): ") or est["apellido"]
            est["carrera"] = input(f"Nueva carrera (actual: {est['carrera']}): ") or est["carrera"]
            guardar_estudiantes(estudiantes)
            print("Estudiante actualizado.\n")
            return
    print("No se encontró estudiante con ese código.\n")


def eliminar_estudiante(estudiantes):
    codigo = input("Ingresa el código del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            estudiantes.remove(est)
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado.\n")
            return
    print("No se encontró un estudiante con ese código.\n")

# Funcion menu principal
def menu():
    estudiantes = cargar_estudiantes()
    while True:
        print("==== MENÚ CRUD ESTUDIANTES ====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        print("6. Iniciar sesión")
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            crear_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.\n")
        
# Instrucción para ejecutar el menú
inicio()
menu()
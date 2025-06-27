import os 
import getpass 
import pwinput
#Se importa el módulo os para usar la función: os.path.exists(ruta)
ARCHIVO="estudiantes.txt"
CLAVE="C"

#Función para cargar el archivo usuarios.txt
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open ("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario] = clave
    return usuarios

#Se define función para autenticación
def inicio():
    print ("======INICIO DE SESIÓN======")
    usuarios = cargar_usuarios()
    intentos = 0
    maximo_intentos=3

    while intentos < maximo_intentos:
        usuario = input("Usuario: ")
        #clave_ingresada = getpass.getpass("Contraseña: ")
        clave_ingresada = pwinput.pwinput("Contraseña: ", mask="*")
        if usuario in usuarios and usuarios[usuario] == clave_ingresada:
            print ("Acceso permitido\n")
            return True
        else:
            intentos +=1
            print (f"Usuario o contraseña incorrectos. Intento {intentos}/{maximo_intentos}\n")
            
    print ("Superó el número de intentos permitidos!")
    return False

#Se define funcion para cargar estudiantes 
def cargar_estudiantes():
    estudiantes=[]
    #La función os.path.exists() verifica si un archivo o carpeta existe en una ruta determinada
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO,"r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")
                #linea.strip() Elimina espacios y saltos de línea (\n) al principio o al final.
                # split(",") Divide la cadena en una lista de partes, usando la coma como separador.
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes

#Se crea función para guardar estudiantes
def guardar_estudiantes(estudiantes):
    with open(ARCHIVO,"w") as archivo:
        for est in estudiantes:
            linea=f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)

#Se crea función para crear estudiantes
def crear_estudiantes(estudiantes):
    codigo=input("Código del estudiante: ")
    #Verificar si el codigo ya existe
    #La funcion any() devuelve True si al menos un elemento de una iterable es verdadero.
    if any(est["codigo"]==codigo for est in estudiantes):
        print ("El código ya existe\n")
        return
    
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    carrera=input("Carrera: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })
    guardar_estudiantes(estudiantes)
    print ("Estudiante agregado correctamente.\n")

#Se crea función para mostrar estudiantes
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print ("No hay estudiantes registrados.\n")
        return
    
    print ("\nLista de estudiantes:")
    for est in estudiantes:
        print (f"código: {est['codigo']}, Nombre: {est['nombre']} {est['apellido']}, Carrera: {est['carrera']}")
    print ()

#Se crea función para actualizar los datos de estudiantes
def actualizar_estudiantes(estudiantes):
    codigo=input("Ingresa el código del estudiante a actualizar: ")
    for est in estudiantes:
        if est["codigo"]==codigo:
            est["nombre"]=input(f"Nuevo nombre (actual: {est['nombre']}): ") or est["nombre"]
            est["apellido"]=input(f"Nuevo apellido (actual: {est['apellido']}): ") or est["apellido"]
            est["carrera"]=input(f"Nueva carrera (actual: {est['carrera']}): ") or est["carrera"]
            guardar_estudiantes(estudiantes)
            print ("Estudiante actualizado.\n")
            return
    print ("No se encontró estudiante con ese código.\n")

#Se crea función para eliminar estudiantes
def eliminar_estudiantes(estudiantes):
    codigo=input("Ingresa el código del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"]==codigo:
            estudiantes.remove(est)
            guardar_estudiantes(estudiantes)
            print ("Estudiante eliminado.\n")
            return
    print ("No se encontró un estudiante con ese código.\n")

#Se crea función para el menú principal
def menu():
    estudiantes=cargar_estudiantes()
    while True:
        print ("===== MENÚ CRUD ESTUDIANTES =====")
        print ("1. Agregar estudiante")
        print ("2. Mostrar estudiante")
        print ("3. Actualizar estudiante")
        print ("4. Eliminar estudiante")
        print ("5. Salir")
        opcion=input ("Selecciona una opción (1-5): ")

        if opcion=="1":
            crear_estudiantes(estudiantes)
        elif opcion=="2":
            mostrar_estudiantes(estudiantes)
        elif opcion=="3":
            actualizar_estudiantes(estudiantes)
        elif opcion=="4":
            eliminar_estudiantes(estudiantes)
        elif opcion=="5":
            print ("Saliendo del programa.")
            break
        else:
            print ("Opción inválida.\n")

#Instrucción para ejecutar el menú
if inicio():
    menu()
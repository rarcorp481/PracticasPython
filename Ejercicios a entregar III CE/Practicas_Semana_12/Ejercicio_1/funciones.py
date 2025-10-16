#Funciones para el diario personal

#Importando la fecha actual con formato
from datetime import datetime

#Devolviendo la fecha actual y definiéndola como una funcion
def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Funcion para guardar el texto
def guardar_entrada(texto):
    fecha_hora = obtener_fecha_actual()
    with open("diario.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{fecha_hora} - {texto}\n")
        archivo.write("-" * 40 + "\n")

#Fecha para pedir la entrada
def pedir_entrada():
    return input("Escribe tu entrada para el diario: ")

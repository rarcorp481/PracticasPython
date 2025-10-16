#Ejercicio 1: Diario Personal

#Importando las funciones necesarias para ejecutar el diario
from funciones import guardar_entrada,pedir_entrada

#Creamos una funcion que contenga las funciones necesarias pera el funcionamiento del diario
def final():
    entrada = pedir_entrada()
    guardar_entrada(entrada)
    print("Tu entrada se ha añadido exitosamente")

#Ejecutamos finalmente la función para añadir entradas y guardarlas
final()



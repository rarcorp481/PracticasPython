#Ejercicio 2: Contador de Líneas

#Solicitando el nombre del archivo al usuario
textFile = input("Ingrese el nombre del texto en formato txt: ")
if not textFile.endswith(".txt"): 
    textFile += ".txt" #Añade la terminación .txt si el usuario no lo hizo
    
#Usando bloque try-except para leer el archivo
try: 
    with open(textFile,"r", encoding = "utf-8") as archivo:
        lineas = archivo.readlines()
        print(f"La longitud de la lista es igual a: {len(lineas)}\n")
        print("El contenido del archivo es:\n")
        for linea in lineas:
            print(linea, end = "" )
        archivo.close()
        
 #Si el archivo no existe, se le muestra este mensaje al usuario   
except FileNotFoundError: 
    print("\nEl archivo no existe, por favor ingrese nuevamente el nombre del archivo\n")

#Sirve si ocurre un error inesperado (guarda el error en la variable "e" y lo muestra al usuario)
except Exception as e: 
        print(f"Ocurrió un error inesperado: {e}")
        
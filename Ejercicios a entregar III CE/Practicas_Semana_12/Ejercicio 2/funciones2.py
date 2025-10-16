#Función de creación de texto
def creacion_archivo():
    textFile = input("Ingrese el nombre del texto que desea crear en formato .txt: ")
    if not textFile.endswitch(".txt"): 
        textFile += ".txt" #se usa el endswitch para poner automaticamente el .txt si el usuario no lo escribe
    cant_lineas = int(input("Ingrese la cantidad de líneas que tendrá su texto: \n"))
     
    #Se creó una lista vacía para llenarla con las líneas del archivo
    texto = []
    for i in range(cant_lineas):
        elementos = input(f"Ingrese la línea {i+1}: ")
        texto.append(elementos)
  
    #Ya "texto[]" lleno,se crea el archivo y se recorre la lista con for para escribir las líneas
    with open(textFile, "w", encoding ="utf-8") as file:
        for linea in texto:
            file.write(linea + "\n")
        print("¡Archivo creado con éxito!\n")
    return textFile, texto


#Función de lectura de texto en terminal
def lectura_texto():
    try: 
        nombre_texto = input("Ingrese el nombre del texto que desea visualizar en formato .txt: \n")
        if not nombre_texto.endswitch(".txt"): #Valida si termina en .txt
            nombre_texto += ".txt" 
            
        #Se abre el archivo en modo lectura y se guarda en "archivo"    
        with open(nombre_texto,"r", encoding = "utf-8") as archivo:
            lineas = archivo.readlines()
            print(f"La longitud de la lista es igual a: {len(lineas)}\n") #Cantidad de líneas del archivo
            print("El contenido del archivo es: \n")
            for i in lineas: 
                print(i.strip()) #El strip() elimina los saltos de línea dobles por el for
             
        return lineas, nombre_texto #Guarda las variables si se quieren volver a usar
     
     #Sirve por si el archivo no se encuentra por el nombre dado  
    except FileNotFoundError: 
        print("El archivo no existe, por favor ingrese un nombre válido")
    
    #Se ejecuta ante cualquier error inesperado (guarda el error en la variable "e")
    except Exception as e: 
        print(f"Ocurrió un error inesperado: {e}")
        

        
    
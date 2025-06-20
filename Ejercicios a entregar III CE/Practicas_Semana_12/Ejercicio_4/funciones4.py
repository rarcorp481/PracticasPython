#Archivo de funciones para el ejercicio 4

#Función para mostrar los datos de productos leidos desde un csv
def mostrar_datos_productos():
    try:
        with open("productos.csv", "r") as archivo:
            print("\nDatos de productos:\n")
            
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    nombre, precio, stock = linea.split(",")
                    print(f"Producto: {nombre} | Precio: ${precio} | Stock: {stock} unidades")
    
    except FileNotFoundError:
        print("El archivo 'productos.csv' no existe.")
    
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", e)

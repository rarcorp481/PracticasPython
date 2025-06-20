#funciones para la lista de compras en módulo

#Función para generar una lista de compras
def crear_lista_compras():
    try:
        with open("compras.txt", "w") as archivo:
            print("Introduce los productos para tu lista de compras.")
            print("Escribe 'fin' cuando hayas terminado.\n")
            
            while True:
                producto = input("Producto: ").strip()
                if producto.lower() == "fin":
                    break
                archivo.write(producto + "\n")
        
        print("\nLista de compras guardada en 'compras.txt'.")
    
    except Exception as e:
        print("Ocurrió un error al guardar la lista:", e)



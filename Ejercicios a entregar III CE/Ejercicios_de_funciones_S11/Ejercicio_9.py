# Función que imprime la tabla de multiplicar del número recibido
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()  # Salto de línea final

try:
    # Pedir número al usuario
    num = int(input("Ingrese un número entero para ver su tabla de multiplicar:\n"))
    tabla_multiplicar(num)

except ValueError:
    print("\nEntrada inválida. Por favor ingrese un número entero.\n")

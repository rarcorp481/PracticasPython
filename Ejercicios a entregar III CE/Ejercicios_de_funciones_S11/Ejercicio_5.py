# Función que calcula el factorial de un número
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i  # Multiplica acumuladamente
    return resultado

try:
    # Pedimos un número al usuario
    numero = int(input("Ingrese un número para calcular su factorial: "))

    # Verificamos que no sea negativo
    if numero < 0:
        print("No se puede calcular el factorial de un número negativo.")
    else:
        # Mostramos el resultado usando la función
        print(f"El factorial de {numero} es: {factorial(numero)}")

except ValueError:
    # Si el usuario escribe algo que no es un número entero, como letras
    print("⚠️ Entrada inválida. Por favor ingrese un número entero.")

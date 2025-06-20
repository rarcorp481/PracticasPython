# Función que calcula el importe final con descuento según el importe original
def calcular_descuento(importe):
    if importe > 500:
        descuento = 0.12
    elif importe > 300:
        descuento = 0.10
    elif importe > 0:
        descuento = 0.05
    else:
        descuento = 0

    return importe * (1 - descuento)

try:
    # Solicitar al usuario el importe de la compra
    compra = float(input("Ingrese el importe total de la compra (€):\n"))

    if compra <= 0:
        print("\nEl importe debe ser mayor a cero.\n")
    else:
        total = calcular_descuento(compra)
        print(f"\nImporte original: €{compra:.2f}")
        print(f"Importe final con descuento aplicado: €{total:.2f}\n")

except ValueError:
    print("\nEntrada inválida. Por favor ingrese un valor numérico.\n")


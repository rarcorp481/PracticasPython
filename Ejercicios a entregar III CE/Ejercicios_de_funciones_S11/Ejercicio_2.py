print("Programa para calcular el sueldo + las comisiones de ventas de cada vendedor")

def calcular_comision(venta1, venta2, venta3): #definimos la funcion con los datos de venta
    return 0.1 * (venta1 + venta2 + venta3)


n = int(input("¿Cuántos vendedores hay? ")) #Cantidad de empleados 

#Ciclo para ingresar los datos de cada empleado
for i in range(1, n + 1):
    print(f"\nVendedor {i}")
    sueldo_base = float(input("Ingrese el sueldo base: "))
    v1 = float(input("Ingrese el valor de la primera venta: "))
    v2 = float(input("Ingrese el valor de la segunda venta: "))
    v3 = float(input("Ingrese el valor de la tercera venta: "))

    comision = calcular_comision(v1, v2, v3)
    total = sueldo_base + comision

    print(f"\nComisión por las tres ventas: C$ {comision:.2f}\n")
    print(f"Total a recibir (sueldo + comisión): C$ {total:.2f}\n")

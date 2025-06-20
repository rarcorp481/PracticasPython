print("\nPrograma para calcular el salario de un cantidad de empleados con 10% de renta\n")

def salario_empleados():
    
    #Variables a usar y funciones a usar
    import textwrap
    cant_empleados = int(input("Ingrese la cantidad de empleados de la empresa: "))
    Salarios = []
    print()
     
    #Ciclo para ingresar los salarios del total de trabajadores
    for i in range(cant_empleados):
        salario = int(input(f"Ingrese el salario del empleado {i+1}: ")) 
        salario += salario * 0.1
        Salarios.append(salario)
    print("\nCalculando el 10% para cada salario....\n")
    
    #Tabla decorativa usando textwrap.dedent para quitar indentación
    print(textwrap.dedent("""
     =========================
     SALARIOS DE LOS EMPLEADOS
     =========================
    """))
    
    #Ciclo para recorrer la lista y darle formato a los salarios
    for i in range(len(Salarios)):
        print(textwrap.dedent(f"Empleado {i+1}: {Salarios[i]:>10.2f} C$."))

#Invocación de la función
salario_empleados()
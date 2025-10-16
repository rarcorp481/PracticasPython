#programa para calcular el monto de cada departamento dentro de una empresa

def repartir_presupuesto():
    print("Programa para calcular el porcentaje de dinero correspondiente a cada departamento de una fábrica\n")
    
    try: 
        #Pedimos el presupuesto al usuario y luego calculamos los porcentajes de los departamentos
        presupuesto = float(input("Ingrese el presupuesto anual en córdobas de la fábrica: "))
        recursos_humanos = presupuesto * 0.5
        manufactura = presupuesto * 0.25
        empaquetado = presupuesto * 0.15
        publicidad = presupuesto * 0.1
    
        #le asignanos los resultados a una variable
        resumen = f"""
            ==========================
             PRESUPUESTO DEPARTAMENTAL
            ==========================

            Total: {presupuesto:.2f} C$

            Recursos Humanos (50%):  {recursos_humanos:>10.2f} C$
            Manufactura (25%):       {manufactura:>10.2f} C$
            Contabilidad (15%):      {empaquetado:>10.2f} C$
            Publicidad (10%):        {publicidad:>10.2f} C$
        """
        #Importamos la variable textwrap
        import textwrap
        
        #le damos al textwrap.dedent la variable "resumen" para que le quite la indentación
        #que se crea por estar dentro de una función
        print(textwrap.dedent(resumen))
    
    #En caso de ingresar un string:
    except ValueError as v:
        print(f"\nDigite un número válido ({v})\n")
      
    #En caso de un error inesperado:
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado ({e})\n")
    
  
#Invocamos la función
repartir_presupuesto()
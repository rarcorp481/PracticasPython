print("Programa para determinar el monto a pagar en dependencia de las horas trabajadas\n")

def calculo_horas():
    try: 
        a = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        import textwrap
        
        
        if a<= 160: #Menor o igual que 160
            horas = a * 6.5
    
            print(textwrap.dedent(f"""     
                ==================
                REMUNERACIÓN TOTAL
                ==================
                    
                HORAS TRABAJADAS    {a:>8} hrs.
                TOTAL REMUNERADO    {horas:>10.2f} $.
                """))
    

        elif a > 160: #En caso de ser mayor a 160
            horas_extra = a - 160
            horas_restantes = horas_extra * 7.5
            horas = horas_restantes + (160 * 6.5)
        
            print(textwrap.dedent(f"""     
                ==================
                REMUNERACIÓN TOTAL
                ==================
                    
                HORAS TRABAJADAS    {a:>8} hrs.
                HORAS EXTRA         {horas_extra:>8} hrs.
            
                TOTAL REMUNERADO    {horas:>10.2f} $.
                """))
        
    except ValueError: 
        print("\nIngrese un número válido.\n")
    

        
calculo_horas()
print("\nPrograma para determinar el menor de 3 números reales:\n")

def menor_de_tres(a,b,c):
    try:    
        if a<=b and a<=c: #Verifica si la menor no es a
            return a 
        
        elif b<=a and b<=c:  #Verifica si la menor no es b
            return b 
        
        else:  #Si las anteriores no son las menores, entonces es c
            return c
   
    except ValueError:
        print("\nIngrese un valor Real.\n")
        
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado: {e}\n")

#Leer los 3 valores del teclado
x = float(input("Ingrese el primer valor: "))
y = float(input("Ingrese el segundo valor: "))
z = float(input("Ingrese el tercer valor: "))

print("\nEl menor valor de los 3 es: ", menor_de_tres(x,y,z),"\n")



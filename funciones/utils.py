

num_ingresado = int(input("Ingresá un numero: "))


def nums_primos ():
    contador = 0
    for numero_ejemplo in range(1, num_ingresado + 1, 1):        
        limite = (numero_ejemplo // 2) + 1
        numero_primo = True
        
        for numero in range(2, limite):
            
            if (numero_ejemplo % numero) == 0:
                numero_primo = False
                break

        if numero_primo == True:            
            contador += 1
            print(f"{numero_ejemplo} es primo")
            
          
    print(f"La cantidad de numeros primos hasta el {num_ingresado} es: {contador}")
        

nums_primos()
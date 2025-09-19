#Ejercicio 1
# for numero in range(1, 11):
#     print(numero)
    
#Ejercicio 2
# for num in range(10, 0, -1):
#     print(num)
    
# #Ejercicio 3
# num_ingresado = int(input("Ingrese un numero como limite: "))
# for num in range(0, (num_ingresado + 1)):
#     print(num)
    
#Ejercicio 4
    
# numero = int(input("Ingrese un numero: "))

# for i in range(0, 11):
#     resultado = i * numero
#     print(f"{numero} x {i} = {resultado}")

#Ejercicio 5
# numero = 0
# contador = 0


# for contador in range(1, 11):
    
#     numero_alt = int(input("Vamos a sumar y hacer un promedio entre 10 numeros que ud ingrese o hasta que coloque 0: "))
#     if numero_alt == 0:
#         break
    
#     numero += numero_alt
#     promedio = numero / contador
    

# print(f"La suma y el promedio, entre los numeros ingresados es: {numero} y {promedio}")


#Ejercicio 6
# Imprimir los números múltiplos de 3 entre el 1 y el 10.

# print (f"A continuacion mostraremos los numeros impar, desde el 1 hasta el 10")
# for i in range(0, 11, 3):
#     print (f"{i}")

#Ejercicio 7

# print (f"A continuacion mostraremos los numeros par, iniciando en 1 y finalizando en el numero 50")
# for i in range(0, 51, 2):
#     print (f"{i}")

#Ejercicio 8

# limite = int(input("Por favor ingrese un numero, el cual utilizaremos como limite, para fomar una piramide: "))
# limite += 1
# lista = [0, limite]


# num_ingresado = int(input("Ingresa un número: "))

# for i in range(1, num_ingresado + 1):
    
#     linea = ""
    
#     for j in range(1, i + 1):
        
#         linea += str(j)
        
#         if j < i:
#             linea += ","
            
#     print(linea)


#Ejercicio 9
# numIngresado = int(input("Vamos a ver cuantos dividores tiene el numero que ponga a continuacion: "))
# contador = 0

# print("El numero ingresado es", numIngresado)
# for i in range(1, numIngresado + 1):    
#     if numIngresado % i ==  0:
#         contador += 1
#         cantidad = contador
#         print("Los divisores son:", i)
        
# print(f"La cantidad de divisores para el numero {numIngresado}, son {cantidad}")

#Ejercicio 10 Ingresar un número. Determinar si el número es primo o no.

# number = int(input("Ingrese un número: "))

# contador = 0
# primo = True

# for p in range(1, number + 1):
    
#     if (number % p) == 0:
#         contador += 1
        
#     if contador > 2:
#         primo = False
        
# if primo == False:
#     print("No es primo")
# else:
#    print(f"{number} es primo")

#Ejercicio 11

# Muestro primos entre uno y mil
# Es divisible solo por sí mismo y por 1

num_ingresado = int(input("Ingresá un numero: "))

for numero_ejemplo in range(1, num_ingresado + 1, 1):

    limite = (numero_ejemplo // 2) + 1
    numero_primo = True

    for numero in range(2, limite):

        if (numero_ejemplo % numero) == 0:
            numero_primo = False
            break

    if numero_primo == True:
        print(f"{numero_ejemplo} es primo")


#Ejercicio 1
# condicion:bool = True;

# numero:int = 0;

# while condicion:
    
#     numero += 1
#     print(f"{numero}")
#     if numero >= 10:
#         break

#Ejercicio 2
# condicion:bool = True;

# numero:int = 11;

# while condicion:
    
#     numero -= 1
    
#     print(f"{numero}")
#     if numero <= 0:        
#         break;
        
#Ejercicio 3

# condicion:bool = True;
# numero:int = 0;

# while condicion:

#     if numero < 9:
#         numero += 1
#         resultado = numero + 1
#         print(f"{numero} + 1 = {resultado}")
#     else:
#         break
    
#Ejercicio 4

# condicion:bool = True;
# numero:int = 0;

# while condicion:

#     if numero < 10:
#         numero += 2
#         resultado = numero + 1
#         print(f"{numero} + 1 = {resultado}")
#     else:
#         break;
    
#Ejercicio 5
# numero1 = int(input("Ingresa un numero: "))
# numero2 = int(input("Ingresa un numero: "))
# numero3 = int(input("Ingresa un numero: "))
# numero4 = int(input("Ingresa un numero: "))
# numero5 = int(input("Ingresa un numero: "))

# suma_numeros:int = numero1 + numero2 + numero3 + numero4 + numero5
# promedio:int = suma_numeros / 5

# print(f"La suma de los 5 numeros ingresados es {suma_numeros}")
# print(f"El promedio de los 5 numeros ingresados es {promedio}")

#Ejercicio 6

# numero = 0
# continuar = "S"
# contador = 0

# while continuar == "S" or continuar == "s": 
#     num_ingresado = int(input("Ingrese un numero a sumar: "))
#     continuar = input("¿Quiere continuar ? S/N: ")
    
#     contador += 1
#     numero += num_ingresado
#     promedio = numero / contador
    
    
    
    
# print(f"La suma total de los numeros ingresados es: {numero}")
# print(f"El promedio de todos los numeros que ingresó es: {promedio}")

#Ejercicio 7
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

    
# numero = 0
# producto = 1
# continuar = "S"


# while continuar == "S" or continuar == "s": 
#     num_ingresado = int(input("Ingrese un numero a sumar: "))
#     continuar = input("¿Quiere continuar ? S/N: ")
    
#     if num_ingresado >= 0:
#         numero += num_ingresado
#     if num_ingresado < 0:
#         producto *= num_ingresado
    
    
# print(f"La suma total de los numeros ingresados es: {numero}")
# print(f"El producto de los numeros negativos que ingresó es: {producto}")


#Ejercicio 8
# Ingresar 10 números enteros. 
# Determinar el máximo y el mínimo.

# numero = 0;
# contador = 0;
# mayor = 0;

# print("Vas a ingresar 10 numeros y voy a elegir el mayor de ellos.")

# while contador <= 10:
#     contador += 1
#     numero = int(input("Ingresa un numero: "))
    
#     if mayor < numero:
#         mayor = numero

# print(f"Tu numero mayor es: {mayor}")


# ANEXO

#Ejercicio 9
# Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

# print("Vas a ingresar como minimo 5 numeros y voy a hacer la suma y promedio de los mismos.")

# bandera = True;
# contador = 0;
# suma = 0;

# while contador <= 5 or contador > 5 and bandera:
#     contador += 1
#     numero = int(input("Por favor ingresa un numero: "))
    
#     suma += numero
    
#     promedio = suma / contador 
#     if contador >= 5:
#         continuar = input("¿ Quiere continuar ?(S/N): ")
#         if continuar == "n" or continuar == "N":
#             break;
    

# print(f"La suma de los numeros ingresados es: {suma}")
# print(f"El promedio de los numeros ingresados es: {promedio}")

# Ejercicio 10
# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

# print("Vas a ingresar como minimo 5 y como maximo 10 numeros."
#       "Voy a hacer la suma y promedio de los mismos.")


# contador = 0;
# suma = 0;

# while contador < 10:
#     contador += 1
#     numero = int(input("Por favor ingresa un numero: "))
    
#     suma += numero
    
#     promedio = suma / contador 
#     if contador >= 5 and contador <= 10:
#         continuar = input("¿ Quiere continuar ?(S/N): ")
#         if continuar == "n" or continuar == "N":
#             break;
    

# print(f"La suma de los numeros ingresados es: {suma}")
# print(f"El promedio de los numeros ingresados es: {promedio}")


# INTEGRADOR DE WHILE


print("Vas a ingresar todos los numeros que desees.");

bandera = True;
contador_general:int = 0;
contador_positivo:int = 0;
contador_negativo:int = 0;
suma_positivos:int = 0;
suma_negativos:int = 0;
mayor:int = 0;

while bandera:
    
    numero = int(input("Por favor ingresa un número (positivo o negativo): "));
    
    #numeros positivos
    if numero >= 0:
        contador_general += 1;
        contador_positivo += 1;
        suma_positivos += numero;
        continuar = input("¿ Quiere continuar ?(S/N): ");
        
        if mayor < numero:
            mayor = numero;
        if continuar == "n" or continuar == "N":
            break;
        
    #numeros negativos
    if numero < 0:
        contador_general += 1;
        contador_negativo += 1;
        suma_negativos += numero;
        promedio = suma_negativos / contador_negativo;
        continuar = input("¿ Quiere continuar ?(S/N): ");
        
        if continuar == "n" or continuar == "N":
            break;
    
    
    
#porcentaje numeros negativos sobre el total de numeros ingresados
porcentaje_numeros_negativos =  (contador_negativo * 100) / contador_general;
    

print(f"La suma de los numeros positivos ingresados es: {suma_positivos}");
print(f"La suma de los numeros positivos ingresados es: {suma_negativos}");
print(f"El promedio de los numeros negativos ingresados es: {promedio}");
print(f"Tu numero positivo mayor es: {mayor}")
print(f"El porcentaje de numeros negativos sobre el total de numeros ingresados es %{porcentaje_numeros_negativos}")

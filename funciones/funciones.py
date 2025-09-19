# Ejercicio 1
# Crear una función que le solicite al usuario,
# el ingreso de un número entero y lo retorne.

# def numero_int ()-> int:
    
#     valor_ingresado = int(input("Ingresá un número: "))
  
#     return valor_ingresado

# print(f"{numero_int()}")


# Ejercicio 2
# Crear una función que le solicite al usuario,
# el ingreso de un número flotante y lo retorne.

# def numero_float ()-> float:
    
#     valor_ingresado = float(input("Ingresá un número flotante (con decimal): "))
  
#     return valor_ingresado

# print(f"{numero_float()}")

# Ejercicio 3
# Crear una función que le solicite al usuario,
# el ingreso de una cadena y lo retorne.

# def numero_str ()-> str:
    
#     valor_ingresado = str(input("Ingresá una palabra o cadena de texto: "))
  
#     return valor_ingresado

# print(f"{numero_str()}")

# Ejercicio 4
# Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área. 


# def rectangulo(base: int, altura: int):
#     '''
#     '''
    
#     return base * altura

# base = int(input("Por favor ingrese la longitud de la base (b): "));
# altura = int(input("Por favor ingrese la longitud de la altura (h): "));
# print(f"El area del reactangulo es {rectangulo(base, altura)}mts2")

# Ejercicio 5
# Escribe una función que calcule el área de un círculo. 
# La función debe recibir el radio como parámetro y devolver el área.

# def circulo(radio: float, num_pi: float) -> float:
#     '''
#     '''
#     return (radio ** 2) * num_pi
# num_pi = 3.14
# radio = float(input("Por favor ingrese el radio del circulo: "));

# print(f"El area del circulo es {circulo(radio, num_pi)}m2")

# Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.


# Ejercicio 6
# Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.

# def num_impar_par (num_ingresado: int) -> None:
#     '''
#     Este programa verifica si el numero
#     ingresado por el usuario es
#     par o impar.
#     '''
#     if (num_ingresado % 2) == 0:
#         print("Es par")
#     else:
#         print("Es impar")
    
#     return num_impar_par

# num_ingresado = int(input("Ingresá un numero para saber si es par o impar: "))
# num_impar_par(num_ingresado)


#Ejercicio 7
# Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario.

# def num_impar_par (num_ingresado: int) -> None:
#     '''
#     Este programa verifica si el numero
#     ingresado por el usuario es
#     par o impar.
#     '''
#     if (num_ingresado % 2) == 0:
#         print("True")
#     else:
#         print("False")
    
#     return num_impar_par

# num_ingresado = int(input("Ingresá un numero para saber si es par o impar: "))
# print("Si el numero es par, se imprime True. Si el numero es impar, False.")
# num_impar_par(num_ingresado)

#Ejercicio 8
# Define una función que encuentre el máximo de tres números. 
# La función debe aceptar tres argumentos y devolver el número más grande.


# def num_mayor (num_1:int, num_2:int, num_3:int) -> int:
#     '''
#     Este programa verifica el numero mayor
#     de 3 valores ingresados.
#     '''
#     mayor = 0;
#     if num_1 > mayor:
#         mayor = num_1
#     if num_2 > mayor:
#         mayor = num_2
#     if num_3 > mayor:
#         mayor = num_3
        
#     return mayor;


# num_1 = int(input("Ingresa el 1er numero: "))
# num_2 = int(input("Ingresa el 2do numero: "))
# num_3 = int(input("Ingresa el 3er numero: "))

# print(f"El mayor numero de los 3 num ingresadoes es: {num_mayor(num_1,num_2,num_3)}")

#Ejercicio 9
# Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# def calcular_potencia (numero:int, potencia:int) -> int:
    
#     '''
#     El usuario ingresa un numero y una potencia
#     y se calcula dicha potencia.
#     '''
#     elevado = numero ** potencia
    
#     return elevado

# print("Vamos a calcular la potencia que vos elijas, del numero que coloques.")
# numero = int(input("Colocá el numero: "))
# potencia = int(input("Ahora coloca la potencia que queres elevar a tu numero: "))

# print(f"El {numero} elevado al {potencia} es igual a: {calcular_potencia(numero, potencia)}")

#Ejercicio 10
# Crear una función que reciba un número y retorne True 
# si el número es primo, False en caso contrario.

# def primo (number:int) -> None:
    
#     contador = 0
#     primo = True

#     for p in range(1, number + 1):
        
#         if (number % p) == 0:
#             contador += 1
            
#         if contador > 2:
#             primo = False
            
#     if primo == False:
#         print("False (no es primo)")
#     else:
#         print(f"True (es primo)")
        

# number = int(input("Ingrese un número: "))       
# print(f"El numero ingresado es {number}")
# primo(number)

# Ejercicio 11
# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
# muestre todos los números primos comprendidos entre 
# la unidad y un número ingresado como parámetro. 
# La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# import utils # importo una funcion con un for anidado para recorrer los nums primos

# def cantidad_primos () -> None:
#     '''
#     Esta funcion solicita ingresar un valor como para metro
#     Para devolver como resultado, los numeros primos hasta dicho valor ingresado
#     Y tambien cuenta la cantidad de numeros primos hasta ese limite.
#     '''
#     utils.nums_primos()

#Ejercicio 12
# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
# Por defecto es del 1 al 10.

# def tabla_multiplicar (num_ingresado:int ) -> int:
#     '''
#     Esta funcion es una tabla de multiplicar.
#     De base el multiplicador es 10, pero si el usuario
#     desea, puede modificar el mismo.
#     '''
#     if modificar == "S" or modificar == "s":
#         multiplicando_modif = int(input("Pone la cantidad de veces que queres multiplicar tu numero (el multiplicador)"))
#         for multiplicando_modif in range (1, multiplicando_modif + 1): #aca se ejecuta hasta el numero que ponga el usuario
#             multiplo = num_ingresado * multiplicando_modif 
#             print(f"{multiplicando_modif} x {num_ingresado} = {multiplo}"); 
                       
#     else:
#         for i in range (1, 11): #aca se ejecuta hasta x 10
#                 multiplo = num_ingresado * i
#                 print(f"{i} x {num_ingresado} = {multiplo}");
#     # no utilizo return dado que ya me devuelve un print en ambas condiciones.

# print("Bienvenidx. Esto es una tabla de multiplicar.")
# print("Hay 2 valores para ingresar.")
# print("Primero, el  mutiplicando")
# print("Segundo, el multiplicador")
# num_ingresado = int(input("Por favor ingresa el numero a multiplicar (multiplicando): "))
# modificar = input("Queres modificar el multiplicador (por defecto es 10) ? S/N: ")
# tabla_multiplicar(num_ingresado)

# Ejercicio 13
# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. 
# Agregar validaciones.
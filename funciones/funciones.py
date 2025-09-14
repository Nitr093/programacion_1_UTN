# Crear una función que le solicite al usuario,
# el ingreso de un número entero y lo retorne.

# def numero_int ()-> int:
    
#     valor_ingresado = int(input("Ingresá un número: "))
  
#     return valor_ingresado

# print(f"{numero_int()}")


# # Crear una función que le solicite al usuario,
# # el ingreso de un número flotante y lo retorne.

# def numero_float ()-> float:
    
#     valor_ingresado = float(input("Ingresá un número flotante (con decimal): "))
  
#     return valor_ingresado

# print(f"{numero_float()}")


# # Crear una función que le solicite al usuario,
# # el ingreso de un número flotante y lo retorne.

# def numero_str ()-> str:
    
#     valor_ingresado = str(input("Ingresá una palabra o cadena de texto: "))
  
#     return valor_ingresado

# print(f"{numero_str()}")


# Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área. 


# def rectangulo(base: int, altura: int):
#     '''
#     '''
    
#     return base * altura

# base = int(input("Por favor ingrese la longitud de la base (b): "));
# altura = int(input("Por favor ingrese la longitud de la altura (h): "));
# print(f"El area del reactangulo es {rectangulo(base, altura)}mts2")


# Escribe una función que calcule el área de un círculo. 
# La función debe recibir el radio como parámetro y devolver el área.

def circulo(radio: float, num_pi: float) -> float:
    '''
    '''
    return (radio ** 2) * num_pi
num_pi = 3.14
radio = float(input("Por favor ingrese el radio del circulo: "));

print(f"El area del circulo es {circulo(radio, num_pi)}m2")

# Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.




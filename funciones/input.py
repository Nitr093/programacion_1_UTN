from validate import *

def get_int (mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    '''
    Este programa solicita un ENTERO al usuario.
    
    EL minimo y el maximo, lo asigna el usuario,
    
    Al igual que la cantidad de reintentos.
    
    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    
    mínimo: valor mínimo admitido (inclusive)
    
    máximo: valor máximo admitido (inclusive)
    
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
    '''
    
    print(mensaje)
    
    valor = int(input("Ingresa un numero entero: "))
       
    validate_number(valor, mensaje_error, minimo, maximo, reintentos)
        
        
def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:

    '''
    Este programa solicita un FLOTANTE al usuario.
    
    EL minimo y el maximo, lo asigna el usuario,
    
    Al igual que la cantidad de reintentos.
    
    mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    
    mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
    
    mínimo: valor mínimo admitido (inclusive)
    
    máximo: valor máximo admitido (inclusive)
    
    reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

    '''

    print(mensaje)

    valor = float(input("Ingresa un numero flotante: "))
       
    validate_number(valor, mensaje_error, minimo, maximo, reintentos)
        
        
def get_string(longitud: int) -> str|None:
    '''
    Esta funcion validará la longitud de 
    la cadena ingresada dado el parámetro recibido.
    Es decir, la longitud será el maximo permitido
    de caracteres.
    '''
    
    texto = input("Ingrese una cadena de texto: ")
    
    return validate_length(texto, longitud)
    


def validate_number(valor: float|int, mensaje_error:str, minimo:int|float, maximo:int|float, reintentos:int) -> None:
    '''
    probando
    '''
    
    x = 0
    if type(valor) ==  int:
    
        while x < reintentos:
            x += 1
            if minimo <= valor and maximo >= valor:
                print("Su número esta dentro del rango")
                break
            else:
                print(mensaje_error)            
                valor = int(input("Ingresá un número: "))

        if x == reintentos:
            print("Llegaste al limite de reintentos")
            
    if type(valor) ==  float:
    
        while x < reintentos:
            x += 1
            if minimo <= valor and maximo >= valor:
                print("Su numero esta dentro del rango")
                break
            else:
                print(mensaje_error)            
                valor = float(input("Ingresa un numero: "))

        if x == reintentos:
            print("Llegaste al limite de reintentos")


def validate_length(texto:str, longitud:int) -> None:

    '''
    Esta funcion valida la longitud de 
    una cadena de texto.
    '''
    
    bandera = True
    
    while bandera:
        if len(texto) <= longitud:
            bandera = False 
            return texto                  
        else:
            print("ER#0R_*")
            texto = input("Ingrese una cadena de texto: ")
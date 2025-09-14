#Ejercicio 1
#Pedir el ingreso de una clave. 
#Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

# print(f"Vamos a validar si la clave es correcta")

# bandera:bool = True;
# clave:str = "programacion"
# nombre_usuario:str = input("Antes que todo, coloque su nombre, por favor: ")

# while bandera:
#     clave_usuario = input("Introduzca su contraseña: ")
#     if clave_usuario == clave:        
#         bandera = False;
#     else:
#         print(f"Acceso denegado. Intentá de nuevo {nombre_usuario}")

# print(f"Bienvenido {nombre_usuario} !")


#Ejercicio 2
# Pedir el ingreso de una clave. 
# Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

# print(f"Vamos a validar si la clave es correcta")

# bandera:bool = True;
# clave:str = "programacion"
# nombre_usuario:str = input("Antes que todo, coloque su nombre, por favor: ")
# intentos:int = 0;

# while intentos <= 3 and bandera:
#     clave_usuario = input("Introduzca su contraseña: ")
#     if clave_usuario == clave:
#         print(f"Bienvenido {nombre_usuario} !")          
#         bandera = False;
#     else:
#         print(f"Acceso denegado. Intentá de nuevo {nombre_usuario}")
#         print(f"Te quedan {3 - intentos} intentos")
#         intentos += 1

# print("Este programa finalizó.")

#Ejercicio 3
# Pedir al usuario el ingreso de una nota. 
# La misma debe estar comprendida entre 1 y 10 inclusive.


# bandera:bool = True;

# while bandera:
#     numero = int(input("Ingresa un numero del 1 al 10: "))
#     if numero >= 1 and numero <= 10:
#         print(f"El numero que pusiste es: {numero}")    
#         bandera = False;
#     else:
#         print(f"Solo se permiten numeros entre el 1 y el 10. Volvé a ingresarlo por favor.")  
        
# print("Este programa finalizó.")

#Ejercicio 4
# Solicitarle al usuario el ingreso de un color. 
# Validar que el mismo sea Rojo, Verde o Azul.


# bandera:bool = True;

# while bandera:
#     color:str = input("Ingresa un color por favor: ")
    
#     if color == "Rojo" or color == "Verde" or color == "Azul":
#         print(f"Bien, me gusta el color {color} !")
#         bandera:bool = False;
#     else:
#         print("Ese color no me agrada para nada.")
#         print("Pone otro color, gracias!")
        
# print("Este programa finalizó.")


#INTEGRADOR VALIDACIONES
#Una empresa dedicada a la toma de datos para realizar estadísticas y censos, 
#nos pide realizar la carga y validación de datos.


bandera:bool = True;
print("Vamos a solicitarle algunos datos para validar.")

while bandera:
    apellido:str = input("Su apellido: ")
    edad:int = int(input("Ponga su edad: ")) #Edad, entre 18 y 90 años inclusive.
    estado_civil:str = input("Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”: ")
    num_legajo:int = int(input("Número de legajo: ")) # valor numérico de 4 cifras, sin ceros a la izquierda.
    
    if edad <= 90 and edad >= 18 and num_legajo >= 1000 and num_legajo < 10000:
        print("-")
        print(f"Bienvenido {apellido}")
        print(f"Su edad es {edad}")
        print(f"Estado Civil {estado_civil}")
        print(f"Su numero legajo es {num_legajo}")
        print("-")
        bandera = False;
    while edad < 18 or edad > 90:
        print(f"Solo se aceptan personas mayores de 18 años hasta 90 años inclusive. Vos tenes {edad} años")
        edad:int = int(input("Ponga su edad: "))
        bandera = False;
        if edad <= 90 and edad >= 18 and num_legajo >= 1000 and num_legajo < 10000:
            print("-")
            print(f"Bienvenido {apellido}")
            print(f"Su edad es {edad}")
            print(f"Estado Civil {estado_civil}")
            print(f"Su numero legajo es {num_legajo}")
            print("-")
        bandera = False;
    while num_legajo < 1000 or num_legajo > 9999:
        print(f"El numero de legajo debe ser de 4 cifras sin 0 a su izquierda. Vos tenes {num_legajo} numero de legajo")
        num_legajo:int = int(input("Número de legajo: "))
        bandera = False;
        if edad <= 90 and edad >= 18 and num_legajo >= 1000 and num_legajo < 10000:
            print("-")
            print(f"Bienvenido {apellido}")
            print(f"Su edad es {edad}")
            print(f"Estado Civil {estado_civil}")
            print(f"Su numero legajo es {num_legajo}")
            print("-")
        bandera = False;

print("Finalizó el programa")
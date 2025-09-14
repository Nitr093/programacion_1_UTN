#El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.

print("Bienvenido.")
print("Con este programa, vamos a requerir datos de 10 empleados.")
print("Vamos a validar y devolver ciertos datos.")
print("Vamos a por ello !")
contador = 1;
empl_masc_mayor = 0;
cant_empl_masc = 0;
cant_empl_nofem_noia = 0;
mayor = 0;

while contador <= 10:
    print("-")
    print(f"Empleado N° {contador}")
    nombre = input("Ponga su nombre: ")
    edad = input("Ponga su edad: ")
    genero = input("Ponga su género(Masculino, Femenino, Otro): ")
    tecnologia = input("Ponga su tecnología(IA, RV/RA, IOT): ")
    contador += 1
    if nombre == "" or edad == "" or genero == "" or tecnologia == "":
        print("No podes dejar ingresos en blanco.")
        break;
    
    edad = int(edad) #casteo a int la variable edad para que pueda utilizar como numero. 
                     #Originalmente lo dejo en str para que me pueda validar con el if de la lina 16.
    
    while edad < 18 and (genero != "masculino" or genero != "Masculino"):
        print(f"LOS MENORES DE 18 AÑOS NO PUEDEN PARTICIPAR.")       
        empl_masc_mayor += 1;
        break;
        
    
    while (genero == "masculino" or genero == "Masculino") and (tecnologia == "IOT" or tecnologia == "IA") and (edad <= 50 and edad >= 25):
        cant_empl_masc += 1;
        break;
        
        
    while genero != "Femenino" and genero != "femenino" and tecnologia != "IA" and tecnologia != "ia":
        if edad >= 33 and edad <= 40:
            cant_empl_nofem_noia += 1;
            break;   
        else:
            break;
        
    while mayor < edad:
        mayor = edad
        nombre_mayor = nombre
        tecnologia_mayor = tecnologia
        break;
                
            
            

porcentaje = (cant_empl_nofem_noia * 100) / contador    #Porcentaje de empleados que NO votaron por IA

if contador > 1:
    print("-")
    print(f"El porcentaje de empleados que no votaron por IA (no femeninos y edad entre 33 y 40 años): % {porcentaje} sobre el total de {contador} empleados")
    print(f"La cantidad de empleados que votaron por IOT/IA, genero masculino y edad entre 25 y 50años (inclusive) son: {cant_empl_masc}")
    print(f"El masculino de mayor edad tiene se llama {nombre_mayor}, tiene {mayor} años, y la tecnologia que eligió fue {tecnologia_mayor} ")
    print("-")



# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).

# Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.

# Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.
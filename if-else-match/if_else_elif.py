import random

# Ejercicio 1
print("EJERCICIO 1")
altura:int = int(input("Por favor ponga su altura en centimetros (num entero): "))
print(f"Su altura es {altura}cm")

if altura < 160:
    print(f"Usted debe jugar en la posicion Base")
elif altura <= 179:
    print(f"Usted debe jugar en la posicion Escolta")
elif altura <= 199:
    print(f"Usted debe jugar en la posicion Alero")
else:
    print(f"Usted debe jugar en la posicion Pivot")
    

# Ejercicio 2
print("EJERCICIO 2")
nota_directa = int(random.randint(1, 10))
print(f"El numero aleatorio generado es {nota_directa}")

if nota_directa >= 6:
    print(f"Promoción directa, la nota es {nota_directa}");
elif nota_directa >= 4:
    print(f"Aprobado, la nota es {nota_directa}");
else:
    print(f"Desaprobado, la nota es {nota_directa}");

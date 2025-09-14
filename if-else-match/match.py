estacion = input("Ponga la estacion del año en la que quiere viajar: ");
destino = input("Elija su destino (Bariloche, Mar del Plata, Cataratas):");


match estacion:
    case "verano":
        if destino == "Mar del plata" or destino == "Cataratas":
            print(f"Puede viajar");
        else:
            print(f"No puede viajar");        
    case "invierno":
        if destino == "Bariloche":
            print(f"Puede viajar")
        else:
            print(f"No puede viajar")
    case "primavera":
        if destino == "Bariloche":
            print(f"No puede viajar")
        else:
            print(f"Puede viajar")        
    case _:
        print(f"Puede viajar")
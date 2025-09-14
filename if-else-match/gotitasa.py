m3_consumidos = float(input("Ponga los m3 que ud. haya consumido: "));
tipo_cliente = input("Tipo de cliente, (que puede ser: Residencial, Comercial o Industrial): ");


cargo_fijo:int = 7000;
costo_m3:int = 200;
bonificacion:int = 0;
bonificacion_adicional:int = 0;
recargo:int = 0;
IVA:int = 1.21;

total_consumido_sin_bonif_sin_imp:int = cargo_fijo + (costo_m3 * m3_consumidos) 
# Genero esta variable para calcular el consumo total sin bonif y recargo, para hacer el descuento, 
# SI ES QUE APLICA, en el usuario residencial con un gasto menor a 35.000.

match tipo_cliente:
    case "residencial":
        if m3_consumidos <= 30:
            bonificacion:int = 10
            costo_m3_modif:int = costo_m3 - (costo_m3 * (bonificacion /100));
            # Al valor original de costo (200) le RESTO el resultado del producto entre el costo y la BONIFICACION.-
        elif m3_consumidos >= 80:
            recargo:int = 15
            costo_m3_modif:int = costo_m3 + (costo_m3 * (recargo /100));
            # Al valor original de costo (200) le SUMO el resultado del producto entre el costo y el RECARGO.-
        else:
            costo_m3_modif:int = 0;
            recargo:int = 0
    case "comercial":
        if m3_consumidos < 50:
            recargo:int = 5
            costo_m3_modif:int = costo_m3 + (costo_m3 * (recargo /100));
        elif m3_consumidos > 150 and m3_consumidos < 300:
            bonificacion:int = 8
            costo_m3_modif:int = costo_m3 - (costo_m3 * (bonificacion /100));
        elif m3_consumidos >= 300:
            bonificacion:int = 12
            costo_m3_modif:int = costo_m3 - (costo_m3 * (bonificacion /100));
        else:
            costo_m3_modif:int = 0;
            recargo:int = 0
    case "industrial":
        if m3_consumidos < 200:
            recargo:int = 10
            costo_m3_modif:int = costo_m3 + (costo_m3 * (recargo /100));
        elif m3_consumidos >= 500 and m3_consumidos < 1000:
            bonificacion:int = 20
            costo_m3_modif:int = costo_m3 - (costo_m3 * (bonificacion /100));
        elif m3_consumidos >= 1000:
            bonificacion:int = 30
            costo_m3_modif:int = costo_m3 - (costo_m3 * (bonificacion /100));
        else:
            costo_m3_modif:int = 0;
            recargo:int = 0
        

total_m3_consumido:int = (m3_consumidos * costo_m3_modif)
total_consumido_con_iva:int = (total_m3_consumido + cargo_fijo) * IVA;


print(f"El cargo fijo es de $7000")
print(f"El costo por m3 sin bonificacion ni recargo es de $200")


if tipo_cliente == "residencial" and total_consumido_sin_bonif_sin_imp < 35000:
    bonificacion_adicional:int = 5
    total_consumido_con_iva:int = (
                                   (cargo_fijo + 
                                     (m3_consumidos * 
                                      (costo_m3 - (costo_m3 *((bonificacion + bonificacion_adicional) / 100)
                                        )
                                       )
                                      )
                                     )
                                    ) * IVA ;
    costo_m3_modif:int = costo_m3 - (costo_m3 *((bonificacion + bonificacion_adicional) / 100))
    total_m3_consumido:int = m3_consumidos * costo_m3_modif;
    
   
    
    print(f"Ud tiene una bonificacion adicional del % {bonificacion_adicional}, por lo que en total ud tiene una bonificacion del % {bonificacion_adicional + bonificacion}");

print(f"Ud. tiene una bonificacion de: % {bonificacion + bonificacion_adicional}")
print(f"Ud. tiene un recargo de: % {recargo}")
print(f"Por lo que su costo fijo por m3 será de ${costo_m3_modif}")
print(f"El costo de m3 consumido por ud es {total_m3_consumido}")
print(f"El total de su factura es {total_consumido_con_iva}")


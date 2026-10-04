precio_compra = float(input("Introduce el precio de la compra (€): "))

if precio_compra >= 300:
    porcentaje_descuento = 15
elif precio_compra >= 100:
    porcentaje_descuento = 10
else:
    porcentaje_descuento = 0

descuento = precio_compra * porcentaje_descuento / 100
precio_final = precio_compra - descuento

print(f"Precio de la compra: {precio_compra:.2f} €")
print(f"Descuento aplicado: {porcentaje_descuento}%")
print(f"Importe del descuento: {descuento:.2f} €")
print(f"Precio final: {precio_final:.2f} €")
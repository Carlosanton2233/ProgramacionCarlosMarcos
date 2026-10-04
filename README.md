# ProgramacionCarlosMarcos
1. Análisis
Enunciado
Una tienda aplica un descuento del 10 % a partir de 100 € de compra y del 15 % a partir de 300 €.
Entradas
Precio total de la compra en euros. 
Salidas
Descuento aplicado. 
Importe del descuento. 
Precio final de la compra después de aplicar el descuento. 
Restricciones
El precio de la compra debe ser un número mayor o igual que 0. 
Si la compra es menor de 100 €, no se aplica ningún descuento. 
Si la compra es igual o superior a 100 € y menor de 300 €, se aplica un descuento del 10 %. 
Si la compra es igual o superior a 300 €, se aplica un descuento del 15 %. 
En los límites, 100 € recibe el 10 % y 300 € recibe el 15 %.
2. Diseño
2.1 Pseudocódigo

INICIO

    Leer precio_compra

    SI precio_compra >= 300 ENTONCES
        porcentaje_descuento ← 15
    SINO SI precio_compra >= 100 ENTONCES
        porcentaje_descuento ← 10
    SINO
        porcentaje_descuento ← 0
    FIN SI

    descuento ← precio_compra * porcentaje_descuento / 100
    precio_final ← precio_compra - descuento

    Mostrar precio_compra
    Mostrar porcentaje_descuento
    Mostrar descuento
    Mostrar precio_final

FIN

2.2 Ordinograma
Puedes representarlo así en el diagrama de flujo:
```text
+-----------------------------------+
|               INICIO              |
+-----------------------------------+
                  |
                  v
+-----------------------------------+
|        Leer precio_compra         |
+-----------------------------------+
                  |
                  v
        /-------------------\
       /  ¿Precio >= 300?    \
       \                     /
        \-------------------/
          /               \
       SÍ/                 \NO
        v                   v
+---------------+   /-------------------\
|  Descuento    |  /   ¿Precio >= 100?   \
|    = 15%      |  \                     /
+---------------+   \-------------------/
        |             /               \
        |          SÍ/                 \NO
        |           v                   v
        |   +---------------+   +---------------+
        |   |  Descuento    |   |  Descuento    |
        |   |    = 10%      |   |    = 0%       |
        |   +---------------+   +---------------+
        |           |                   |
        +-----------+-------------------+
                  |
                  v
+-----------------------------------+
|        Calcular descuento         |
|  descuento = precio * porcentaje  |
|               / 100               |
+-----------------------------------+
                  |
                  v
+-----------------------------------+
|       Calcular precio final       |
|    precio_final = precio -        |
|             descuento             |
+-----------------------------------+
                  |
                  v
+-----------------------------------+
|         Mostrar resultados        |
+-----------------------------------+
                  |
                  v
+-----------------------------------+
|                FIN                |
+-----------------------------------+


3. Codificación en Python
Archivo: d3_descuento.py

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


4. Pruebas
Se realizan seis casos de prueba, incluyendo los tres límites que pide expresamente la práctica.

Nº	Precio de compra	Descuento	Importe descuento	Precio final
1	50,00 €	0 %	0,00 €	50,00 €
2	99,99 €	0 %	0,00 €	99,99 €
3	100,00 €	10 %	10,00 €	90,00 €
4	150,00 €	10 %	15,00 €	135,00 €
5	299,99 €	10 %	30,00 €	269,99 €
6	300,00 €	15 %	45,00 €	255,00 €
7	500,00 €	15 %	75,00 €	425,00 €


Comprobación de los límites
99,99 €
Descuento: 0 %
Precio final: 99,99 €

Correcto, porque todavía no llega a 100 €.
100 €
Descuento: 10 %
Importe descuento: 10 €
Precio final: 90 €

Correcto, porque a partir de 100 € se aplica el 10 %.
300 €
Descuento: 15 %
Importe descuento: 45 €
Precio final: 255 €
Correcto, porque a partir de 300 € se aplica el 15 %.


5. Documentación
Descripción del programa
El programa solicita al usuario el precio de una compra y determina el porcentaje de descuento que corresponde según el importe. Para compras inferiores a 100 € no se aplica descuento. Para compras desde 100 € hasta menos de 300 € se aplica un 10 %, mientras que para compras de 300 € o más se aplica un 15 %.
Después de determinar el porcentaje, el programa calcula el importe del descuento y lo resta al precio original para obtener el precio final.

Resultado
La solución permite pasar desde el enunciado inicial → análisis → pseudocódigo → ordinograma → código Python → pruebas, cubriendo las fases solicitadas en la práctica D3. 

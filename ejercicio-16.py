# Ejercicio 16: Calculadora de descuentos
def descuento_producto():
    precio = float(input("Ingrese el precio del producto: "))
    if precio < 50:
        descuento = 0
    elif precio <= 100:
        descuento = 0.05 * precio
    else:
        descuento = 0.10 * precio
    print(f"El descuento es {descuento}.")
    
descuento_producto()
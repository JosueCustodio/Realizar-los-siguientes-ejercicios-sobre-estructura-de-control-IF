# Ejercicio 5: Descuento por edad
def descuento_por_edad():
    edad = int(input("Ingrese su edad: "))
    if edad > 60:
        print("Aplica para el descuento del 50%.")
    else:
        print("No aplica para el descuento.")

descuento_por_edad()
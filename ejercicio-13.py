# Ejercicio 13: Verificación de año bisiesto
def es_bisiesto():
    anio = int(input("Ingrese un año: "))
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("El año es bisiesto.")
    else:
        print("El año no es bisiesto.")

es_bisiesto()
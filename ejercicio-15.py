# Ejercicio 15: Comparación de tres longitudes
def es_triangulo():
    a, b, c = sorted([float(input("Ingrese un lado: ")) for _ in range(3)])
    if a + b > c:
        print("Pueden formar un triángulo.")
    else:
        print("No pueden formar un triángulo.")

es_triangulo()
# Ejercicio 12: Clasificación de números
def clasificacion_numeros():
    nums = [int(input("Ingrese un número: ")) for _ in range(3)]
    if all(n > 0 for n in nums):
        print("Todos son positivos.")
    elif all(n < 0 for n in nums):
        print("Todos son negativos.")
    elif any(n == 0 for n in nums):
        print("Hay al menos un cero.")
    else:
        print("Los números son mixtos.")

clasificacion_numeros()
# Ejercicio 9: Mayor entre tres números
def mayor_de_tres():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    print(f"El mayor es {max(num1, num2, num3)}.")

mayor_de_tres()
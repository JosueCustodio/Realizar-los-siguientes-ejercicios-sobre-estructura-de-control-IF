# Ejercicio 2: Número par o impar
def par_o_impar():
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

par_o_impar()
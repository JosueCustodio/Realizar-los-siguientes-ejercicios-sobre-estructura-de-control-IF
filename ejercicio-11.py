# Ejercicio 11: Cálculo de impuestos
def calculo_impuestos():
    salario = float(input("Ingrese su salario mensual: "))
    if salario < 10000:
        impuesto = 0
    elif salario <= 30000:
        impuesto = 0.10 * salario
    else:
        impuesto = 0.20 * salario
    print(f"El impuesto a pagar es {impuesto}.")

calculo_impuestos()
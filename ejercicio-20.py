# Ejercicio 20: Clasificación de IMC
def clasificar_imc():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    
    print(f"Su IMC es {imc:.2f}")
    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc <= 24.9:
        print("Normal")
    elif 25 <= imc <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidad")

clasificar_imc()
# Ejercicio 7: Día de la semana
def dia_de_la_semana():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    num = int(input("Ingrese un número del 1 al 7: "))
    if 1 <= num <= 7:
        print(f"El día de la semana es {dias[num-1]}.")
    else:
        print("Número fuera de rango.")

dia_de_la_semana()
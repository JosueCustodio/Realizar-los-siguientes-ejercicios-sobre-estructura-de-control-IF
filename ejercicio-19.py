# Ejercicio 19: Conversión de horas a turnos
def convertir_hora():
    hora = int(input("Ingrese la hora (0-23): "))
    if 6 <= hora <= 11:
        print("Mañana")
    elif 12 <= hora <= 17:
        print("Tarde")
    elif 18 <= hora <= 23:
        print("Noche")
    elif 0 <= hora <= 5:
        print("Madrugada")
    else:
        print("Hora no válida.")

convertir_hora()
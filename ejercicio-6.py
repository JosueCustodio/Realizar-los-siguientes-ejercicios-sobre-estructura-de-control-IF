# Ejercicio 6: Calificación aprobatoria
def calificacion_aprobatoria():
    nota = int(input("Ingrese su calificación (0-100): "))
    if nota >= 60:
        print("Aprobado.")
    else:
        print("Reprobado.")

calificacion_aprobatoria()
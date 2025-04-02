# Ejercicio 14: Conversión de calificaciones
def conversion_calificacion():
    nota = int(input("Ingrese su calificación (0-100): "))
    if nota >= 90:
        print("A")
    elif nota >= 80:
        print("B")
    elif nota >= 70:
        print("C")
    elif nota >= 60:
        print("D")
    else:
        print("F")

conversion_calificacion()
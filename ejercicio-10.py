# Ejercicio 10: Clasificación de ángulos
def clasificacion_angulo():
    angulo = int(input("Ingrese el ángulo en grados: "))
    if angulo < 90:
        print("Ángulo agudo.")
    elif angulo == 90:
        print("Ángulo recto.")
    elif angulo < 180:
        print("Ángulo obtuso.")
    else:
        print("Ángulo llano.")

clasificacion_angulo()
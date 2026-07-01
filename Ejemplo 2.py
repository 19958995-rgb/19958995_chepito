# Ingresa tu calificacion
calificacion = int(input("Introduce la calificación numérica (0-100): "))

# verificamos que el numero sea correcto
if calificacion < 0 or calificacion > 10:
    print("Error: La calificación debe estar entre 0 y 100")
else:
    # revisamos la calificación para asignar la letra correspondiente
    if calificacion >= 9:
        letra = "A"
    elif calificacion >= 8:
        letra = "B"
    elif calificacion >= 7:
        letra = "C"
    elif calificacion >= 6:
        letra = "D"
    else:
        letra = "F"

    #resultado
    print(f"Tu calificación es: {letra}")
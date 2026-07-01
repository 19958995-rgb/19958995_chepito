lado1, lado2, lado3 = 5, 5, 5

# Validación de existencia
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Es un triángulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo Isósceles.")
    else:
        print("Es un triángulo Escaleno.")
else:
    print("Los lados proporcionados no forman un triángulo válido.")
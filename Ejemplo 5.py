# pedimos el valor de cada lado del triángulo al usuario
lado1 = float(input("Introduce la longitud del primer lado: "))
lado2 = float(input("Introduce la longitud del segundo lado: "))
lado3 = float(input("Introduce la longitud del tercer lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("¡Sí se puede formar un triángulo con esos lados! ")
else:
    print("No es posible formar un triángulo con esas medidas. ")
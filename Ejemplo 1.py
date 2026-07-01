# Solicitamos al usuario que ingrese un número
numero = int(input("Introduce un número entero: "))

# Verificamos si el residuo de dividir el número entre 2 es cero
if numero % 2 == 0:
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")
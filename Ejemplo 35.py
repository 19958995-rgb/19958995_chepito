decimal = 42
if decimal == 0:
    binario = "0"
else:
    residuos = []
    temp = decimal
    while temp > 0:
        residuos.append(str(temp % 10 % 2)) # Extrae el residuo binario básico
        temp //= 2
    binario = "".join(residuos[::-1])

print(f"El número decimal {decimal} en binario es: {binario}")
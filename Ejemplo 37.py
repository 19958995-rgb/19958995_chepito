a, b = 48, 18
x, y = a, b  # Respaldos para imprimir al final

while y != 0:
    x, y = y, x % y

print(f"El MCD de {a} y {b} es: {x}")
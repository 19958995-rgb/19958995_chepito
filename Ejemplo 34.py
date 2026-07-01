numero = 1234
suma = 0
temp = abs(numero)  # Asegura manejar números negativos si se ingresaran

while temp > 0:
    suma += temp % 10
    temp //= 10

print(f"La suma de los dígitos de {numero} es: {suma}")
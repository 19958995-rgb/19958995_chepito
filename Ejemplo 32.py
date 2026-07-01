numero = 17
es_primo = True

if numero < 2:
    es_primo = False
else:
    # Optimización: comprobar hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

print(f"¿El número {numero} es primo?: {es_primo}")
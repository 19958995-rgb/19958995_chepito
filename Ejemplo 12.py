numeros = [23, 45, 12, 67, 34, 89, 21]

# Alternativa manual para no usar max() y min() directamente si se quiere evaluar lógica
mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print(f"Mayor: {mayor}, Menor: {menor}")
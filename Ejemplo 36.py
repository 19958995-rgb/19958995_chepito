texto = "Anita lava la tina"
# Limpiar el texto eliminando espacios y convirtiendo a minúsculas
texto_limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())

es_palindromo = True
i = 0
j = len(texto_limpio) - 1

while i < j:
    if texto_limpio[i] != texto_limpio[j]:
        es_palindromo = False
        break
    i += 1
    j -= 1

print(f"¿La frase '{texto}' es un palíndromo?: {es_palindromo}")
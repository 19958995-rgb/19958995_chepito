# 1. El usuario ingresa el texto, la vocal a buscar y su valor numérico
texto = input().lower()
vocal_buscar = input().lower()
valor = int(input())

# 2. Se cuenta cuántas veces aparece la vocal seleccionada en el texto
conteo = texto.count(vocal_buscar)

# 3. Se multiplica el total de vocales encontradas por el valor asignado
resultado = conteo * valor

# 4. Se muestra el resultado final en la terminal
print(f"{vocal_buscar.upper()}: {resultado}")
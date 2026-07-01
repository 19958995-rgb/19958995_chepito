texto = "programacion en python"
conteo = {}

for caracter in texto:
    if caracter != " ": 
        conteo[caracter] = conteo.get(caracter, 0) + 1

print("Frecuencia de caracteres:", conteo)
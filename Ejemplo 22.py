texto = "hola mundo hola python mundo mundo"
palabras = texto.split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencias)
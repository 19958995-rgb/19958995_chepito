texto = """Python es un lenguaje de programación. Es muy popular en la actualidad. Python es versátil."""
palabras = [p.strip(".,¡!¿?").lower() for p in texto.split()]
oraciones = [o.strip() for o in texto.split(".") if o.strip()]

total_palabras = len(palabras)

frecuencias = {}
for p in palabras:
    frecuencias[p] = frecuencias.get(p, 0) + 1
palabra_mas_comun = max(frecuencias, key=frecuencias.get)

longitud_promedio = sum(len(p) for p in palabras) / total_palabras if total_palabras else 0

print(f"Total de palabras: {total_palabras}")
print(f"Palabra más frecuente: '{palabra_mas_comun}' ({frecuencias[palabra_mas_comun]} veces)")
print(f"Longitud promedio de palabras: {longitud_promedio:.2f} caracteres")
print(f"Total de oraciones encontradas: {len(oraciones)}")
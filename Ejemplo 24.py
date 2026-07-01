traducciones = {"hola": "hello", "mundo": "world", "python": "python"}

palabra_buscar = "hola"
print(f"Traducción de '{palabra_buscar}': {traducciones.get(palabra_buscar, 'No encontrada')}")
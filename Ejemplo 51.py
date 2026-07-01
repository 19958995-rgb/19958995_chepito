mensaje = "Hola Mundo"
desplazamiento = 3
resultado = ""

for caracter in mensaje:
    if caracter.isalpha():
        base = ord('A') if caracter.isupper() else ord('a')
        # Calcular nueva posición alfabética rotativa
        nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
        resultado += nuevo_caracter
    else:
        resultado += caracter

print(f"Mensaje cifrado: {resultado}")
filas = 4

for i in range(1, filas + 1):
    # Espacios en blanco a la izquierda
    espacios = " " * (filas - i)
    
    # Secuencia ascendente
    ascendente = "".join(str(x) for x in range(1, i + 1))
    
    # Secuencia descendente
    descendente = "".join(str(x) for x in range(i - 1, 0, -1))
    
    print(espacios + ascendente + descendente)
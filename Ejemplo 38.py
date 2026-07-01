inicio, fin = 10, 50

def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primos_en_rango = [x for x in range(inicio, fin + 1) if es_primo(x)]
print(f"Números primos entre {inicio} y {fin}: {primos_en_rango}")
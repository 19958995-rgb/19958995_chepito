# pedimos al usuario hasta qué número desea sumar
limite = int(input("¿Hasta qué número natural deseas sumar?: "))

# este será el acumulador
suma_total = 0

# El bucle va desde 1 hasta el número ingresado por el usuario (+ 1 para incluirlo)
for i in range(1, limite + 1):
    suma_total += i

# resultado final
print(f"La suma de los primeros {limite} números naturales es: {suma_total}")
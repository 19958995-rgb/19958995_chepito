numero = int(input())
factorial = 1

if numero < 0:
    print("Error")
else:
    while numero > 0:
        factorial *= numero
        numero -= 1
    print(factorial)
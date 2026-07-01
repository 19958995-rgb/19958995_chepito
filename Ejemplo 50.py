import random

def jugar_adivina():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡He pensado un número entre 1 y 100!")

    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("Muy bajo.")
        elif intento > numero_secreto:
            print("Muy alto.")
        else:
            print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
            break

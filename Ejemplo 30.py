jugador1 = "piedra"
jugador2 = "tijeras"

opciones_validas = ["piedra", "papel", "tijeras"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Una o ambas opciones no son válidas.")
elif jugador1 == jugador2:
    print("¡Empate!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijeras" and jugador2 == "papel"):
    print("¡Gana el Jugador 1!")
else:
    print("¡Gana el Jugador 2!")
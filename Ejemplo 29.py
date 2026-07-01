peso = 70  # kg
altura = 1.75  # metros

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Tu IMC es {imc:.2f} y tu clasificación es: {clasificacion}")
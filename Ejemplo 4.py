# pedimos los datos al usuario
num1 = float(input("Introduce el primer número: "))
operador = input("Introduce el operador (+, -, *, /): ")
num2 = float(input("Introduce el segundo número: "))

# Revisamos el operador para que no cometa errores
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2 if num2 != 0 else "Error: División por cero"
else:
    resultado = "Operador no válido"

# resultado final 
print(f"Resultado: {resultado}")
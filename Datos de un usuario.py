# datos personales del Usuario
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
mail = input("Ingrese su correo: ")

# Validación de la edad
while True:
    try:
        age = input("Ingrese su edad: ")
        age = int(age) 
        if 0 <= age <= 120:
            break  # Si la edad es correcta pasa a la siguiente pregunta
        else:
            print("Error: Ingrese una edad válida (entre 0 y 120 años).")
    except ValueError:
        print("Error: Debe ingresar un número entero para la edad.")

sexo = input("Ingrese su sexo: ")
phone = input("Ingrese su numero de telefono: ")

# Procesos finales
birthyear = 2026 - age
print("\n=")
print("=")
print(f"Nombre: {name}")
print(f"Apellido: {lastname}")
print(f"Correo: {mail}")
print(f"Edad: {age}")
print(f"Sexo: {sexo}")
print(f"Telefono: {phone}")
print(f"Tu año de nacimiento es: {birthyear}")

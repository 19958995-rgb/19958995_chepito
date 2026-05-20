1. #Solicitud de datos al usuario
nombre = input("Ingresa el nombre del estudiante: ")
edad_texto = input("Ingresa la edad del estudiante: ")
seccion = input("Ingresa la sección del estudiante: ")
grado = input("Ingresa el grado del estudiante: ")

# 2. Conversión de tipos de datos necesarios
# Convertimos la edad a un número entero
edad = int(edad_texto)

# Creamos una variable booleana automáticamente basada en la edad
es_mayor_de_edad = edad >= 18

print("\n" + "="*40)
print("  RESULTADOS Y TIPOS DE DATOS")
print("="*40)

# 3. Impresión de los valores y sus tipos de datos usando type()
print(f"Nombre: {nombre} -> Tipo: {type(nombre)}")
print(f"Edad: {edad} -> Tipo: {type(edad)}")
print(f"Sección: {seccion} -> Tipo: {type(seccion)}")
print(f"Grado: {grado} -> Tipo: {type(grado)}")
print(f"¿Es mayor de edad?: {es_mayor_de_edad} -> Tipo: {type(es_mayor_de_edad)}")

print("="*40)

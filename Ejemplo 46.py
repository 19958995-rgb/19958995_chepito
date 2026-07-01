agenda = {}

def agregar(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto {nombre} añadido.")

def buscar(nombre):
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print(f"Contacto {nombre} no encontrado.")

def eliminar(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"Error: El contacto {nombre} no existe.")

# Pruebas del sistema
agregar("Carlos", "555-1234")
buscar("Carlos")
eliminar("Carlos")
eliminar("Carlos") # Valida si existe antes de borrar
tareas = []

def agregar_tarea(descripcion, prioridad):
    # prioridades: 1 (Alta), 2 (Media), 3 (Baja)
    tarea = {"descripcion": descripcion, "prioridad": prioridad, "completada": False}
    tareas.append(tarea)

def completar_tarea(descripcion):
    for t in tareas:
        if t["descripcion"] == descripcion:
            t["completada"] = True
            break

def mostrar_tareas():
    # Ordenar por prioridad numéricamente menor de forma preestablecida
    tareas_ordenadas = sorted(tareas, key=lambda x: x["prioridad"])
    for t in tareas_ordenadas:
        estado = "✔️" if t["completada"] else "❌"
        print(f"[{estado}] Prioridad {t['prioridad']}: {t['descripcion']}")

agregar_tarea("Estudiar Python", 1)
agregar_tarea("Comprar despensa", 3)
completar_tarea("Estudiar Python")
mostrar_tareas()
import random
import string

def generar_contraseña(longitud=12):
    if longitud < 4:
        return "Longitud mínima requerida: 4"
        
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Asegurar que tenga al menos uno de cada tipo según requerimientos estándar
    contraseña = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Llenar el resto
    contraseña += [random.choice(caracteres) for _ in range(longitud - 4)]
    random.shuffle(contraseña)
    
    return "".join(contraseña)

print("Contraseña segura generada:", generar_contraseña(14))
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
    
    contraseña += [random.choice(caracteres) for _ in range(longitud - 4)]
    random.shuffle(contraseña)
    
    return "".join(contraseña)

print("Contraseña segura generada:", generar_contraseña(14))
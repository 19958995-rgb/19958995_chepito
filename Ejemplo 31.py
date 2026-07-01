contraseña = "Python3.9!"

tiene_longitud = len(contraseña) >= 8
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
tiene_especial = any(c in "!@#$%^&*()-_=+[{]};:',.<>?/|~`" for c in contraseña)

if tiene_longitud and tiene_mayuscula and tiene_numero and tiene_especial:
    print("La contraseña es segura.")
else:
    print("La contraseña NO cumple con los criterios de seguridad.")
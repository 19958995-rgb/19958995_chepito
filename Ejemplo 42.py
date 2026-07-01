lista_principal = [1, 2, 3, 4, 5, 6]
subsecuencia = [2, 4, 6]

it = iter(lista_principal)
es_subsecuencia = all(item in it for item in subsecuencia)

print(f"¿Es subsecuencia?: {es_subsecuencia}")
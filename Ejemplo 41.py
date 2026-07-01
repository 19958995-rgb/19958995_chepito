anidada = [[1, 2], [3, 4, 5], [6]]
plana = []

for sublista in anidada:
    for item in sublista:
        plana.append(item)

print("Lista aplanada:", plana)
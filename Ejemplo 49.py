registro = {
    "Ana": {"Matemáticas": [85, 90], "Historia": [88]},
    "Luis": {"Matemáticas": [70, 80], "Historia": [95]}
}

# Promedio por estudiante
for estudiante, materias in registro.items():
    todas_notas = []
    for notas in materias.values():
        todas_notas.extend(notas)
    promedio = sum(todas_notas) / len(todas_notas) if todas_notas else 0
    print(f"Promedio de {estudiante}: {promedio:.2f}")

# Promedio por materia (Ejemplo con Matemáticas)
materia_buscar = "Matemáticas"
notas_materia = []
for materias in registro.values():
    if materia_buscar in materias:
        notas_materia.extend(materias[materia_buscar])

prom_materia = sum(notas_materia) / len(notas_materia) if notas_materia else 0
print(f"Promedio general en {materia_buscar}: {prom_materia:.2f}")
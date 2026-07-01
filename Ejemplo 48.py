
inventario = {
    "Manzanas": (1.50, 100),
    "Leche": (2.20, 4),
    "Pan": (0.80, 15),
    "Huevos": (3.00, 2)
}

valor_total = 0
bajo_stock = []

for producto, (precio, stock) in inventario.items():
    valor_total += precio * stock
    if stock < 5:
        bajo_stock.append(producto)

print(f"Valor total del inventario: ${valor_total:.2f}")
print(f"Productos con bajo stock (<5 unidades): {bajo_stock}")
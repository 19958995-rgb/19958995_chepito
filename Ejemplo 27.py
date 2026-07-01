a, b, c = 15, 8, 22

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"Números ordenados de menor a mayor: {a}, {b}, {c}")
n = int(input())

if n <= 0:
    pass
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    print(a)
    print(b)
    for _ in range(n - 2):
        a, b = b, a + b
        print(b)
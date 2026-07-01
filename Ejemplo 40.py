lista = [1, 2, 3, 4, 5]
k = 2
n = len(lista)
k = k % n
lista_rotada = lista[-k:] + lista[:-k]
print("Lista rotada:", lista_rotada)
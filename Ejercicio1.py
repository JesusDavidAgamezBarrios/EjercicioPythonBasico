import random

# 1. lista de 10 números aleatorios.
lista_aleatoria = random.sample(range(1, 11), 10)
print("Lista original: ", lista_aleatoria)

# 2.lista en orden ascendente 
lista_ascendente = sorted(lista_aleatoria)
print("Lista ordenada en orden ascendente: ", lista_ascendente)

# 3.lista en orden descendente 
lista_descendente = sorted(lista_aleatoria, reverse=True)
print("Lista ordenada en orden descendente: ", lista_descendente)
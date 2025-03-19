"""
Vetores e Matrizes sao dinamicos e podem ser de qualquer tipo.
Dinamicos: Nao possuem tamanho fixo, podemos criar a lista e ir adicionando elementos.

As listas em Python sao representadas por colchetes: []
"""

lista1 = [1, 4, 6, 10, 3, 4]
lista2 = ['a', 'G', 'u', '!', 'r', '?']

# Checa se determinado valor esta contido na lista:
num = 10
if num in lista1:
    print('Existe numero 10 na lista')
else:
    print('Nao existe numero 10 na lista')

# Orderna a lista:
lista1.sort()
print(lista1)

# Contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(4))

# Adicionando valores a lista:
lista1.append(9)
print(lista1)

# Adicionando multiplos valores a lista:
lista1.extend([5, 9, 8])
print(lista1)

# Adicionando valores em indices especificos.
lista1.insert(1, 2)
print(lista1)

# Contando elementos existentes na lista:
print(len(lista1))

# Removendo o ultimo elemento da lista:
lista1.pop()
print(lista1)

# Removendo elemento pelo indice:
lista1.pop(1)
print(lista1)

# Limpando uma lista:
lista1.clear()
print(lista1)
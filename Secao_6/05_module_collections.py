# Counter - Recebe um iteravel e cria um objeto tipo collections counter, parecido com um dicionário, como chave o elemento da lista
# e como valor a quantidade de repetições desse elemento.

from collections import Counter


lista = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1, 2, 2, 3]

print(Counter(lista))

"""
Tupla sao parecidas com listas, existem basicamente duas diferencas:
1. As tuplas sao representadas por parenteses `()`.
2. Tuplas sao imutaveis (toda operacao em uma tupla, gera uma nova tupla).
"""

# Gerando tupla dinamicamente com range(inicio, fim, passo):
tupla1 = tuple(range(11))
print(tupla1)

tupla2 = ('Daniel', 24, 1.80, True)
print(tupla2)

# Soma, Maximo e Minimo e Tamanho de tuplas:
tupla3 = (2, 3, 1, 5, 4)
print(sum(tupla3))
print(max(tupla3))
print(min(tupla3))
print(len(tupla3))

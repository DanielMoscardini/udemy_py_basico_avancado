nome = 'Arthur Pendragon'

# Convertendo string em uma lista:
nome = nome.split()
print(nome)

lista = [1, 2, 3, 4, 5]

# Soma, Valor Maximo e Minimo e Tamanho:
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformando listas em tuplas:
tupla = tuple(lista)
print(lista)
print(tupla)

# Desempacotamento de listas:
num1, num2, num3, num4, num5 = lista
print(num1)
print(num2)
print(num5)

# Deep Copy e Shallow Copy
# Deep Copy eh quando a copia e a original sao independentes, ou seja, uma nao afeta a outra.
nova = lista.copy()
nova.append(6)
print('\nDeep Copy:')
print(lista)
print(nova, "\n\nShallow Copy:")

# Shallow Copy eh quando a lista nova e original sao dependentes, a alteracao de uma reflete na outra.
nova2 = lista
nova2.append(6)
print(lista)
print(nova2)




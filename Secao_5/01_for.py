nome = 'Frodo Baggins'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Iterando em uma string:
for letra in nome:
    print(letra, end='')
print('\n')

# Iterando sobre uma lista
for numero in lista:
    print(numero, end='')
print('\n')

# Iterando sobre um range (o valor final nao eh inclusive):
for numero in numeros:
    print(numero, end='')

# range(valor_de_parada) -> valor_de_parada nao inclusive, inicio padrao 0 e passo de 1 em 1.

for num in range(11):
    print(num, end=' ')
print('\n')

for num in range(1, 11):
    print(num, end=' ')
print('\n')

for num in range(1, 11, 2):
    print(num, end=' ')
print('\n')

# Forma inversa.
for num in range(10, 0, -1):
    print(num, end=' ')
print('\n')

lista = list(range(10))
print(lista)

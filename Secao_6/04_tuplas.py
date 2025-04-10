# Tuplas sao mais rapidas do que listas (+ performance).
# Codigo mais seguro (imutaveis).

tupla = (1, 2, 3, 4, 5)
for n in tupla:
    print(n, end=' ')

print('\n')

for indice, valor in enumerate(tupla):
    print(f'Indice: {indice} - Valor: {valor}')
print()

tupla2 = ('a', 'b', 'b', 'c')
print(tupla2.count('b'), '\n')

meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
print(meses[2])

i = 0
while i < len(meses):
    print(meses[i], end=' ')
    i += 1
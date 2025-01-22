"""
Leia um numero inteiro. Se esse numero for positivo, calcule a raiz quadada e mostre ela.
Se for negativo, mostre uma mensagem dizendo que o numero eh invalido.
"""

from math import sqrt


num = int(input('Digite um numero: '))

if num > 0:
    print(f'A raiz quadrada do numero eh: {int(sqrt(num))}')
else:
    print('Numero nao eh valido!')

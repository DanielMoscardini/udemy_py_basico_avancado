# Receba dois inteiros e mostre qual o maior deles.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O primeiro numero eh maior.')
elif num2 > num1:
    print('O segundo numero eh maior.')
else:
    print('Os numeros sao iguais.')

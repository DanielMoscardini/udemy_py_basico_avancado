# receba tres valores e apresenta a soma dos quadrados dos valores lidos.


num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
num3 = int(input('Digite o terceiro numero inteiro: '))

q_num1, q_num2, q_num3 = (num1 ** 2), (num2 ** 2), (num3 ** 2)
soma = q_num1 + q_num2 + q_num3
print(f'A soma dos quadrados eh: {soma}')

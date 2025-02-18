qtde = int(input('Quantas vezes o loop deve rodar? '))
soma = 0

for n in range(1, qtde + 1):
    num = int(input(f'Informe o {n}/{qtde} valor: '))
    soma += num
print(f'A soma eh {soma}')

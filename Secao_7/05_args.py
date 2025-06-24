def soma_tudo(*args):
    return sum(args)


print(soma_tudo(1, 1, 1, 1))
print(soma_tudo(1, 2, 3, 4, 5, 6, 7))

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(soma_tudo(*numeros))
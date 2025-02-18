# forcando loop infinito:
while True:
    comando = int(input('Digite [1] para sair: '))
    if comando == 1:
        break
    else:
        print('Comando errado, tente novamente!')

print('Comando correto, programa finalizado.')

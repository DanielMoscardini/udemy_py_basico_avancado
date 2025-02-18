# Determine e mostre os cinco primeiros numeros multipos de 2:

count = 0
multiplos = []

while True:
    numeros = int(input('Digite numeros ate eu falar chega: '))
    if numeros % 2 == 0:
        count += 1
        multiplos.append(numeros)
        if count == 5:
            print('CHEGA!!!')
            break

print(f'Os cinco primeiros numeros multiplos de 2 foram: {multiplos}')

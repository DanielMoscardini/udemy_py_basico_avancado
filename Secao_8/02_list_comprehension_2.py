numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Refatorando:
pares2 = [numero for numero in numeros if not numero % 2]
print(pares2)
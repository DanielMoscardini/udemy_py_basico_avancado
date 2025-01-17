variavel_global = 1
variavel_global2 = 11

if variavel_global > 10:
    variavel_local = variavel_global + 10

if variavel_global2 > 10:
    variavel_local2 = variavel_global2 + 10

# print(variavel_local)  >> Nao podemos acessar, pois a variavel nunca foi definida.

print(variavel_local2)
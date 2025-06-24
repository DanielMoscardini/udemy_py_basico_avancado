"""
Em algumas linguagens, dicionarios sao conhecidos como Mapas.
Dicionarios sao colecoes do tipo Chave/Valor.
Chave e Valor podem ser de qualquer tipo de dado, pode-se misturar tipos de dados.
Sao representados por chaves '{}'
Não podemso ter chaves repetidas.
"""

paises = {
    'BR': 'Brasil',
    'EUA': 'Estados Unidos',
    'PY': 'Paraguai'
}

print(paises)
print(paises['BR'])

# Eh recomendado utilizar o metodo Get para buscar o valor da chave do dict.
# Com Get, caso selecione uma chave inexistente, sera retornado None, e nao um KeyError.
print(paises.get('EUA'))
print(paises.get('RU', 'Pais nao encontrado.'))

# Adicionando valores ao dicionário.
paises['JP'] = 'Japão'

print(paises)

carrinho = []
produto1 = {'Nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'Nome': 'Notebook', 'Quantidade': 1, 'Preço': 3000.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho[0])
"""
Em algumas linguagens, dicionarios sao conhecidos como Mapas.
Dicionarios sao colecoes do tipo Chave/Valor.
Chave e Valor podem ser de qualquer tipo de dado, pode-se misturar tipos de dados.
Sao representados por chaves '{}'
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
print(paises.get('RU', 'Pais nao encontrado.'))
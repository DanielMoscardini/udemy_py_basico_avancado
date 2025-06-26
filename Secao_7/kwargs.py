def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')

cores_favoritas(marcos='Verde', julia='Vermelho')
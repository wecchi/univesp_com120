"""
    Arquivo com as funções a serem testadas
"""
def soma(arg):
    """
    Soma uma lista de valores, propositalmente estamos iniciando a variável total com 1 para gerar uma soma errada
    :param arg:
    :return: soma dos elementos de uma lista
    """
    total = 1
    for i in arg:
        total += i
    return total


def multiplica(arg):
    total = 1
    for i in arg:
        total *= i
    return total
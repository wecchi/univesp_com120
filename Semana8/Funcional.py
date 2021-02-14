"""
    Estudo de programação funcional: Estados e Dados imutáveis
        - Stateless (funções não dependem e não alteram nehum dado externo - devem retornar como se fosse a 1ª chamada)
        - Immutable (uma vez atribuído um valor a uma variável, nunca deve ser alterada)
    Para isso funcionar as funções devem ser independentes:
        1. A função deve ter pelo menos um argumento
        2. A função deve retornar algo (dado processado ou mesmo uma outra função)
        3. Não existem loops (laços são criados por meio da recursão)

    A função deve ser pura e não terá nenhum efeito colateral ou secundário, em Python 3:
        - First-Class functions: funções que podem ser passadas como argumento para outras funções
        - High-Order functions: são funções que recebem uma ou mais funções e retornam funções
        - Lambda expression
        - List Comprehensions
    https://docs.python.org/3/howto/functional.html
"""


## Exemplo de soma em programação funcional:
def soma(val1, val2):
    return val1 + val2


print(soma(200, 400))

## Exemplo de impressão das letras de uma string usando função anônima (lambda)
# e map (recebe uma lista e retorna uma nova lista),
# também existe o filter (que compara cada elemento da lista a uma regra de filtragem):
canal = lambda x: x
lista = list(map(str, canal('CDFTV')))
print(lista)

## Exemplo de soma de itens de uma lista:
numbers = list(range(1, 21))
sum(numbers)

## Exemplo de if/else numa linha e dentro de uma função:
print('Works' if True else 'Error!')


## Exemplo de Imutabilidade:
def soma(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        first = numbers[0]
        rest = numbers[1:]
        return first + soma(rest)


soma([1, 2, 3, 4, 5])

## Exemplo de composição de funções:
import toolz  # pacote para programação funcional

clean_and_lower = toolz.compose(str.strip, str.lower)
clean_and_lower('    Python Brasil 13 - Programação Funcional em Python 3 de Forma Simples   ')

## Exemplo de First-Class functions:
frutas = ['melancia', 'uva', 'ameixa', 'abacaxi', 'pessego', 'goiaba', 'atemoia', 'framboesa']
my_sorted = list.sort
my_sorted(frutas)
print(frutas)


## Exemplos de High-Order functions:
def convert(number, to_what):
    return to_what(number)


print(convert(98, float))
print(convert(79.88, str))


def to_squared(number):
    return number ** 2


list(map(to_squared, [5, 10, 11, 13, 17, 21]))

## Exemplos de Lambda expression (como função anônima, sem nomeá-la)
list(map(lambda n: n * 2, [5, 10, 11, 13, 17, 21]))
my_dogs = ['Bruce', 'Khyra', 'Lunna', 'Moksha', 'Khael', 'Bolinha', 'Cinty', 'Sansão', 'Pitucha', 'Miucha']
list(map(lambda name: 'I love ' + name, my_dogs))

## Exemplo de List Comprehensions (expressions):
print(['I love ' + dog for dog in my_dogs])

## Exemplos de Operator + Reduce
import operator
from functools import reduce

print(operator.add(1, 2))
print(operator.concat('Programação', ' Funcional'))

print(reduce(operator.add, [1, 2, 3, 4, 5]))
reduce(operator.concat, ['Reduce', ' is', ' very', ' cool!!'])

## Exemplo de partial:
from functools import partial

add_one = partial(operator.add, 1)
add_one(90)

## Exemplo de attrgetter
from operator import attrgetter
import collections

person = collections.namedtuple('Person', 'name age gender')
peoples = [person('André', 39, 'm'), person('Renato', 35, 'm'), person('Magali', 22, 'f'), person('Ludimila', 19, 'f'),
           person('Marcelo', 49, 'm'), person('Gabriela', 27, 'f'), person('Ferando', 34, 'm'), person('Bia', 18, 'f')]

sorted(peoples, key=attrgetter('name'))
sorted(peoples, key=attrgetter('age'))

## Do exemplo anterior poderíamos melhorar a função com a 'partial':
sort_name = partial(sorted, key=attrgetter('name'))
sort_age = partial(sorted, key=attrgetter('age'))

sort_name(peoples)
sort_age(peoples)

## Outras maneiras de implementar partial (fatoração de função):
# Define uma função que busca uma valor dentro de do JSON, por exemplo
user_one = {'name': 'Marcelo', 'redes': [{'name': 'facebook', 'prof_img': '', 'cover_img': 'imagemC'},
                                         {'name': 'twitter', 'prof_img': 'imagemP', 'cover_img': ''},
                                         {'name': 'linkedin', 'prof_img': 'imagemPL', 'cover_img': 'imagemCI'}]}


def get_img(what_img, user):
    """
    Retorna a 1ª imagem encontrada, conforme seletor
    :param what_img: seletor do tipo de imagem a ser encontrada
    :param user: JSON de usuário
    :return: Nome da imagem
    """
    for rede in user['redes']:
        if rede[what_img] != '':
            return rede[what_img]
    return 'default'


# Criando as chamadas partial, fixando o parâmetro what_img
get_prof_img = partial(get_img, 'prof_img')
get_cover_img = partial(get_img, 'cover_img')

# A chamada retorna
get_prof_img(user_one)
get_cover_img(user_one)
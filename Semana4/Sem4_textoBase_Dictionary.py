"""
    Ljubomir, P. Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações.
    São Paulo: Grupo GEN, 2016. 9788521630937. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788521630937/. Acesso em: 01 Nov 2020
    
    Um Dicionário como um Substituto para a Condição Multivias
    Quando apresentamos os dicionários no início desta seção, nossa motivação foi a necessidade de um contêiner
    com índices definidos pelo usuário. Agora, mostramos usos alternativos para os dicionários. Suponha que
    quiséssemos desenvolver uma pequena função, chamada complete(), que aceite a abreviação de um dia da semana,
    como 'Ter', e retorne o dia correspondente, que para a entrada 'Ter' seria 'Terça'.
"""

def complete(abreviacao):
    'retorna dia da semana correspondente à abreviação'
    
    dias = {'Seg': 'Segunda', 'Ter':'Terça', 'Qua': 'Quarta',
            'Qui': 'Quinta', 'Sex': 'Sexta', 'Sab': 'Sábado',
            'Dom':'Domingo'}

    return dias[abreviacao]



complete('Ter')



## Problema Prático 6.4 (p. 184)
# Implemente a função contaPalavra(), que aceite como entrada um texto — como uma string — e exiba a frequência de cada palavra no texto.
# Você pode considerar que o texto não possui pontuação e que as palavras são separadas por espaços em branco.
def countWords(text):
    """
        Retorna um dicionário com as ocorrências das palavras
    """
    words ={}
    for word in text.split(' '):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


texto = 'all animals are equal but some animals are more equal than others'
for key, value in countWords(texto).items():
    if value < 2:
        print('{:15} appears {} time.'.format(key, value))
    else:
        print('{:15} appears {} times.'.format(key, value))



## operações matemáticas de conjunto (união, interseção, diferença e diferença simétrica)
agenda1 = {'123-45-67', '234-56-78', '345-67-89'}
agenda2 = set()
agenda3 = {'345-67-89', '456-78-90'}

# União
agenda1 | agenda3
# {'456-78-90', '123-45-67', '345-67-89', '234-56-78'}

# Intersecção
agenda1 & agenda3
#{'345-67-89'}

# Diferença (tudo que está em agenda1 e não está em agenda3)
agenda1 - agenda3
#{'123-45-67', '234-56-78'}

# Diferença simétrica (o que não é comum aos dois conjuntos
agenda1 ^ agenda3
#{'456-78-90', '123-45-67', '234-56-78'}


## Problema Prático 6.6
# Implemente a função sync() que aceita uma lista de agendas (em que cada agenda é um conjunto de
# números de telefone) como entrada e retorna uma agenda (como um conjunto) contendo a união de todas as agendas.
agenda4 = {'234-56-78', '456-78-90'}
agendas = [agenda1, agenda2, agenda3, agenda4]

def sync(l):
    """
        Une as listas apenas com os elementos únicos
    """
    results = set()
    # para cada contêiner embutido do Python da classe set, recebido na lista, realiza união
    for e in l:
        results = results | e
    
    return results



sync(agendas)














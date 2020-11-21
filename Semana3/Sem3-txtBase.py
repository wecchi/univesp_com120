'''
    Estudo do capítulo 10 - Recursão
    Ljubomir, P. Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações.
    São Paulo: Grupo GEN, 2016. 9788521630937.
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788521630937/. Acesso em: 22 Oct 2020
'''


## Exemplo da função vertical:
def vertical(n):
    'exibe os dígitos de um número verticalmente na ordem'
    if n < 10:
        print(n)
    else:  # etapa recursiva, n tem 2 ou mais dígitos
        vertical(n // 10)  # chama a sí mesma passando o número menos um decimal
        print(n % 10)  # imprime o resto da divisão por 10, ou seja a unidade


print('\n' + str('''>>>  Execução da função "vertical(789456)" proposto:  <<<''').center(80, '-'))
vertical(789456)


## Problema Prático 10.1
# Implemente o método recursivo reverse(), que aceita um inteiro não negativo como entrada e exibe os dígitos
# de n verticalmente, começando com o dígito de ordem baixa.
def reverse(n):
    'exibe os dígitos de um número verticalmente na ordem inversa'
    cStr = str(n)  # Converte o número para string
    nStr = len(cStr)  # Obtêm a quantidade de dígitos
    if nStr == 1:  # Verifica se o tamanho do número é 1 posição
        print(cStr)  # Imprime a string
    else:  # Chamada recursiva para os casos em que o tamanhao é maior que 1
        print(cStr[-1])  # Imprime a última posição da string
        reverse(cStr[0:(nStr - 1)])  # Chama a função reverse passando todos elementos, exceto o último


print('\n' + str('''>>>  Execução da função "reverse(728904561)" Problema prático 10.1:  <<<''').center(80, '-'))
reverse(728904561)


## Problema Prático 10.2
# Use o pensamento recursivo para implementar a função recursiva cheers() que, sobre a entrada inteira n,
# exibe n strings "Hip " seguidos por "Hurrah!!!".
def cheers(n):
    # Caso básico n=0
    if n == 0:
        print('Hurrah!!!')
    # Chamada de recursão
    else:
        n -= 1
        print('Hip', end=' ', flush=True)
        cheers(n)


print('\n' + str('''>>>  Execução da função "cheers(3)" Problema prático 10.2:  <<<''').center(80, '-'))
cheers(3)


##Problema Prático 10.3
# No Capítulo 5, implementamos a função fatorial() iterativamente. A função fatorial n! tem uma
# definição recursiva natural:      n! =  1       se n = 0
#                                 n · (n− 1)!     se n > 0
def factorial(n):
    n = int(abs(n))
    if n in [0, 1]:
        return 1
    else:
        return (n * factorial(n - 1))


print('\n' + str('''>>>  Execução da função "factorial(9)" Problema prático 10.3:  <<<''').center(80, '-'))
factorial(9)


## Padrão Recursivo de Sequência Numérica
# Começamos implementando a função pattern(), que aceita um inteiro não negativo n e exibe um padrão numérico
def pattern(n):
    'exibe o enésimo padrão'
    if n == 0:
        print(0, end=' ')
    else:  # etapa recursiva: n > 0
        pattern(n - 1)
        print(n, end=' ')
        pattern(n - 1)


print('\n' + str('''>>>  Execução da função "pattern(4)" - Módulo ch10.py:  <<<''').center(80, '-'))
pattern(4)


## Problema Prático 10.4
# Implemente o método recursivo pattern2(), que aceita um inteiro não negativo como entrada e exibe o padrão
# mostrado a seguir. Os padrões para as entradas 0 e 1 são nada e um asterisco, respectivamente:
# >>> pattern2(2)
# *
# **
# *
# >>> pattern2(3)
# *
# **
# *
# ***
# *
# **
# *
def patternStar(n):
    'exibe n estrelas'
    if n > 0:
        patternStar(n - 1)
        print(n * '*')
        patternStar(n - 1)


print('\n' + str('''>>>  Execução da função "patternStar(3)" - Problema Prático 10.4:  <<<''').center(80, '-'))
patternStar(3)

## Padrão snowflake
from turtle import *


def koch(n):
    'retorna direções turtle para desenhar a curva Koch(n)'
    if n == 0:
        return 'F'
    tmp = koch(n - 1)
    return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp


def drawSnowflake(n):
    'desenha enésima curva de floco de neve com função koch() 3 vezes'
    s = Screen()
    t = Turtle()
    directions = koch(n)
    for i in range(3):
        for move in directions:  # desenha koch(n)
            if move == 'F':
                t.fd(300 / 3 ** n)
            if move == 'L':
                t.lt(60)
            if move == 'R':
                t.rt(120)
        t.rt(120)  # gira 120 graus para a direita
    s.bye()


print('\n' + str('''>>>  Execução da função "drawSnowflake(4)" - Problema Prático 10.5:  <<<''').center(80, '-'))
drawSnowflake(4)

##Analisador de Vírus
# Agora, usamos a recursão para desenvolver um analisador de vírus, ou seja, um programa que examina sistematicamente
# cada arquivo no sistema de arquivos e exibe os nomes dos arquivos que contêm uma assinatura de vírus de computador
# conhecida. A assinatura é uma sequência específica que evidencia a presença do vírus no arquivo.
# Usamos um dicionário para armazenar as diversas assinaturas de vírus:
signatures = {'Creeper':'ye8009g2h1azzx33',
              'Code Red':'99dh1cz963bsscs3',
              'Blaster':'fdp1102k1ks6hgbc'}

import os
def scan(pathname, signatures):
    'varre recursivamente os arquivos contidos, direta ou indiretamente, na pasta pathname'
    for item in os.listdir(pathname):      # para cada arquivo ou pasta
                                           # na pasta pathname
        # cria pathname para item chamado next
        # next = pathname + '/' + item        # somente Mac
        # next = pathname + '\' + item        # somente Windows
        next = os.path.join(pathname, item)   # qualquer SO
        try: # faz recursão cega sobre next
            scan(next, signatures)
        except: # caso básico: exceção significa que next é um arquivo
            # para cada assinatura de vírus
            for virus in signatures:
                # verifica se arquivo next tem assinatura de vírus
                if open(next).read().find(signatures[virus]) >= 0:
                    print('{}, found virus {}'.format(next,virus))

scan('COM110', signatures)

## A função timingAnalysis toma como entrada a função func e os números start, stop, inc e runs. Primeiro,
# ela executa func sobre várias entradas de tamanho start e exibe o tempo de execução médio. Depois, ela repete isso
# para os tamanhos de entrada start+inc, start+2*inc,… até o tamanho de entrada stop.
import time


def buildInput(n):
    'retorna entrada para funções'
    return n


def timing(func, n):
    'roda func sobre entrada retornada por buildInput'
    funcInput = buildInput(n)  # obtém entrada para func
    start = time.time()  # toma hora inicial
    func(funcInput)  # roda func sobre funcInput
    end = time.time()  # toma hora final
    return end - start  # retorna tempo de execução


def timingAnalysis(func, start, stop, inc, runs=2):
    '''
        exibe tempos de execução médios da função func sobre entradas
        de tamanho start, start+inc, start+2*inc, … até stop
    '''
    for n in range(start, stop, inc):  # para cada tamanho de entrada n
        acc = 0.0  # inicializa acumulador
        for i in range(runs):  # repete runs vezes:
            acc += timing(func, n)  # roda func sobre entrada de tamanho n e acumula tempos de execução
        # exibe tempos de execução médios para tamanho de entrada n
        formatStr = 'Tempo de execução de {}({}) é {:.7f} segundos.'
        print(formatStr.format(func.__name__, n, acc / runs))


print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "pattern()" (p. 373):  <<<''').center(80, '-'))
timingAnalysis(pattern, 2, 20, 2)

##A busca binária é fácil de implementar recursivamente. O caso básico é quando a lista lst está vazia: target
# possivelmente não pode estar nela, e retornamos –1. Caso contrário, comparamos target com a mediana da lista.
# Dependendo do resultado da comparação, terminamos ou continuamos a busca, recursivamente, sobre uma sublista de lst.
# Implementamos a busca binária como a função recursiva search(). Como as chamadas recursivas serão feitas sobre
# sublistas lst[i:j] da lista original lst, a função search() deverá aceitar, como entrada, não apenas lst e target,
# mas também os índices i e j
import random


def search(lst, target, i, j):
    '''tenta achar target na sublista classificada lst[i:j]
       índice de target é retornado se achado, -1 caso contrário'''
    if i == j:  # caso básico: lista vazia
        return -1  # target não pode estar na lista
    mid = (i + j) // 2  # índice da mediana de l[i:j]
    if lst[mid] == target:  # target é a mediana
        return mid
    if target < lst[mid]:  # busca à esquerda da mediana
        return search(lst, target, i, mid)
    else:  # busca à direita da mediana
        return search(lst, target, mid + 1, j)


def buildInput(n):
    'retorna uma amostra aleatória de n números no intervalo [0, 2n]'
    lst = random.sample(range(2 * n), n)
    lst.sort()  # Ordenar a lista
    return lst


# Criar uma lista aleatória com 27 itens
lst = buildInput(27)
target = 45
search(lst, target, 0, len(lst))


def binary(lst):
    'escolhe item aleatório na lista lst e roda search() sobre ele'
    target = random.choice(lst)
    return search(lst, target, 0, len(lst))


def linear(lst):
    'escolhe item aleatório na lista lst e roda index() sobre ele'
    target = random.choice(lst)
    return lst.index(target)


print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "linear()" (p. 379):  <<<''').center(100, '-'))
timingAnalysis(linear, 200000, 1000000, 200000, 20)

print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "binary()" (p. 379):  <<<''').center(100, '-'))
timingAnalysis(binary, 200000, 1000000, 200000, 20)

##Teste de Exclusividade Consideramos este problema: dada uma lista, verificar se cada item da mesma é exclusivo.
# Um modo natural de resolver esse problema é percorrer a lista e, para cada item, verificar se o item aparece mais
# de uma vez. A função dup1 implementa essa ideia:
def dup(lst):
    'retorna True se lista lst tiver duplicatas; caso contrário, False'
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False


# E se classificássemos a lista primeiro? O benefício de fazer isso é que os itens duplicados ficarão um ao
# lado do outro na lista ordenada.
def dup2(lst):
    'retorna True se lista lst tiver duplicatas; caso contrário, False'
    lst.sort()
    for index in range(1, len(lst)):
        if lst[index] == lst[index - 1]:
            return True
    return False


def dup3(lst):
    'retorna True se lista lst tiver duplicatas, caso contrário, False'
    s = set()
    for item in lst:
        if item in s:
            return False
        else:
            s.add(item)
    return True


def dup4(lst):
    'retorna True se lista lst tiver duplicatas, caso contrário, False'
    return len(lst) != len(set(lst))

# Problema Prático 10.7
# Usando um experimento, analise o tempo de execução das funções dup1(), dup2(), dup(3) e dup(4).
# Você deverá testar cada função nas 10 listas de tamanho 2000, 4000, 6000 e 8000, obtidas por:
import random
def buildInput(n):
    'retorna uma lista de n inteiros aleatórios no intervalo [0, n**2]'
    res = []
    for i in range(n):
        res.append(random.choice(range(n**2)))
    return res

print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "dup()" (p. 381):  <<<''').center(100, '-'))
timingAnalysis(dup, 2000, 10000, 2000, 10)
print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "dup2()" (p. 381):  <<<''').center(100, '-'))
timingAnalysis(dup2, 2000, 10000, 2000, 10)
print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "dup3()" (p. 381):  <<<''').center(100, '-'))
timingAnalysis(dup3, 2000, 10000, 2000, 10)
print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "dup4()" (p. 381):  <<<''').center(100, '-'))
timingAnalysis(dup4, 2000, 10000, 2000, 10)



## Calculando o Item que Ocorre com Mais Frequência
# O problema que consideramos em seguida é procurar o item que ocorre com mais frequência em uma lista.
# Na realidade, sabemos como fazer isso, e mais: no Capítulo 6, vimos como os dicionários podem ser usados para
# calcular a frequência de todos os itens em uma sequência. Porém, se tudo o que queremos é encontrar o item mais
# frequente, o uso de um dicionário é desnecessário e um desperdício de espaço de memória.
# Vimos que, classificando uma lista, todos os itens duplicados serão próximos um do outro. Se percorrermos a lista
# ordenada, poderemos contar o tamanho de cada sequência de duplicatas e registrar a maior. Aqui está a implementação
# dessa ideia:
def frequent(lst):
    '''retorna item que ocorre com mais frequência
    na lista lst não vazia'''
    s = dict()
    for item in lst:
        x = lst.count(item)
        if (x > 1) and item not in s:
            s[item] = x
    return s

print('\n' + str('''>>>  Análise Experimental do Tempo de Execução função "frequent()" (p. 382):  <<<''').center(100, '-'))
timingAnalysis(frequent, 2000, 10000, 2000, 10)
#Tempo de execução de frequent(2000) é 0.1073021 segundos.
#Tempo de execução de frequent(4000) é 0.4261907 segundos.
#Tempo de execução de frequent(6000) é 0.9563113 segundos.
#Tempo de execução de frequent(8000) é 1.7066795 segundos.
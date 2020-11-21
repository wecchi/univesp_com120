## Estudo de Recursão 2: https://youtu.be/rBc49w5FZxM
'''
    Comparando os tempos entre iteração e recursão
'''
import time

#Versão Recursiva
def fib_rec(n):
    if n< 2:
        return n
    else:
        res = fib_rec(n-1) + fib_rec(n-2)
        return res


#Versão Iterativa
def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res


print('\n' + str('>>>  Comparando os tempos de processamento  <<<').center(120,'-') )
n = 35
# Rodando e medindo tempo com a função recursiva
start = time.time()
fib_n = fib_rec(n)
print('\n', 'Recursive Fb({}) = {} in: {} sec'.format(n, fib_n, time.time() - start))

# Rodando e medindo tempo com a função iterativa
start = time.time()
fib_n = fib_it(n)
print('\n', 'Iterative Fb({}) = {} in: {} sec'.format(n, fib_n, time.time() - start))

## Memoização
m = dict()
def fat(n):
    if n==0:
        return 1
    # Se o enésimo termo já foi calculado, obtenha do dicionário
    elif m.get(n) != None:
        return m[n]
    # Do contrário
    else:
        m[n] = n*fat(n-1)
        return m[n]


print('\n' + str('>>>  Calculando Fatorial com técnica de memoização  <<<').center(120,'-') )
start = time.time()
fat_n = fat(n)
print('\n', 'Memoization N{}! = {} in: {} sec'.format(n, fat_n, time.time() - start))


## Memoização para Fibonacci
m = dict()
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
        return m[n]

## Exercício proposto na aula 2 de Recursão:
import random
'''
1. Dada uma lista l de n números, implemente uma função recursiva que retorna o maior elemento do conjunto.
2. Dada uma lista l de n números, implemente uma função recursiva que retorna a soma de todos os elementos do conjunto.
'''

def maxToList(lista, item):
    if item == 1:
        return lista[0]
    else:
        checkItem = maxToList(lista, item - 1)
        if checkItem > lista[item - 1]:
            return checkItem
        else:
            return lista[item - 1]


def sumList(lista, item):
    if item == 1:
        return lista[0]
    else:
        soma = lista[item] + sumList(lista, item - 1)
        return soma

print('\n' + str('>>>  Exercícios propostos em aula:  <<<').center(120,'-') )
# Criando uma lista com números de bytes, em seguida embaralhando a lista para testar a função
lstBytes= [x*2 for x in range (4,2049,4) if x%8==0]
random.shuffle(lstBytes)
tamLista = len(lstBytes)

maxItem = maxToList(lstBytes, tamLista)
print('\n', '1. O maior valor numérico da lista L(len={}) é {}'.format(tamLista, maxItem))

sumItem = sumList(lstBytes, tamLista-1)
print('\n', '2. A soma dos itens da lista L(len={}) é {}'.format(tamLista, sumItem))
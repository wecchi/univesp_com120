"""
    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018.
    9788536530253. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/.
    Acesso em: 30 Oct 2020
"""


## 1. Funções comuns – números primos Escreva uma função que receba como parâmetro de entrada um número inteiro N.
# Ela deve retornar 1 se N for primo ou 0, caso não seja.
def isPrimeNum(n, i=2):
    '''
    Verifica se um número é primo ou não
    :param n: integer
    :param i: index to divide number
    :return: boolean
    '''

    # Base cases
    if (n <= 2):
        return True if (n == 2) else False
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    else:
        return isPrimeNum(n, i + 1)


print('\n' + str('''>>>  1. Função números primos "isPrimeNum(43)" (p. 135):  <<<''').center(100, '-'))
isPrimeNum(43)


## 2. Funções comuns – interseção de listas. Escreva uma função que receba duas listas L1 e L2 como parâmetro de entrada
# e retorne uma lista que seja a interseção de L1 e L2, em que uma lista interseção é aquela que contém os elementos
# que estejam presentes em ambas, L1 e L2.
def intersection(l1, l2):
    '''
    Obtem apenas elementos comuns as duas listas
    :param l1: list
    :param l2: list
    :return: list
    '''
    lr = []
    for e in l1:
        if e in l2:
            lr.append(e)
    return lr


print('\n' + str('''>>>  2. Função interseção de listas "intersection(l1, l2)" (p. 136):  <<<''').center(100, '-'))
lista1 = list(range(2, 63, 5))
print('l1 =', lista1, sep=' ')
lista2 = list(range(63, 10, -3))
print('l2 =', lista2, '\n', sep=' ')
intersection(lista1, lista2)


## 3. Função recursiva – soma dos elementos de uma lista Suponha que uma lista está carregada com diversos números
# inteiros. Escreva uma função recursiva que calcule a soma desses valores. Para testar essa função,
# use a lista L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cuja soma resulta = 55

def sumListItens(l):
    '''
    soma dos elementos de uma lista
    :param l: list
    :return: int
    '''
    print(l)
    if l == []:
        return 0
    else:
        return l[0] + sumListItens(l[1:])


print(
    '\n' + str('''>>>  3. Soma recursiva dos valores contidos em uma lista "sumListItens(l)" (p. 136):  <<<''').center(
        100, '-'))
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = sumListItens(l)
print('\n', 'Soma dos elementos de l = {0}'.format(s), sep='')


## 4. Função recursiva – busca binária em lista ordenada Escreva uma função que recebe dois parâmetros: uma lista L
# contendo números inteiros e organizada em ordem crescente; um número inteiro N. Essa função deve verificar se N está
# contido em L utilizando o algoritmo de busca binária e retornar à posição em que ele se encontra ou retornar 0 caso
# N não esteja na lista.

def searchBin(l, n, start, end):
    '''
    Verifica se um número 'n' existe na lista
    :param l: list
    :param n: integer; item to search
    :param start: item index to start search
    :param end: item index to stop search
    :return: boolean; if exists 'n' in list
    '''
    if l[0] == n:
        return '0'
    elif start > end:
        return 0
    else:
        m = (start + end) // 2
        if n == l[m]:
            return m
        elif n < l[m]:
            return searchBin(l, n, start, m - 1)
        else:
            return searchBin(l, n, m + 1, end)


print(str('''>>>  4. Busca na lista "searchBin(Lista, X)" (p. 138):  <<<''').center(100, '-'))

Lista = [3, 8, 11, 14, 16, 19, 25, 29, 31, 37, 42, 46, 53, 58, 60, 63, 71, 82]
print(Lista, '\n', sep='')

X = int(input('Digite um valor para pesquisa na lista: '))

while X != 0:
    Pos = searchBin(Lista, X, 0, len(Lista) - 1)
    if Pos == 0:
        print('{0} não está na lista'.format(X), '\n', sep='')
    else:
        print('{0} está na posição {1} da lista'.format(X, Pos), '\n', sep='')

    X = int(input('Digite um valor para pesquisa na lista (para sair digite 0): '))

print('\nFim do Programa')


## Exercícios propostos
# 1. Escreva uma função que recebe um número inteiro como parâmetro de entrada e retorna o texto # “PAR” ou “ÍMPAR”

def typeIsNum(n):
    '''
    Verifica que tipo de número foi informado
    :param n: integer
    :return: [PAR] se número for par e [ÍMPAR] para número ímpar
    '''
    if n % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'


print(str('''>>>  Exercício 1. Busca na lista "typeIsNum(n)" (p. 139):  <<<''').center(100, '-'))

x = int(input('Digite um número: '))

while x != 0:
    results = typeIsNum(x)
    print('O número {0} é {1}'.format(x, results), '\n', sep='')
    x = int(input('Digite um número: (digite 0 para sair)'))


## Exercícios propostos
# 2. Utilize a função EPrimo desenvolvida no Exercício resolvido 5.1 para carregar uma lista contendo os N primeiros
# números primos, em que N é um número inteiro fornecido pelo usuário

def allPrimeNum(n):
    '''
    Retorna os números primos até n
    :param n: integer
    :return: list primos
    '''

    l = []
    for i in range(1, n + 1):
        if i in [2, 3]:
            l.append(i)
        elif i % 2 != 0:
            for t in range(3, i + 1, 2):
                if (i % t == 0) and (i != t):
                    break
                elif (i == t):
                    l.append(i)
    return l


print(str('''>>>  Exercício 2. lista contendo de N primos "allPrimeNum(N)" (p. 139):  <<<''').center(100, '-'))

x = int(input('Digite um número: '))

while x != 0:
    results = allPrimeNum(x)
    print('Foram encontrados os seguintes números primos {0} até {1}'.format(results, x), '\n', sep='')
    x = int(input('Digite um número: (digite 0 para sair)'))


## 3. Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e
# retorne 1 se A for divisível por B e 0 caso contrário.

def isDivisible(a, b):
    """
    Verifica se a é divisível por b
    :param a: integer
    :param b: integer
    :return: bit
    """
    return 1 if (a % b == 0) else 0


print(str('''>>>  Exercício 3. verifica se 'b' divide 'a' "isDivisible(a, b)" (p. 139):  <<<''').center(100, '-'))
a, b = int(input('''Digite o número 'a': ''')), int(input('''Digite o número 'b': '''))

while b != 0:
    results = isDivisible(a, b)
    txt = 'é' if (results == 1) else 'não é'
    print('O número {0} {1} divisível pelo número {2}'.format(a, txt, b), '\n', sep='')
    a, b = int(input('''Digite o número 'a': ''')), int(input('''Digite o número 'b' (digite 0 para sair): '''))


## 4. Escreva uma função que receba um número inteiro N e retorne uma lista com os bits 0 e 1,
# que representam N convertido para binário. Não use nenhuma função Python de conversão para
# binários. Em vez disso, elabore uma lógica baseada no processo de divisões sucessiva
def convBinary(n):
    '''
    Converte um inteiro em binário
    :param n: integer
    :return: string 'cadeia binária'
    '''
    r = n % 2
    q = n // 2
    if (n < 2):  # Saída da recursiva, quando o número for manor que 2
        return '1'
    else:  # Chamada da recursiva, quando o quociente for maior que um
        return str(convBinary(q)) + '0' if (r == 0) else str(convBinary(q)) + '1'


print(str('''>>>  Exercício 4. converte 'n' em binário "convBinary(n)" (p. 139):  <<<''').center(100, '-'))
n = int(input('''Digite o número 'n': '''))

while n != 0:
    results = convBinary(n)
    print('({0})₁₀ = ({1})₂'.format(n, results), '\n', sep='')
    n = int(input('''Digite o número 'n' (digite 0 para sair): '''))

## 5. Escreva uma função que receba como parâmetro de entrada uma lista L de números inteiros e um valor.
# A função deve retornar quantas vezes o valor está contido na lista. Caso ele não esteja em L, retorne 0
import random


def countNinList(l, n):
    '''
    Conta quantas vezes aparece um número 'n'
    na lista l
    :param l: list of integer
    :param n: integer to search in list
    :return: number of the occur in list
    '''
    x = 0
    for i in l:
        if i == n: x += 1
    return x


print(str('''>>>  Exercício 5. conta ocorrêcias de 'n' na lista "countNinList(l,n)" (p. 139):  <<<''').center(100, '-'))
lista = random.sample(range(1, 100), 20)
for i in (1, 5):
    lista = lista + random.sample(lista, 5)

random.shuffle(lista)
print(lista)
n = int(input('''Digite o número 'n' a ser contabilizado: '''))

while n != 0:
    results = countNinList(lista, n)
    print('Encontrei {0} ocorrências para o número {1}!'.format(results, n), '\n', sep='')
    n = int(input('''Digite o número 'n' a ser contabilizado: (ou digite 0 para sair): '''))


## 6. Escreva um programa que receba como parâmetro de entrada um número inteiro de 5 dígitos no intervalo
# fechado [10000, 30000] que represente códigos de produtos vendidos em uma loja. A função deve calcular e retornar
# o dígito verificador utilizando regra de cálculo explicada a seguir.
def calcVerifDig(n):
    '''
    Calcula o dígito verificador do número
    :param n: inteiro de 5 dígitos no intervalo fechado [10000, 30000]
    :return: dígito verificador
    '''
    nStr = str(n)
    peso = 2
    soma = 0
    for d in nStr:
        soma += peso * eval(d)
        peso += 1
    return soma % 7


print(str('''>>>  Exercício 6. Cálculo de dígito verificador "calcVerifDig(n)" (p. 139):  <<<''').center(100, '-'))
n = int(input('''Informe um código de produto 'n' [10000, 30000]: '''))

while n in range(10000, 30001):
    results = calcVerifDig(n)
    print('Dígito verificador é "{0}" para o código de produto "{1}"!'.format(results, n), '\n', sep='')
    n = int(input('''Informe um código de produto 'n' [10000, 30000]: '''))


##7. Escreva uma função que receba como parâmetro de entrada dois números reais Min e Max. Essa função deve ler do
# teclado um número real e retorná-lo caso esteja dentro do intervalo fechado [Min, Max]. Caso contrário, a função
# deve exibir uma mensagem de erro e ler um novo valor.

def isInterval(rMin, rMax):
    if rMin > rMax:
        rMin, rMax = rMax, rMin
    r = float(input('Forneça um número Real: '))
    while r != 0:
        if rMin <= r and r <= rMax:
            print(r)
        else:
            print('ERRO! o valor informado {0:.8f} está fora do intervalo fechado [{1:.3f}, {2:.3f}]!'
                  .format(r, rMin, rMax), '\n', sep='')
        r = float(input('Forneça um número Real (ou 0 para sair): '))


print(str('''>>>  Exercício 7. Verifica se está no intervalo "isInterval(min, max)" (p. 139):  <<<''').center(100, '-'))
nmin, nmax = float(input('[Min, do intervalo fechado= ')), float(input(', Max], do intervalo fechado= '))
isInterval(nmin, nmax)


## Programa conversor de base
def toStr(n, base):
    convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base not in range(2, len(convertString) + 1):
        return 'ERROR: base {0} not found!'.format(base)
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


print(str('''>>>  Programa 3. Conversor de base "toStr(n, b)" (PensePython):  <<<''').center(100, '-'))
n, base = int(input('''Informe um número 'n': ''')), int(input('''Informe a base 'b' [2:36]: '''))

while base in range(2, 37):
    results = toStr(n, base)
    print('''Número ({0})₁₀ convertido para a base "{1}" é "{2}"'''.format(n, base, results), '\n', sep='')
    n, base = int(input('''Informe um número 'n': ''')), int(input('''Informe a base 'b' [2:36]: '''))


## Escreva uma função que recebe um string como parâmetro e retorna um novo string que é o reverso do string de entrada.
def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[0:len(s) - 1])


print(str('''>>>  'Teste seu entendimento' - Reversor de string "reverse(s)" (PensePython):  <<<''').center(100, '-'))
s = input('''Informe um texto 's': ''')

while s != '':
    results = reverse(s)
    print('''O texto '{0}' de trás para frente é "{1}"'''.format(s, results), '\n', sep='')
    s = input('''Informe um texto 's' (<ENTER> para sair): ''')


## Escreva uma função que recebe um string como um parâmetro e retorna True se o string é um palíndromo,
# False contrário. Lembre-se que um string é um palíndromo se ele é o mesmo quando escrito de trás para a frente.
# Por exemplo: radar é um palíndromo. Como um bônus, palíndromos também podem ser frases, mas você precisa r
# remover os espaços e pontuação antes de verificar. Por exemplo: “madam i’m adam” é um palíndromo.
# Outros palíndromos divertidas incluem:
# 'kayak', 'aibohphobia', 'Live not on evil', 'Reviled did I live, said I, as evil I did deliver', 'Go hang a salami;
# I’m a lasagna hog.', 'Able was I ere I saw Elba', 'Kanakanak', 'Wassamassaw'


def removePunctuation(s):
    strRemove = """ .,:;?/\|<>[]{}()-_'’"`´¨^~=+!@#$%&*"""
    temp = s.lower()
    for e in strRemove:
        temp = temp.replace(e, '')
    return temp


def isPalindrome(s):
    '''
    Verifica se o texto é um palíndromo, isto é se ele é o mesmo
    quando escrito de trás para a frente
    :param s: Text clean and normalized (without punctuation)
    :return: True if is a palindrome
    '''
    if len(s) <= 1:
        return True
    else:
        return (s[0] == s[-1]) and isPalindrome(s[1:len(s) - 1])


print(str('''>>>  'Teste seu entendimento' - Verifica  palíndromo "isPalindrome(s)" (PensePython):  <<<''').center(100,
                                                                                                                   '-'))
s = input('''Informe um texto 's': ''')

while s != '':
    results = isPalindrome(removePunctuation(s))
    print('''O texto '{0}' resultou em "{1}" para palíndromo'''.format(s, results), '\n', sep='')
    s = input('''Informe um texto 's' (<ENTER> para sair): ''')

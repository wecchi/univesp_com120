## Exemplo de uma função qualquer para imprimir os itens de uma lista
def imprime(l):
    for i in range(len(l)):
        print(l[i])


'''
    Quando usar RECURSIVA?
    1. Dependendo do problema, a recursão pode ser bem ou mal empregada.
    2. Geralmente, se existe uma versão simples e não recursiva da função, ela deve ser usada.
    3. Usamos recursão quando o problema pode ser definido recursivamente de forma natural.
'''


# versão de 'imprime' com recursividade
def imprime_rec(l, i=0):
    if i < len(l):
        print(l[i])
        imprime_rec(l, i + 1)

# Definindo uma lista com 20 elementos
l = list(range(1, 21))
print('\n' + str('>>>  Exemplo: imprimindo itens da lista  <<<').center(120,'-') )
imprime(l)
print('\n' + str('>>>  Exemplo: imprimindo itens da lista - Função recursiva  <<<').center(120,'-') )
imprime_rec(l)

## Usando para o problema do fatorial
'''
    Necessário definir 3 pontos:
    1) Definir o problema de forma recursiva, ou seja, em termos dele mesmo
    2) Definir a condição de término (ou condição básica)
    3) A cada chamada recursiva, deve-se tentar garantir que se está mais próximo de satisfazer a condição de término
'''


def fat(n):
    if n == 0:
        return 1
    else:
        res = n * (fat(n - 1))
        return res

print('\n' + str('>>>  Exemplo: Cálculo de 5! (Fatorial de 5) - Função recursiva  <<<').center(120,'-') )
fat(5)

## Exercício proposto na aula Recursão 1: https://youtu.be/Q6lqtu-1Jac
'''
    Implementar uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci.
    Considere os três pontos definidos para o problema:
    1) f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) p/ n>=2
    2) n=0 ou n=1
    3) n deve ser decrementado a cada chamada
'''

def fibonacci(n):
    if (n == 1) or (n == 0):
        return n
    elif (n>0):
        res = fibonacci(n-1) + fibonacci(n-2)
        return res

print('\n' + str('>>>  Exercício: Calculando Nº Fibonacci para F(10) - Função recursiva  <<<').center(120,'-') )
fibonacci(10)

print('\n' + str('>>>  Exercício: Imprimindo Nº Fibonacci para F(0..20) - Função recursiva  <<<').center(120,'-') )
l = []
for i in range(21):
    l.append(fibonacci(i))
print(l)


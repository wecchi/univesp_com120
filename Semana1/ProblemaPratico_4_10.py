## Definição do exercício:
'''
    Problema Prático 4.10
    Explique o que causa o erro de sintaxe em cada instrução listada anteriormente.
    Depois, escreva uma versão correta de cada instrução Python.

# Parte 1 – Avaliação dos problemas apresentados

>> > if x == 5
SyntaxError: invalid syntax ► está faltando os dois pontos após o 5

>> > print 'hello'
SyntaxError: invalid syntax ► necessário incluir parênteses na função print()

>> > lst = [4; 5; 6]
SyntaxError: invalid  syntax ► os elementos da lista devem ser separados por VIRGULA

>> > for i in range(10):
print(i)
SyntaxError: expected an indented block ► no laço for é necessário incluir indentação da instrução print
'''

## Parte 2 – Reescrita dos códigos acima sem BUGs
print(str('>>> Problema Prático 4.10 - correção de BUGs <<<').center(80, '-'),'\n')

x = 5
if x == 5:
    print('hello')

lst = [4, 5, 6]

for i in range(10):
    print(i)
## Definição do problema de negócio
'''
    Exercício resolvido 7.4 – Gerador de dados em arquivo do tipo CSV
    Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas
    com os dados listados na tabela seguinte. O arquivo deve ter o nome “Estoque.csv” e deve usar o caractere “;”
    (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática.
    São Paulo: Editora Saraiva, 2018. 9788536530253. Disponível em:
    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 09 Oct 2020
'''

## Parte 1 - Geração dos dados
print(str('>>> Exercício resolvido 7.4 – Gerador de dados em arquivo do tipo CSV <<<').center(100, '-'),'\n')
from random import randint
arqNome = "Estoque.csv"                  # define o nome do arquivo numa variável
N = 0
while (N < 10) or (N > 10000):           # definindo a quantidade solicitada
    N = int(input("Digite N entre [10, 10000]: "))
cod = []                        # cria uma lista vazia
cont = 0
while cont < N:
    a = randint(10000, 50000)   # gera um número inteiro e aleatório entre 10000 e 50000
    if a not in cod:            # verifica se o número gerado já foi incluído na lista (antes de inseri-lo)
        cod.append(a)
        cont += 1

## Parte 2 – Gerando o arquivo e gravando os dados formatados
S = "{0};{1};{2:.2f};{3}\n"
ICMS = (7, 12, 18)
arq = open(arqNome, "w")
cont = 0
while cont < N:
    qtde = randint(1, 3800)             # gera uma quantidade para o produto
    PcUn = randint(180, 43590) / 100    # gera um valor aleatório para o produto
    i = randint(0, 2)                   # gera um índice aleatório para o ICMS
    arq.write(S.format(cod[cont], qtde, PcUn, ICMS[i])) # grava a linha formatada
    cont += 1                           # incrementa o contador de itens "N"
arq.close()
print('\n', str('>>> Fim do programa 7.4 <<<').center(100, '-'))
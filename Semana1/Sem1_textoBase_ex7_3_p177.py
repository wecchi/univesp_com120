##
'''
    Exercício resolvido 7.3 – Ler um arquivo do tipo CSV
    Escreva um programa que leia um arquivo texto que contém diversas linhas que representam uma lista de compras.
    Em cada linha há três informações: nome de um produto, quantidade e preço unitário, separados pelo caractere “;”.
    Pede-se que cada item da lista seja exibido na tela, incluindo o valor total do item. Ao final,
    exiba o total da compra.

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática.
    Editora Saraiva, 2018. 9788536530253. Disponível em:
    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 08 Oct 2020
'''

## Parte 1 - Leitura do arquivo
print(str('>>> Exercício resolvido 7.3 – Ler um arquivo do tipo CSV <<<').center(80, '-'),'\n')
arqNome = "Compras.txt"           # define o nome do arquivo numa variável
somaTotal = 0
for arqLinha in open(arqNome, 'r', encoding='utf-8'):
    arqLinha = arqLinha.rstrip()        # remove caracter \n
    L = arqLinha.split(',')             # separa a string numa lista com os elementos produto, qtde e valor
    L[1], L[2] = int(L[1]), float(L[2]) # converte para inteiro e float o conteúdo da linha
    totalProd = L[2] * L[1]             # calcula o sub total dos produtos
    somaTotal += totalProd              # totaliza o valor total da compra
    print(" {0:>12} :  {1:3}  x{2:6.2f} = {3:7.2f}"
          .format(L[0], L[1], L[2], totalProd)) # imprime dados da linha com formatação

## Parte 2 – Exibe a soma geral
print("-" * 40)
print('Total da lista de compras {0:>13}'.format(somaTotal))
print('\n', str('>>> Fim do programa 7.3 <<<').center(80, '-'))
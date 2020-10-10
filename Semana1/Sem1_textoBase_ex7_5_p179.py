## Definição do problema de negócio
'''
    Exercício resolvido 7.5 - Lê e processa dados de um arquivo do tipo CSV
    Escreva um programa que leia um arquivo com o layout especificado no Quadro 7.3 e apresente os seguintes resultados:
     ● valor total das mercadorias em estoque;
     ● valor total do imposto ICMS pago referente a essas mercadorias.

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018. 9788536530253.
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 09 Oct 2020
'''

## Parte 1 - Formatação dos dados
print(str('>>> Exercício resolvido 7.5 - Lê e processa dados de um arquivo do tipo CSV <<<').center(100, '-'),'\n')
arqNome = "Estoque.csv"                  # define o nome do arquivo numa variável
print("\nCálculo de Estoque\n")
saida = "{:>7}{:>13.2f}{:>10.2f}{:>12.2f}"
TotICMS = 0
TotMerc = 0

## Parte 2 – Abertura, processamento e apresentação dos resultados
print("Produto    Val.Compra     ICMS   Mercadoria")
arq = open("Estoque.csv", "r")
for s in arq.readlines():
    s = s.rstrip()
    L = s.split(";")
    L[0] = int(L[0])
    L[1] = int(L[1])
    L[2] = float(L[2])
    L[3] = float(L[3])/100
    compra = L[1] * L[2]
    icms = compra * L[3]
    merc = compra - icms
    TotICMS += icms
    TotMerc += merc
    print(saida.format(L[0], compra, icms, merc))
arq.close()
print(saida.format("Totais", TotMerc+TotICMS, TotICMS, TotMerc))

print('\n', str('>>> Fim do programa 7.5 <<<').center(100, '-'))
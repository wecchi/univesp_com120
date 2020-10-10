## Definição do problema de negócio
'''
    3. Escreva um programa que leia o arquivo NUMEROS.TXT gerado no Exercício 2, colocando-os em uma lista. Ordene a
    lista utilizando o método Bubble Sort e grave os números ordenados no arquivo “ORDENADOS.TXT”.
    Não use funções prontas de ordenação e recorra ao Exercício resolvido 4.11 para se lembrar do algoritmo Bubble
    Sort.

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018.
    9788536530253. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 09 Oct 2020
'''

## Parte 1 - Criação da função para ordenação da lista
def ordenaLista(l):
    trocou = 1
    while trocou:
        trocou = 0
        i = 0
        while i < len(l) - 1:
            if eval(l[i]) > eval(l[i + 1]):
                l[i], l[i + 1] = l[i +1], l[i]
                trocou = 1
            i += 1

## Parte 2 – Leitura do arquivo e ordenação da lista
print(str('>>> Exercício 3 – Arquivo com 2000 números ordenados <<<').center(80, '-'),'\n')
arqNome = "NUMEROS.TXT"
arq = open(arqNome,'r')
listaNum = arq.readlines()
arq.close()
ordenaLista(listaNum)

## Parte 3 - Gravação dos números orndenados no arquivo
arqNome = "NUMEROS2.TXT"
arq = open(arqNome,'w')
arq.writelines(listaNum)
arq.close()
print('''\nForam ordenados {0} números aleatórios com sucesso e gravados em "{1}"'''.
      format(len(listaNum), arqNome))

print('\n', str('>>> Fim do exercício 3 <<<').center(80, '-'))
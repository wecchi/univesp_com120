## Definição do problema de negócio
'''
    2. Escreva um programa que grave o arquivo NUMEROS.TXT com 2000 números, um em cada linha, gerados com a
    função randint no intervalo fechado [1, 100.000].

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018.
    9788536530253. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 09 Oct 2020
'''

## Parte 1 - Criação da função para geração dos números aleatórios
from random import randint
def geraNumeros(n):
    listaNum = []
    i = 1
    while i <= n:
        numeroRnd = randint(1, 100000)
        if n not in listaNum:
            listaNum.append(numeroRnd)
            i += 1
    return listaNum

## Parte 2 – Obtenção do range de valores para criação da lista de nímeros
print(str('>>> Exercício 2 – Arquivo com 2000 números aleatórios <<<').center(80, '-'),'\n')
n = int(input('Informe a quantidade de números inteiros aleatórios [1, 100.000]: '))
listaTemp = geraNumeros(n)
# transformando os números da lista em strings com marcador de final de linha
listaNum= []
for i in listaTemp:
    listaNum.append(str(i) + '\n')

## Parte 3 - Gravação dos números no arquivo
arqNome = "NUMEROS.TXT"
arq = open(arqNome,'w')
arq.writelines(listaNum)
arq.close()

print('''\nForam gerados {0} números aleatórios entre 1  e 100.000\n Dados armazenados com sucesso em "{1}"'''.
      format(n, arqNome))
print('\n', str('>>> Fim do exercício 2 <<<').center(80, '-'))
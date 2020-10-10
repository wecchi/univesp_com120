## Definição do problema de negócio
'''
    1. Escreva um programa que leia um número inteiro N e grave em um arquivo em disco todos os números primos
    existentes no intervalo fechado [2, N], um número em cada linha.
    Sugestão: use uma função para determinar se o número é primo

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018.
    9788536530253. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 09 Oct 2020
'''

## Parte 1 - Criação da função para cálculo dos números primos
def checaNumPrimo(n):
    if n <= 1:
        return 'erro'
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        raizNumero = n**0.5
        resto = 1
        i = 3
        while i <= raizNumero and resto !=0:
            resto = n % i
            i += 2
        return resto

## Parte 2 – Obtenção do range de valores para cálculo dos primos
print(str('>>> Exercício 1 – Arquivo de número primo <<<').center(80, '-'),'\n')
n = int(input('Informe um número inteiro para obtenção dos primos: '))
listaNum = []
if n > 2:
    for i in range(2, n + 1):
        if checaNumPrimo(i) == 1:
            listaNum.append(str(i) + ' \n')
else:
    listaNum.append('2 \n')

## Parte 3 - Gravação dos números no arquivo
arqNome = "NumerosPrimos.txt"
arq = open(arqNome,'w')
arq.writelines(listaNum)
arq.close()

print('''Foram encontrados {0} números primos entre 2 e {1}\n Dados armazenados com sucesso em "{2}"'''.
      format(len(listaNum),n, arqNome))
print('\n', str('>>> Fim do exercício 1 <<<').center(80, '-'))
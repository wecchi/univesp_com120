##
'''
    Exercício resolvido 7.1a – Números reais gravados em arquivo com write
    Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0.
    Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha,
    com três casas decimais.

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática.
    Editora Saraiva, 2018. 9788536530253. Disponível em:
    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 08 Oct 2020
'''

## Parte 1 - Criação do aruivo e gravação dos números
print(str('>>> Exercício 7.1a – Números reais gravados em arquivo com write <<<').center(80, '-'),'\n')
arqNome = "ValsReais.txt"           # define o nome do arquivo numa variável
arq = open(arqNome, "w")            # abre o arquivo para gravar
x = float(input('Digite um número Real (para sair digite 0): '))
l = 0
while x !=0:
    arq.write('{0:.3f}\n'.format(x))
    x = float(input('Digite um número Real (para sair digite 0): '))
    l += 1

## Parte 2 – fechamento do arquivo
arq.close()                                 # fecha o arquivo
print('''Foram gravados %d números no arquivo "%s"'''%(l,arqNome))
print('\n', str('>>> Fim do programa 7.1a <<<').center(80, '-'))
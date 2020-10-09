##
'''
    Exercício resolvido 7.1b – Números reais gravados em arquivo com writelines
    Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0.
    Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha,
    com três casas decimais.

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática.
    Editora Saraiva, 2018. 9788536530253. Disponível em:
    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 08 Oct 2020
'''

## Parte 1 - Obtém os dados do usuário
print(str('>>> Exercício 7.1b – Números reais gravados em arquivo com write <<<').center(80, '-'),'\n')
arqNome = "ValsReais2.txt"           # define o nome do arquivo numa variável
listaNum = []
x = float(input('Digite um número Real (para sair digite 0): '))
while x !=0:
    listaNum.append('{0:.3f}\n'.format(x))
    x = float(input('Digite um número Real (para sair digite 0): '))

## Parte 2 – cria arquivo e grava os dados
arq = open(arqNome, "w")            # abre o arquivo para gravar
arq.writelines(listaNum)            # grava a lista toda
arq.close()                         # fecha o arquivo
print('''Foram gravados %d números no arquivo "%s"'''%(len(listaNum),arqNome))
print('\n', str('>>> Fim do programa 7.1b <<<').center(80, '-'))
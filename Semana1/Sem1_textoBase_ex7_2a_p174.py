##
'''
    Exercício resolvido 7.2a – Números reais gravados em arquivo com writelines
    Escreva um programa que leia um arquivo texto contendo um número inteiro em cada linha. Exiba na tela e faça a
    totalização dos valores lidos.

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática.
    Editora Saraiva, 2018. 9788536530253. Disponível em:
    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 08 Oct 2020
'''

## Parte 1 - Leitura do arquivo
print(str('>>> Exercício 7.2a – Leitura de arquivo e totalização de valores <<<').center(80, '-'),'\n')
arqNome = "Inteiros.txt"           # define o nome do arquivo numa variável
somaNum = 0
contNum = 0
arq = open(arqNome, "r")            # abre o arquivo para leitura
linhaNum = arq.readline()
while linhaNum != '':
    num = int(linhaNum)            # converte para inteiro o conteúdo da linha
    somaNum += num                 # acumula a soma
    contNum += 1                   # conta quantidade de linhas (números)
    print('Elemento {0} = {1}'.format(contNum, num))
    linhaNum = arq.readline()      # Lê a próxima linha
## Parte 2 – fecha o arquivo e exibe a soma
arq.close()                         # fecha o arquivo
print('\nSoma = {0}'.format(somaNum))
print('''Foram lidos %d números no arquivo "%s"'''%(contNum,arqNome))
print('\n', str('>>> Fim do programa 7.2a <<<').center(80, '-'))
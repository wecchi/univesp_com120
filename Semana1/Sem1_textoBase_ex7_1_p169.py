##
'''
    Exemplo 7.1 Gravação e leitura de um arquivo texto

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática.
    Editora Saraiva, 2018. 9788536530253. Disponível em:
    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 08 Oct 2020
'''

## Parte 1 - Gravação do arquivo
print(str('>>> Início do programa 7.1 <<<').center(80, '-'),'\n')
G = "Gravação e Leitura de Arquivo Texto"   # carrega o string G
arq = open("Exemplo7_1.txt", "w")           # abre o arquivo para gravar
arq.write(G)                                # executa a gravação da string G
arq.close()                                 # fecha o arquivo

## Parte 2 – Leitura do arquivo gravado na Parte 1
arq = open("Exemplo7_1.txt", "r")           # abre o arquivo para leitura
L = arq.readline()                          # executa a leitura e armazena em L
arq.close()                                 # fecha o arquivo
print("String lido = {}".format(L))         # exibe a string lida
print('\n', str('>>> Fim do programa 7.1 <<<').center(80, '-'))
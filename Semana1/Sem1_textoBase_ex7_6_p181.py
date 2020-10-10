## Definição do problema de negócio
'''
    Exercício resolvido 7.6 – Arquivos texto com codificação conflitante
    Foi criada uma função chamada GravaLe(grava, le) que recebe dois parâmetros aos quais são passados os textos
    “ANSI” ou “UTF-8”, conforme cada caso. Esses parâmetros são utilizados, respectivamente, na gravação e na leitura
    do arquivo. Foi usado um objeto S inicializado com um string que contém diversos caracteres acentuados para
    serem gravados no arquivo

    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018.
    9788536530253. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/.
    Acesso em: 09 Oct 2020
'''

## Parte 1 - Criação da função
def GravaLe(grava, le):
    arqNome = "ArquivoEncoding.txt"  # define o nome do arquivo numa variável
    print("\n--", grava, " para ", le, "-"*29)
    arq = open(arqNome, "w", encoding=grava)
    arq.write(S)
    arq.close()
    arq = open(arqNome, "r", encoding=le)
    L = arq.readlines()
    arq.close()
    for x in L:
        print(x)
        print("-"*50)

## Parte 2 – Abertura, processamento e apresentação dos resultados
print(str('>>> Exercício resolvido 7.6 – Arquivos texto com codificação conflitante <<<').center(100, '-'),'\n')
print("\nDemonstra os conflitos de codificação de arquivos\n\n")

S = """Uma boa porção de caracteres com acento 
Maiúsculas: Á É Í Ó Ú Ã Õ Â Ê Ô À Ç 
Minúsculas: á é í ó ú â ô â ê ô à ç"""

while True:
    print("O que deseja fazer?")
    print(" para gravar ANSI e ler ANSI digite 1")
    print(" para gravar UTF8 e ler UTF8 digite 2")
    print(" para gravar UTF8 e ler ANSI digite 3")
    print(" para gravar ANSI e ler UTF8 digite 4")
    print(" para sair digite 0")
    opc = int(input(" ...opc = "))
    if opc == 0:
        break
    elif opc == 1:
        GravaLe("ANSI", "ANSI")
    elif opc ==2:
        GravaLe("UTF-8", "UTF-8")
    elif opc == 3:
        GravaLe("UTF-8", "ANSI")
    elif opc ==4:
        GravaLe("ANSI", "UTF-8")

print('\n', str('>>> Fim do programa 7.6 <<<').center(100, '-'))
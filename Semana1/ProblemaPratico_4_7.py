def stringCount(filename, strFind):
    '''
        Problema Prático 4.7
        Escreva a função stringCount() que aceita duas entradas de string
            — um nome de arquivo e uma string de alvo
            — e retorna o número de ocorrências da string alvo no arquivo.
    '''
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    countStrFind = content.count(strFind)
    print(countStrFind)
    

stringCount('teste.txt', 'arquivo')

def countLines(filename, strFind):
    '''
        Problema Prático 4.9
        Implemente a função meuGrep(), que toma como entrada duas strings:
            um nome de arquivo e uma string alvo
            e exibe cada linha do arquivo que contém a string alvo como uma substring.

        >>> meuGrep('example.txt', 'line')
        The 3 lines in this file end with the new line character.
        There is a blank line above this line.
    '''
    countLines = 0
    infile = open(filename, 'r')
    for line in infile:
        if line.count(strFind)>0:
            countLines += 1
            print(line, end='')
    infile.close()
    return countLines

print('''\nEncontrado %d linha(s) no arquivo "teste.txt" com a palavra "%s"'''%(countLines('teste.txt', 'separar'),'separar'))

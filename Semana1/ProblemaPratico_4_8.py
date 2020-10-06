def numWords(filename):
    '''
        Problema Prático 4.8
        Escreva a função palavras() que aceita um argumento de entrada
            — um nome de arquivo
            — e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.
            >>> palavras('example.txt')
            ['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',
             'the', 'new', 'line', 'character', 'There', 'is', 'a',
             'blank', 'line', 'above', 'this', 'line']
    '''
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    for i in '''.,;:/?-!'"|_''':
        content = content.replace(i, '')
    lstWords = content.split()
    print(lstWords)
    return len(lstWords)

print(numWords('teste.txt'))

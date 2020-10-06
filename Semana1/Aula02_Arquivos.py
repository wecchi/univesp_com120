def readFile(filename):
    '''
        Lê um arquivo texto, imprime as palavras encontradas no arquivo e retorna
        a quantidade de palavras e o tamanho do arquivo lido
    '''
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)

n_words, n_chars = readFile('teste.txt')

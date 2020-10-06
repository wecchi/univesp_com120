def createFile(filename, contents):
    '''
        Gravando em um Arquivo de TextoPara gravar em um arquivo de texto, este precisa ser aberto para gravação (ou escrita):
        >>> arqSaída = open('teste.txt', 'w')
        Se não houver um arquivo teste.txt no diretório de trabalho ativo, a função open() o criará. Se o arquivo teste.txt já existir,
        seu conteúdo será apagado. Nos dois casos, o cursor apontará para o início do arquivo (vazio).
        (Se quiséssemos acrescentar mais conteúdo ao arquivo (existente), usaríamos o modo 'a' em vez de 'w'.)
    '''
    infile = open(filename, 'w')
    infile.write(contents)
    infile.flush()
    return '''Arquivo "%s" criado com sucesso!'''%filename

createFile('NewFile.txt', 'Se não houver um arquivo NewFile.txt no diretório de trabalho ativo, a função open() o criará.\nSe o arquivo NewFile.txt já existir, seu conteúdo será apagado.\nNos dois casos, o cursor apontará para o início do arquivo (vazio).')

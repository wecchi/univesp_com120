def trocaPU(lstPU):
    '''
        Problema Prático 3.14
        Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
        Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.
        >>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
        >>> trocaPU(ingredientes)
        >>> ingredientes
        ['maçãs', 'açúcar', 'manteiga', 'farinha']
    '''
    UltimoItem = lstPU[-1]
    lstPU[-1], lstPU[0] = lstPU[0], UltimoItem
    

print('\n' + str('>>> Problema Prático 3.14 função para Swith de itens da lista <<<').center(80,'-') )
ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs', 'gelatina', 'abacaxi', 'laranja']
print('lista original: ', ingredientes)
trocaPU(ingredientes)
print('lista trocada (Primeiro/Último): ', ingredientes)


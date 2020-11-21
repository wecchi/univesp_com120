##Ordenar um conjunto antes de realizar a busca permite melhorar o desempenho do algoritmo.
# Busca linear
l = [49, 25, 84, 71, 57, 48, 37, 7, 12, 20, 92, 86, 77, 33, 41, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14, 1, 3]

37 in l  # Existe 7 na lista
l.index(37)  # Retorna a posição em que o elemento 7 encontra-se na lista


def buscaLinear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1


print(str('>>  Busca linear, percorrendo todos os elementos da lista  <<').center(80, '-'))
for i in range(1, 21):
    e = buscaLinear(l, i)
    if e != -1:
        print('''O elemento "{0}" foi encontrado na posição {1}º da lista {2}'''.format(i, e, l))
    else:
        print('''O elemento "{0}" não existe na lista {1}'''.format(i, l))


##Busca binária
# Requer que a lista esteja ordenada
def buscaBinaria(v, i, f, chave):
    if f < i:
        return -1
    m = (i + f) // 2
    if v[m] == chave:
        return m
    elif chave < v[m]:
        return buscaBinaria(v, i, m - 1, chave)
    else:
        return buscaBinaria(v, m + 1, f, chave)


print(str('>>  Busca Binária, percorrendo todos os elementos da lista  <<').center(80, '-'))
l = [49, 25, 84, 71, 57, 48, 37, 7, 12, 20, 92, 86, 77, 33, 41, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14, 1, 3]
l.sort()
for i in range(1, 21):
    e = buscaBinaria(l, 0, len(l)-1, i)
    if e != -1:
        print('''O elemento "{0}" foi encontrado na posição {1}º da lista {2}'''.format(i, e, l))
    else:
        print('''O elemento "{0}" não existe na lista {1}'''.format(i, l))
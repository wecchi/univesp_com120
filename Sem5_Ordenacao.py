"""
    Ziviani, N. Projeto de Algoritmos: com Implementações em Pascal e C – 3ª edição revista e ampliada.
    São Paulo: Cengage Learning Brasil, 2018. 9788522126590.
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788522126590/. Acesso em: 08 Nov 2020

    O aspecto predominante na escolha de um algoritmo de ordenação é o tempo gasto para ordenar um arquivo.
    Para algoritmos de ordenação interna que utilizam o princípio da comparação de chaves, as medidas de complexidade
    relevantes contam o número de comparações entre chaves e o número de movimentações (ou trocas) de itens do arquivo.
    Considere C uma função de complexidade tal que C(n) é o número de comparações entre chaves, e considere M uma função
    de complexidade tal que M(n) é o número de movimentações de itens no arquivo, em que n é o número de itens do
    arquivo. Para algoritmos de ordenação interna que utilizam o princípio da distribuição, a medida de complexidade
    relevante conta o número de vezes que cada chave é manipulada.

    A quantidade extra de memória auxiliar utilizada pelo algoritmo é também um aspecto importante. O uso econômico da
    memória disponível é um requisito primordial na ordenação interna. Os métodos que utilizam a estrutura vetor e
    executam a permutação dos itens no próprio vetor, exceto para a utilização de uma pequena tabela ou pilha, são
    conhecidos como algoritmos que ordenam in situ. Os métodos que utilizam listas encadeadas necessitam de n palavras
    extras de memória para os apontadores, e são utilizados apenas em algumas situações especiais. Os métodos que
    necessitam de quantidade extra de memória para arma-zenar outra cópia dos itens a serem ordenados são importantes
    porque executam em tempo linear na prática.

    Os métodos de ordenação interna que utilizam o princípio da comparação de chaves são classificados em métodos
    simples e métodos eficientes. Os métodos simples são adequados para pequenos arquivos e requerem O(n2) comparações,
    enquanto os métodos eficientes são adequados para arquivos maiores e requerem O(n log n) comparações.
"""

## Programa 4.3 Ordenação por seleção
# [https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/selecao/]
# O algoritmo de ordenação por seleção é um dos métodos de ordenação mais simples que existem. Além disso, o método
# possui um comportamento espetacular quanto ao número de movimentos de registros, cujo tempo de execução é linear no
# tamanho da entrada, o que é muito difícil de ser alcançado por qualquer outro método.
# Como aspectos negativos cabe registrar que:
# (i) o fato de o arquivo já estar ordenado não ajuda em nada, pois o custo continua quadrático;
# (ii) o algoritmo não é estável, pois ele nem sempre deixa os registros com chaves iguais na mesma posição relativa.
# O algoritmo de ordenação por seleção possui complexidade quadrática (O(n2)) no número de elementos do vetor de
# entrada, é um algoritmo in-place, mas não é estável..
import random
def ordenacao_selecao(A):
    n = len(A)
    # Percorre a lista A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]

A = random.sample(range(-20, 21), 20)

print(str('>>  Programa 4.3 Ordenação por seleção  <<').center(100, '-'))
print("\nArranjo não ordenado: ", A)

ordenacao_selecao(A)

print("Arranjo ordenado:", A)


## 4.1.2 Ordenação por Inserção
# Para um vetor A de n números, execute os seguintes passos:
# A cada iteração i do algoritmo, troque de posição o elemento A[i] com cada elemento maior que ele que
# esteja à sua esquerda.
# Seguindo a regra acima, a cada iteração i do algoritmo, todos os elementos à esquerda do índice i estarão ordenados
# e elementos à direita do elemento no índice i ainda não foram processados (podem ser menores, iguais, ou maiores que
# o elemento em A[i]).
# No pior caso, o algoritmo de ordenação por inserção possui complexidade quadrática (O(n2)) no número de elementos do
# vetor de entrada, é um algoritmo in-place e é estável.
def ordenacao_insercao(A):
    n = len(A)
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave


A = random.sample(range(-20, 21), 20)

print(str('>>  Programa 4.4 Ordenação por inserção  <<').center(100, '-'))
print("\nArranjo não ordenado: ", A)

ordenacao_insercao(A)

print("Arranjo ordenado:", A)





## Bubble sort
# A cada iteração comprara cada elemento com seu sucessor [i+1], e troca de lugar caso esteja na ordem incorreta
def bubbleSort(v):
    n = len(v)
    for i in range(n):
        for j in range(n - i - 1):
            if v [ j ] > v[ j + 1 ]:
                v[ j ], v[ j + 1 ] = v[ j + 1 ], v[ j ]


x = [25, 57, 48, 37, 12, 92, 86, 33, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14]
bubbleSort(x)
print(x)


## Insertion sort
# Ordenar o conjunto inserindo os elementos em um subconjunto já ordenado
def insertionSort(v):
    for i in range(1, len(v)):
        chave = v [ i ]
        j = i - 1
        while j >= 0 and v[ j ] > chave:
            v[j + 1] = v[ j ]
            j -= 1
        v[j + 1] = chave


x = [25, 57, 48, 37, 12, 92, 86, 33, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14]
insertionSort(x)
print(x)

## Mergesort
# Também chamado de ordenação por intercalação.
# Ideia básica: dividir para conquistar
# - Um vetor v é dividido em duas partes, recursivamente.
# - Cada metade é ordenada e ambas são intercaladas formando o vetor ordenado.
# - Usa um vetor auxiliar para intercalar.
# No pior caso, o Mergesort possui complexidade O(nlogn) no número de elementos do vetor de entrada, ele é um algoritmo estável, mas não é in-place, pois usa um vetor auxiliar para combinar os sub-vetores ordenados.
#
# Note que a complexidade do Mergesort é inferior à dos algoritmos de ordenação por seleção e inserção. Na verdade,
# como veremos mais à frente, O(nlogn) é a melhor complexidade que podemos obter para um algoritmo de ordenação
# genérico. O Bucketsort e o Radixsort possuem complexidade linear, mas não são algoritmos genéricos eles só funcionam
# para entradas específicas.
def mergeSortJoin(l, r):
    if len(l) == 0:
        return r
    if len(r) == 0:
        return l
    res = []
    idx_l = idx_r = 0
    while len(res) < len(l) + len(r):
        if l[idx_l] <= r[idx_r]:
            res.append(l[idx_l])
            idx_l += 1
        else:
            res.append(r[idx_r])
            idx_r += 1
        if idx_r == len(r):
            res += l[idx_l:]
            break
        if idx_l == len(l):
            res += r[idx_r:]
            break
    return res


def mergeSort(v):
    if len(v) < 2:
        return v
    meio = len(v) // 2
    return mergeSortJoin(
        l = mergeSort(v[:meio]),
        r = mergeSort(v[meio:]))


x = [49, 25, 84, 57, 48, 37, 7, 12, 20, 92, 86, 77, 33, 41, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14, 1, 3]
print(mergeSort(x))


## Quick sort
# Algoritmo também baseado na estratégia de "dividir para conquistar".
# Ideia básica:
# - Dividir o vetor em dois vetores menores que serão ordenados independentemente
#  e combinados para produzir o resultado final.
#
#  No QuickSort, escolhemos um elemento arbitrário (que chamamos de pivô), e particionamos o arranjo de entrada de modo
#  que todos os elementos menores que o pivô apareçam antes dele no arranjo e os elementos maiores que ele apareçam
#  depois dele no arranjo. Assim, o Quicksort pode ser dividida em três etapas:
#   1 Seleção do pivô.
#   2 Particionamento (reorganização) dos elementos do arranjo em torno do pivô.
#   3 Ordenação recursiva das partes obtidas no passo anterior.
#  No pior caso, o Quicksort possui complexidade O(n2) no número de elementos do vetor de entrada, complexidade O(nlogn)
#  no caso médio. Ele não é um algoritmo estável, mas é in-place, pois não usa um vetor auxiliar durante sua execução.
# Na verdade, esta é a grande vantagem do Quicksort sobre o Mergesort: ambos executam em O(nlogn), mas o Quicksort
# executa in-place, ao passo que o Mergesort usa um vetor auxiliar do tamanho do vetor de entrada.

from random import randint
def quickSort(v):
    if len(v) < 2:
        return v
    l, p, h = [], [], []
    pivo = v[len(v)//2]
    for x in v:
        if x < pivo:
            l.append(x)
        elif x == pivo:
            p.append(x)
        elif x > pivo:
            h.append(x)
    return quickSort(l) + p + quickSort(h)


x = [49, 25, 84, 57, 48, 37, 7, 12, 20, 92, 86, 77, 33, 41, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14, 1, 3]
print(quickSort(x))


## Heap sort
# Utiliza uma estrutura heap para ordenar os elementos.
# Um heap é uma estrutura de dados em que há uma ordenação dos elementos: representação via árvore binária.
# Um heap observa conceitos de ordem e de forma:
# - Ordem: o item de qualquer nó deve satisfazer uma relação de ordem com os itens dos nós filhos.
#   -- Heap máximo: pai >= filhos
#   -- Heap mínimo: pai <= filhos
# - Forma: árvore binária tem que ser completa até o penúltimo nível, sendo que no último nível os nós têm
# que estar agrupados à esquerda.
# O heapsort é um algoritmo de ordenação in-place, que possui complexidade assintótica O(nlogn) no pior caso,
# mas que não é estável.

def heapSortArrange(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapSortArrange(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapSortArrange(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapSortArrange(arr, i, 0)


x = [49, 25, 84, 71, 57, 48, 37, 7, 12, 20, 92, 86, 77, 33, 41, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14, 1, 3]
heapSort(x)
print(x)


## O shell sort, às vezes chamaado de “ordenação por incrementos diminutos”, melhora a ordenação por inserção ao quebrar
# a lista original em um número menor de sublistas, as quais são ordenadas usando a ordenação por inserção. A forma
# única como essas sublistas são escolhidas é a chave para o shell sort. Em vez de quebrar a lista em sublistas de itens
# contíguos, o shell sort usa um incremento i, às vezes chamado de gap, para criar uma sublista escolhendo todos os
# itens que estão afastados i itens uns dos outros.

def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
        for i in range(gap, n):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2


x = [49, 25, 84, 71, 57, 48, 37, 7, 12, 20, 92, 86, 77, 33, 41, 10, 30, 31, 15, 50, 60, 5, 22, 35, 14, 1, 3]
shellSort(x)
print(x)

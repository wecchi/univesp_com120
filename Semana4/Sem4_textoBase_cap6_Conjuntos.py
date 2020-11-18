"""
    Luiz, B. S. Python 3 - Conceitos e Aplicações - Uma abordagem didática. São Paulo: Editora Saraiva, 2018.
    9788536530253. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788536530253/. Acesso em: 05 Nov 2020

    https://integrada.minhabiblioteca.com.br/#/books/9788536530253/pageid/144

"""
##Exemplo 6.2 Conjuntos
# Cria um conjunto (set) com 5 elementos

# Opção direta
c_a = {1, 2, 3, 4 ,5}
print(c_a)
print(type(c_a))
print(len(c_a))

#Opção com construtor
c_b = set('12345')
print(c_b)
print(type(c_b))
print(len(c_b))

#Se as chaves forem coladas sem conteúdo, Phyton cria um dictionary
c_c = {}
print(c_c)
print(type(c_c))
print(len(c_c))

##Exemplo 6.4 Operações com conjuntos
a,b = set('abacaxi'), set('abacate')
print("A = ", a)
print("B = ", b)
print("A - B = ", a - b)
print("B - A = ", b - a)
print("A ∪ B = ",a | b)
print("A ∩ B = ",a & b)
print("A Δ B = (A∪B)−(A∩B) = ",a ^ b)


##Exemplo 6.5 Métodos com conjuntos
a,b = set('abacaximexiricapapaia'), set('abacatemelanciaameixa')
print("A =", a)
print("B =", b)

#Adiciona um elemento
a.add('y')
print("A.add(y) =", a)

#Limpa o conjunto
a.clear()
print("A.clear() =", a)
a = set('abacaximexiricapapaiay')

#Retorna uma cópia do conjunto
print("A.copy() =", a.copy())

#Retorna um novo conjunto contendo a diferença de dois ou mais conjuntos.
print("A.difference(B) =", a.difference(b))
print("B.difference(A) =", b.difference(a))

# Atualiza o conjunto, removendo de seus elementos os que estejam no conjunto passado como parâmetro.
a.difference_update(b)
print("A.difference_update(B) =", a)
a = set('abacaximexiricapapaiay')
b.difference_update(a)
print("B.difference_update(A) =", b)
b = set('abacatemelanciaameixa')

#Se parâmetro estiver presente no conjunto, então o remove, caso não esteja não faz nada.
a.discard('m')
print("A.discard(m) =", a)
b.discard('m')
print("B.discard(m) =", b)

#Retorna um novo conjunto contendo a interseção de dois ou mais conjuntos.
print("A.discard(B) =", a.intersection(b))

#Atualiza o conjunto com a interseção entre seus elementos e o conjunto passado como parâmetro.
a.intersection_update(b)
print("A.intersection_update(B) =", a)

#Retorna True se os dois conjuntos têm interseção vazia e False, caso contrário
print("A.isdisjoint(B) =", a.isdisjoint(b))

#Retorna True se é um subconjunto do conjunto passado como parâmetro.
print("A.issubset(B) =", a.issubset(b))

#Retorna True se está contido no conjunto passado como parâmetro.
print("B.issuperset(A) =", b.issuperset(a))
print("A.issuperset(B) =", a.issuperset(b))


#Remove e retorna um elemento arbitrário do conjunto. Se o conjunto estiver vazio, gera uma exceção KeyErro
print("A.pop() =", a.pop())
print("B.pop() =", b.pop())

#Remove do conjunto um elemento que seja seu membro. Caso contrário, gera uma exceção KeyError
a.remove('x')
print("A.remove(x) =", a)
b.remove('t')
print("B.remove(t) =", b)

#Retorna a diferença simétrica de seus elementos com o conjunto passado como parâmetro
print("A.symmetric_difference(B) =", a.symmetric_difference(b))

#Atualiza o conjunto com a diferença simétrica de seus elementos com o conjunto passado como parâmetro.
b.symmetric_difference_update(a)
print("B.symmetric_difference_update(A) =", b)

#Retorna um novo conjunto com a união de C e o conjunto passado como parâmetro
print("A.union(B) =", a.union(b))

#Atualiza o conjunto C com a união de sim, mesmo com o conjunto passado como parâmetro.
b.update(a)
print("B.update(A) =", b)

##Exercício resolvido 6.1 – Operações com conjuntos
Msg = "Digite Valor: " 
print("Dados do primeiro conjunto")
C1 = set()
x = int(input(Msg)) 
while x != 0:
    C1.add(x)
    x = int(input(Msg)) 
print("Dados do segundo conjunto")
C2 = set()
x = int(input(Msg)) 
while x != 0: 
    C2.add(x) 
    x = int(input(Msg)) 
print("Conjunto 1: {}".format(C1))
print("Conjunto 2: {}".format(C2))
print("União de C1 e C2", C1 | C2)
print("Interseção de C1 e C2", C1 & C2)
print("\nFim do programa")


## Conjuntos complementares Considere que todos os valores no intervalo fechado [1, 60] devam ser divididos em dois
# grupos, A e B, de 30 valores cada, de maneira aleatória. É importante que um valor que está em A não esteja em B, e
# vice-versa, bem como que todos os valores do intervalo estejam em algum grupo.
from random import randint
A = set()
while len(A) < 30:
    A.add(randint(1, 60))
    
B = set(range(1, 61)) - A
print("Conjunto A: {}".format(A))
print("Conjunto B: {}".format(B))
print("\nFim do programa")


##Dicionários - O modo mais elementar de inserir um par chave:valor em um dicionário é criar uma expressão
# D[chave] = valor. Se a chave não existir, ocorrerá a inserção. Essas operações estão feitas no bloco 1 do Exemplo 6.8.
# No bloco 2 foi utilizado o método fromkeys para gerar um dicionário a partir de uma tupla preexistente.
# Cada elemento da tupla foi utilizado como chave e, se o segundo parâmetro opcional for utilizado, ele será o valor
# atribuído a todos os membros. No exemplo, fromkeys é utilizado duas vezes, sem e com o segundo parâmetro

# bloco 1 >>>
a = {}
a['k1'] = 'Valor 1'
a['k2'] = 'qq.coisa’'
print(a)
a['k2'] = 'Valor 2'
print(a)

# bloco 2 >>>
t = (16, 12, 25, 14)
b = dict.fromkeys(t)
print(b)
b = dict.fromkeys(t,0)
print(b)

# bloco 3 >>>
c = {'Nome':'Pedro', 'Idade':32, 'Profissão': 'Professor'}
print(c)
print(c.keys())
print(c.values())
print(c.items())

# bloco 4 >>>
d = {'Local':'FATEC-SP', 'Cidade':'São Paulo', 'Idade':42}
print(d)
d.update(c)
print(d)


## Construção de um dicionário e exibição de seus dados Escreva um programa que leia do teclado o código de uma peça
# e a quantidade disponível no estoque. Esses dois dados de entrada são números inteiros. Acrescente o par
# código:quantidade em um dicionário apenas se o código não estiver presente. Caso esteja, dê uma mensagem informando
# essa situação e descarte os dados. O laço termina quando for fornecido 0 para o código. Exibir na tela os dados do
# dicionário, um membro por linha.
pecas = {}
print("Leitura dos dados")
while True:
    cod = input(" Digite o código: ")
    if cod == '0':
        break # interrompe o laço se cod == 0
    elif cod in pecas:
        print(" A peça {} já está no cadastro".format(cod))
        continue
    qtde = int(input(" Digite a quantidade: "))
    pecas[cod] = qtde # próxima iteração se cod in pecas # acrescenta novo item ao dicionário
print("Fim da leitura dos dados\n")
print("Estoque de peças")
for c in pecas:
    print(" {1:4} unidades da peça {0}".format(c, pecas[c]))
print("\nFim do programa")


##Escreva um programa que permaneça em laço efetuando a leitura dos seguintes dados: número de matrícula, nome do aluno,
# idade e curso. O número de matrícula é a chave, e os demais dados constituem o valor. Faça a leitura desses dados e
# construa o dicionário enquanto não for digitado zero para o número de matrícula
alunos = {}
n = 0
print(str('Início da leitura dos dados').center(80,'-'))
while True:
    n += 1
    matricula = int(input('Matrícula do aluno Nº{}: '.format(n)))
    if matricula == 0:
        break
    elif matricula in alunos:
        print(' *** A matrícula {} já está no cadastro! ***'.format(matricula),"\n")
        n -= 1
        continue
    nome = input('Nome do aluno: ')
    idade = input('Idade do aluno: ')
    curso = input('Curso: ')
    alunos[matricula] = (nome, idade, curso)
print(str('Fim da leitura dos dados').center(80,'-'))

print('\nCadastro dos alunos')
print('{0:20} {1:4} {2:4} {3}'.format('Nome', 'Matrícula', 'Idade', 'Curso'))
for m, d in alunos.items():
    print('{0:20} {1:9}    {2} {3}'.format(d[0], m, d[1], d[2]))


##Métodos com Dicionário
# D.clear( ) - Remove todos os elementos do dicionário.

# D.copy( ) - Retorna uma cópia do dicionário

# D.fromkeys(i, v=None) - Recebe o iterável i como parâmetro e retorna um novo dicionário tendo os elementos do
# iterável como chave. Se o segundo parâmetro (opcional) for fornecido, cada valor será inicializado com ele.

# D.get(k [,d]) - Retorna o valor associado com a chave k passada como parâmetro. Caso a chave não esteja presente,
# retorna o segundo parâmetro (opcional) e, na ausência deste, retorna None (na prática não faz nada).

# D.items( ) - Retorna um conjunto contendo os itens do dicionário (o par chave:valor). Esse retorno é do tipo
# dict _ items e se assemelha ao tipo set, podendo ser utilizado como tal.


# D.keys( ) - Retorna um conjunto contendo as chaves do dicionário. Esse retorno é do tipo dict _ keys e se assemelha
# ao tipo set, podendo ser utilizado como tal.


# D.pop(k [,d]) - Remove a chave k e retorna o valor a ela associado. Caso k não esteja presente, o segundo parâmetro
# (opcional) é retornado e, na ausência deste, gera a exceção KeyError.

# D.popitem( ) - Remove do dicionário e retorna um par chave:valor arbitrário. Se o dicionário estiver vazio, gera
# a exceção KeyError.

# D.setdefault(k [,d]) - Se a chave k estiver presente, seu retorno funciona como um get(k, d).
# Caso contrário, inclui o par k:d no dicionário, em que d é opcional e, em sua ausência, é utilizado None.
# Esse método representa uma maneira alternativa de inicializar um dicionário.
#
# D.update(E)- Atualiza o dicionário D a partir dos itens contidos no dicionário E. Se algum item de E não estiver em D,
# então, será incluído, e caso esteja será atualizado. O parâmetro E também pode ser uma lista ou tupla que contenha
# seus elementos na forma (e1, e2).

# D.values( )- Retorna um conjunto contendo os valores do dicionário. Esse retorno é do tipo dict _ values e se
# assemelha ao tipo set, podendo ser utilizado como tal.


## 3. Escreva um programa que permaneça em laço lendo números inteiros do teclado. Esse laço termina quando for
# digitado zero ou qualquer valor negativo. O programa deve contar quantas vezes cada valor positivo foi digitado.
# Ao término do laço de leitura o programa deve mostrar quais valores foram digitados e quantas vezes cada um.
# Use um dicionário para resolver esse problema
numeros = {}
print(str('Início da leitura dos números').center(80,'-'))
while True:
    n = int(input('Nº '))
    if n <= 0:
        break
    else:
        numeros[n] = (numeros[n] + 1) if n in numeros else 1

print('\nLista dos números')
print('       Nº   Ocorrências')
for n, q in numeros.items():
    print('{0:8} {1:5}'.format(n, q))

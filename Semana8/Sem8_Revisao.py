## Funções simples
def f(x, y):
    # A função só troca os valores internamente, para quem a chamou nada muda
    y, x = x, y


def g(lista):
    # A função troca o 1º elemento da lista pelo número 9
    lista[0] = 9


print('\n', str('>>> tentativa de alteração de valor de variável <<<').center(80, '-'), sep='')
x, y = 2, 3
f(x, y)
print(x, y)

print('\n', str('>>> alteração de uma lista por uma função <<<').center(80, '-'), sep='')
l = [1, 2, 3]
g(l)
print(l)


## Função recursiva: é aquela definida em seus próprios termos
def soma(v, i):
    if i == 0:
        return v[0]
    else:
        return v[i] + soma(v, i - 1)


print('\n', str('>>> soma de elementos por uma função recursiva <<<').center(80, '-'), sep='')
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soma(l, len(l) - 1))


## Programação Orientada a Objeto - POO
class Point:
    '''
        Representação de ponto num plano cartesiano
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return '({0}, {1})'.format(self.x, self.y)

    def move(self, offSetX, offSetY):
        self.x += offSetX
        self.y += offSetY

    def reset(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        'representação de string canônica'
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __str__(self):
        'representação de string elegante'
        return 'Point(x = {0}, y = {1})'.format(self.x, self.y)

    # x + y, se (2,3) + (2,2) = (4,5)
    # x + y, se (2,3) + 8     =(10,11)
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x,
                         self.y + other.y)
        else:
            return Point(self.x + other,
                         self.y + other)

    def __eq__(self, other):
        if type(other) == Point:
            return ((self.x == other.x) and (self.y == other.y))
        else:
            return False

    def distancia(self, other):
        if type(other) == Point:
            d = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
            return d
        else:
            return 'Na'

    def up(self):
        Point.move(self, 0, 1)

    def down(self):
        Point.move(self, 0, -1)

    def left(self):
        Point.move(self, -1, 0)

    def right(self):
        Point.move(self, 1, 0)


# Herança - Criando a Classe Point3D com a coordenada z:
class Point3D(Point):
    def __init__(self):
        super(Point3D, self).__init__()
        self.z = 0

    def setz(self, z):
        self.z = z

    def get(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)

    def move(self, offSetX, offSetY, offSetZ):
        super().move(offSetX, offSetY)
        self.z += offSetZ

    def __str__(self):
        'representação de string elegante'
        return 'Point3D(x = {0}, y = {1}, z = {2})'.format(self.x, self.y, self.z)


print('\n', str('>>> Usando herança em POO <<<').center(80, '-'), sep='')
r = Point3D()
r.setx(1)
r.sety(2)
r.setz(3)
print(r)
r.move(1, 2, 3)
print(r)


## Pilhas e filas
class Pilha():
    """
    LIFO (UEPS): o termo se refere a Last in, first out ou Último a entrar, primeiro a sair, em português.
    Nessa estratégia, o produto mais recente no estoque (com menor tempo de armazenagem) é despachado primeiro.
    Com isso, pode haver divergência entre o custo da mercadoria vendida e o custo do estoque remanescente, já
    que nem sempre é possível pagar o mesmo preço por lotes distintos de produtos.
    """

    def __init__(self):
        self.data = []

    def push(self, elemento):
        self.data.append(elemento)

    @property
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        else:
            return None

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    def empty(self):
        return len(self.data) > 0


class Fila():
    """
    FIFO (PEPS): FIFO é uma sigla para First in, first out ou Primeiro a entrar, primeiro a sair, na tradução
    em português. Trata-se de uma estratégia de gestão de estoque na qual os produtos que estão armazenados há mais
    tempo são despachados primeiro para os consumidores. Isso garante que o custo da mercadoria vendida e o custo do
    estoque remanescente sejam correspondentes.
    """

    def __init__(self):
        self.data = []

    def push(self, elemento):
        self.data.append(elemento)

    @property
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        else:
            return None

    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    def empty(self):
        return len(self.data) > 0


print('\n', str('>>> Usando Pilha: FIFO <<<').center(80, '-'), sep='')
p = Pilha()
for i in range(5, 101, 5):
    p.push(i)
print(p.data)
print(p.pop)
print(p.top())

print('\n', str('>>> Usando Fila: FIFO <<<').center(80, '-'), sep='')
f = Fila()
for i in range(5, 101, 5):
    f.push(i)
print(f.data)
print(f.pop)
print(f.top())

## Árvores binárias de busca
"""
    Grau - Cada nó possui no máximo 2 elementos filhos
    Ordem - Se a árvore for binária de busca: o elemento à esquerda de um nó deve ter valor menor que o nó e o elemento
    da direita de um nó deve ter valor maior que o nó em questão.
    Busca eficiente em árvores balanceadas - poucas consultas nLog
    Conceitos para remoção de nós:
    1 - O nó e folha e não possui filhos: remove o nó
    2 - O nó possui um único filho: remove o nó e "sobe" o filho para o lado correspondente (se maior que novo nó pai,
    ficará na esquerda, se menor ficará na direita)
    3 - O nó possui os dois filhos: encontre o maior nó da sub-arvore da esquerda do nó que está sendo removido, e o
    coloque no lugar de seu ancestral. Depois aplica as regras 1, 2 e 3 para os filhos desse nó que foi movido para cima
"""


class Node():
    def __init__(self, value=None):
        self.key = value
        self.left = None
        self.right = None

    def add(self, key):
        """
            Adiciona um novo nó para uma árvore binária de busca
        """
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.add(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.add(key)
        else:
            self.key = key

    def get(self, key):
        """
            Retorna uma referência ao nó solicitado
        """
        if self.key == key:
            return self
        else:
            node = self.left if key < self.key else self.right
            if node is not None:
                return node.get(key)
            else:
                return None

    def printTreeIn(self):
        """
        Imprime os nós da árvore usando busca Simétrica (ou em Ordem)
        :return:
        """
        if self.left:
            self.left.printTreeIn()
        print(self.key, end="-")
        if self.right:
            self.right.printTreeIn()

    def printTreePre(self):
        """
        Imprime os nós da árvore usando busca Pré-ordem (ou em Ordem Polonesa)
        :return:
        """
        print(self.key, end="-")
        if self.left:
            self.left.printTreePre()
        if self.right:
            self.right.printTreePre()

    def printTreePos(self):
        """
        Imprime os nós da árvore usando busca Pós-ordem (ou em Ordem Polonesa inversa)
        :return:
        """
        if self.left:
            self.left.printTreePos()
        if self.right:
            self.right.printTreePos()
        print(self.key, end="-")


print('\n', str('>>> Usando Árvore <<<').center(80, '-'), sep='')

from random import randint
# Gerando uma lista com 22 elementos aleatórios (letras)
lista = [chr(randint(65, 89)) for x in range(1, 23)]
# Crio o 1º nó sendo o item 10 da lista, poderia ser qualquer um
Tree = Node(lista[10])
# Vamos inserir os demais itens da lista na árvore
for i in lista:
    Tree.add(i)

print("⇒ Em ordem:")
Tree.printTreeIn()
print("\n⇒ Em Pré-ordem (Polonesa):")
Tree.printTreePre()
print("\n⇒ Em Pós-ordem (Polonesa inversa:)")
Tree.printTreePos()
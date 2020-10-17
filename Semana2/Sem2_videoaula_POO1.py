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
        return '({0}, {1})'.format(self.x ,self.y)

    def move(self, offSetX, offSetY):
        self.x += offSetX
        self.y += offSetY

    def reset(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        'representação de string canônica'
        return 'Point({0}, {1})'.format(self.x ,self.y)

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

    #8.12 Inclua o método distância() à classe Ponto.
    # Ele apanha outro objeto Ponto como entrada e retorna a distância té esse ponto
    # (a partir do ponto chamando o método).
    def distancia(self,other):
        if type(other) == Point:
            d = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
            return d
        else:
            return 'Na'

    #8.14 Acrescente à classe Ponto os métodos up(), down(), left() e right(), que movem o objeto Ponto em 1 unidade
    # na direção apropriada. A implementação de cada um não deverá modificar as variáveis de instância x e y
    # diretamente, mas indiretamente, chamando o método move() existente.
    def up(self):
        Point.move(self, 0, 1)

    def down(self):
        Point.move(self, 0, -1)

    def left(self):
        Point.move(self, -1, 0)

    def right(self):
        Point.move(self, 1, 0)


##Problema Prático 8.8
# Implemente a classe Vetor, que aceita os mesmos métodos da classe Ponto que desenvolvemos na Seção 8.4.
# A classe Vetor também deverá aceitar a adição de vetor e operações de produto. A adição de dois vetores

class Vector(Point):
    def __repr__(self):
        'representação de string canônica'
        return 'Vector({0}, {1})'.format(self.x, self.y)

    def __str__(self):
        'representação de string elegante'
        return 'Vector(x = {0}, y = {1})'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x,
                         self.y + other.y)
        else:
            return Vector(self.x + other,
                         self.y + other)

    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

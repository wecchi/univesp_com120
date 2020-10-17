from random import shuffle
'''
    Estudo do capítulo 8:
    Ljubomir, P. Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações. 
    São Paulo: Grupo GEN, 2016. 9788521630937. 
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788521630937/. Acesso em: 17 Oct 2020
'''

##Classe Animal
# Desenvolver uma nova classe, chamada Animal, que abstrai animais e aceita três métodos:
# •setEspécie(espécie): define a espécie do objeto animal como espécie.
# •setLinguagem(linguagem): define a linguagem do objeto animal como linguagem.
# •fala(): apresenta uma mensagem do animal, como mostramos em seguida.

class Animal:
    'Representa um animal'

    def __init__(self, Especie='', Linguagem=''):
        'Constroi o objeto animal'
        self.especie = Especie
        self.linguagem = Linguagem

    def setLinguagem(self, Linguagem):
        'Define o idioma (fala) do animal'
        self.linguagem = Linguagem

    def setEspecie(self, Especie):
        'Define a espécie do animal'
        self.especie = Especie

    def speak(self):
        'Exibe a sentença do animal'
        return 'Eu sou um {0} e sei {1}'.format(self.especie, self.linguagem)

    #8.13 Inclua na classe Animal os métodos setIdade e getIdade() e defina e recupere a idade do objeto Animal.
    def setIdade(self, anos):
        self.idade = anos

    def getIdade(self):
        return self.idade


class Ave(Animal):
    'Representa uma ave - subclasse de Animal'
    def speak(self):
        return '{}!'.format(self.linguagem * 3)

## Problema Prático 8.3
# Implemente a classe Retângulo, que representa retângulos.
# A classe deverá implementar estes métodos:
# •setTamanho(largura, comprimento): aceita dois valores numéricos como entrada e define o comprimento e largura do retângulo.
# •perímetro(): retorna o perímetro do retângulo.
# •área(): retorna a área do retângulo.

class Retangulo:
    'Representa um retângulo'

    #8.15 Inclua um construtor à classe Retângulo de modo que o comprimento e a largura do retângulo possam ser
    # definidos no momento em que o objeto Retângulo é criado. Use valores padrão de 1 se o comprimento ou largura
    # não forem especificados.
    def __init__(self, largura = 1, comprimento = 1):
        'Constroi um objeto retângulo'
        self.l = largura
        self.c = comprimento

    def setTamanho(self, largura, comprimento):
        'Define as dimensões do retângulo'
        self.l = largura
        self.c = comprimento

    def perimetro(self):
        'Calcula o perímetro do retângulo'
        return 2 * (self.l + self.c)

    def area(self):
        'Calcula a área do retângulo'
        return self.c * self.l

    def __repr__(self):
        return '[{0:.3f} x {1:.3f}]'.format(self.c,self.l)


##Jogando com a Classe Carta
# Desenvolver uma classe Carta para representar jogos de carta; deverá admitir um construtor de dois argumentos
# para criar objetos Carta, exemplo: carta = Carta('3', '\u2660')
# A string '\u2660' é a sequência de escape que representa o caractere Unicode♠.
# Queremos que a classe Carta aceite estes métodos:
# •Carta(valor, naipe): construtor que inicializa o valor e o naipe da carta.
# •pegaValor(): retorna o valor da carta.
# •pegaNaipe(): retorna o naipe da carta.

class Carta:
    'Representa uma carta do baralho'

    def __init__(self, valor, naipe):
        'Constroi a carta'
        self.v = valor
        self.n = naipe

    def pegaValor(self):
        'Informa o valor da carta'
        return self.v

    def pegaNaipe(self):
        'Informa o naipe da carta'
        return self.n

    def __repr__(self):
        # Problema Prático 8.6 Implemente operadores sobrecarregados repr() e == para a classe Carta.
        # Sua nova classe Carta deverá se comportar como a seguir:
        # >>> Carta('3', '♠') == Carta('3', '♠')
        return """Carta('{0}', '{1}')""".format(self.v, self.n)

    def __str__(self):
        return self.v + self.n

    def __eq__(self, other):
        if type(other) == Carta:
            return ((self.v == other.v) and (self.n == other.n))
        else:
            return False

    #8.17 Sobrecarregue operadores apropriados para a classe Carta de
    # modo que você possa comparar as cartas com base no valor
    def __gt__(self, other):
        'Sobrecarrecando o operador de >'
        if type(other) == Carta:
            return (self.v > other.v)
        else:
            return 'Na'

    def __ge__(self, other):
        'Sobrecarrecando o operador de >='
        if type(other) == Carta:
            return (self.v >= other.v)
        else:
            return 'Na'

    def __lt__(self, other):
        'Sobrecarrecando o operador de <'
        if type(other) == Carta:
            return (self.v < other.v)
        else:
            return 'Na'

    def __le__(self, other):
        'Sobrecarrecando o operador de <='
        if type(other) == Carta:
            return (self.v <= other.v)
        else:
            return 'Na'


##Criando uma Classe que Representa um Baralho de Cartas
#Os métodos que a classe Baralho deverá implementar são:
# •Baralho(): construtor que inicializa o baralho para conter um baralho padrão de 52 cartas de jogo.
# •embaralhar(): misturar as cartas do baralho de maneira aleatória.
# •pegarCarta(): retira e retorna a carta no topo do baralho.

class Baralho:
    'Representa um objeto baralho'
    # valores e naipes são variáveis da classe Baralho, para compor a tupla
    # Problema Prático 8.5 Modifique o construtor da classe Baralho de modo que a classe também possa ser usada
    # para jogos de carta que não usam o baralho padrão de 52 cartas.
    # Para esses jogos, precisaríamos oferecer a lista de cartas explicitamente no construtor.
    valores = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    # naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, valores = None):
        'Construtor do objeto baralho'
        self.cartas = []

        if valores == None:
            valores = Baralho.valores
        for naipe in Baralho.naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, naipe))

    def pegarCarta(self):
        'Retorna a carta do "topo" a remove do das cartas'
        return self.cartas.pop()

    def embaralhar(self):
        'Mistura as cartas aleatoriamente'
        shuffle(self.cartas)

    def __repr__(self):
        'Representação de string canônica'
        return 'Baralho({})'.format(self.cartas)

    def __str__(self):
        'Representação de string elegante, usada no método print()'
        return 'Baralho(N={0})'.format(len(self.cartas))

    def __eq__(self, other):
        'Implementação do método de comparação - somente válido para mesma classe'
        if type(other) == Baralho:
            return self.cartas == other.cartas
        else:
            return False

    def __len__(self):
        'Implementação do método de tamanho (quantidade de cartas do baralho)'
        return len(self.cartas)


##Classe Contêiner Queue
# Queue (queue) é um tipo de contêiner que abstrai uma fila, como uma fila de compradores em um supermercado,
# aguardando no caixa. Em uma fila desse tipo, os clientes são atendidos em um padrão do tipo “primeiro a entrar,
# primeiro a sair (FIFO — first-in, first-out). Um cliente se posicionará no final da fila e a primeira pessoa na fila
# é a próxima a ser atendida pelo caixa. Geralmente, todas as inserções são feitas ao final da fila, e todas as
# retiradas devem ser pela frente:

class Queue:
    'Fila de coisas'
    def __init__(self, q = None):
        'Instância um objeto fila'
        if q == None:
            self.q = []
            self.n = 0
        else:
            self.q = q
            self.n = len(q)

    def isEmpty(self):
        'Retorna True se a fila estiver vazia'
        return (self.n==0)

    def enQueue(self, item):
        'Insere um item na fila'
        if item not in self.q:
            self.q.append(item)
            self.n += 1

    def deQueue(self):
        'Exibe e remove o primeiro item da fila'
        if len(self.q) > 0:
            self.n -= 1
            return self.q.pop(0)
        else:
            return 'Na'

    def __len__(self):
        'Retorna o tamanho da fila'
        return len(self.q)

    def __repr__(self):
        'Representação de string canônica'
        if (self.n > 0):
            strlist = ''
            for i in self.q:
                strlist += """, '{}'""".format(i)
            return 'Queue([{0}])'.format(strlist[2:])
        else:
            return 'Queue([])'

    def __str__(self):
        'Representação de string elegante - usado com print()'
        if (self.n > 0):
            return 'This is a queue with {0} items!'.format(len(self.q))
        else:
            return 'Was no items in this queue!'

    def __eq__(self, other):
        'método para comparar se duas filas são iguais'
        if type(other) == Queue:
            return self.q == other.q
        else:
            return False

    def __getitem__(self, key):
        'operador de indexação para obter o item de uma Queue no índice - key exemplo filaCaixa2[3]'
        return self.q[key]

    def __iter__(self):
        'retorna o iterador de Queue - a ser usado de trás para frente'
        return QueueIterator(self)


# Iteradores e Padrões de Projeto POO Python aceita a iteração por todos os contêineres embutidos que já vimos:
# strings, listas, dicionários, tuplas e conjuntos.
class QueueIterator:
    'iterador para a classe de contêiner Queue'

    def __init__(self, q):
        self.indice = len(q) - 1
        self.q = q

    def __next__(self):
        ''' Sobrescrevendo o iterador para percorrer a lista do final para o início'
        retorna próximo item de Queue; se não houver item seguinte, levanta exceção StopIteration '''
        if self.indice < 0:
            raise StopIteration()

        # Retorna o próximo item
        item = self.q[self.indice]
        self.indice -= 1
        return item


## Herdando Atributos de uma Classe
# Seria muito conveniente ter uma classe que se comporte exatamente como a classe embutida list.
# A classe Queue que desenvolvemos nas Seções 8.3 e 8.4 é apenas um modo de projetar e implementar uma classe de fila.
# Criar a classe Queue de modo que cada objeto Queue seja um objeto list (subclasse de list):

class Queue2(list):
    'Uma classe herdando list, ou subclasse de list'
    def isEmpty(self):
        return (len(self) == 0)

    def deQueue(self):
        if len(self) == 0:
            raise EmptyQueueError('Remoção de uma fila vazia!')
        return self.pop(0)

    def enQueue(self, item):
        return self.append(item)


# Melhorando o Encapsulamento da Classe Queue2
# Vamos definir uma nova classe de exceção EmptyQueueError e reimplementar o método dequeue() de modo que levante
# uma exceção desse tipo se ele for invocado sobre uma fila vazia.
class EmptyQueueError(Exception):
    'Classes de Exceção Definidas pelo Usuário'
    pass


##Problema Prático 8.11
# Desenvolva a subclasse listaEstranha de list que se comporta exatamente como uma lista,
# exceto pelo comportamento peculiar do laço 'for'de iteração pula itens alternadamente na lista

class listaEstranha(list):
    def __iter__(self):
        'retorna o iterador Estranho'
        return EstranhoIterator(self)


class EstranhoIterator:
    def __init__(self, l):
        self.indice = 0
        self.l = l

    def __next__(self):
        if self.indice == len(self.l):
            raise StopIteration()
        # Retorna o próximo item
        item = self.l[self.indice]
        self.indice += 2
        return item

    def __repr__(self):
        print(self)
import random
"""
    Fila
    Definição: estrutura para armazenar um conjunto de elementos, que funciona da seguinte forma:
    - Novos elementos sempre entram no fim da fila
    - O único elemento que pode ser retirado da fila, em um determinado momento, é seu primeiro elemento

    Para que serve?
    Modelar situações em que é preciso armazenar um conjunto ordenado de elementos, no qual o primeiro
    elemento a entrar no conjunto será também o primeiro elemento a sair, e assim por diante - FIFO.
    Exemplo: filas do mundo real: em bancos, aguardando para ser atendido, por exemplo
"""


class fila():

    def __init__(self):
        self.data = []

    def inserir(self, x):
        """insere um elemento no fim da fila"""
        self.data.append(x)

    def remover(self):
        """remove o primeiro elemento da fila"""
        if len(self.data) > 0 :
            return self.data.pop(0)

    def top(self):
        """consulta o próximo item a ser atendido"""
        if len(self.data) > 0 :
            return self.data[0]

    def empty(self):
        """verifica se a fila está vazia"""
        return len(self.data) == 0


# Exercício: Implementar um programa de gerenciamento de duas filas em um banco: prioritária e normal.
# Seu programa deverá permitir que pessoas sejam inseridas no fim de cada fila, dependendo da idade de cada uma
# (acima de 60 anos entra na fila prioritária).
# A saída de pessoas da fila deve ocorrer da seguinte forma: a cada duas pessoas que saem da
# fila prioritária, uma sai da fila normal


class filaBanco:

    """Classe fila do Banco"""
    def __init__(self):
        self.prioritaria = fila()
        self.normal = fila()
        self.contaP = 0


    def retiraSenha(self, cliente, acima60):
        """Cliente se identifica e retira uma senha"""
        if acima60:
            senha = 'P' + str(random.randint(1, 1000))
            x = {senha: cliente}
            self.prioritaria.inserir(x)
        else:
            senha = 'N' + str(random.randint(2000, 9000))
            x = {senha: cliente}
            self.normal.inserir(x)


    def chamaSenha(self):
        if (self.contaP < 2) and (not self.prioritaria.empty()):
            self.contaP += 1
            return self.prioritaria.remover()
        elif not self.normal.empty():
            self.contaP = 0
            return self.normal.remover()
        else:
            return 'Todos os clientes já foram atendidos'


    def empty(self):
        return self.normal.empty() and self.prioritaria.empty()


# Criando objeto fila do banco
filaBancoBrasil = filaBanco()


# Gerando uma massa de dados aleatória com 200 clientes
# Fonte: https://data.world/alexandra/baby-names
infile = open('names.csv', 'r')
content = infile.readlines()
infile.close()
random.shuffle(content)
content = random.sample(content, 500)
for c in content:
    # Cria randomicamente perfil idoso
    idoso = bool(random.randint(0, 1))
    # Adiciona o cliente na fila do banco
    filaBancoBrasil.retiraSenha(c.split(',')[0], idoso)

while not filaBancoBrasil.empty():
    x = filaBancoBrasil.chamaSenha()
    # Obtendo a senha e o cliente do Dicionário
    senha, cliente = next(iter(x.items()))
    print('Senha: {0}; cliente: {1}'.format(senha, cliente))

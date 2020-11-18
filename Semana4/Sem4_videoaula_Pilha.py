class pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        'operação para empilhar um elemento'
        self.data.append(x)

    def pop(self):
        'operação que retira o elemento do topo, desempilha'
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):
        'acessa o elemento do topo sem desempilhá-lo'
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        'verifica se a pilha está vazia'
        return not len(self.data) > 0


# Implementar um programa em Python que realiza a conversão decimal para binário usando pilha

# criando o objeto pilha e inciando um número qualquer
p = pilha()
num = 43692
print('O número ({0})₁₀ convertido para binário é: ('.format(num), sep='', end='')

# empilhando os restos da divisão por 2
while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

#desempilhando os restos para apresentar a conversão do binário
while not p.empty():
    print(p.pop(), sep='', end='')

print(')₂ - esta conversão foi calculada através do conceito de pilha')
## Pergunta 1: Cálculo de número fatorial - função recursiva
def f1(n):
    if n <= 1:
        return 1
    else:
        return n * f1(n - 1)


print(f1(4))
#24 - Fatorial de 4

## Pergunta 3: Cálculo do número de Fibonnacci - função recursiva
def f(n):
    if n < 2:
        return n
    else:
        return f(n - 1) + f(n - 2)


print(f(6))
#8

## Pergunta 4: Obtém o maior item da lista - função recursiva
def f(v, i):
    if i == 0:
        return v[i]
    else:
        return max(v[i], f(v, i - 1))


l = [5, 4, 6, 8, 1, 2]
print(f(l, len(l) - 1))
#8

## Pergunta 5: Soma todos os itens de uma lista - função recursiva
def f5(v, i):
    if i == 0:
        return v[i]
    else:
        return v[i] + f5(v, i - 1)


l = [5, 4, 6, 8, 1, 2]
print(f5(l, len(l) - 1))
#26


## Pergunta 9: Impressão em ordem inversa de itens de uma lista
class S:
    def __init__(self):
        self.v = []
        self.i = -1

    def push(self, x):
        self.i += 1
        self.v.append(x)

    def pop(self):
        if (not self.empty()):
            self.i -= 1
            return self.v.pop()

    def empty(self):
        return self.i < 0


s = S()
for i in range(10):
    s.push(i)

while not s.empty():
    print(s.pop())

'''
9
8
7
6
5
4
3
2
1
0
'''


## Pergunta 10: Impressão na mesma ordem de itens de uma lista
class S:
    def __init__(self):
        self.v = []
        self.i = -1

    def push(self, x):
        self.i += 1
        self.v.insert(0, x)

    def pop(self):
        if (not self.empty()):
            self.i -= 1
            return self.v.pop()

    def empty(self):
        return self.i < 0


s = S()
for i in range(10):
    s.push(i)

while not s.empty():
    print(s.pop())

"""
0
1
2
3
4
5
6
7
8
9
"""
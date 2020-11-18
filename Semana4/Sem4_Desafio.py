"""
    Imagine uma aplicação onde é necessário fazer o parsing de uma expressão aritmética, que faz uso de parênteses,
    colchetes e chaves. Como você implementaria a funcionalidade de verificar se os pares de abre/fecha
    parênteses/colchetes/chaves estão na ordem correta? Lembre-se que a ordem de fechamento desses caracteres
    deve ser inversa à ordem de abertura deles.
"""


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


def checkFormula(expression):
    """
    Check error in Open/Close parentheses ( ), brackets  [ ] and keys {}
    :param expression:
    :return:
    """
    p = pilha()
    b = pilha()
    k = pilha()
    resp =''
    for e in expression:
        if e == "{":
            k.push(e)
        elif e == "[":
            b.push(e)
        elif e == "(":
            p.push(e)
        elif e == ")":
            p.pop()
        elif e == "]":
            b.pop()
        elif e == "}":
            k.pop()
    if not k.empty():
        resp = 'Faltou fechar {}\n'
    if not b.empty():
        resp += 'Faltou fechar []\n'
    if not p.empty():
        resp += 'Faltou fechar ()\n'
    return resp


str = '{93+[(46 * 9)^4 + [8979 / 78 *(34 / 2) + (9/72]}}'
print(str,checkFormula(str), sep='\n')

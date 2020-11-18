"""
    A árvore representa os nós conectados por arestas.
    É uma estrutura de dados não linear. Possui as seguintes propriedades:
    - Um nó é marcado como nó raiz.
    - Cada nó, exceto a raiz, está associado a um nó pai.
    - Cada nó pode ter um número arbitrário de nó filho.

    Uma árvore de pesquisa binária (BST) é uma árvore na qual todos os nós seguem as propriedades mencionadas abaixo
    - A subárvore esquerda de um nó tem uma chave menor ou igual à chave de seu nó pai.
    - A subárvore direita de um nó tem uma chave maior do que a chave de seu nó pai.
    Assim, o BST divide todas as suas subárvores em dois segmentos; a subárvore esquerda e a subárvore direita e
    podem ser definidas como: left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)
"""


class Node:

    def __init__(self, key, data):

        self.left = None
        self.right = None
        self.key = key
        self.data = data

# Insert method to create nodes
    def insert(self, key, data):

        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, data)
                else:
                    self.left.insert(key, data)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, data)
                else:
                    self.right.insert(key, data)
        else:
            self.key = key
            self.data = data

    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            # ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self.right._min()
            self.key, self.value = tmp.key, tmp.value
            self.right._remove_min()
        return self

    def _min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:
            return self
        else:
            return self.left._min()

    def _remove_min(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._removeMin()
        return self

# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.key:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.key:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.key) + ' Is Found'

    def get(self, key):
        """Retorna uma referência ao nó de chave key
        """
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.key),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.key)
            res = res + self.inorderTraversal(root.right)
        return res


    def traverse(self, visit, order='pre'):
        """Percorre a árvore na ordem fornecida como parâmetro (pre, pos ou in)
           visitando os nós com a função visit() recebida como parâmetro.
        """
        if order == 'pre':
            visit(self)
        if self.left is not None:
            self.left.traverse(visit, order)
        if order == 'in':
            visit(self)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'post':
            visit(self)


root = Node(20, 'Raiz')
for i in range(1, 41):
    if i != 20:
        root.insert(i,'Folha {}'.format(i))

print(root.findval(7))
print(root.findval(50))
root.PrintTree()
print(root.inorderTraversal(root))
root.traverse(print, 'in')
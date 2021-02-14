##1.2. Considere uma classe “Fracao” em Python e dois objetos definidos como segue:
class Fracao:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return str(self.num) + '/' + str(self.den)


f1 = Fracao(1, 2)
f2 = Fracao(3, 4)
print(f1)
print(f2)


## PERGUNTA 2. Implemente uma classe em Python que represente o conceito ‘Horário’, contendo os seguintes atributos:
# hora, minuto e segundo. Em seguida, crie um objeto h dessa classe, em que ao executar a instrução ‘print(h)’,
# o programa deverá imprimir uma string no formato: ‘hora:minuto:segundo’.
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def __repr__(self):
        return '{}:{}:{}'.format(self.hora, self.minuto, self.segundo)


h = Horario(19, 13, 50)
print(h)

## PERGUNTA 3. Para que serve a variável entry?
from tkinter import Tk, Button, Label, Entry, END

def clicked():
    global entry
    name = entry.get()
    print('Ola', name)
    entry.delete(0, END)


root = Tk()
label = Label(root, text='Nome:')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='OK', command=clicked)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()

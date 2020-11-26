"""
    Para implementar programas com interfaces gráficas (GUI - Graphical User Interface)
    é necessário fazer uso de APIs que fornecem funções para criação de janelas, botões,
    gráficos e gerenciamento de eventos.
    Usaremo o Tkinter que é uma biblioteca da linguagem Python que acompanha a instalação padrão
    e permite desenvolver interfaces gráficas. Isso significa que qualquer computador que tenha o
    interpretador Python instalado é capaz de criar interfaces gráficas usando o Tkinter, com
    exceção de algumas distribuições Linux, exigindo que seja feita o download do módulo separadamente
    Conceitos de GUI (Graphic User Interface)

    Uma GUI aborda muitos conceitos, dos quais os mais comuns são:

    Container – É uma analogia a um container físico e tem como objetivo organizar e guardar objetos. Da mesma forma
    este conceito serve para um container em interface. Nesse caso, os objetos que estamos armazenando são os widgets;
    Widget – É um componente qualquer na tela, que pode ser um botão, um ícone, uma caixa de texto, etc.;
    Event Handler – São tratadores de eventos. Por exemplo, ao clicarmos em um botão para executar uma ação, uma
    rotina é executada. Essa rotina é chamada de event handler;
    Event Loop – O event loop verifica constantemente se outro evento foi acionado. Caso a hipótese seja verdadeira,
    ele irá executar a rotina correspondente.
    Material das Lives (2020-Nov): https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F12qVnoDgTHgxXkqIKrQbPWv-UAGolte0tGuNozqRyYcE%2Fedit
"""
## Implementando uma janela básica com um texto:
from tkinter import Tk, Label

# Criando a classe de janela
root = Tk()

# Criando um objeto da classe label
hello = Label(master=root, text="Olá classe")

# Empacotando do label na janela master=root
hello.pack()

# Instancia a janela. Sem o event loop, a interface não será exibida!
root.mainloop()

## Implementando uma janela básica com uma imagem (PhotoImage só aceita extensões GIF):
from tkinter import Tk, Label, PhotoImage

# Criando a classe de janela
root = Tk()

# Criando um objeto da classe PhotoImage (o método .subsample(5) reduz em 5 para 1 pixel da imagem original)
#photo = PhotoImage(file='computer2.gif').subsample(5)
photo = PhotoImage(file='computer2.gif').zoom(5)
# Criando um objeto da classe label e inserindo a imagem dentro
image = Label(master=root, image=photo, width=300, height=180)

# Empacotando do label na janela master=root
image.pack()
# Instancia a janela. Sem o event loop, a interface não será exibida!
root.mainloop()

## Implementando uma janela básica com uma imagem e um texto:
from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

# Criando a classe de janela
root = Tk()

# Criando um objeto da classe PhotoImage
photo = PhotoImage(file='computer1.gif')
# Criando um objeto da classe label e inserindo a imagem dentro e definindo a posição em TOP
image = Label(master=root, image=photo)
image.pack(side=TOP)

# Criando um outro objeto label e inserindo um texto
text = Label(master=root, font=("Arial", 20), text='Olá alunos da UNIVESP!')
# Empacotando do label na janela master=root
text.pack(side=BOTTOM)

# Instancia a janela. Sem o event loop, a interface não será exibida!
root.mainloop()

## Exercício 1 = Criar um teclado na janela
from tkinter import Tk, Label, RAISED

root = Tk()
labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]
for r in range(4):
    for c in range(3):
        label = Label(root, relief=RAISED, padx=30, text=labels[r][c])
        label["font"] = ("Verdana", "20", "italic", "bold")
        label["fg"] = "#006400"
        label.grid(row=r, column=c)
root.mainloop()

## Abordagem de programação orientada a eventos - Exibindo uma mensagem para o usuário
from tkinter import Tk, Button, BOTTOM
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S - %p\n', localtime())
    showinfo(message=time)

root = Tk()
root.geometry("400x200")
button = Button(root, text="Que dia é hoje?")
button["command"] = clicked
button.pack(side = BOTTOM)
root.mainloop()


## Abordagem de programação orientada a eventos - Entrada de dados pelo usuário
from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def transformDate():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%d/%m/%Y'))
    showinfo(message='{} was a {}'.format(date, weekday))

root = Tk()
# Definindo o label e sua posição:
label = Label(root, text="Informe uma data (DD/MM/YYYY):")
label.grid(row=0, column=0)

# Definindo o o campo para entrada de dados
entry = Entry(root)
entry.grid(row=0, column=1)

# Definindo o botão
button = Button(root, text="Calcular Data/Hora", command=transformDate)
button.grid(row=1, columnspan=2)
root.mainloop()


## Abordagem de programação orientada a eventos - Captura de eventos na digitação de texto - método bind()
from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    print('mouse left clicked')

def mouse_clickec_right(event):
    print('mouse right clicked')

def mouse_clicked_middle(event):
    print('mouse middle clicked')

# Instanciando a Janela
root = Tk()
root.title('Captura de eventos na digitação de texto - método bind()')
root.geometry("500x300")

# Definindo a caractetística da caixa de textos:
text = Text(root, bg='#FFD700', fg='#4B0082', font=("Verdana", "20", "italic"))
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-2>', mouse_clicked_middle)
text.bind('<Button-3>', mouse_clickec_right)
text.pack(expand=True, fill=BOTH)
root.mainloop()

## Tkinter Frame Example:
from tkinter import *

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text="Hello world")
label.pack()

button1 = Button(leftframe, text="Button1")
button1.pack(padx=3, pady=3)
button2 = Button(rightframe, text="Button2")
button2.pack(padx=3, pady=3)
button3 = Button(leftframe, text="Button3")
button3.pack(padx=3, pady=3)

root.title("Test")
root.mainloop()



## Adicionando Widgets e montando a interface
""" https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
    Para poder trabalhar com widgets é necessário entender o conceito de container, que é uma estrutura onde os widgets
    são colocados. Por questão de organização e para sua correta criação, definimos os containeres, e dentro de cada
    container, um ou mais widgets que o compõe. Sempre que um container for criado dentro de outro, devemos, no momento 
    e sua criação, definir qual é o container pai. A mesma questão de hierarquia serve para a criação de widgets, 
    evendo ser definido na sua criação qual o container pai, ou seja, em que container ele será incluído.
    ogo após definirmos a hierarquia de containeres e widgets, podemos posicionar os elementos na tela, indicando a 
    osição em que o elemento irá aparecer. O módulo Tkinter oferece três formas de trabalharmos com 
    geometria e posicionamento:
     
    # Pack;
    # Grid;
    # Place.
    Vamos ver algumas configurações de estilo mais comuns que podemos definir:
        Width – Largura do widget;
        Height – Altura do widget;
        Text – Texto a ser exibido no widget;
        Font – Família da fonte do texto;
        Fg – Cor do texto do widget;
        Bg – Cor de fundo do widget;
        Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).
        Por padrão, o side vem definido como Top, então vamos usá-lo para ver o que acontece.
"""
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1["bg"] = "#87CEFA"
        self.widget1["bd"] = 3
        self.widget1["height"] = 200
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "20", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Verdana", "12")
        self.sair["width"] = 20
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack(side=RIGHT)

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

root = Tk()
Application(root)
root.mainloop()
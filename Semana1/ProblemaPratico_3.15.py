'''
    Problema Prático 3.15
    Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos mostrados a seguir.
    Use a função jump() do módulo ch3. Você conseguirá obter a imagem desenhada executando:
    >>> import turtle
    >>> s = turtle.Screen()
    >>> t = turtle.Turtle()
    >>> olimpíadas(t)

'''

def jump(t,x, y):
    'faz tartaruga saltar para coordenadas (x, y)'
    t.penup()
    t.goto(x,y)
    t.pendown()


def emoticon(t,x,y):
    'tartaruga t desenha uma carinha com queixo na coordenada (x, y)'
    # define direção da tartaruga e tamanho da caneta
    t.pensize(3)
    t.setheading(0)
 
    # move para (x, y) e desenha cabeça
    jump(t,x,y)
    t.circle(100)
 
    # desenha olho direito
    jump(t, x+35, y+120)
    t.dot(25)
 
    # desenha olho esquerdo
    jump(t, x-35, y+120)
    t.dot(25)
 
    #desenha sorriso
    jump(t, x-60.62, y+65)
    t.setheading(-60) # sorriso está em 120 graus
    t.circle(70, 120)  # seção de um círculo

def olimpiadas(t):
    # define direção da tartaruga e tamanho da caneta
    t.pensize(3)
    t.setheading(0)
 
    # move para (x, y) e desenha um círculo tamanho 100
    for i in range(-100, 401, 220):
        jump(t,i,100)
        t.circle(100)
 
    for i in range(10, 250, 220):
        jump(t,i,-20)
        t.circle(100)    

import turtle
s = turtle.Screen()
t = turtle.Turtle()
olimpiadas(t)
#emoticon(t, -100, 100)
#emoticon(t, 150, 100)
    

print('\n' + str('>>> Problema Prático 3.15 função olimpíadas(t) <<<').center(80,'-') )



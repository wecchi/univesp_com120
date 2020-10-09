##
def GetMDC(x,y):
    '''
        Algoritmo 3.2 Algoritmo para calcular o máximo divisor comum entre dois números.

        Concilio, M.A.F.D.S.M.M.G.M.V.S. R. Algoritmos e lógica de programação: um texto introdutório para a engenharia.
        Cengage Learning Brasil, 2019. 9788522128150. Disponível em:
        https://integrada.minhabiblioteca.com.br/#/books/9788522128150/. Acesso em: 08 Oct 2020
    '''
    r = 0
    while y != 0:
        r = x % y
        x = y
        y = r
    return x



##
print('\n' + str('>>> Algoritmo 3.2 Algoritmo de EUCLIDES MDC <<<').center(80, '-'))
x = input("Digite os números para cáclulo do MDC: ")
x = x.split(' ')
y = eval(x[1])
x = eval(x[0])
##
print('\nMDC(%d,%d) = %d'%(x,y,GetMDC(x,y)))

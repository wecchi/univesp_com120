## Definindo a função para cálculo
def CalculaBascara(a, b, c):
    '''
        Algoritmo 3.5.3 Problema raízes de uma equação de segundo grau (Ax² + Bx + C)

        Concilio, M.A.F.D.S.M.M.G.M.V.S. R. Algoritmos e lógica de programação: um texto introdutório para a engenharia.
        Cengage Learning Brasil, 2019. 9788522128150. Disponível em:
        https://integrada.minhabiblioteca.com.br/#/books/9788522128150/. Acesso em: 08 Oct 2020
    '''
    import math
    delta = (b**2 - 4*a*c)
    if delta >=0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    else:
        x1 = x2 = 'Não existe'
    return x1, x2

## Obtendo as variáveis do usuário
print('\n' + str('>>> Algoritmo 3.5.3 Problema raízes de uma equação de segundo grau <<<').center(80, '-'))
a= input("Digite o valor da constante A (Ax² + Bx + C): ")
b = input("Digite o valor da constante B (Ax² + Bx + C): ")
c = input("Digite o valor da constante C (Ax² + Bx + C): ")
a = eval(a)
b = eval(b)
c = eval(c)

## Exibindo o resultado
x1, x2 = CalculaBascara(a, b, c)
if x1 == 'Não existe':
    print('''\nNão existem raízes reais para a equação "%dx² + %dx + %d"!''' % (a, b, c))
else:
    print('''\nAs raízes encontradas para a equação "%dx² + %dx + %d"  são:\n X1 = %f\n X2 = %f'''%(a, b, c, x1, x2))

## Definindo a função para cálculo
def CalculaF(h, d, gama):
    '''
        Algoritmo 3.5.2 Problema da força exercida por um líquido.

        Concilio, M.A.F.D.S.M.M.G.M.V.S. R. Algoritmos e lógica de programação: um texto introdutório para a engenharia.
        Cengage Learning Brasil, 2019. 9788522128150. Disponível em:
        https://integrada.minhabiblioteca.com.br/#/books/9788522128150/. Acesso em: 08 Oct 2020
    '''
    import math
    f = math.pi * gama * math.sqrt(d)*h/4
    return round(f,4)

## Obtendo as variáveis do usuário
print('\n' + str('>>> Algoritmo 3.5.2 Problema da força exercida por um líquido <<<').center(80, '-'))
h = input("Digite a altura do reservatório (m): ")
d = input("Digite o diâmetro da válvula (m): ")
gama = input('Digite o peso específico do líquido (N/m³): ')
h = eval(h)
d = eval(d)
gama = eval(gama)

## Exibindo o resultado
print('\nA força exercida na tampa da válvula é %dN'%CalculaF(h, d, gama))

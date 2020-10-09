## Definindo o problema de negócio
def CalcMediaTemperatura(n):
    '''
        Algoritmo 3.5.5 Problema média de N temperaturas fornecidas pelo usuário.
        Deve-se entender o problema com a experiência pessoal obtida ou por meio de dados fornecidos.
        Os dados do problema induzem:
        1. o número de temperaturas é variável e indeterminado, representado simbolicamente pela variável N.
        2. para realizar a média de N temperaturas é necessário, primeiramente, que esses N valores sejam fornecidos
        pelo usuário.
        3. não é possível resolver esse problema se N 0≤ , pois não tem sentido fazer a média de um conjunto com
        zero ou menos valores.

        Concilio, M.A.F.D.S.M.M.G.M.V.S. R. Algoritmos e lógica de programação: um texto introdutório para a engenharia.
        Cengage Learning Brasil, 2019. 9788522128150.
        Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788522128150/. Acesso em: 09 Oct 2020
    '''
    s = 0
    i = 1
    while i <= n:
        t = float(input('--> Forneça a temperatura N°%d: '%i))
        s += t
        i += 1
    m = s/n
    return m

## Obtendo as quantidade de temperatura do usuário
print('\n' + str('>>> Algoritmo 3.5.5 média de N temperaturas fornecidas pelo usuário <<<').center(80, '-'))
n = int(input("Informe quantas temperaturas serão forncecidas para o cálculo da média: "))

## Exibindo o resultado para o usuário
if n > 0:
    print('A média encontrada para as {0} temperaturas foi de {1:.2f}°C.'
          .format(n, CalcMediaTemperatura(n)))
else:
    print('A quantidade de temperaturas informadas deve ser maior que zero!')
print('\n', str('>>> Fim do programa 3.5.5 <<<').center(80, '-'))
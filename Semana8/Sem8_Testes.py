"""
    Testes automatizados para verificar a corretude dos programas desenvolvidos. Testes automatizados verificam a
    qualidade do código desenvolvido.
    Ao longo do curso foram feitos testes exploratórios, sem planejamento para verificar se o código funciona.
    Quando se tem um planejamento completo de um processo de verificação do software desenvolvido, a cada modificação
    do software é necessário executar todo o processo de verificação novamente (testes manuais são caros e propensos
    a erros). Diferentes entrada como o programa lida com os tipos diferentes de entrada? Existem dois tipos de testes
    automatizados:
    - Testes unitários (trata de verificar uma funcionalidade bem específica)
    - Testes integrados (mais difícil de identificar a causa do problema pois realiza um teste amplo que não distingue
    eventuais funcionalidades distintamente)
"""

## Exemplo de teste unitário por meio da função assert. Porém neste caso ao executar o test_soma o programa interrompe
# a execução pois houve uma exceção e não executa o test_multiplica. Para que esse problema seja contornado é necessádio
# usar Test Runners que são aplizações especialmente projetadas para depurar uma sequência de testes unitátios sem
# interrupção. Podemos usar o unittest, nose/nose2, pytest dentre outros - pesquise!!
# from Sem8_func import soma, multiplica
#
#
# def test_soma():
#     assert soma([1, 2, 3]) == 6, "Deve ser 6!"
#
#
# def test_multiplica():
#     assert multiplica([2, 3, 4]) == 24, "Deve ser 24!"
#
#
# if __name__ == "__main__":
#     test_soma()
#     test_multiplica()
#
#     print("\nTudo OK!")
# (base) D:\Python\Univesp\COM120>python Sem8_Testes.py
# Traceback (most recent call last):
# File "Sem8_Testes.py", line 26, in <module>
# test_soma()
# File "Sem8_Testes.py", line 19, in test_soma
# assert soma([1, 2, 3]) == 6, "Deve ser 6!"
# AssertionError: Deve ser 6!

## Exemplo de teste unitário usando Test Runners
import unittest
from Sem8_func import soma, multiplica


class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(soma([1, 2, 3]), 6, "Deve ser 6!!")

    def test_sum2(self):
        self.assertEqual(soma([1, 2, 3]), 7, "Deve ser 7!!")

    def test_mult1(self):
        self.assertEqual(multiplica([2, 3, 4]), 24, "Deve ser 24!!")

    def test_mult2(self):
        self.assertEqual(multiplica([20, 31, 47]), 29130, "Deve ser 29140!!")


if __name__ == "__main__":
    unittest.main()

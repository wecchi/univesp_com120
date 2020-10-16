from datetime import date 
  
class Funcionario():
    def __init__(self, nome):
        self.nome = nome

    def setNome(self, nome):
        self.nome = nome

    def setDataAdmissao(self, data):
        self.dataAdm = date(int(data[-4:]),
                            int(data[3:5]),
                            int(data[0:2]))

    def setSalario(self, salario):
        self.salario = salario

    def getNome(self):
        return self.nome

    def getDataAdmissao(self):
        try:
            return self.dataAdm
        except:
            print('Na')
         

    def getSalario(self):
        try:
            return self.salario
        except:
            print('Na')

    def getTempoCasa(self):
        try:
            hoje = date.today()
            delta = hoje - self.dataAdm
            dias = delta.days
            anos = dias // 365
            dias -= (anos * 365)
            meses = dias // 30
            dias -= (meses * 30)
            return 'Tempo de casa: {0} ano(s), {1} meses e {2} dias'.format(anos, meses, dias)
        except:
            print('você precisa informar a data de admissão do funcionário!!')
            

    def __repr__(self):
        return 'Funcionário: {0}'.format(self.nome)

class Gerente(Funcionario):
    def setBonus(self, bonus = 0.1):
        if bonus > 1: bonus /=100
        self.bonus = bonus

    def getBonus(self):
        try:
            return self.bonus
        except:
            print('Na')

    def CalculaBonus(self):
        try:
            return round(self.salario * self.bonus,2)
        except:
            print('Na')

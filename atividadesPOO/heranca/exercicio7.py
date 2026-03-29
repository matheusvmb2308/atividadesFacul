"""
Diagrama de Classes de Empregados
"""
class Empregado():
    def __init__(self, codigo, nome, email, salario):
        self.__codigo = codigo
        self.__nome = nome
        self.__email = email
        self.__salario = salario
    def getSalario(self):
        return self.__salario
    def setSalario(self, novo_salario):
        self.__salario = novo_salario
    def setAumentaSalario(self, percentual):
        self.__salario += self.__salario * percentual / 100
        return self.__salario
class Chefe(Empregado):
    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(codigo, nome, email, salario)
        self.__beneficio = beneficio
    def setAumentaSalario(self, percentual):
        salario = super().setAumentaSalario(percentual)
        return self.setSalario(salario + self.__beneficio)
class Estagiario(Empregado):
    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.__desconto = desconto
    def setAumentaSalario(self, percentual):
        salario = super().setAumentaSalario(percentual)
        return self.setSalario(salario - self.__desconto)
chefe = Chefe(1, "Carlos", "carlos@gmail.com", 10000, 500)
estagiario = Estagiario(1, "Carlos", "carlos@gmail.com", 1000, 200)
chefe.setAumentaSalario(10)
estagiario.setAumentaSalario(10)
print(chefe.getSalario())
print(estagiario.getSalario())

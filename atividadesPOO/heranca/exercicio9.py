"""
9. Implemente o código para as classes abaixo:
a) uma classe Funcionario com os atributos (nome, endereço, telefone, email) e com os
métodos (construtor, exibeDados())
b) crie a classe Assistente, que também é Funcionário, e que possui um número de
matrícula (use o método get).
c) sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos
possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e
Administrativo. Para cada um destas classes, imprima o número de matrícula e o nome de cada
um deles.
"""
class Funcionario():
    def __init__(self, nome, endereco, telefone, email):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
    def getExibeDados(self):
        return self.__nome, self.__endereco, self.__telefone, self.__email
    def getNome(self):
        return self.__nome
class Assistente(Funcionario):
    def __init__(self, nome, endereco, telefone, email, num_matricula):
        super().__init__(nome, endereco, telefone, email)
        self.__num_matricula = num_matricula
    def getMatricula(self):
        return self.__num_matricula
class Tecnico(Assistente):
    def __init__(self, nome, endereco, telefone, email, num_matricula, bonus):
        super().__init__(nome, endereco, telefone, email, num_matricula)
        self.__bonus = bonus
    def getMatricula(self):
        return f"{super().getMatricula()}, {self.getNome()}"
class Administrativo(Assistente):
    def __init__(self, nome, endereco, telefone, email, num_matricula, turno):
        super().__init__(nome, endereco, telefone, email, num_matricula)
        self.__turno = turno
        self.__bonus = 0
    def getMatricula(self):
        return f"{super().getMatricula()}, {self.getNome()}"
tecnico = Tecnico("Matheus", "Joinville","9999", "matheus@gmail.com", 1, 100)
administrativo = Administrativo("Matheus", "Joinville","9999", "matheus@gmail.com", 2, "Noturno")
print(tecnico.getMatricula())
print(administrativo.getMatricula())
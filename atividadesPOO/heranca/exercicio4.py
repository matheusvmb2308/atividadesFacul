"""
4. Crie uma classe Pessoa com os atributos nome e idade. Em seguida, crie uma classe
Funcionario que herda da classe Pessoa e adicione o atributo salario. Crie um método
aumento() na classe Funcionario que aumenta o salário em uma porcentagem específica.
"""
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    def aumento(self):
        porcentagem = 10 / 100
        self.salario += self.salario * porcentagem
    def mostraSalario(self):
        return self.salario
funcionario = Funcionario("Carlos", "25", 2000)
funcionario.aumento()
print(funcionario.mostraSalario())
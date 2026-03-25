"""
1. Crie uma classe Pessoa com os atributos nome e idade. Crie uma classe Aluno que herda de
Pessoa e adicione o atributo nota. Crie um método para imprimir as informações da Pessoa e um
método para imprimir as informações do Aluno.
"""
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostraDados(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
    def mostraDados(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}"
aluno1 = Aluno("Matheus", "19", 10)
print(aluno1.mostraDados())
        
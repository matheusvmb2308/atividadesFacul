"""
• Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: envelhecer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm.
"""
class Pessoa():
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
    self.nova_idade = idade
  def envelhecer(self):
    self.nova_idade = self.idade + 1
    self.idade = self.nova_idade
  def crescer(self):
    if self.idade < 21:
      if self.idade != self.nova_idade:  
        self.altura += 0.5
  def emagrescer(self):
    self.peso -= 1
  def engordar(self):
    self.peso += 1
  def getMostraDados(self):
    return f"Nome: {self.nome}, idade: {self.idade}, peso: {self.peso}, altura: {self.altura}"
pessoa1 = Pessoa("Matheus", 19, 60, 170)
pessoa1.envelhecer()
pessoa1.crescer()
print(pessoa1.getMostraDados())
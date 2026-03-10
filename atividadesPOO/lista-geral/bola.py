"""
Classe Bola: Crie uma classe que modele uma bola:

*   Item da lista
*   Item da lista


a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor
"""
class Bola():
  def __init__(self, cor, circuferencia, material):
    self.__cor = cor
    self.__circuferencia = circuferencia
    self.__material = material
  def setTrocaCorBola(self, cor):
    self.__cor = cor
  def defMostraCor(self):
    return f"A cor da bola é {self.__cor}"
bola = Bola("azul", 2, "plastico")
print(bola.defMostraCor())
bola.setTrocaCorBola("vermelha")
print(bola.defMostraCor())
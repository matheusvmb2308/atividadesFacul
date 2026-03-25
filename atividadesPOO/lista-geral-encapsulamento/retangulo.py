"""
• Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
de rodapés necessárias para o local.
"""
class Retangulo():
  def __init__(self, ladoA,  ladoB):
    self.ladoA = ladoA
    self.ladoB = ladoB
  def setMudaValor(self, novoLadoA, novoLadoB):
    self.ladoA = novoLadoA
    self.ladoB = novoLadoB
  def calculaArea(self):
    self.area = self.ladoA * self.ladoB
  def calculaPerimetro(self):
    self.perimetro = (self.ladoA*2) + (self.ladoB*2)
  def getRetornaValor(self):
    return f"O valor dos lados é: {self.ladoA}, {self.ladoB}"
  def getRetornaAreaPerimetro(self):
    return f"O valor do área é: {self.area}m² e o valor do perímetro é {self.perimetro}"
ladoA = int(input("Digite o valor do comprimento do local: "))
ladoB = int(input("Digite o valor da base do local: "))
retangulo = Retangulo(ladoA, ladoB)
retangulo.calculaArea()
retangulo.calculaPerimetro()
print(retangulo.getRetornaValor())
print(retangulo.getRetornaAreaPerimetro())
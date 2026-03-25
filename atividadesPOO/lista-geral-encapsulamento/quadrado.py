"""
• Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado():
  def __init__(self, tamanho):
    self.tamanho = tamanho
  def setMudaValorLado(self, mudaTamanho):
    self.tamanho = mudaTamanho
  def calculaArea(self):
    self.area = self.tamanho ** 2
  def getRetornaValor(self):
    return f"O valor do lado é {self.tamanho} e a área do quadrado é {self.area}"
quadrado = Quadrado(2)
quadrado.calculaArea()
print(quadrado.getRetornaValor())
quadrado.setMudaValorLado(3)
quadrado.calculaArea()
print(quadrado.getRetornaValor())
"""
5. Crie uma classe Forma com o método area(). Em seguida, crie duas subclasses: Retangulo e
Circulo, que herdam da classe Forma. Adicione os atributos comprimento e largura na
classe Retangulo e o atributo raio na classe Circulo. Agora calcula a área de cada polígono.
"""
import math
class Forma():
    def area(self):
        pass
class Retangulo(Forma):
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento
    def area(self):
        return self.largura * self.comprimento 
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * (self.raio ** 2)
circulo = Circulo(5)
retangulo = Retangulo(10, 5)
print(f"Área do circulo: {circulo.area():.2f}")
print(f"Área do retangulo: {retangulo.area()}")
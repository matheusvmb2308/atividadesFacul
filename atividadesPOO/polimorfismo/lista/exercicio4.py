"""
4. Crie uma classe Forma com um método area(). Em seguida, crie duas classes filhas, Circulo e
Quadrado, que herdam da classe Forma. Cada uma destas classes filhas deve ter seu próprio
método area() que calcula a área do círculo ou do quadrado, respectivamente. Em seguida, crie
uma lista de formas que inclua um círculo e um quadrado. Por fim, itere sobre a lista e chame o
método area() de cada forma.
"""
from math import pi
class Forma:
    def __init__(self):
        pass
    def area():
        pass
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return pi * self.raio**2
circulo = Circulo(4)
quadrado = Quadrado(5)
for forma in circulo, quadrado:
    print(forma.area())
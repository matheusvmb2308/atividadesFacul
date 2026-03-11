"""
• Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o
outro. É possível criar um macaco canibal?
R= É possivel
""" 
class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []
    def __repr__(self):
        return self.nome
    def verBucho(self):
        return print(self.estomago)
    def comer(self, alimento):  
        self.estomago.append(alimento)
        self.verBucho()
    def digerir(self):
        self.estomago.clear()
macaco1 = Macaco("Cesar")
macaco2 = Macaco("Charles")
macaco1.comer("Banana")
macaco2.comer("Maçã")
macaco1.comer("Laranja")
macaco1.comer("Uva")
macaco2.comer("Laranja")
macaco2.comer("Uva")
macaco1.comer(macaco2)
macaco1.digerir()
macaco1.verBucho()
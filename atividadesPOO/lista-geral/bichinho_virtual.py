"""
• Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então
não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a
qualquer momento.
"""
class Bichinho():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.setHumor()
    def setHumor(self):
        if self.fome < 50 or self.saude < 50:
            if self.fome < 10 or self.saude < 10:
                self.humor = "Depressivo"
                return
            else:
                self.humor = "Triste"
            return
        elif self.fome >= 50 and self.saude >= 50:
            if self.fome > 80 and self.saude > 80:
                self.humor = "Animado"
            else:
                self.humor = "Feliz"
    def setSaude(self,saude):
        self.saude = saude
        self.setHumor()
    def setFome(self, fome):
        self.fome = fome
        self.setHumor()
    def getMostraDados(self):
        return f"Nome: {self.nome}, Saúde: {self.saude}, Fome: {self.fome}, Humor: {self.humor}, Idade: {self.idade}"
tamaguchi = Bichinho("Tamaguchi", 50, 50, 20)
print(tamaguchi.getMostraDados())
tamaguchi.setFome(10)
print(tamaguchi.getMostraDados())
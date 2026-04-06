"""
Nesta atividade prática, vamos retornar à classe Usuario que usamos nas atividades anteriores. Para
implementar o princípio do polimorfismo, criaremos uma classe chamada Usuario. A partir dela
criaremos algumas classes como: para calcular o número de pontuações que um usuário tem, e o número
de artigos que ele criou ou editou. Baseado nesta classe (Usuario), vamos criar as classes Autor e
Editor, e ambas calcularão o número de pontuações com o método calcPontuacao(), embora o
valor calculado seja diferente entre estas duas classes.
"""
class Usuario:
    def __init__(self):
        self.__pontos = 0
        self.__numeroArtigos = 0
    def setPontos(self, pontos):
        self.__pontos = pontos
    def getPontos(self):
        return self.__pontos
    def setNumArtigos(self, nart=int):
        self.__numeroArtigos = nart
    def getNumArtigos(self):
        return self.__numeroArtigos
class Autor(Usuario):
    def __init__(self):
        super().__init__()
    def calcPontuacao(self):
        self.setPontos(self.getNumArtigos() * 10 + 20)
class Editor(Usuario):
    def __init__(self):
        super().__init__()
    def calcPontuacao(self):
        self.setPontos(self.getNumArtigos() * 6 + 15)
autor1 = Autor()
editor1 = Editor()
autor1.setNumArtigos(8)
editor1.setNumArtigos(15)
autor1.calcPontuacao()
editor1.calcPontuacao()
print(autor1.getPontos())
print(editor1.getPontos())

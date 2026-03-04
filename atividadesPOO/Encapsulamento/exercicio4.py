'''
4. Crie uma classe chamada Robo(). Ela deverá ter duas propriedades privadas: nome e
ano_construcao. Também deverá ter um método de nome “diga_alo()”, para mostrar na
tela o nome do robô e seu ano de construção. Crie os métodos “setters” e “getters”
necessários. Instancie a classe e use os métodos criados para visualizar / atualizar os dados.
'''
class Robo():
    def __init__(self, nome="", ano_construcao=0):
        self.__nome = nome
        self.__ano = ano_construcao
    def setNomeAno(self, nome, ano):
        self.__nome = nome
        self.__ano = ano
    def getDiga_alo(self):
        return f"O nome do robô é {self.__nome} e foi contruido em {self.__ano}"
robo = Robo("Charles", 2023)
print(robo.getDiga_alo())
robo.setNomeAno("Mat", 2015)
print(robo.getDiga_alo())

"""
• Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
retângulo, que deve ser um objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
ponto que indique os valores de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""
class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mostraDados(self):
        return f"Pontos: X = {self.x}, Y={self.y}"
class Retangulo():
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto
    def encontraCentro(self):
        centro_x = self.ponto.x + self.largura /2
        centro_y = self.ponto.y + self.altura / 2
        return Ponto(centro_x, centro_y)
retangulo = Retangulo(10, 6, Ponto(0, 0))
while True:
    print("[1] Mostre o centro do Retangulo")
    print("[2] Mude a altura do retangulo")
    print("[3] Mude a base do retangulo")
    print("[4] Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        centro = retangulo.encontraCentro()
        print(centro.mostraDados())
    if escolha == 2:
        retangulo.largura = float(input("Nova largura: "))
    if escolha == 3:
        retangulo.altura = float(input("Nova altura: "))
    if escolha == 4:
        break
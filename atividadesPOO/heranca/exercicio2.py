"""
método para imprimir as informações do Aluno.
2. Crie uma classe Veiculo com os atributos marca, modelo e ano. Crie classes filhas Carro e
Moto que adicionam o atributo quantidade_de_portas e cilindradas, respectivamente. Crie
um método para imprimir as informações do Veiculo e um método para imprimir as informações
do Carro e da Moto.
"""
class Veiculo():
    def __init__(self, marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def mostraDados(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_porta):
        super().__init__(marca, modelo, ano)    
        self.quantidade_porta = quantidade_porta
    def mostraDados(self):
        return super().mostraDados() + f", Quantiade de portas: {self.quantidade_porta}"
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def mostraDados(self):
        return super().mostraDados() + f", Cilindradas: {self.cilindradas}"
carro = Carro("Ferrari", "Puro Sangue", 2026, 4)
moto = Moto("Honda", "CG 160", 2026, 200)
print(carro.mostraDados())
print(moto.mostraDados())
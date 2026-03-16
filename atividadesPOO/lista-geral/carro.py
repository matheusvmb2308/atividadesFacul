"""
• Classe Carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
quantidade de combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15) # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.
meuFusca.andar(100) # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.
"""
class Carro():
    def __init__(self, consumo_combustivel, quantidade_combustivel=0):
        self.consumo = consumo_combustivel
        self.quantidade = quantidade_combustivel
    def andar(self, distancia):
        self.quantidade -= distancia / self.consumo
    def adicionarGasolina(self, quantidade):
        self.quantidade += quantidade 
    def obterGasolina(self):
        return print(f"Quantidade do Tanque = {self.quantidade:.2f}")
meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()

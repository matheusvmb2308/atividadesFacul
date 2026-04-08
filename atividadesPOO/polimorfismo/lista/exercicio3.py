"""
3. Crie uma classe chamada Carro com um método dirigir(). Em seguida, crie duas subclasses,
CarroGasolina e CarroEletrico, cada uma com sua própria implementação de dirigir().
Demonstre o polimorfismo passando instâncias de ambas as subclasses para uma função que recebe
um objeto Carro.
"""
class Carro:
    def dirigir(self):
        return "Dirigindo"
class CarroGasolina(Carro):
    def dirigir(self):
        return "Dirigindo, gastando gasolina"
class CarroEletrico(Carro):
    def dirigir(self):
        return "Dirigindo, gastando bateria"
gasolina = CarroGasolina()
eletrico = CarroEletrico()
for carro in gasolina, eletrico:
    print(carro.dirigir())
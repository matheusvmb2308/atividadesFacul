"""
6. Crie uma classe chamada ContaBancaria com os métodos deposito() e retirada(). Crie
duas subclasses: ContaPoupanca e ContaCorrente. Cada uma dessas subclasses deve ter sua
própria taxa de juros (a taxa de juros da Conta Poupança é maior que a da Conta Corrente).
"""
class ContaBancaria:
    def __init__(self, poupanca):
        self.poupanca = poupanca
    def retirada(self, valor_retirada):
        self.poupanca -= valor_retirada
    def deposito(self, valor_deposito):
        self.poupanca += valor_deposito
class ContaPoupanca(ContaBancaria):
    def __init__(self, poupanca):
        super().__init__(poupanca)
        self.taxa_juros = 10 /100
    def aplicaJuros(self):
        self.poupanca += self.poupanca * self.taxa_juros
    def retirada(self, valor_retirada):
        return super().retirada(valor_retirada)
    def deposito(self, valor_deposito):
        return super().deposito(valor_deposito)
class ContaCorrente(ContaBancaria):
    def __init__(self, poupanca):
        super().__init__(poupanca)
        self.taxa_juros = 5 / 100
    def aplicaJuros(self):
        self.poupanca += self.poupanca * self.taxa_juros
    def retirada(self, valor_retirada):
        return super().retirada(valor_retirada)
    def deposito(self, valor_deposito):
        return super().deposito(valor_deposito)
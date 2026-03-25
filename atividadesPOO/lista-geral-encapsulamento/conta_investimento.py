"""
Classe Conta de Investimento: Faça uma classe chamada contaInvestimento que seja semelhante à
classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um
construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros
(sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
adicioneJuros() cinco vezes e imprime o saldo resultante.
"""
class contaInvestimento():
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo_inicial = saldo_inicial
        self.taxa_juros = taxa_juros
        self.juros = self.taxa_juros / 100
    def adicionaJuros(self):
        self.saldo_inicial += self.saldo_inicial * (self.juros)
    def obterSaldo(self):
        return print(f"O saldo é: {self.saldo_inicial}")
conta = contaInvestimento(1000, 10)
for i in range(5):
    conta.adicionaJuros()
conta.obterSaldo()
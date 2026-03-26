"""
Diagrama de Conta Bancária
"""
class CCorrente():
    def __init__(self, numero, saldo, cliente):
        self.__numero = numero
        self.__saldo = saldo
        self.__cliente = cliente
    def creditar(self, valor):
        self.__saldo += valor
    def debitar(self, valor):
        self.__saldo -= valor
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, valor):
        self.__saldo = valor
class CEspecial(CCorrente):
    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.__limite = limite
    def debitar(self, valor):
        if valor <= self.getSaldo() + self.__limite:
           super().debitar(valor)
        else: 
            print("Valor maior que limite!")
class CPoupanca(CCorrente):
    def __init__(self, numero, saldo, cliente, saldo_minimo):
        super().__init__(numero, saldo, cliente)
        self.__saldo_minimo = saldo_minimo
    def debitar(self, valor):
        super().debitar(valor)
    def AtualizarSaldo(self, novo_saldo):
        if novo_saldo < self.__saldo_minimo:
            print(f"Esse saldo é menor que o saldo mínimo de {self.__saldo_minimo}")
        else:
            self.setSaldo(novo_saldo)
    def getSaldoMinimo(self):
        return self.__saldo_minimo
class CInvestimento(CCorrente):
    def __init__(self, numero, saldo, cliente, diaInvestimento, periodo):
        super().__init__(numero, saldo, cliente)
        self.__diaInvestimento = diaInvestimento
        self.__periodo = periodo
    def atualizarSaldo(self, valor):
        self.setSaldo(valor)
contaE = CEspecial(1, 100, "matheus", 500)
print(contaE.getSaldo())
contaE.debitar(300)
print(contaE.getSaldo())
contaP = CPoupanca(1, 500, "matheus", 100)
print(contaP.getSaldo())
contaP.AtualizarSaldo(200)
print(contaP.getSaldo())
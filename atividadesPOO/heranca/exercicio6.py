"""
Diagrama de Conta Bancária
"""
#Código ainda não finalizado!
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
class CEspecial(CCorrente):
    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.__limite = limite
    def debitar(self, valor):
        return super().debitar(valor)
class CPoupanca(CCorrente):
    def __init__(self, numero, saldo, cliente, saldo_minimo):
        super().__init__(numero, saldo, cliente)
        self.__saldo_minimo = saldo_minimo
    def debitar(self, valor):
        return super().debitar(valor)
    def atualizarSaldo(self):
        pass
    def getSaldoMinimo(self):
        return self.__saldo_minimo
class CInvestimento(CCorrente):
    def __init__(self, numero, saldo, cliente, diaInvestimento, periodo):
        super().__init__(numero, saldo, cliente)
        self.__diaInvestimento = diaInvestimento
        self.__periodo = periodo
    def atualizarSaldo(self):
        pass

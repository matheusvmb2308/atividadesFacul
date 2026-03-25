"""
• Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque. No construtor, saldo é opcional, com valor default zero e os
demais atributos são obrigatórios.
"""
class Conta_corrente():
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    def setAlterarNome(self, nome_correntista):
        self.nome_correntista = nome_correntista
    def setDeposito(self, deposito):
        self.saldo += deposito
    def setSaque(self, saque):
        if self.saldo <= 0:
            return print("Não é possivel sacar, saldo é 0")
        else:
            if self.saldo < saque:
                return print(f"Impossível sacar, saque maior que saldo")
            else:
                self.saldo -= saque
    def getDados(self):
        return f"Número da conta: {self.numero_conta}, Nome: {self.nome_correntista}, Saldo: {self.saldo}"
conta1 = Conta_corrente(1, "Matheus",50)
conta1.setSaque(50)
print(conta1.getDados())
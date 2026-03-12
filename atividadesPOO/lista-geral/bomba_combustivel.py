class Bomba():
    def __init__(self, tipo, valor, quantidade):
        self.__tipoCombustivel = tipo
        self.__valorCombustivel = valor
        self.__quantidadeCombustivel = quantidade
    def AbastecerPorValor(self, valorPago):
        self.valorPago = valorPago
        self.valorTirado = self.valorPago / self.__valorCombustivel
        self.__quantidadeCombustivel -= self.valorTirado
        print(f"Foram abastecidos {self.valorTirado:.2f} litros")
        return 
    def AbastecerPorLitro(self, litro):
        self.litro = litro
        self.pagamento = self.litro * self.__valorCombustivel
        self.__quantidadeCombustivel -= self.litro
        print(f"O valor a ser pago é de {self.pagamento:.2f}")
        return
    def setMudaValor(self, valorNovo):
        self.__valorCombustivel = valorNovo
    def setMudaTipo(self, tipo):
        self.__tipoCombustivel = tipo
    def setMudaQuantidadeCombustivel(self, quantidade_nova):
        self.__quantidadeCombustivel = quantidade_nova
    def getDados(self):
        return f"Quantidade Restante {self.__quantidadeCombustivel:.2f}L | Valor R${self.__valorCombustivel} | Tipo: {self.__tipoCombustivel}"
bomba1 = Bomba("Gasolina", 6, 100)
bomba1.setMudaTipo("Etanol")
bomba1.setMudaValor(8)
bomba1.setMudaQuantidadeCombustivel(1000)
while True:
    print("BEM VINDO AO POSTO - ESSA É A BOMBA 1")
    print("COMO VOCÊ PRETENDE ABASTECER SEU CARRO?")
    print("[1] POR LITRO")
    print("[2] POR VALOR")
    print(bomba1.getDados())
    print("[3] SAIR")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        litro = int(input("Digite a quantidade de litros: "))
        bomba1.AbastecerPorLitro(litro)
    if escolha == 2:
        valor = float(input("Digite o valor a ser pago: "))
        bomba1.AbastecerPorValor(valor)
    if escolha == 3: 
        break
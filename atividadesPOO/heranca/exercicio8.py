"""
8. Implemente o código para as classes abaixo:
a) crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor()
b) crie uma classe VIP que herda de Ingresso e possui um valor adicional. Crie também um método
que retorne o valor do ingresso VIP (como o adicional incluído).
c) crie uma classe Normal, que herda Ingresso e possui um método que imprime: "Ingresso Normal".
d) crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos para acessar e
imprimir esta localização) e uma classe CamaroteSuperior, que é mais cara (possui valor
adicional). Esta última possui um método para retornar o valor do ingresso. Ambas as classes herdam
a classe VIP.
"""
class Ingresso():
    def __init__(self, valor):
        self.__valor = valor
    def getImprimeValor(self):
        return self.__valor
class VIP(Ingresso):
    def __init__(self, valor, adicional = 30):
        super().__init__(valor) 
        self.__adicional = adicional
    def getImprimeValor(self):
        return super().getImprimeValor() + self.__adicional
class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def imprimeIngresso(self):
        return f"Ingresso Normal"
class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.__localizacao = localizacao
    def getLocalizacao(self):
        return self.__localizacao
class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, adicional_camarote = 50):
        super().__init__(valor, adicional)
        self.__adicional_camarote = adicional_camarote    
    def getImprimeValor(self):
        return super().getImprimeValor() + self.__adicional_camarote
vip = VIP(20)
camaroteInferior = CamaroteInferior(20, 30, "Bloco A")
camaroteSuperior = CamaroteSuperior(20, 30)
print(f"R${vip.getImprimeValor()}")
print(f"R${camaroteSuperior.getImprimeValor()}")
print(f"Localização: {camaroteInferior.getLocalizacao()}")

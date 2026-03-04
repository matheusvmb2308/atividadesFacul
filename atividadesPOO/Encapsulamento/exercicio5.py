"""
5. Implemente uma classe chamada Laptop que possua um atributo privado chamado “preco”
que armazena o preço do laptop (sem qualquer validação). Em seguida, implemente um método
para ler esse atributo chamado “get_preco()” e um método para modificar esse atributo
chamado “set_preco()” sem validação também. Em seguida, crie uma instância da classe
Laptop siga estas etapas:
• usando o método “get_preco()” imprima o valor do atributo “preco” na tela
• usando o método “set_preco()”, defina o valor do atributo “preco” para 3999”
"""
class Laptop():
    def __init__(self, preco=0):
        self.__preco = preco
    def getPreco(self):
        return self.__preco
    def setPreco(self, novo_preco):
        self.__preco = novo_preco
laptop = Laptop(2000)
print(laptop.getPreco())
laptop.setPreco(3999)
print(laptop.getPreco())
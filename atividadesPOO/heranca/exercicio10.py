"""
Diagrama de Pessoa
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.__dinheiro = dinheiro
    def fazCompras(self):
        return f"Fazendo compras e gastando R${self.__dinheiro}"
class Pobre(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def trabalha(self):
        return "Trabalhando"
class Miseravel(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def mendiga(self):
        return "Mendigando"
pobre = Pobre("Matheus", 19)
rica = Rica("Carlos", 20, 1000)
print(pobre.trabalha())
print(rica.fazCompras())

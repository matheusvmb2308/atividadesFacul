"""
3. Crie uma classe chamada Empregado(), com três propriedades: nome, salario (deve ser
privada) e projeto. Ela também possui um método chamado “trabalho()”, que deverá
imprimir o nome do funcionário e o projeto em que ele está trabalhando e um outro método
chamado “mostrar()” para exibir os detalhes desse empregado (i.e. nome e salário). Atente
para o modificador de acesso da propriedade “salario”. Use o método adequado para ter
acesso a ela. Crie um objeto desta classe (i.e. instância) e use os métodos para visualizar os
dados.
"""
class Empregado():
    def __init__(self, nome, salario, projeto):
        self.projeto = projeto
        self.__nome = nome
        self.__salario = salario
    def getTrabalho(self):
        return f"{self.__nome} está trabalhando no projeto {self.projeto}"
    def getMostrar(self):
        return self.__nome, self.__salario
jose = Empregado("Jose", 1300, "XXX")
print(jose.getTrabalho())
print(jose.getMostrar())
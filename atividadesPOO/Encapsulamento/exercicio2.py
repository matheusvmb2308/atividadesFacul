#Crie uma propriedade na classe Usuario chamada primeiroNome e evite que qualquer código
#de fora da classe altere o seu valor, usando o modificador de acesso apropriado.
'''''
Agora, crie um método para retornar o valor primeiroNome.
Crie um objeto chamado usuario1. Depois defina seu primeiro nome como "Joe" e faça com
que ele retorne este nome.
'''
class Usuario():
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome
    def getPrimeiroNome(self):
        return self.__primeiroNome
usuario1 = Usuario("Joe")
print(usuario1.getPrimeiroNome())


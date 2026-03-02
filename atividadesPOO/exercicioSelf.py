#1Qual palavra-chave (keyword) você usaria para ter acesso às propriedades e métodos de uma classe estando dentro dela?
#A palavra-chave self  

#2. Acrescente ao método hello() a capacidade de acessar a propriedade primeiroNome, para que
#o método possa retornar a string "Olá, primeiroNome".

class Usuario():
  def __init__(self, primeiroNome, ultimoNome):
    self.primeiroNome = primeiroNome
    self.ultimoNome = ultimoNome

  def getPrimeiroNome(self):
    self.nome = self.primeiroNome
  
  def __str__(self):
    return f"Ola, {self.nome}"
usuario1= Usuario("Matheus","Bernardes")  
usuario1.getPrimeiroNome()
print(usuario1)
#3. Crie um novo objeto com o primeiro nome de "Jonnie" e sobrenome de "Bravo".
jonnie = Usuario("Jonnie", "Bravo")
jonnie.getPrimeiroNome()
print(jonnie)
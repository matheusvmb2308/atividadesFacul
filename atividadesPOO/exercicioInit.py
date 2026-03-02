class Usuario():
  def __init__(self, primeiroNome, ultimoNome):
    self.primeiroNome = primeiroNome
    self.ultimoNome = ultimoNome
  def getPrimeiroNome(self):
    return f'{self.primeiroNome}'
  def getUltimoNome(self):
    return f'{self.ultimoNome}'
  def getNomeCompleto(self):
    return f"{self.primeiroNome} {self.ultimoNome}"
usuario1 = Usuario("Matheus", "Bernardes")
print(usuario1.getPrimeiroNome())
print(usuario1.getUltimoNome())
print(usuario1.getNomeCompleto())
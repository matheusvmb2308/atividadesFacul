"""
3. Crie uma classe Animal com os atributos nome e peso, e um método comer(). Em seguida, crie
duas subclasses, Cachorro e Gato, que herdam da classe Animal. Adicione um método
latir() na classe Cachorro e um método miar() na classe Gato.
"""
class Animal():
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
    def comer(self, comida):
        return f"Comendo {comida}"
    def __repr__(self):
        return self.nome
class Cachorro(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def latir(self):
        return f"Latindo"
class Gato(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def miar(self):
        return f"Miando"
gato = Gato("Miau", 30)
cachorro = Cachorro("Dog", 40)
print(cachorro.comer(gato))
print(gato.miar())
print(cachorro.latir())    
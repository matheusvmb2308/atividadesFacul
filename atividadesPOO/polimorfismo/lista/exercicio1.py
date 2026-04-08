"""
1. Crie uma hierarquia de classes para animais, com uma classe mãe Animal e subclasses Cachorro,
Gato e Peixe. Cada subclasse deve ter um método falar() que retorne uma string
representando o som que o animal faz. Demonstre o polimorfismo chamando falar() nas
instâncias de cada subclasse.
"""
class Animal:
    def __init__(self,nome):
        self.nome = nome
    def falar(self):
        pass
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def falar(self):
        return f"Auau"
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def falar(self):
        return "Miau"
class Peixe(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def falar(self):
        return "Blub"
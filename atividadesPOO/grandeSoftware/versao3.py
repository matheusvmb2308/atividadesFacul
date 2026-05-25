from enum import Enum

# Podemos nos referir a eles como Wood.SITKA ou Builder.GIBSON 
# e evitar todas essas comparações de strings completamente
class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

#Cada "enum" toma o lugar de uma das propriedades de uma guitarra
class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"


# Podemos nos referir a eles como Wood.SITKA ou Builder.GIBSON 
# e evitar todas essas comparações de strings completamente
class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class Guitar:
    def __init__(self, serial_number, price, GuitarSpec):
        self.serial_number = serial_number
        self.price = price
        self.spec = GuitarSpec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_spec(self):
        return self.spec

#Classe GuitarSpec
class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood
        
    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood

#Classe Inventory
class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar_espec = GuitarSpec(builder, model, typeg, back_wood, top_wood)
        guitar = Guitar(serial_number, price, guitar_espec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_guitar):
        found_guitars = []
        for guitar in self.guitars:
            guitar_spec = guitar.get_spec()
            self.search_guitar_espec = search_guitar.get_spec()
            # Parece que nada mudou, mas com "Enums", não precisamos nos preocupar com essas comparações 
            # sendo prejudicadas por erros ortográficos ou problemas de maiúscula/minúscula
            if self.search_guitar_espec.get_builder() != guitar_spec.get_builder():
                continue
            
            # A única propriedade com a qual precisamos nos preocupar é o "model", já que ainda é uma String
            model = self.search_guitar_espec.get_model().lower()
            if model and model != "" and model != guitar_spec.get_model().lower():
                continue
            
            # Parece que nada mudou, mas com "Enums", não precisamos nos preocupar com essas comparações 
            # sendo prejudicadas por erros ortográficos ou problemas de maiúscula/minúscula
            if self.search_guitar_espec.get_typeg() != guitar_spec.get_typeg():
                continue
            if self.search_guitar_espec.get_back_wood() != guitar_spec.get_back_wood():
                continue
            if self.search_guitar_espec.get_top_wood() != guitar_spec.get_top_wood():
                continue
            found_guitars.append(guitar)
        if found_guitars:
            return found_guitars
        return None
    
# Testando o Sistema

# Set up Rick’s guitar inventory
inventory = Inventory()

# Adiciona guitarras ao estoque
inventory.add_guitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
inventory.add_guitar("V92341", 1600.00, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
inventory.add_guitar("11277", 3999.95, Builder.COLLINGS.value, "Stratocastor", TypeG.ACOUSTIC.value, Wood.INDIAN_ROSEWOOD.value, Wood.INDIAN_ROSEWOOD.value)

guitar_epec = GuitarSpec(Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
# Buscando por uma guitarra que o Erin gosta: Fender Stratocastor elétrica com corpo de Alder e tampo de Alder
whatErinLikes = Guitar(" ", 0, guitar_epec)
guitars = inventory.search_guitar(whatErinLikes)
if guitars is not None:
    for guitar in guitars:
        guitar_spec = guitar.get_spec()
        print(f"Erin, talvez você goste desta: {guitar_spec.get_builder()} {guitar_spec.get_model()} {guitar_spec.get_typeg()} guitar:\n{guitar_spec.get_back_wood()} na traseira e laterais, {guitar_spec.get_top_wood()} no tampo.\nEla pode ser sua por apenas US${guitar.get_price()}! \n")
else:
  print("Desculpe Erin, não temos nada para você")
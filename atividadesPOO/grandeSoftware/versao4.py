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
    def __init__(self, builder, model, typeg, back_wood, top_wood, numStrings):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.numStrings = numStrings
        
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
    def get_num_stings(self):
        return self.numStrings
    def matches(self, otherSpec):
        if self.builder != otherSpec.get_builder():
            return False
        if self.model and self.model.lower() != otherSpec.get_model().lower():
            return False
        if self.typeg != otherSpec.get_typeg():
            return False
        if self.back_wood != otherSpec.get_back_wood():
            return False
        if self.top_wood != otherSpec.get_top_wood():
            return False
        if self.numStrings != otherSpec.get_num_stings():
            return False
        return True

#Classe Inventory
class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serialNumber, price, spec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, searchGuitar):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.get_spec().matches(searchGuitar):
                matchingGuitars.append(guitar)
        return matchingGuitars
    
# Testando o Sistema

# Set up Rick’s guitar inventory
def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELETRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.add_guitar("V95693", 1499.95, spec1)
    inventory.add_guitar("V99999", 1599.95, spec1)
    
    #spec2 = GuitarSpec(Builder.MARTIN, "D-18", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("122784", 5495.95, spec2)
    #inventory.addGuitar("76531", 6295.95, Builder.MARTIN, "OM-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
    #inventory.addGuitar("70108276", 2295.95, Builder.GIBSON, "Les Paul", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue", TypeG.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6)
    #inventory.addGuitar("77023", 6275.95, Builder.MARTIN, "D-28", TypeG.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6)
 

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELETRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.get_spec()
            print(f"\nGuitarra: {guitar.get_serial_number()} {guitarSpec.get_builder().value} {guitarSpec.get_model()} {guitarSpec.get_typeg().value} guitar:\n{guitarSpec.get_back_wood().value} na traseira e laterais,\n{guitarSpec.get_top_wood().value} no tampo, com {guitarSpec.get_num_stings()} cordas\nEla pode ser sua por apenas US${guitar.get_price():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()
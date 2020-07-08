#Klasa -okr, jakiego rodzaju info będziemy przechowywać
# w oparciu o klasę powstaje INSTANCJA KLASY czyli OBIEKT
# ObIEKT odwołuje się do wszystkich właściwości jakie posiada klasa
#Cechy opisane przez klasę to ATRYBUTY
# Funkcje przypisane do klasy to METODY

class Car: #init to konstruktor, tworzący Instancję, czyli OBiekt
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK):#self to definicja konkretnego obiektu (inicjowany obiekt), po sefl okreslam jego atrybuty które musi posiadać
        self.brand=brand #ten self oznacza, ze chodzi o właściwość definiowanej instancji
        self.model=model
        self.isAirBagOK=isAirBagOK
        self.isPaintingOK=isPaintingOK
        self.isMechanicalOK=isMechanicalOK
car_01=Car('seat', 'ibiza', True, True, True) #lista INSTANCJI tej KLASY
car_02=Car('opel', 'corsa', True, False, True)
#mam 2 instancje klasy car
print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicalOK)



#ZADANIE
class Cake:
     def __init__(self, name, kind, taste,additives, filling,weight):
        self.name=name
        self.kind=kind
        self.taste=taste
        self.additives=additives
        self.filling=filling
        self.weight=weight
cake_01=Cake('Beza Pavlova', 'tort', 'bardzo słodki', 'owoce', ' mascarpone', 1.2)
cake_02=Cake('Czekoladowe', 'tort', 'słodko-gorzki', 'orzechy', 'mascarpone i czekolada', 2)
bakery_offer=[]
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)

print('dzisiaj w naszej ofercie:')
for c in bakery_offer:
    print('{}-({}) main taste:{} with additives of {}, filled with {}, weight {}'.format(c.name, c.kind, c.taste, c.additives, c.filling, c.weight))
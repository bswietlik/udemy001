

class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK):
        self.brand=brand
        self.model=model
        self.isAirBagOK=isAirBagOK
        self.isPaintingOK=isPaintingOK
        self.isMechanicalOK=isMechanicalOK
    def isDamaged(self): #funkcja staje się elementem składowym klasy. definiujemy ją w klasie
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK) #pisząc metodę klasy odwołuję się do atrybutów klasy z self
    def GetInfo(self):
        print("{}  {}".format(self.brand, self.model).upper())
        print("air bag   -   ok    -    {}".format(self.isAirBagOK))
        print("painting    - ok-     {}".format(self.isPaintingOK))
        print('-----------------')

car_01 = Car('seat', 'ibiza', True, True, True)
car_02=Car('opel', 'corsa', True, False, True)
print (car_01.brand, car_01.model, car_01.isDamaged())
car_01.GetInfo()


#ZADANIE dodaj metody do klasy CAKE
class Cake:
    def __init__(self, name, kind, taste, additives, filling, weight):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.weight = weight
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if self.additives:
            print("Additives: {}".format(self.additives))
            for a in self.additives:
                print("{}".format(a))
        if self.filling:
            print("Filling: {}".format(self.filling))
        print('-'*20)
    def set_filling(self,new_filling):
        self.filling=new_filling
    def add_additives(self,new_additives):
        self.additives.append(new_additives)

cake_01 = Cake('Beza Pavlova', 'tort', 'bardzo słodki', ['owoce', 'mascarpone'], [' mascarpone'], 1.2)
cake_02 = Cake('Czekoladowe', 'muffin', 'słodko-gorzki', ['orzechy'], '', 2)
bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)

cake_01.set_filling('krem pistacjowy')
cake_02.add_additives('maliny')

print('dzisiaj w naszej ofercie:')
for c in bakery_offer:
    c.show_info()
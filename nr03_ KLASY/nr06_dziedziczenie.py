#do przykładu z samochodami chcemy dodać właściwość łądowność, ale nie zmieniając atrybutów
#chcę dodać nową klasę Truck, którą będzie dziedziczyć właściwości z klasy car
brandOnSale='Opel'
class Car:

    numberOfCars=0
    listOfCars=[]

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale):
        self.brand=brand
        self.model=model
        self.isAirBagOK=isAirBagOK
        self.isPaintingOK=isPaintingOK
        self.isMechanicalOK=isMechanicalOK
        self.__isOnSale=isOnSale #ukrycie atybutu
        Car.numberOfCars+=1
        Car.listOfCars.append(self)

    def isDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK)

    def GetInfo(self):
        print("{}  {}".format(self.brand, self.model).upper())
        print("air bag   -   ok    -    {}".format(self.isAirBagOK))
        print("painting    - ok-     {}".format(self.isPaintingOK))
        print('OS ON SALE       {}'.format(self.__isOnSale))
        print('-----------------')


    def GetIsOnSale(self):
        return self.__isOnSale

    def SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand==brandOnSale:
            self.__isOnSale=newIsOnSaleStatus
            print('zmiana statusu isOnSale to {} for {}'.format(newIsOnSaleStatus,self.brand))
        else:
            print('Nie można zmienić statusu isOnSale. Wyprzedaż tylko dla {}'.format(brandOnSale))


    IsOnSale=property(GetIsOnSale, SetIsOnSale, None, 'jeśli zmiana na true, samochód jest na sprzedaż w promocji')#wybieram metody

#Tworzę klasę, która dziedziczy z Car
class Truck(Car):
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale, capacityKg):
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale)#odwołuje się do instancji klasay rodzicielskiej
        # inna metoda to : Car.__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale)
        self.capacityKg=capacityKg
 #dodajemy metodę GetInfo ale z dopisaniem Capacity i musimy mieć jej właściwości z klasy rodzicielskiej
    def GetInfo(self):
        super().GetInfo()
        print('CapacityKg    -     {}'.format(self.capacityKg))


truck_01=Truck('Ford','Transit', True, False, True, False, 1600 )
truck_02=Truck('Renault', 'Trafic', True, True, True, True, 1200)

print('Calling properties:')
print(truck_01.brand, truck_01.capacityKg, truck_01.IsOnSale, truck_02.brand, truck_02.capacityKg, truck_02.IsOnSale)
truck_01.GetInfo() #korzystamy z metody z klasy Car, ale tam nie ma nic o CapacityKgMusimy to dodać


#Zadanie
class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

class SpecialCake(Cake):
    def __init__(self,name, kind, taste, additives, filling, ocassion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.ocassion=ocassion
        self.shape=shape
        self.ornaments=ornaments
        self.text=text
    def show_info(self):
        super().show_info()
        print('ocassion:    {}:'.format(self.ocassion))
        print('shape     {}:'.format(self.shape))
        print('ornaments     {}:'.format(self.ornaments))
        print('text     {}:'.format(self.text))

birthday=SpecialCake('Torcik Orzechowy', 'tort', 'czekoladowo-orzechowy', 'orzechy', 'mascaropne', 'na urodziny', 'okrągły', [], 'sto lat')

wedding=SpecialCake('Tort Weselny', '3 poziomowy', 'smak egzotyczny', 'ananasy', 'mascarpone', 'na wesele', 'prostokątny', 'para młoda', [])

birthday.show_info()
wedding.show_info()

for cake in SpecialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()
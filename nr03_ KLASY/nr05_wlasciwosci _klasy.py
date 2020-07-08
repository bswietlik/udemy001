brandOnSale='Opel' #oznaczam, ze można modyfikować tylko warunki promocyjnej sprzedazy marki opel
class Car:

    numberOfCars=0
    listOfCars=[] #jesli utworzymy nowy obiekt to dodamy go do listy

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK, isOnSale):
        self.brand=brand #atrybuty instancji
        self.model=model
        self.isAirBagOK=isAirBagOK
        self.isPaintingOK=isPaintingOK
        self.isMechanicalOK=isMechanicalOK
        self.__isOnSale=isOnSale #ukrycie atybutu
        Car.numberOfCars+=1 #po dodaniu nowego samochodu(obiektu)  zwiększa się liczba o 1
        Car.listOfCars.append(self)  #dodaje się do listy samochodow

    def isDamaged(self): #funkcja staje się elementem składowym klasy. definiujemy ją w klasie
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK) #pisząc metodę klasy odwołuję się do atrybutów klasy z self

    def GetInfo(self):
        print("{}  {}".format(self.brand, self.model).upper())
        print("air bag   -   ok    -    {}".format(self.isAirBagOK))
        print("painting    - ok-     {}".format(self.isPaintingOK))
        print('OS ON SALE       {}'.format(self.__isOnSale))
        print('-----------------')

#Modyfikowanie właśćiwości atrybutu
    def GetIsOnSale(self):
        return self.__isOnSale
#zmienienie właściwości atrybutu
    def SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand==brandOnSale:
            self.__isOnSale=newIsOnSaleStatus
            print('zmiana statusu isOnSale to {} for {}'.format(newIsOnSaleStatus,self.brand))
        else:
            print('Nie można zmienić statusu isOnSale. Wyprzedaż tylko dla {}'.format(brandOnSale))

     #definiuję nową właściwośc dla klasy
    IsOnSale=property(GetIsOnSale, SetIsOnSale, None)#wybieram metody
car_01 = Car('seat', 'ibiza', True, True, True, False) #zdefiniowana instancja klasy
car_02=Car('Opel', 'corsa', True, False, True, True)

print('Status of car:' ,car_01.GetIsOnSale(), car_02.GetIsOnSale())
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print('Status of car:' ,car_01.GetIsOnSale(), car_02.GetIsOnSale())
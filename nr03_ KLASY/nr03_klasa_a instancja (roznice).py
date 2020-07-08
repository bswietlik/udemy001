
class Car:
#zmienne można zdefiniować na poziomie klasy
    numberOfCars=0
    listOfCars=[] #jesli utworzymy nowy obiekt to dodamy go do listy

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicalOK):
        self.brand=brand #atrybuty instancji
        self.model=model
        self.isAirBagOK=isAirBagOK
        self.isPaintingOK=isPaintingOK
        self.isMechanicalOK=isMechanicalOK
        Car.numberOfCars+=1 #po dodaniu nowego samochodu(obiektu)  zwiększa się liczba o 1
        Car.listOfCars.append(self)  #dodaje się do listy samochodow

    def isDamaged(self): #funkcja staje się elementem składowym klasy. definiujemy ją w klasie
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicalOK) #pisząc metodę klasy odwołuję się do atrybutów klasy z self

    def GetInfo(self):
        print("{}  {}".format(self.brand, self.model).upper())
        print("air bag   -   ok    -    {}".format(self.isAirBagOK))
        print("painting    - ok-     {}".format(self.isPaintingOK))
        print('-----------------')

car_01 = Car('seat', 'ibiza', True, True, True) #zdefiniowana instancja klasy
car_02=Car('opel', 'corsa', True, False, True)

print('Ilość zmiennych klasy po stworzeniu instancji:', Car.numberOfCars, Car.listOfCars)

print('ID of class is:' , id(Car))
print ('ID od instances are:' , id(car_01), id(car_02))
#czy instancja pochodzi od danje klasy, czy została utworzona od danej klasy
print('Sprawdź czy instancja pochodzi od klasy używając instance:', isinstance(car_01,Car))
print('Sprawdź czy instancja pochodzi od klasy używając type:', type(car_01) is Car)
print('Sprawdź czy instancja pochodzi od klasy używając __class__:', car_01.__class__)

#sprawdzamy atrybuty tego obiektu, wyświetla słownik.
print('lista atrybutów instancji z artościami:', vars(car_01))
print('lista atrybutów instancji z artościami:', vars(Car))

#f. dir wskazuje na listę różnych funkcji
print('lista atrybutów instancji z artościami:', dir(car_01))
print('lista atrybutów instancji z artościami:', dir(Car))
#jesteśmy w stanie pobierać wartości znajdujace się na poziomie klasy odwołując się do nich na poziomie instancji

#ZADANIE
class Cake:
    known_types=['ciasta','mufinki', 'biszkopty', 'eklerki', 'siwiąteczne', 'precle', 'inne']
    bakery_offer=[]
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_types: #jako parametr kind zostanie przekazana wartość znajdująca się na liście known_kinds, to zostanie zaakceptowana, ale jeśli ktoś przekaże wartość spoza tej listy, to do nowo tworzonego obiektu do atrybutu kind zostanie wpisany napis other.
            self.kind=kind
        else:
            self.kind='other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)

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

cake_01 = Cake('Beza Pavlova', 'tort', 'bardzo słodki', ['owoce', 'mascarpone'], [' mascarpone'])
cake_02 = Cake('Czekoladowe', 'muffin', 'słodko-gorzki', ['orzechy'], '')
cake_03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

cake_01.set_filling('krem pistacjowy')
cake_02.add_additives('maliny')

print('dzisiaj w naszej ofercie:')
for c in Cake.bakery_offer:
    c.show_info()

print('Is cake01 of type Cake? (isinstance)', isinstance(cake_01, Cake))
print('Is cake01 of type Cake? (type)', type(cake_01) is Cake)
print('vars cake01', vars(cake_01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake_01))
print('dir Cake?', dir(Cake))
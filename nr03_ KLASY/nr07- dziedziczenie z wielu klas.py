#Dziedziczenie po kilku klasach bazowych

class Car:

    def __init__(self, brand, model, isOnSale):
        print('>>Class Car-init-starting')
        self.brand=brand
        self.model=model
        self.isOnSale=isOnSale
        self.name="{}  {}".format(brand,model)
        print(">>Class Car -- init-- finishing")

    def GetInfo(self):
        print ('>>Class Car-Get Info-starting')
        super().GetInfo()
        print("{}  {}".format(self.brand, self.model).upper())
        print("IS ON SALE      {}".format(self.isOnSale))
        print('>>Class Car-Get Info-finishing')


class Specialist:
    def __init__(self, firstname, lastname, brand):
        print('>>Class Specialist-init-starting')
        self.firstname=firstname
        self.lastname=lastname
        self.name="{}  {}".format(firstname,lastname)
        self.brand=brand
        print('>>Class Specialist-init-finishing')

    def GetInfo(self):
        print('>>Class Specialist-Get Info-starting')
        print("{}   {}-  (())".format(self.firstname, self.lastname, self.brand))
        print('>>Class Specialist-Get Info-finishing')

#tworzymy klasę dziedziczącą po dwóch ostatnich

class CarSpecialist(Car, Specialist):
    def __init__ (self, brand, model, isOnSale, firstname, lastname):
        print('>>Class CarSpecialist-init-starting')
        Car.__init__(self, brand, model, isOnSale) #metoda super zwróiłaby tylko jednego rodzica, dlatego stosujemy tę metodę
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print('>>Class CarSpecialist-init-finishing')
#tworzę obiekt

Tom=CarSpecialist('toyota', 'corolla', True, 'Tom', 'Smith' )
print(vars(Tom))
from sensores import MonederoSensor
class cafeteraBasica(object):

    def __init__(self,agua,cafe,azucar,moneda):
        self.agua = agua
        self.cafe = cafe
        self.azucar = azucar
        self.moneda = moneda
    def hacerCafe(self):
        if self.disponibilidad()==True:
            return True
        else:
            return False
    def disponibilidad(self):
        if self.moneda<1:
            return False
        elif self.agua<250:
            return False
        elif self.azucar<10:
            return False
        elif self.cafe<50:
            return False
        else:
            self.moneda-=1
            self.agua-=250
            self.azucar-=10
            self.cafe-=50

            return True

class CafeteraPremium(object):

    def __init__(self,agua,cafe,azucar,moneda):
        self.agua = agua
        self.cafe = cafe
        self.azucar = azucar
        self.moneda = moneda

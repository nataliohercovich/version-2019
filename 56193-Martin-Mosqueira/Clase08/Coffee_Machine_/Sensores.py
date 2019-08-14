
class MonederoSensor():
    def __init__(self):
        self.dinero=1000

    def get_dinero(self):
        return self.dinero

    def quitar_dinero(self, dinero):
        self.dinero -= dinero

    def poner_dinero(self, dinero):
        self.dinero += dinero

    def controlar_dinero(self,moneda):
        if moneda == 1:
            return True
        else:
            return False

class VasoSensor():
    def __init__(self):
        self.seleccionar_vaso=False

    def poner_vaso(self):
        self.seleccionar_vaso=True

    def controlar_vaso(self):
        if self.seleccionar_vaso == False:
            return False
        else:
            return True

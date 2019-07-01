from Class_Coffee import Coffee

class Coffee_Premium(Coffee):
    def __init__(self):
        super(Coffee_Premium,self).__init__()
        self.leche=1000
        self.seleccionar_leche=False

    def control_cantidad_leche(self):
        if self.leche >= 120:
            return True
        else:
            return False

    def leche_cantidad(self,moneda):
        self.leche=self.leche-120*moneda

        return str(self.leche)+'ml'

    def colocar_leche(self):
        self.seleccionar_leche=True


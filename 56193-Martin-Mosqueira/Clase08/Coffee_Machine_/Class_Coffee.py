
class Coffee():
    def __init__(self):
        self.agua=1000
        self.cafe=50
        self.azucar=600
        self.seleccionar_azucar=False

    def control_cantidad(self):
        if self.agua >= 250 and self.cafe >= 10 and self.azucar >= 8:
            return True
        else:
            return False

    def cafe_cantidad(self,moneda):
        self.cafe=self.cafe-10*moneda
        self.agua = self.agua - 250 * moneda

        return str(self.cafe)+'g'+str(self.agua)+'ml'

    def colocar_azucar(self):
        self.seleccionar_azucar=True


    def azucar_cantidad(self,moneda):
        self.azucar=self.azucar-8*moneda

        return str(self.azucar)+'g'





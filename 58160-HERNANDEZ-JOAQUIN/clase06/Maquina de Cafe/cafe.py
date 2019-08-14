class pagoCafetera():
    def __init__(self):
        self.moneda = False
        self.monedaCont = 0
        self.haciendoCafe = False
        self.agua = 1000
        self.cafe = 100
        self.azucar = 100

    def pago(self, moneda):
        if moneda == True:
            if self.agua == 0:
                self.moneda = False
                return 'No hay agua'

            if self.cafe == 0:
                self.moneda = False
                return 'No hay cafe'

            if self.azucar == 0:
                self.moneda = False
                return 'No hay azucar'

            else:

                self.haciendoCafe = True
                self.monedaCont += 1
                return 'Haciendo cafe'

    def terminado(self):
        if self.haciendoCafe == True:
            self.haciendoCafe = False
            return 'Cafe hecho'

        else:
            return 'No puedo hacer el cafe' 

class cafeteraBasica(pagoCafetera):
    def __init__(self):
        super().__init__()

    def aguaCant(self, aguaML):
        if self.haciendoCafe == True:
            if int(aguaML) > self.agua:
                self.haciendoCafe = False
                self.agua = 1000
                self.cafe = 100
                self.azucar = 100
                return 'No hay agua suficiente'
            else:
                self.agua -= int(aguaML)
                return 'Con ' + str(aguaML) + 'ml de agua'

    def cafeCant(self, cafeG):
        if self.haciendoCafe == True:
            if cafeG > self.cafe:
                self.agua = 1000
                self.cafe = 100
                self.azucar = 100
                self.haciendoCafe = False
                return 'No hay cafe suficiente'
            else:
                self.cafe -= cafeG
                return 'Con ' + str(cafeG) + 'g de cafe'

    def azucarCant(self, azucarG):
        if self.haciendoCafe == True:
            if azucarG > self.azucar:
                self.agua = 1000
                self.cafe = 100
                self.azucar = 100
                self.haciendoCafe = False
                return 'No hay azucar suficiente'
                
            if azucarG == 0:
                return 'Sin azucar'
            else:
                self.azucar -= azucarG
                return 'Con ' + str(azucarG) + 'g de azucar' 


class cafeteraPremium(pagoCafetera):
    def __init__(self):
        super().__init__()   

    def vasoSN(self, vasoOP):
        if vasoOP == False:
            self.haciendoCafe = False
            return 'Ponga un vaso'

    def aguaCantP(self, aguaMLP):
        if self.haciendoCafe == True:
            if int(aguaMLP) > self.agua:
                self.agua = 1000
                self.cafe = 100
                self.azucar = 100
                self.haciendoCafe = False
                return 'No hay agua suficiente'

            else:
                self.agua -= int(aguaMLP)
                return 'Con ' + str(aguaMLP) + 'ml de agua'

    def cafeCantP(self, cafeGP):
        if self.haciendoCafe == True:
            if cafeGP > self.cafe:
                self.agua = 1000
                self.cafe = 100
                self.azucar = 100
                self.haciendoCafe = False
                return 'No hay cafe suficiente'

            else:
                self.cafe -= cafeGP
                return 'Con ' + str(cafeGP) + 'g de cafe'

    def azucarCantP(self, azucarGP):
        if self.haciendoCafe == True:
            if azucarGP > self.azucar:
                self.agua = 1000
                self.cafe = 100
                self.azucar = 100
                self.haciendoCafe = False
                return 'No hay azucar suficiente'

            if azucarGP == 0:
                return 'Sin azucar'
            else:
                self.azucar -= azucarGP
                return 'Con ' + str(azucarGP) + 'g de azucar'  

    def lecheCant(self, lecheSN):
        if self.haciendoCafe == True:
            if lecheSN == True:
                return 'Con leche'
            if lecheSN == False:
                return 'Sin leche'

    def hacerCafeP(self):
        if self.haciendoCafe == True:
            self.haciendoCafe = False
            return 'Cafe hecho'
        else:
            self.agua = 1000
            self.cafe = 100
            self.azucar = 100
            return 'No puedo hacer el cafe'
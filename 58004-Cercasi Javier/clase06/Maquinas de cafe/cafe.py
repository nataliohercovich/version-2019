class Maquinabasica (object):

    def __init__(self):
        self.nivel_agua=1000
        self.cant_cafe=100
        self.azucar=1000
        self.moneda=0
        self.working=False

    def sensor_moneda (self,mon):
        self.moneda=mon
        if self.moneda==0:
            self.working=False
            return ('Ingrese una moneda')

        if self.moneda ==1:
            if self.nivel_agua==0:
                return ('Disculpe,no poseo agua')
                self.moneda= self.moneda -1

            if self.cant_cafe==0:
                return ('Disculpe,no poseo cafe')
                self.moneda= self.moneda -1

            if self.azucar==0:
                return ('Disculpe,no poseo azucar')
                self.moneda= self.moneda -1

            else:
                self.working=True
                return ('Procesando, aguarde un momento')


    def CantidadAgua (self,cantidad):
        if self.working==True:
            if cantidad > self.nivel_agua:
                return ('Disculpe, cantidad de agua no disponible')
                self.working=False
            if cantidad < self.nivel_agua:
                self.working=True
                self.nivel_agua= self.nivel_agua-cantidad
                return (str(cantidad)+'ml de agua')

    def CantidadCafe (self,cafe):
        if self.working==True:
            if cafe > self.cant_cafe:
                self.working=False
                return ('Disculpe, cantidad de cafe no disponible')
            if cafe < self.cant_cafe:
                self.cant_cafe= self.cant_cafe - cafe
                return (str(cafe)+'g. de cafe')

    def CantidadAzucar (self,azucar):
        if self.working==True:
            if azucar > self.azucar:
                self.working=False
                return ('Disculpe, cantidad de azucar no disponible')
            if azucar < self.azucar:
                self.azucar= self.azucar - azucar
                return (str(azucar)+'g. de azucar')

    
    


            

            

            











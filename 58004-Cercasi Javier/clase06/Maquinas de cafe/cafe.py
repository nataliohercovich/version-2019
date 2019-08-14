class MaquinaBasica (object):

    def __init__(self):
        self.nivel_agua=1000
        self.cant_cafe=100
        self.azucar=1000
        self.moneda=0                   #puede tomar valores 0 o 1
        self.fondos=0
        self.working=False

    def sensor_moneda (self,mon):
        
        if mon==0:
            self.working=False
            return ('Ingrese una moneda')

        if mon >=1:
            if self.nivel_agua==0:
                self.moneda= self.moneda -1     #Resta una moneda, porque la devuelve
                return ('Disculpe,no poseo agua')
                
            if self.cant_cafe==0:
                self.moneda= self.moneda -1
                return ('Disculpe,no poseo cafe')
                
            if self.azucar==0:
                self.moneda= self.moneda -1
                return ('Disculpe,no poseo azucar')
              
            else:
                self.working=True
                self.fondos+=self.fondos
                return ('Procesando, aguarde un momento')


    def cantidadAgua (self,cantidad):
        if self.working==True:

            if cantidad > self.nivel_agua:
                self.working=False
                return ('Disculpe, cantidad de agua no disponible')
                
            if cantidad < self.nivel_agua:
                self.working=True
                self.nivel_agua= self.nivel_agua-cantidad
                return (str(cantidad)+'ml de agua')

    def cantidadCafe (self,cafe):
        if self.working==True:

            if cafe > self.cant_cafe:
                self.working=False
                return ('Disculpe, cantidad de cafe no disponible')

            if cafe < self.cant_cafe:
                self.cant_cafe= self.cant_cafe - cafe
                return (str(cafe)+'g. de cafe')

    def cantidadAzucar (self,azucar):
        if self.working==True:

            if azucar > self.azucar:
                self.working=False
                return ('Disculpe, cantidad de azucar no disponible')

            if azucar < self.azucar:
                self.azucar= self.azucar - azucar
                return (str(azucar)+'g. de azucar')

    def terminado(self):
        if self.working==True:
            self.working==False
            return('Cafe hecho')
        else:
            self.nivel_agua=1000
            self.cant_cafe=100
            self.azucar=1000
            return('No puedo preparar su cafe')


class Maquinapremium(MaquinaBasica):

    def __init__(self):
        super().__init__()
        self.cant_leche=1000 #Gramos de leche en polvo
        self.vaso=False

    def cantidadLeche(self,leche):  
        if self.cant_leche:

            if leche==True:
                self.cant_leche-=20
                return ('Con leche')

            else:
                return('Sin leche')

        else:
            self.working=False
            return ('Disculpe, no poseo leche')

    def vasoSN(self,vaso):
        
        if vaso==True:
            self.working=True
            return ('Vaso colocado')
        
        if vaso==False:
            self.working=False
            return ('Vaso no colocado')
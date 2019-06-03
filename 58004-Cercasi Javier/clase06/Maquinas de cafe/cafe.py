class Maquinabasica (object):

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

        if mon ==1:
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
                self.fondos+=1
                return ('Procesando, aguarde un momento')

    def terminado(self):
        if self.working==True:
            self.working==False
            return('Cafe hecho')
        else:
            return('No puedo preparar su cafe')




    def cantidadAgua (self,cantidad):
        if self.working==True:
            if cantidad > self.nivel_agua:
                return ('Disculpe, cantidad de agua no disponible')
                self.working=False
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

    
    


            

            

            











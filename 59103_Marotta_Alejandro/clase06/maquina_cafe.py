class Cafe:

    def __init__(self,agua=1110,gramoscafe=1110,azucar = 1110,leche= 1110): #si no le paso ningun valor toma esos por defecto
        self.agua = agua #en ml
        self.gramoscafe = gramoscafe
        self.azucar = azucar #en gr
        self.leche = leche #en ml
        
   
   
class CafeChico (Cafe):
   
    def cafe_con_azucar (self,eleccion): # 1 para si y cero para no, la maquina no tiene mas botones
        dulce = int (eleccion)
        if dulce ==1:
            self.azucar -= 5
            self.agua -=110
            self.gramoscafe -= 10
            
        else:
            self.agua -=110
            self.gramoscafe -= 10
                   
             
    
        

class CafePremium (Cafe): #es mas grande
    
    def cafe_con_leche (self, eleccion): # 1 para si y cero para no, teniendo en cuneta que solo tiene dos botones
        leche = int(eleccion)
        if leche == 1:
            self.leche -= 40
            self.agua -= 90
            self.gramoscafe -= 10
        else:
            self.agua -= 130
            self.gramoscafe -= 10

    def cafe_con_azucar (self,eleccion): # del 0 al 5, teniendo en cuanta que la maquina no tiene mas botones
        dulce = int (eleccion)
        if dulce ==1:
            self.azucar -= 1
        if dulce ==2:
            self.azucar -= 2
        if dulce ==3:
            self.azucar -= 3
        if dulce ==4:
            self.azucar -= 4
        if dulce ==5:
            self.azucar -= 5
        else:
            pass


class Sensor:  #controla que tengan los valores minimos como para poder funcionar correctamente

    def controlar(self,agua,gramoscafe,azucar,leche):
        self.agua = agua
        self.gramoscafe = gramoscafe
        self.azucar = azucar
        self.leche = leche

        if agua <130:
            print ('No hay agua, debe reiniciar la maquina')
            return False

        if gramoscafe <10:
            print ('No hay cafe, debe reiniciar la maquina')
            return False


        if azucar < 5 and leche < 40:
            reinicio = input('No hay ni azucar ni leche , desea tomarlo puro? si/no ')
            if reinicio == 'si':
                return True
            else :
                print ('No hay azucar ni leche  ,debe cargar la maquina')
                return False


        if azucar < 5:
            reinicio = input('No hay azucar, desea tomarlo amargo? si/no ')
            if reinicio == 'si':
                return True
            else :
                print ('No hay azucar ,debe cargar la maquina')
                return False

        if leche < 40:
            reinicio = input('No hay leche, desea tomarlo puro? si/no ')
            if reinicio == 'si':
                return True
            else :
                print ('No hay leche ,debe cargar la maquina')
                return False
        else:
            return True


        




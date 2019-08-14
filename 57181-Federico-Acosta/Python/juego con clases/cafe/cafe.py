
class MonederoSensor():
    def __init__(self):
        self.dinero = 0
    def get_dinero(self):
        return self.dinero
    def quitar_dinero(self, dinero):
        dinero = int(dinero)
        self.dinero -= dinero
    def poner_dinero(self, dinero):
        dinero = int(dinero)
        self.dinero += dinero
class VasoSensor():
    def __init__(self):
        self.vaso = False
    def poner_vaso(self):
        self.vaso = True
    def quitar_vaso(self):
        self.vaso = False
        
class Basico():

    def __init__(self):
        self.cafe = 100
        self.azucar = 100
        self.agua = 100
        self.ingredientes = [0, 0, 0]
        self.trabajando = False
        self.moneda = MonederoSensor()

    def todo_disponible(self):
        self.ingredientes = [0, 0, 0]
        azucar = ""
        if self.agua == 0:
            print("Se acabo el agua!")
            return False
        else:
            self.ingredientes[0] = 1
        if self.cafe == 0:
            print("Se acabo el cafe!")
            return False
        else:
            self.ingredientes[1] = 1
        if self.azucar == 0:
            print("No hay mas azucar")
            while azucar != "si" and azucar != "no":
                azucar = input("Continuar sin Azucar?")
                if azucar == "si":
                    self.ingredientes[2] = 0
                    return True
                elif azucar == "no":
                    return False
                else:
                    print("Ingrese 'si' o 'no'")
        else:
            while azucar != "si" and azucar != "no":
                azucar = input("Quiere agregar Azucar?")
                if azucar == "si":
                    self.ingredientes[2] = 1
                    return True
                elif azucar == "no":
                    self.ingredientes[2] = 0
                    return True
                else:
                    print("Ingrese 'si' o 'no'")
    def descuento(self):
        self.agua = self.agua - self.ingredientes[0]
        self.cafe = self.cafe - self.ingredientes[1]
        self.azucar = self.azucar - self.ingredientes[2]
        return True
    def hacer_cafe(self):

        moneda = ""
        while moneda != "1":
            moneda = input("Ponga '1' para ingresar una moneda: ")
            if moneda == "1":
                self.moneda.poner_dinero(moneda)
                if self.todo_disponible() == True:
                    self.trabajando == True
                    self.descuento()
                    print("Cafe completado")
                    self.trabajando == False
                elif self.todo_disponible() == False:
                    print("No se hizo el cafe")
                    print("Devolviendo el dinero")
                    self.moneda.quitar_dinero(moneda)
                else:
                    print("ERROR")
            else:
                print("Solo se aceptan monedas de '1'")

        
        

class Premium(Basico):
    def __init__(self):
        self.cafe = 100
        self.azucar = 100
        self.agua = 100
        self.leche = 100
        self.ingredientes = [0, 0, 0, 0]
        self.trabajando = False
        self.moneda = MonederoSensor()
        self.vaso = VasoSensor()
        

    def todo_disponible(self):
        self.ingredientes = [0, 0, 0, 0]
        azucar = ""
        leche = ""
        cantidad = ""
        if self.agua == 0:
            print("Se acabo el agua!")
            return False
        else:
            self.ingredientes[0] = 1
        if self.cafe == 0:
            print("Se acabo el cafe!")
            return False
        else:
            self.ingredientes[1] = 1
        if self.azucar == 0:
            print("No hay mas azucar")
            while azucar != "si" and azucar != "no":
                azucar = input("Continuar sin Azucar?")
                if azucar == "si":
                    self.ingredientes[2] = 0
                elif azucar == "no":
                    return False
                else:
                    print("Ingrese 'si' o 'no'")
        else:
            while azucar != "si" and azucar != "no":
                azucar = input("Quiere agregar Azucar?")
                if azucar == "si":
                    while cantidad != '0' or cantidad != '1' or cantidad != '2' or cantidad != '3' or cantidad != '4' or cantidad != '5':
                        cantidad = input("ingrese del 0 al 5 cuantos gramos quiere agregar: ")
                    self.ingredientes[2] = int(cantidad)
                elif azucar == "no":
                    self.ingredientes[2] = 0
                else:
                    print("Ingrese 'si' o 'no'")
        if self.leche == 0:
            print("No hay mas leche")
            while leche != "si" and leche != "no":
                leche = input("Continuar sin Leche?")
                if leche == "si":
                    self.ingredientes[3] = 0
                elif leche == "no":
                    return False
                else:
                    print("Ingrese 'si' o 'no'")
        else:
            while leche != "si" and leche != "no":
                leche = input("Quiere agregar Leche?")
                if leche == "si":
                    self.ingredientes[3] = 1
                elif leche == "no":
                    self.ingredientes[3] = 0
                else:
                    print("Ingrese 'si' o 'no'")
    
    def descuento(self):
        self.agua = self.agua - self.ingredientes[0]
        self.cafe = self.cafe - self.ingredientes[1]
        self.azucar = self.azucar - self.ingredientes[2]
        self.leche = self.leche - self.ingredientes[3]
        return True
    
def main():
    
    prueba = Basico()
    print(prueba.cafe, prueba.agua, prueba.azucar, prueba.moneda.dinero)
    prueba.hacer_cafe()
    print(prueba.cafe, prueba.agua, prueba.azucar, prueba.moneda.dinero)

    prueba2= Premium()
    print(prueba2.cafe, prueba2.agua, prueba2.azucar, prueba2.leche, prueba2.moneda.dinero,)
    prueba2.hacer_cafe()
    print(prueba2.cafe, prueba2.agua, prueba2.azucar, prueba2.leche, prueba2.moneda.dinero)
main()
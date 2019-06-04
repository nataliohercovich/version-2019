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

class Basico():

    def __init__(self):
        self.cafe = 100
        self.azucar = 100
        self.agua = 100
        self.ingredientes = [0, 0, 0]
        self.trabajando = False
        self.moneda = MonederoSensor()

    def check_agua(self):
        if self.agua == 0:
            return False
        else:
            return True
    
    def check_cafe(self):
        if self.cafe == 0:
            return False
        else:
            return True

    def check_azucar(self):
        if self.azucar == 0:
            return False
        else:
            return True

    def todo_disponible(self):
        agua = self.check_agua()
        cafe = self.check_cafe()
        azucar = self.check_azucar()

        if agua == False:
            print("No queda Agua!")
            return False
        if cafe == False:
            print("No queda Cafe!")
            return False

        
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
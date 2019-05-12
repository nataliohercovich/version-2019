class Calculadora(object):
    def __init__(self):
        self.ingresado = ''
        self.ingresado_1 = ''
        self.operador = ''  

    
    def ingresar(self,letra):    
        try:
            num = int (letra)
            if self.operador:
                self.ingresado_1 = num
            else:
                self.ingresado = num
        except:
            if letra == '=':
                if self.operador == '+':
                    self.ingresado = self.ingresado + self.ingresado_1
                    self.ingresado_1 = ''
                    self.operador = ''

                if self.operador == '-':
                    self.ingresado = self.ingresado - self.ingresado_1
                    self.ingresado_1 = ''
                    self.operador = ''

                if self.operador == '*':
                    self.ingresado = self.ingresado * self.ingresado_1
                    self.ingresado_1 = ''
                    self.operador = ''

                if self.operador == '/':
                    self.ingresado = int(self.ingresado / self.ingresado_1)
                    self.ingresado_1 = ''
                    self.operador = ''

            else:
                self.operador = letra
            
    def display(self):
        display = str(self.ingresado)
        return display    
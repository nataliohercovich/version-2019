class calculadora():
    def __init__(self):
        self.calculando=True
        self.operador=''
    def ingresar(self, letra):
        try:
            num=int(letra)
            if self.operador: #si hay operador
                self.ingresado_1=num #en ingresado_1 va el numero
            else:
                self.ingresado=num #si no hay operador en ingresado va el numero
        except:
            if letra== '=':
                if self.operador == '+':
                    self.ingresado= str(int((int(self.ingresado) + int(self.ingresado_1))))
                    self.ingresado_1= ''
                    self.operador=''

                if self.operador == '-':
                    self.ingresado= str(int((int(self.ingresado) - int(self.ingresado_1))))
                    self.ingresado_1= ''
                    self.operador=''

                if self.operador == '/':
                    self.ingresado= str(int((int(self.ingresado) / int(self.ingresado_1))))
                    self.ingresado_1= ''
                    self.operador=''

                if self.operador == '*':
                    self.ingresado= str(int((int(self.ingresado) * int(self.ingresado_1))))
                    self.ingresado_1= ''
                    self.operador=''
            else:
                self.operador=letra

    def display(self):
        display= self.ingresado + self.operador + self.ingresado_1
        return display



    



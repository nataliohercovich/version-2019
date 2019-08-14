class calculadora():
    def __init__(self):
        self.ingresado = 0
        self.operador = None
        self.ingresado1 = 0
    def ingresar(self,letra):
        if letra == 'C':
            self.ingresado = 0
            self.operador = None
            self.ingresado1 = 0
            return
        try:
            num = int (letra)
            if self.operador == None:
                self.ingresado = self.ingresado * 10 + num
                return
            self.ingresado1 = self.ingresado1 * 10 + num
        except:
            op_anterior = False
            if self.ingresado != None:
                op_anterior = True
            if letra == '=' or op_anterior == True: 
                if self.operador == '+':
                    self.ingresado = self.ingresado + self.ingresado1
                if self.operador == '*':
                    self.ingresado = self.ingresado * self.ingresado1
                if self.operador == '-':
                    self.ingresado = self.ingresado - self.ingresado1
                if self.operador == '/':
                    self.ingresado = self.ingresado // self.ingresado1
            else:
                self.operador = letra
                return
            self.operador = None
            self.ingresado1 = 0
            if op_anterior == True:
                self.operador = letra
    def display (self):
        return str(self.ingresado)
    
class Calculadora (object):
    def __init__(self):
        self.ingresado2=0
        self.ingresado1=0
        self.operador=None

    def ingresar(self,letra):

        if letra=='C':
            self.operador=None
            self.ingresado1=0
            self.ingresado2=0
        
        try:

            num=int(letra)
            if self.operador:       #si hay operador
                self.ingresado2=num
                
            else:
                self.ingresado1=num
                    
        except:

            if letra == '=':
                

                if self.operador == '+':
                    
                    self.ingresado1= self.ingresado1 + self.ingresado2

                if self.operador == '-':
                    
                    self.ingresado1= self.ingresado1 - self.ingresado2

                if self.operador == '/':
    
                    self.ingresado1 /= self.ingresado2

                if self.operador == '*':

                    self.ingresado1 *= self.ingresado2
                
                self.operador=None      #debemos blanquear el atributo, porque queda guardado
                self.ingresado2=0
            
            else:
                self.operador=letra
                return

    def display (self):
        return str(self.ingresado1)


                
                

  

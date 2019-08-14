class calculo (object):

    def __init__ (self):

        self.operando1= 0
        self.operador= None
        self.operando2= 0
       
        
        


    def ingresar(self, character):


        try:
            num = int(character)
            if self.operador == None:
                self.operando1 = self.operando1*10 + num
                return
            self.operando2 = self.operando2*10 + num
            
        except:            
           
            operacion_anterior = False
            if self.operador != None:
                operacion_anterior = True

            
            if character == '=' or operacion_anterior == True:
                if self.operador == '+':
                    self.operando1 += self.operando2
                    
                if self.operador== '-':
                    self.operando1 -= self.operando2              

                if self.operador== '*':
                    self.operando1 *= self.operando2                  

                if self.operador == '/':
                    self.operando1 /= self.operando2
                
                self.operador = None
                self.operando2 = 0

                if operacion_anterior == True:
                    self.operador= character    


            if character == 'c':
                self.operando1= 0
                self.operador= None
                self.operando2= 0
       
            else:
                self.operador = character
                

                
    
    def display (self):

        display = str (self.operando1)

        return display
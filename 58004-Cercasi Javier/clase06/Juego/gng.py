import random

class Game():
    def __init__(self):
        self.is_playing=True
    def finish(self):
        self.is_playing=False

class HumanAgainstComputerGame(Game):       #como tambien es un juego, puedo llamar a la clase Game (herencia)

    def __init__(self):
        self.is_playing=True #nos ahorramos esto con la clase game
        self.secret_number= random.randrange(101)       #self es un objeto,para reutilizarlo

        '''super().__init__() '''    #aca llama al init de la clase Game, es como la general

    def pensar_numero(self,number):
        if self.secret_number> number:
            return "My number is bigger"

        if self.secret_number< number:
            return "My number is smaller"

        if self.secret_number == number:
            self.finish()
            return "You win"
            

class ComputerAgainstHumanGame(Game):

    def __init__(self):
        self.is_playing = True
        self.cliente = 50
        self.cota_max=100 #self porque la vamos a usar varias veces
        self.cota_min=0
    

    def play(self,respuesta):           
        try:
            respuesta = int(respuesta)
        except:
            if respuesta == '+':            #aca hace la logica de que este entre 50 y 100, despues entre 75 y 50
                self.cota_min = self.cliente
                self.cliente = self.cliente + int((self.cota_max - self.cota_min)/2)
                
            if respuesta == '-':
                self.cota_max = self.cliente
                self.cliente = self.cliente - int((self.cota_max - self.cota_min)/2)
                
            if respuesta == '=':
                self.is_playing = False
        return

    def input_text(self):

        ans = ('Is it your number '+str(self.cliente)+'?')
        return ans
        


        
    
class Game():
    def __init__(self):
        self.isplaying=True
    def finish(self):
        self.playing=False

class HumanAgainstComputerGame(Game):       #como tambien es un juego, puedo llamar a la clase Game (herencia)

    def __init__(self):
        '''self.is_playing=True #nos ahorramos esto con la clase game'''

        super()__init__():      #aca llama al init de la clase Game, es como la general
        self.secret_number= random.randrange(101)       #self es un objeto,para reutilizarlo


    def pensar_numero(self,number):
        if self.secret_number> number:
            return "My number is bigger"

        if self.secret_number< number:
            return "My number is smaller"

        if self.secret_number == number:
            return "You win"

class ComputerAgainstHumanGame(object):

    def __init__(self):
        '''self.isplaying=True'''
        self.cota_max=100 #self porque la vamos a usar varias veces
        self.cota_min=1

    def input_text (self):
        #aca hace la logica de que este entre 50 y 100, despues entre 75 y 50


    def play (self,respuesta):
        #


    

        


        
    
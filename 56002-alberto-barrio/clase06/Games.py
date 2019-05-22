from random import randint
class Game():
    def __init__(self):
        self.is_playing= True
    def finish(self):
        self.is_playing=False

class HumanAgainstComputerGame(Game):
    def __init__(self):
        self.thinknumber()

    def thinknumber(self):
        self.secret_number=randint(1,100)
    
    def play(self,number):
        if self.secret_number > number:
            return "My number is bigger"
        elif self.secret_number < number:
            return "My number is smaller"
        else:
            self.finish()
            return "You win"

class ComputerAgainstHumanGame(Game):
    def __init__(self):
        self.cota_minina=1
        self.cota_maxima=100
    
    def input_text(self):#la computadora pienza
        pass
    
    def play(self,answer):#el humano respomde
        pass  
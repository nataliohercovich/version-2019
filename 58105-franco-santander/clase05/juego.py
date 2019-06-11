from random import randint

class Game ():
    def __init__ (self):
        self.is_playing = True
    def finish ():
        self.is_playing = False

class HumanAgainstComputerGame(Game):
    def __init__(self):
        '''self.is_playing = True (Esto no va por que ya esta heredado)'''
        self.secret_number = random.randint(1, 100)

    def play(self, num):
        number = int(num)
        if self.secret_number > number :
            return 'My number is bigger'
        elif self.secret_number < number :
            return 'My number is smaller'
        elif self.secret_number == number :
            self.is_playing = False
            return "You win"

class ComputerAgainstHumanGame(Game):
    def __init__ () :
        '''self.is_playing = True (Esto no va por que ya esta heredado)'''
        self.cota_min = 1
        self.cota_max = 100
        self.mitad = int(((self.cota_max + self.cota_min) - 1) / 2)
        self.input_text = f"Is it your number {self.mitad}?"
    
    def play(self, respuesta):
        if respuesta == "+": '''(significa que nuestro numero es mayor que el de la maquina)'''
            self.cota_min = self.mitad
            self.mitad = int(((self.cota_max + self.cota_min) - 1) / 2)
            self.input_text = f"Is it your number {self.mitad}?"
        elif respuesta == "-": '''(significa que nuestro numero es menor que el de la maquina)'''
            self.cota_max = self.mitad
            self.mitad = int(((self.cota_max + self.cota_min) - 1) / 2)
            self.input_text = f"Is it your number {self.mitad}?"
        elif respuesta == "=": '''(significa que nuestro numero es igual que el de la maquina)'''
            print("You win")
            self.is_playing = False
            return "I win"









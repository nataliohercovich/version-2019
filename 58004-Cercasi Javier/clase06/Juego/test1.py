import unittest
from gng import (
   
   HumanAgainstComputerGame,
   ComputerAgainstHumanGame
   
)

class TestHumanAgainstComputerGame(unittest.TestCase):
    def setUp(self):
        self.game = HumanAgainstComputerGame()
        self.game.secret_number = 78

    '''def test_play_small(self):
       self.game = HumanAgainstComputerGame()   #Esto es lo mismo que lo de arriba,pero para no repetir
       self.game.secret_number = 78
       self.assertEquals(self.game.play(50), 'My number is bigger')
       self.assertTrue(self.game.is_playing)'''

    def test_play_small(self):
        self.assertEquals(self.game.pensar_numero(50), 'My number is bigger')
        self.assertTrue(self.game.is_playing)
    
    def test_play_big(self):
        self.assertEquals(self.game.pensar_numero(80), 'My number is smaller')
        self.assertTrue(self.game.is_playing)

    def test_play_win(self):
        self.assertEquals(self.game.pensar_numero(78), 'You win')
        self.assertFalse(self.game.is_playing)


class TestComputerAgainstHuman(unittest.TestCase):
    def setUp(self):
        self.game = ComputerAgainstHumanGame()

    def test_guess_number(self):  

        
        self.assertEquals(self.game.input_text(), 'Is it your number 50?')
        self.game.play('+')
        self.assertTrue(self.game.is_playing)
        
        self.assertEquals(self.game.input_text(), 'Is it your number 75?')
        self.game.play('+')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 87?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 81?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 78?')
        self.game.play('-')
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.input_text(), 'Is it your number 77?')
        self.game.play('=')


if __name__ == "__main__":
   unittest.main()

    
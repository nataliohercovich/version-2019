
import unittest
from cafe import Maquina

class TestHumanAgainstComputerGame(unittest.TestCase):
    def test_play_small(self):
       self.game = HumanAgainstComputerGame()   #Esto es lo mismo que lo de arriba,pero para no repetir
       self.game.secret_number = 78
       self.assertEquals(self.game.play(50), 'My number is bigger')
       self.assertTrue(self.game.is_playing)
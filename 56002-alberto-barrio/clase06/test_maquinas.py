import unittest

from Maquinas_de_cafe import Maquina_de_Cafe_Basica


class TestCoffeMachine(unittest.TestCase):
    
    def test_cafe(self):
        self.cafe = Maquina_de_Cafe_Basica()
        self.assertEquals(self.cafe.coins(1), 'Start')
        
if __name__ == "__main__":
    unittest.main()
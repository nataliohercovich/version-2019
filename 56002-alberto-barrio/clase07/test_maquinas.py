import unittest
from cafe import (
    cafeteraBasica
)


class Cafetera_Basica(unittest.TestCase):
    def setUp(self):
        self.cafeBasico = cafeteraBasica(1000,2000,100,100)
    
    def test_cafe_basico(self):
        self.assertTrue(self.cafeBasico.hacerCafe())
    
    def test_cafe_basico_no_agua(self):
        self.cafeBasico.agua = 0
        self.assertFalse(self.cafeBasico.hacerCafe())
    
    def test_cafe_basico_no_cafe(self):
        self.cafeBasico.cafe = 0
        self.assertFalse(self.cafeBasico.hacerCafe())

    def test_cafe_basico_no_azucar(self):
        self.cafeBasico.azucar = 0
        self.assertFalse(self.cafeBasico.hacerCafe())

    def test_cafe_basico_dos(self):
        self.assertTrue(self.cafeBasico.hacerCafe())
        self.assertTrue(self.cafeBasico.hacerCafe())
    
    def test_cafe_basico_se_acabp(self):
        self.assertTrue(self.cafeBasico.hacerCafe())
        self.assertTrue(self.cafeBasico.hacerCafe())
        self.assertTrue(self.cafeBasico.hacerCafe())
        self.assertTrue(self.cafeBasico.hacerCafe())
        self.assertFalse(self.cafeBasico.hacerCafe())
        
if __name__ == "__main__":
    unittest.main()
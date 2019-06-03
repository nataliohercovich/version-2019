import unittest
from cafe import (Maquinabasica)


class Test_CafeteraBasica(unittest.TestCase):
    def setUp(self):
        self.cafeB = Maquinabasica()

    def test_cafe_1(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.CantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.CantidadCafe(5), '5g. de cafe')
        self.assertEqual(self.cafeB.CantidadAzucar(0), '0g. de azucar')

    def test_cafe_2(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.CantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.CantidadCafe(15), '15g. de cafe')
        self.assertEqual(self.cafeB.CantidadAzucar(3), '3g. de azucar')

    
    def test_cafe_SinAgua(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.CantidadAgua(1001),'Disculpe, cantidad de agua no disponible')
    def test_cafe_SinCafe(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.CantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.CantidadCafe(101), 'Disculpe, cantidad de cafe no disponible')

    def test_cafe_SinMoneda(self):
        self.assertEqual(self.cafeB.sensor_moneda(0), 'Ingrese una moneda')

if __name__ == "__main__":
    unittest.main()
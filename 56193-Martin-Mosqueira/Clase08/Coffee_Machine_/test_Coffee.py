import unittest
from Class_Coffee import Coffee
from Class_Coffee_Premium import Coffee_Premium
from Sensores import VasoSensor
from Sensores import MonederoSensor

class Test_Coffee_Machine(unittest.TestCase):

    def test_cafe_cantidad0(self):
        result=Coffee().cafe_cantidad(2)
        self.assertEqual(result,'30g500ml')

    def test_azucar_cantidad_true0(self):
        result=Coffee().azucar_cantidad(3)
        self.assertEqual(result,'576g')

    def test_leche_cantidad(self):
        result=Coffee_Premium().leche_cantidad(5)
        self.assertEqual(result,'400ml')
    def test_leche_cantidad(self):
        result=Coffee_Premium().leche_cantidad(3)
        self.assertEqual(result,'640ml')

    def test_controlar_vaso(self):
        result=VasoSensor().controlar_vaso()
        self.assertFalse(result)
    def test_controlar_dinero0(self):
        result=MonederoSensor().controlar_dinero(1)
        self.assertTrue(result)
    def test_contolar_dinero1(self):
        result=MonederoSensor().controlar_dinero(10)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

import unittest
from interfaz_hexa_to_deci import interfaz_hexa_to_deci

class TestDecimal(unittest.TestCase):

    def test_decimal_1(self):
        result = interfaz_hexa_to_deci('1')
        self.assertEqual(result, 1)
    def test_decimal_2(self):
        result = interfaz_hexa_to_deci('a')
        self.assertEqual(result, 10)
    def test_decimal_3(self):
        result = interfaz_hexa_to_deci('fab')
        self.assertEqual(result, 4011)
    def test_decimal_4(self):
        result = interfaz_hexa_to_deci('ff')
        self.assertEqual(result, 255)
    def test_decimal_5(self):
        result = interfaz_hexa_to_deci('')
        self.assertEqual(result, 'Por favor, ingrese un numero')
    def test_decimal_6(self):
        result = interfaz_hexa_to_deci('-ff')
        self.assertEqual(result, 'Debe ingresar un numero hexadecimal positivo')
    def test_decimal_7(self):
        result = interfaz_hexa_to_deci('KHKDS')
        self.assertEqual(result, 'Debe ingresar un numero hexadecimal positivo')

if __name__ == '__main__':
    unittest.main()
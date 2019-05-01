import unittest
from interfaz import Hexa_interfaz


class TestDecimal(unittest.TestCase):

    
    def test_Decimal_Vacio(self):
        result = Hexa_interfaz('')
        self.assertEqual(result, 'Error1')

    def test_decimal_Hola(self):
        result = Hexa_interfaz('Hola')
        self.assertEqual(result, 'Error2')

    
if __name__ == '__main__':
    unittest.main()
import unittest
from interfaz_hexa_a_decimal import interfaz_hexadecimal

class TestInterfaz(unittest.TestCase):
    def test_interfaz_5(self):
        result = interfaz_hexadecimal('5')
        self.assertEqual(result,5)

    def test_interfaz_hola(self):
        result = interfaz_hexadecimal('HOLA')
        self.assertEqual(result,False)

    def test_interfaz_punto(self):
        result = interfaz_hexadecimal('6.1')
        self.assertEqual(result,False)
    
    def test_interfaz_coma(self):
        result = interfaz_hexadecimal('6,8')
        self.assertEqual(result,False)

    def test_interfaz_234(self):
        result = interfaz_hexadecimal('EA')
        self.assertEqual(result,234)

    def test_hexa_17(self):
        result = interfaz_hexadecimal('11')
        self.assertEqual(result, 17)

    def test_hexa_negativo(self):
        result = interfaz_hexadecimal('-11')
        self.assertEqual(result, False)

    def test_hexa_0(self):
        result = interfaz_hexadecimal('0')
        self.assertEqual(result, 0)

    def test_hexa_minusculas(self):
        result = interfaz_hexadecimal('fff')
        self.assertEqual(result, 4095)

    def test_hexa_minusculas2(self):
        result = interfaz_hexadecimal('4d2')
        self.assertEqual(result, 1234)




if __name__ == '__main__':
  unittest.main()
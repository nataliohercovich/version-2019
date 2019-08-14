import unittest
from hexa_a_decimal import hexa_decimal

class TestHexadecimal(unittest.TestCase):

    def test_hexa_5(self):
        result = hexa_decimal('5')
        self.assertEqual(result,5)
    def test_hexa_10(self):
        result = hexa_decimal('A')
        self.assertEqual(result, 10)
    
    def test_hexa_17(self):
        result = hexa_decimal('11')
        self.assertEqual(result, 17)
    def test_hexa_16(self):
        result = hexa_decimal('10')
        self.assertEqual(result, 16)
    def test_hexa_4095(self):
        result = hexa_decimal('FFF')
        self.assertEqual(result, 4095)    
    def test_hexa_1234(self):
        result = hexa_decimal('4D2')
        self.assertEqual(result, 1234)
    def test_hexa_234(self):
        result = hexa_decimal('EA')
        self.assertEqual(result, 234)
    def test_hexa_51489(self):
        result = hexa_decimal('C921')
        self.assertEqual(result,51489)
    
    
    
    
if __name__ == '__main__':
  unittest.main()
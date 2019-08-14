import unittest
from hexa_to_decimal import hexa_to_decimal

class TestHexaToDecimal(unittest.TestCase):
    def test_convert_A(self):
        result_convert = hexa_to_decimal('A')
        self.assertEqual(result_convert, '10')

    def test_convert_FF(self):
        result_convert = hexa_to_decimal('FF')
        self.assertEqual(result_convert, '255')

    def test_convert_AB(self):
        result_convert = hexa_to_decimal('AB')
        self.assertEqual(result_convert, '171')

    def test_convert_9(self):
        result_convert = hexa_to_decimal('9')
        self.assertEqual(result_convert, '9')

if __name__ == '__main__':
    unittest.main()
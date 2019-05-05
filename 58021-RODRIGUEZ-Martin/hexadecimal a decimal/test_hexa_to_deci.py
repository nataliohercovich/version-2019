import unittest
from hexa_to_deci import hexa_to_deci

class TestDecimal(unittest.TestCase):

    def test_decimal_1(self):
        result = hexa_to_deci('1')
        self.assertEqual(result, 1)
    def test_decimal_2(self):
        result = hexa_to_deci('a')
        self.assertEqual(result, 10)
    def test_decimal_3(self):
        result = hexa_to_deci('fab')
        self.assertEqual(result, 4011)
    def test_decimal_4(self):
        result = hexa_to_deci('ff')
        self.assertEqual(result, 255)
    def test_decimal_5(self):
        result = hexa_to_deci('3f')
        self.assertEqual(result, 63)

if __name__ == '__main__':
    unittest.main()
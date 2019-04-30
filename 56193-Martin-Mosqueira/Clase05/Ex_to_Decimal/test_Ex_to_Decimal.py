import unittest
from Ex_to_Decimal import Hex

class Test_Hex_to_Decimal_number(unittest.TestCase):
    def test_hex_to_decimal_number0(self):
        number=Hex('5')
        self.assertEqual(number,5)
    def test_hex_to_decimal_number1(self):
        number=Hex('A')
        self.assertEqual(number,10)
    def test_hex_to_decimal_number2(self):
        number=Hex('C')
        self.assertEqual(number,12)
    def test_hex_to_decimal_number3(self):
        number=Hex('FFF')
        self.assertEqual(number,4095)
    def test_hex_to_decimal_number4(self):
        number=Hex('4D2')
        self.assertEqual(number,1234)
    def test_hex_to_decimal_number5(self):
        number=Hex('-A')
        self.assertEqual(number,0)
    def test_hex_to_decimal_number6(self):
        number=Hex('-5')
        self.assertEqual(number,0)

if __name__ == '__main__':
    unittest.main()
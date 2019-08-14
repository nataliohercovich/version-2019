import unittest

from hexa_to_decimal import (hexa_to_decimal,hexadecimal_to_decimal)

class TestHexaToDecimal(unittest.TestCase):

    def test_0hex_to_0dec(self):
        ans = hexadecimal_to_decimal('0')
        self.assertEqual(ans,'0')

    def test_1hex_to_1dec(self):
        ans = hexadecimal_to_decimal('1')
        self.assertEqual(ans,'1')

    def test_5hex_to_5dec(self):
        ans = hexadecimal_to_decimal('5')
        self.assertEqual(ans,'5')

    def test_Ahex_to_10dec(self):
        ans = hexadecimal_to_decimal('A')
        self.assertEqual(ans,'10')

    def test_Fhex_to_1dec(self):
        ans = hexadecimal_to_decimal('F')
        self.assertEqual(ans,'15')

    def test_1Ahex_to_26dec(self):
        ans = hexadecimal_to_decimal('1A')
        self.assertEqual(ans,'26')

    def test_82hex_to_130dec(self):
        ans = hexadecimal_to_decimal('82')
        self.assertEqual(ans,'130')

    def test_8BAhex_to_139dec(self):
        ans = hexadecimal_to_decimal('8BA')
        self.assertEqual(ans,'2234')

    def test_4D2hex_to_1234dec(self):
        ans = hexadecimal_to_decimal('4D2')

        self.assertEqual(ans,'1234')

    def test_F5Dhex_to_3933dec(self):

        ans = hexadecimal_to_decimal('F5D')

        self.assertEqual(ans,'3933')

    def test_FFFFhex_to_65535dec(self):
        ans = hexadecimal_to_decimal('FFFF')
        self.assertEqual(ans,'65535')

if __name__ == "__main__":
    unittest.main()
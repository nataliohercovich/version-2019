import unittest
from ronam_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
   def test_roman_I_to_decimal(self):
        import ipdb; ipdb.set_trace()
        decimal_number = roman_to_decimal('I')
      
        self.assertEqual(decimal_number, 1)


if __name__ == '__main__':
    unittest.main()
import unittest
from interface import ishexa

class TestInterface(unittest.TestCase):
    def test_convert_A(self):
        result_convert = ishexa('A')
        self.assertEqual(result_convert, '10')

    def test_is_hexa(self):
        result_convert = ishexa('GHP')
        self.assertEqual(result_convert, 'ERROR: debe ingresar un numero hexadecimals')

if __name__ == '__main__':
    unittest.main()
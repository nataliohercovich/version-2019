import unittest
from interface import isnumber

class TestInterface(unittest.TestCase):
    def test_interfaz_factorial_5(self):
        result = isnumber("casanueva","pais")
        self.assertEqual(result,"raascumnp")

    def test_interfaz_encrypt_number(self):
        result = isnumber(1,1)
        self.assertEqual(result, "Debe ingresar solo letras")

if __name__ == '__main__':
    unittest.main()
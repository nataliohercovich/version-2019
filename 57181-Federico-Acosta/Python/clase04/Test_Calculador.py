import unittest

from calculadora import Calculadora

class TestCalculador(unittest.TestCase):

    def test_Calculadora_1_add_1_(self):

        calc = Calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'2')

    def test_Calculadora_2_rest_1_(self):

        calc = Calculadora()
        calc.ingresar('2')
        calc.ingresar('-')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'1')

    def test_Calculadora_2_x_2_(self):

        calc = Calculadora()
        calc.ingresar('2')
        calc.ingresar('*')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'4')

    def test_Calculadora_10_div_5_(self):

        calc = Calculadora()
        calc.ingresar('1')
        calc.ingresar('0')
        calc.ingresar('/')
        calc.ingresar('5')
        calc.ingresar('=')

if __name__ == "__main__":
    unittest.main()
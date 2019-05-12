import unittest
from calc import Calculadora

class TestCalc (unittest.TestCase):
    def test_calcular_1_mas_2(self):
        calc = Calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'3')

    def test_calculator_2_rest_1_(self):

        calc = Calculadora()

        calc.ingresar('2')

        calc.ingresar('-')

        calc.ingresar('1')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'1')

    def test_calculator_2_x_2_(self):

        calc = Calculadora()

        calc.ingresar('2')

        calc.ingresar('*')

        calc.ingresar('2')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'4')

    def test_calculator_10_div_5_(self):

        calc = Calculadora()

        calc.ingresar('10')

        calc.ingresar('/')

        calc.ingresar('5')

        calc.ingresar('=')

        self.assertEqual(calc.display(),'2')

if __name__ == "__main__":

    unittest.main()


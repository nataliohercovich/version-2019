import unittest

from calculadora import calculo

class TestCalc(unittest.TestCase):
    def test_calc_1(self):
        calc = calculo()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '3')

    def test_calc_2(self):
        calc = calculo()
        calc.ingresar('1')
        calc.ingresar('-')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '0')
        
    def test_calc_3(self):
        calc = calculo()
        calc.ingresar('2')
        calc.ingresar('*')
        calc.ingresar('3')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '6')

    def test_calc_4(self):
        calc = calculo()
        calc.ingresar('1')
        calc.ingresar('5')
        calc.ingresar('/')
        calc.ingresar('3')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '5.0')

    def test_calc_5(self):
        calc = calculo()
        calc.ingresar('5')
        calc.ingresar('1')
        calc.ingresar('-')
        calc.ingresar('c')

        self.assertEqual(calc.display(), '0')

    def test_calc_6(self):
        calc = calculo()
        calc.ingresar('1')
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '22')

    def test_calc_7(self):
        calc = calculo()
        calc.ingresar('4')
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('3')
        calc.ingresar('-')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '42')



if __name__ == '__main__':
    unittest.main()
import unittest
from calc import calculadora

class calctest(unittest.TestCase):
    def test_calcular_1_ma_2(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'3')
    def test_calcular_1_ma_3(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'5')
    def test_calcular_2_ma_1(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'1')
    def test_calcular_2(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('*')
        calc.ingresar('3')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'6')
    def test_calcular_3(self):   
        calc = calculadora()
        calc.ingresar('4')
        calc.ingresar('-')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'2')
    def test_calcular_4(self):   
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('/')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'1')

if __name__ == '__main__':
   unittest.main()
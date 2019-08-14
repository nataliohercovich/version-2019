import unittest
from calc import calculadora
class TestCalculador(unittest.TestCase):
    def test_calcular_1_mas_2(self):
        calc=calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'3')
    def test_calcular_2_menos_1(self):
        calc=calculadora()
        calc.ingresar('2')
        calc.ingresar('-')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'1')
    def test_calcular_2_por_1(self):
        calc=calculadora()
        calc.ingresar('2')
        calc.ingresar('*')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'2')
    def test_calcular_4_dividido_2(self):
        calc=calculadora()
        calc.ingresar('4')
        calc.ingresar('/')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'2')
if __name__ == '__main__':
    unittest.main()


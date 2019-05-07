
import unittest
from calc2 import Calculadora

class TestCalc(unittest.TestCase):
    def test_calcular_1_mas_2(self):
        calc=Calculadora()  #clase que va a recibir cada uno de los ingresos,define el estado inicial
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('3')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'6')

    '''def test_calcular_1_mas_1(self):
        calc=Calculadora()  #clase que va a recibir cada uno de los ingresos
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'2')

    def test_calcular_1_por_5(self):
        calc=Calculadora()  #clase que va a recibir cada uno de los ingresos
        calc.ingresar('1')
        calc.ingresar('*')
        calc.ingresar('5')
        calc.ingresar('=')
        self.assertEqual(calc.display(),'5')'''

    
if __name__ == '__main__':
    unittest.main()
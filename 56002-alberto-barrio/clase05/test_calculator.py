import unittest

from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calcular_1_igual(self):
        calc=Calculator()
        calc.input_number('1')
        calc.input_number('=')
        self.assertEqual(calc.display(),'1')

    def test_calcular_1_mas_1(self):
        calc=Calculator()
        calc.input_number('1')
        calc.input_number('1')
        calc.input_number('+')
        calc.input_number('2')
        calc.input_number('=')
        self.assertEqual(calc.display(),'13')
    
    def test_calcular_1_mas_2_mas_3(self):
        calc=Calculator()
        calc.input_number('1')
        calc.input_number('+')
        calc.input_number('2')
        calc.input_number('+')
        calc.input_number('3')
        calc.input_number('=')
        self.assertEqual(calc.display(),'6')



if __name__ == '__main__':
    unittest.main()
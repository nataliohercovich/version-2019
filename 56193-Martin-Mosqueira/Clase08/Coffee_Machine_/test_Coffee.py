import unittest
from Class_Coffee import Coffee
from Class_Coffee_Premium import Coffee_Premium
from Coffee_Machine import coffee_machine

class Test_Coffee_Machine(unittest.TestCase):
    def test_water_quantity0(self):
        result=Coffee(3).water_quantity()
        self.assertEqual(result,'250ml')
    def test_water_quantity1(self):
        result=Coffee(4).water_quantity()
        self.assertEqual(result,'add more water')
    def test_water_quantity2(self):
        result=Coffee(5).water_quantity()
        self.assertEqual(result,'add more water')

    def test_coffee_quantity(self):
        result=Coffee(2).coffee_quantity()
        self.assertEqual(result,'30g')
    def test_coffee_quantity(self):
        result=Coffee(5).coffee_quantity()
        self.assertEqual(result,'add more coffee')

    def test_sugar_quantity0(self):
        result=Coffee(2).sugar_quantity()
        self.assertEqual(result,'584g')
    def test_sugar_quantity1(self):
        result=Coffee(0).sugar_quantity()
        self.assertEqual(result,'600g')

    def test_milk_quantity(self):
        result=Coffee_Premium(2).milk_quantity()
        self.assertEqual(result,'760ml')

    def test_coffee_machine(self):
        result=coffee_machine(0)
        self.assertEqual(result,'wrong option')
    def test_coffee_machine(self):
        result=coffee_machine(2)
        self.assertEqual(result,'ok')

if __name__ == '__main__':
    unittest.main()


import unittest
from cafe import (Maquinabasica)


class Test_CafeteraBasica(unittest.TestCase):
    def setUp(self):
        self.cafeB = Maquinabasica()

    def test_cafe_1(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(5), '5g. de cafe')
        self.assertEqual(self.cafeB.cantidadAzucar(0), '0g. de azucar')
        self.assertEqual(self.cafeB.terminado(),'Cafe hecho')       #(Agregar () en terminado)
        #Ahora restare los ingredientes de la maquina:
        self.assertEqual(self.cafeB.nivel_agua,990)
        self.assertEqual(self.cafeB.cant_cafe,95)
        self.assertEqual(self.cafeB.azucar,1000)


    def test_cafe_2(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(15), '15g. de cafe')
        self.assertEqual(self.cafeB.cantidadAzucar(3), '3g. de azucar')
        self.assertEqual(self.cafeB.terminado(),'Cafe hecho')
        
        self.assertEqual(self.cafeB.nivel_agua,990)
        self.assertEqual(self.cafeB.cant_cafe,85)
        self.assertEqual(self.cafeB.azucar,997)

    
    def test_cafe_SinAgua(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(1001),'Disculpe, cantidad de agua no disponible')
        self.assertEqual(self.cafeB.terminado(),'Cafe hecho')


    def test_cafe_SinCafe(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(101), 'Disculpe, cantidad de cafe no disponible')

    def test_cafe_SinMoneda(self):
        self.assertEqual(self.cafeB.sensor_moneda(0), 'Ingrese una moneda')

if __name__ == "__main__":
    unittest.main()
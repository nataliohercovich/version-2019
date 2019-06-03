import unittest
from cafe import (
    cafeteraBasica,
    cafeteraPremium
)

class Cafetera_Basica(unittest.TestCase):
    def setUp(self):
        self.cafeB = cafeteraBasica()

    def test_cafe_solo(self):
        #Ingresa moneda y verifica el estado de los ingredientes
        self.assertEqual(self.cafeB.pago(True), 'Haciendo cafe')
        #Define la cantidad de agua
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        #Define la cantidad de cafe
        self.assertEqual(self.cafeB.cafeCant(5), 'Con 5g de cafe')
        #Define la cantidad de azucar
        self.assertEqual(self.cafeB.azucarCant(0), 'Sin azucar')
        #Se fija si esta todo correcto y hace el cafe o no
        self.assertEqual(self.cafeB.terminado(), 'Cafe hecho')

        #La maquina queda en: 
        self.assertEqual(self.cafeB.agua, 990)
        self.assertEqual(self.cafeB.cafe, 95)
        self.assertEqual(self.cafeB.azucar, 100)

    def test_cafe(self):
        self.assertEqual(self.cafeB.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(7), 'Con 7g de cafe')
        self.assertEqual(self.cafeB.azucarCant(3), 'Con 3g de azucar')
        self.assertEqual(self.cafeB.terminado(), 'Cafe hecho')

        self.assertEqual(self.cafeB.agua, 990)
        self.assertEqual(self.cafeB.cafe, 93)
        self.assertEqual(self.cafeB.azucar, 97)


    #Hacemos de cuenta que el producto en la cafetera es menor a la que necesita el vaso

    def test_cafe_agua_insuficiente(self):

        self.assertEqual(self.cafeB.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(9999), 'No hay agua suficiente')
        self.assertEqual(self.cafeB.terminado(), 'No puedo hacer el cafe')

        self.assertEqual(self.cafeB.agua, 1000)
        self.assertEqual(self.cafeB.cafe, 100)
        self.assertEqual(self.cafeB.azucar, 100) 

    def test_cafe_cafe_insuficiente(self):

        self.assertEqual(self.cafeB.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(9999), 'No hay cafe suficiente')
        self.assertEqual(self.cafeB.terminado(), 'No puedo hacer el cafe')

        self.assertEqual(self.cafeB.agua, 1000)
        self.assertEqual(self.cafeB.cafe, 100)
        self.assertEqual(self.cafeB.azucar, 100)

    def test_cafe_azucar_insuficiente(self):

        self.assertEqual(self.cafeB.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(5), 'Con 5g de cafe')
        self.assertEqual(self.cafeB.azucarCant(9999), 'No hay azucar suficiente')
        self.assertEqual(self.cafeB.terminado(), 'No puedo hacer el cafe')

        self.assertEqual(self.cafeB.agua, 1000)
        self.assertEqual(self.cafeB.cafe, 100)
        self.assertEqual(self.cafeB.azucar, 100)

class Cafetera_Premium(unittest.TestCase):
    def setUp(self):
        self.cafeA = cafeteraPremium()

    def test_cafe_solo_con_leche(self):

        self.assertEqual(self.cafeA.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeA.aguaCantP(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeA.cafeCantP(5), 'Con 5g de cafe')
        self.assertEqual(self.cafeA.azucarCantP(0), 'Sin azucar')
        self.assertEqual(self.cafeA.lecheCant(True), 'Con leche')
        self.assertEqual(self.cafeA.hacerCafeP(), 'Cafe hecho')

        self.assertEqual(self.cafeA.agua, 990)
        self.assertEqual(self.cafeA.cafe, 95)
        self.assertEqual(self.cafeA.azucar, 100)

    def test_cafe_sin_vaso(self):

        self.assertEqual(self.cafeA.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeA.vasoSN(False), 'Ponga un vaso')
        self.assertEqual(self.cafeA.hacerCafeP(), 'No puedo hacer el cafe')

        self.assertEqual(self.cafeA.agua, 1000)
        self.assertEqual(self.cafeA.cafe, 100)
        self.assertEqual(self.cafeA.azucar, 100)

    def test_cafe_sin_leche(self):

        self.assertEqual(self.cafeA.pago(True), 'Haciendo cafe')
        self.assertEqual(self.cafeA.aguaCantP(7), 'Con 7ml de agua')
        self.assertEqual(self.cafeA.cafeCantP(3), 'Con 3g de cafe')
        self.assertEqual(self.cafeA.azucarCantP(2), 'Con 2g de azucar')
        self.assertEqual(self.cafeA.lecheCant(False), 'Sin leche')
        self.assertEqual(self.cafeA.hacerCafeP(), 'Cafe hecho')

        self.assertEqual(self.cafeA.agua, 993)
        self.assertEqual(self.cafeA.cafe, 97)
        self.assertEqual(self.cafeA.azucar, 98)

if __name__ == "__main__":
    unittest.main()
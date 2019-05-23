import unittest
from maquina_cafe import Cafe
from maquina_cafe import CafeChico
from maquina_cafe import CafePremium

class TestCafe(unittest.TestCase):
          
       
    def test_cafechico_delce_cantidad(self):      
        cafecito= CafeChico()   
        cafecito.cafe_con_azucar(1)
        self.assertEqual(cafecito.__dict__ , {'agua': 1000, 'gramoscafe': 1100, 'azucar': 1105, 'leche': 1110})

            
       
    def test_cafechico_amargo_cantidad(self):      
        cafecito= CafeChico()   
        cafecito.cafe_con_azucar(0)
        self.assertEqual(cafecito.__dict__ , {'agua': 1000, 'gramoscafe': 1100, 'azucar': 1110, 'leche': 1110})


    def test_cafepremium_1(self):
        cafep= CafePremium()    
        cafep.cafe_con_azucar(1)
        cafep.cafe_con_leche(1)    
        self.assertEqual(cafep.__dict__, {'agua': 1020, 'gramoscafe': 1100, 'azucar': 1109, 'leche': 1070})
        
       
    def test_cafepremium_2(self):      
        cafep= CafePremium()    
        cafep.cafe_con_azucar(3)
        cafep.cafe_con_leche(0)    
        self.assertEqual(cafep.__dict__, {'agua': 980, 'gramoscafe': 1100, 'azucar': 1107, 'leche': 1110})

    def test_cafepremium_3(self):      
        cafep= CafePremium()    
        cafep.cafe_con_azucar(0)
        cafep.cafe_con_leche(0)    
        self.assertEqual(cafep.__dict__, {'agua': 980, 'gramoscafe': 1100, 'azucar': 1110, 'leche': 1110})

  

    



if __name__ == '__main__':
    unittest.main()
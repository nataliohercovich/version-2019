
import unittest
import conversiones

class main(unittest.TestCase):
  

  def test_romanos_a_decimal(self):
    self.assertEquals(conversiones.romano_a_decimal('I'),1)
    self.assertEquals(conversiones.romano_a_decimal('XX'),20)
    self.assertEquals(conversiones.romano_a_decimal('CXV'),115)



  def test_decimal_a_romano(self):
    self.assertEquals(conversiones.decimal_a_romano(1),'I')
    self.assertEquals(conversiones.decimal_a_romano(200),'CC')
    self.assertEquals(conversiones.decimal_a_romano(20),'XX')  
    self.assertEquals(conversiones.decimal_a_romano(900),'CM')  
    



if __name__ == '__main__':
    unittest.main()
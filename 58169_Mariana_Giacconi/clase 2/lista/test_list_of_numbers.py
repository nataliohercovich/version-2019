import unittest
from list_of_numbers import find_max

class Main(unittest.TestCase):
    
    def test_find_max(self):
        maxNum=find_max([1,6,9,10])
        self.assertEqual(maxNum,10)
    
        
if __name__ == '__main__':
    unittest.main()
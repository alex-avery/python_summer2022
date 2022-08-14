import unittest
from lab03 import *

class Test_string_functions(unittest.TestCase):
    
    def test_shout(self): 
        self.assertEqual(shout('My name is Alex'), 'MY NAME IS ALEX')
    
    def test_reverse(self):
        self.assertEqual(reverse('My name is Alex'), 'xelA si eman yM') 

    def test_reversewords(self):
    	self.assertEqual(reversewords('My name is Alex'), 'Alex is name My') 
    
    def test_reversewordletters(self):
    	self.assertEqual(reversewordletters('My name is Alex'), 'yM eman si xelA') 

if __name__ == '__main__': 
    unittest.main()
    


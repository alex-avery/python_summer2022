## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test in your script and see your results.
def count_vowels(word):
    vowels = []
    try:
        for i in word:
            if i == 'a':
                vowels.append(1)
            elif i == 'e':
                vowels.append(1)
            elif i == 'i':
                vowels.append(1)
            elif i == 'o':
                vowels.append(1)
            elif i == 'u':
                vowels.append(1)
        num_vowels = sum(vowels)
        out = num_vowels
    except TypeError:
        print("This is an integer. 'Word' must be a string.")
        out = None
    finally:
        return out 

#test
count_vowels("cat") #1
count_vowels("foo") #2
count_vowels("classroom") #3
count_vowels(3) #error

import unittest

class Test_count_vowels(unittest.TestCase):
	
	def test_count(self): 
		self.assertEqual(count_vowels('foo'), 2)
	
	def test_integer(self):
		with self.assertRaises(TypeError): 
			count_vowels(3)
		

if __name__ == '__main__': 
	unittest.main()
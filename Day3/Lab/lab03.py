## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int

class IntException(Exception):
    def _init_(self, value):
        Exception.init(self, )

## make all characters capitalized
def shout(txt): 
    return txt.upper()
 
## test
shout('I am taking the python course.')


## reverse all characters in string
def reverse(txt):
    return txt[::-1]

## test
reverse('I am taking the python course.')

## reverse word order in string
def reversewords(txt):
    words = txt.split()
    words_reverse = list(reversed(words))
    print(" ".join(words_reverse))

## test
reversewords('I am taking the python course.')

## reverses letters in each word
def reversewordletters(txt):
    words = txt.split()
    reverse_letters = []
    for word in words:
        reverse_letters.append(word[::-1])
    new_txt = " ".join(reverse_letters)
    return new_txt
        
## test
reversewordletters('I am taking the python course.')

## optional -- change text to piglatin.. google it!
def piglatin(txt):
    words = txt.split()
    for i in words:
        if i[0] in 'aeiou': 
            words[i] = word[0:]+ "ay"
        else:
            words[words] = word[1:] + word[0] + 'ay'
    return words

piglatin('how are you')

def pig_it(text):
    '''Converts text into pig-latin'''
    split_text = text.split(' ')
    pig_latin_ = ' '
    
    for word in split_text:
        if word in '!.%&?':
            pig_sentence = pig_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence = pig_sentence + pig_word + ' '
    
    
    return pig_sentence.strip(' ') 

     
        
## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

reverse_string = []
for word in range(len(string_list)):
	try:
		reverse_string.append(reverse(string_list[word]))
	except TypeError:
		print(str(word) + " is not a string")
print(reverse_string)
			
			
			
			


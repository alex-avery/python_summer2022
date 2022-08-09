# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

def fibonacci(x):
    sequence = []
    if x == 1:
        sequence = [0]
    else: 
        sequence = [0,1]
        for i in range(1, x-1):
            sequence.append(sequence[i-1] + sequence[i])
    return(sequence)

fibonacci(11)
    

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False 

has_no_e('dog')
has_no_e('bear')
    
"""return true if there is e in 'word', else false"""
def has_e(word):
    if 'e' in word:
        return True
    else:
        return False

has_e('dog')
has_e('bear')


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    return all([letter in word2 for letter in word1])

uses_only('centour', 'cent')
    


"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
    return all([letter in word1 for letter in word2])

uses_all('centour', 'cent')



"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
#create empty list to check methods
empty = []
dir(empty)
type(empty)

def is_abecedarian(word):
    list1 = [letter for letter in word]
    list2 = [letter for letter in word]
    list2.sort()
    return list1 == list2

is_abecedarian('abcdef')
is_abecedarian('abcedf')
    




#Python Course - Summer 2022
#Day 1: Class Exercise
#Alex Avery

# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

def fibonacci(n):
    sequence = []
    for i in range(0, n): 
        if i == 0 or i == 1:
            sequence.append(1)
        else: 
            sequence.append(sequence[-1] + sequence[-2])
    return sequence 

#test
fibonacci(0) #should return nothing in the sequence
fibonacci(4) #should return [1, 1, 2, 3]
    

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
    if 'e' not in word:
        return True
    else:
        return False 

#test
has_no_e('you') #True
has_no_e('me') #False
    
"""return true if there is e in 'word', else false"""
def has_e(word):
    if 'e' in word:
        return True
    else:
        return False

#test
has_e('you') #False
has_e('me') #True


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    return all([letter in word2 for letter in word1])

#test
uses_only('adb', 'ab') #False
uses_only('adb', 'abdc') #True
    


"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
    return all([letter in word1 for letter in word2])

#test
uses_all('adb', 'ab') #True
uses_all('adb', 'abdc') #False


"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):
    list1 = [letter for letter in word]
    list2 = [letter for letter in word]
    list2.sort()
    return list1 == list2

#test
is_abecedarian('abcdef') #True
is_abecedarian('abcedf') #False
    




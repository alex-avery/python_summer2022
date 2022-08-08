# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:24:34 2020

@author: rzava
"""


# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

fibby = []
for i in range(0, 10):
    if len(fibby) < 2:
        fibby.append(1) 
    else:
        fibby.append(fibby[i-1] + fibby[i-2])
        
print(fibby)

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence



"""return true if there is no e in 'word', else false"""
def has_no_e(word):
    if "e" not in word:
        return True
    else:
        return False
has_no_e("me")
has_no_e("you")

"""return true if there is e in 'word', else false"""
def has_e(word):
    if 'e'in word:
        return True
    else:
        return False


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    allTs = []
    for i in range(0, len(word1)):
        if word1[i] in word2:
            allTs.append(True)
        else:
            allTs.append(False)
    return(all(allTs) == True)
        
uses_only("stop", "spspson")

"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
    allTs = []
    for i in range(0, len(word2)):
        if word2[i] in word1:
            allTs.append(True)
        else:
            allTs.append(False)
    return(all(allTs) == True)

uses_all("abc", "abd")

"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):
    word2 = [i for i in word]
    return(sorted(word2) == word2)

is_abecedarian("abdc")

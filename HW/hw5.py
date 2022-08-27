# Python Course — Summer 2022
# Homework 5
# Alex Avery

# first create node class (given in assignment instructions)
class Node: 
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next 
    def __str__(self):
        return str(self.value)

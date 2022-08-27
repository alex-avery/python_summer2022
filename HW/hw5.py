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

# next create linkedlist class
class LinkedList:
    
    def _init_(self):
        self.head = None
        
    def addNode(self,new_value):
        new_node = Node(new_value)
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            last_node = last_node.next 
            last_node.next = new_node
        

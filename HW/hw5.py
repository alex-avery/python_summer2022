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
    
    def addNodeAfter(self, new_value, after_node):
        new_node = Node(new_value)
        if after_node == None:
            print("The previous node does not exist.")
            return
        new_node.next = after_node.next
        after_node.next = new_node
    
    def addNodeBefore(self, new_value, before_node):
        new_node = Node(new_value)
        if before_node == None:
            print("The node does not exist.")
            return
        position = self.linkedlist.index(before_node.value)
        self.linkedlist.insert(position, new_value.value)
    
    def removeNode(self, node_to_remove):
        head = self.head 
        if head != None:
            if head.value == node_to_remove:
                self.head = head.next 
                return
        while head != None:
            if head.value == node_to_remove:
                break
            previous = head
            head = head.next 
        if head == None:
            return
        previous.next = head.next 
        head = None
        
        







         

         

        


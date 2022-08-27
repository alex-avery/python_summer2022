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
    
    def __init__(self):
        self.head = None
        
    def addNode(self,new_value):
        if self.head == None:
            self.head = Node(new_value)
        else:
            first_node = self.head 
            while first_node.next != None:
                first_node = first_node.next 
            first_node.next = Node(new_value)
   
    def addNodeAfter(self, new_value, after_node):
        if after_node == None:
            print("The previous node does not exist.")
        else: 
            new_node = Node(new_value)
            new_node.next = after_node.next
            after_node.next = new_node
                 
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
    
    def removeNodesByValue(self, value):
        for i in self.linklist:
            if i == value:
                self.linkedlist.remove

    def reverse(self): 
        initial = None
        first = self.head 
        second = first.next 
        while first:
            first.next = initial 
            initial = first 
            first = second 
            if second:
                second = second.next 
        self.head = initial 
    
    def __str__(self):
        head = self.head
        linkedlist = ''
        while head:
            linkedlist += str(head.value) + ', '
            head = head.next 
        return linkedlist
    
    def length(self):
        return len(self.linkedlist)
   

        
        
# tests

my_list = LinkedList()

my_list.addNode(1)
my_list.addNode(3)
my_list.addNode(5)

my_list.addNodeAfter(4, my_list.head.next)

print(my_list)






         

         

        


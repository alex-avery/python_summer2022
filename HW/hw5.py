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
    
    # define initializer 
    def __init__(self):
        self.head = None
    
    # create addNode function
    def addNode(self,new_value):
        # make Node head node if head is empty
        if self.head == None:
            self.head = Node(new_value)
        # else add node to after head node and its children 
        else:
            first_node = self.head 
            # get the children of the head node 
            while first_node.next != None:
                first_node = first_node.next 
            # append new node to the end of the linked list 
            first_node.next = Node(new_value)
   
    # create addNodeAfter function
    def addNodeAfter(self, new_value, after_node):
        # account for if the after node given does not exist in linked list 
        if after_node == None:
            print("The previous node does not exist.")
        # else add new node after given node 
        else: 
            new_node = Node(new_value)
            new_node.next = after_node.next
            after_node.next = new_node
            
    # create addNodeBefore function
    def addNodeBefore(self, new_value, before_node):
        head = self.head 
        # account for if user want to add a new node before the current head 
        if head == before_node:
            new_node = Node(new_value)
            new_node.next = head 
            head = new_node
        # else index nodes to find node to add new node before 
        else:
            index = None
            new_node = head
            while (new_node != before_node):
                index = new_node 
                new_node = new_node.next 
            newer_node = Node(new_value)
            newer_node.next = index.next 
            index.next = newer_node 
    
    # create removeNode function
    def removeNode(self, node_to_remove):
        # account for if no nodes exist
        if self.head == None:
            return
        # else index nodes to remove given node 
        index = 0
        node = self.head 
        while node.next and index < node_to_remove:
            previous = node 
            node = node.next 
            index += 1
        if index == 0: 
            self.head = self.head.next 
        else:
            previous.next = node.next 
    
    # create removeNodeByValue function
    def removeNodeByValue(self, value):
        node = self.head 
        if node != None:
            if node.value == value:
                self.head = node.next 
                node = None
        while node != None:
            if node.value == value:
                break
            previous = node 
            node = node.next 
        if node == None:
            return
        previous.node = node.next 
        node = None

    # create reverse function 
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
    
    # create print function 
    def __str__(self):
        head = self.head
        linkedlist = ''
        while head:
            linkedlist += str(head.value) + ', '
            head = head.next 
        return linkedlist
    
    # create lenth function 
    def length(self):
        # start counter and add one for every element in list 
        counter = 1
        node = self.head 
        while node.next != None:
            node = node.next 
            counter += 1
        # return counter to get length 
        return counter
    

# tests

my_list = LinkedList()

my_list.addNode(1)
my_list.addNode(3)
my_list.addNode(5)

print(my_list)

my_list.addNodeAfter(4, my_list.head.next)

print(my_list)

my_list.addNodeBefore(2, my_list.head.next)

print(my_list)

my_list.removeNode(3)

print(my_list)

my_list.removeNodeByValue(1)

print(my_list)

my_list.reverse()

print(my_list)

my_list.length()







         

         

        


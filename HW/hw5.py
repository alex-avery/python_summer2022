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
    
    #def addNodeBefore(self, new_value, before_node):
        #if before_node == None:
           # print("The node does not exist.")
       # else:
            #new_node = Node(new_value)
            #new_node.next = 
  
    def removeNodeByValue(self, node_to_remove):
        node = self.head 
        if node != None:
            if node.value == node_to_remove:
                self.head = node.next 
                node = None
        while node != None:
            if node.value == node_to_remove:
                break
            previous = node 
            node = node.next 
        if node == None:
            return
        previous.node = node.next 
        node = None

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
        counter = 1
        node = self.head 
        while node.next != None:
            node = node.next 
            counter += 1
        return counter
    


# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print ("
Linked List after Deletion of 1:")
llist.printList()

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)


# tests

my_list = LinkedList()

my_list.addNode(1)
my_list.addNode(3)
my_list.addNode(5)

print(my_list)

my_list.addNodeAfter(4, my_list.head.next)

print(my_list)

my_list.removeNodeByValue(1)

print(my_list)

my_list.reverse()

print(my_list)

my_list.length()







         

         

        


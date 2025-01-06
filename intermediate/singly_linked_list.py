'''
Implement a Singly Linked List
Description:
Write a Python class to implement a Singly Linked List. The linked list should support the following operations:

append(x): Adds an element x to the end of the linked list.
prepend(x): Adds an element x to the beginning of the linked list.
delete(value): Deletes the first occurrence of value in the linked list.
search(value): Searches for the element value in the linked list and returns True if found, otherwise False.
display(): Displays all the elements in the linked list.
A Singly Linked List is a collection of nodes where each node contains:

data (the value of the node)
next (a reference to the next node in the list)

'''

class node:
    def __init__(self,data=None):
        self.data = data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def prepend(self,data):
        new_node = node(data)
        new_node.next = self.head.next
        self.head.next = new_node
    
    def delete(self,index):
        if index>=self.length():
            print("Error: 'Delete' Index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index== index:
                last_node.next = cur_node.next
                return
            cur_index += 1
    

    def search(self,index):
        if index >=self.length():
            print ("Error: 'Search' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index: return cur_node.data
            cur_index += 1

    def length(self):
        cur = self.head
        total = 0
        while cur.next !=None:
            total +=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next !=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print (elems)
    


my_list = linked_list()

my_list.append(10)
my_list.append(30)
my_list.append(20)
my_list.append(40)
my_list.display()
my_list.prepend(50)
my_list.display()
#my_list.delete(1)
#my_list.display()
#print('element at second Index', my_list.search(2))




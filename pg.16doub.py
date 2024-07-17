#write a program to create Doubly linked list by appending node at front
#Searching for a node and deleting node at the begining
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        ptr = self.head
        if(ptr is None):
            print("Empty list")
        while ptr is not None:
            print (ptr.data, end = "<->")
            ptr = ptr.next
        print()

    def search(self,key):
        ptr = self.head
        while ((ptr is not None) and (ptr.data != key)):
                ptr = ptr.next
        if(ptr is None):
                print("key not found")
        else:
                print("key  found")
                
    def insert(self,value):
        new_node=Node(value)
        if(self.head == None): 
            list.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            

    def delete(self):
        if(self.head is None):
            print("Empty list")
        else:
            print("Node value deleted is", self.head.data)
            self.head.prev = None
            self.head = self.head.next
            
   
            
list = DLinkedList()
#Creating the list
n= int(input("How many nodes you want?"))
for i in  range(n):
    value=int(input("enter node value"))
    list.insert(value)

list.listprint()
print("\n Demonstrating Search Insert and Delete operations")
key = int(input("\n Enter key to search :"))
list.search(key)
print("\n Inserting a Node at the begining")
value=int(input("\n enter value to insert :"))
list.insert(value)
print("\n List after inserting\n")
list.listprint()
print("\n Deleting a Node")
list.delete()
print("List after deleting first node")
list.listprint()
print("-----End----")
    

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class slinkedlist:
    def __init__(self):
        self.head=None

    def listprint(self):
        ptr=self.head
        if(ptr is None):
            print("empty list")
        while ptr is not None:
            print(ptr.data,end="-->")
            ptr=ptr.next
        print()
    def search(self,key):
        ptr=self.head
        while((ptr is not None)and(ptr.data !=key)):
            ptr=ptr.next
        if(ptr is None):
            print("key not found")
        else:
            print("key found")

    def delete(self):
        ptr=self.head
        if(ptr is None):
            print("empty list")
        else:
            print("node value deleted is",ptr.data)
            self.head=ptr.next
#driver code
list=slinkedlist()
n=int(input("how many nodes you want?"))
for i in range(n):
    value=int(input("enter node value"))
    if(i==0):
        list.head=Node(value)
    else:
        n1=Node(value)
        n1.next=list.head
        list.head=n1
list.listprint()
print("enter 1 to search","\n""2 to delete 3 to print""\n" "4 to stop")
choice=int(input("input choice:"))
while(choice==1 or choice==2 or choice==3 or choice==4):
    if(choice==1):
        key=int(input("enter key to search:"))
        list.search(key)
    elif(choice==2):
        list.delete()
    elif(choice==3):
        list.listprint()
    elif(choice==4):
        break
    choice=int(input("\n input choice:"))
print("-----end-----")

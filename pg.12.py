class node:
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
            print(ptr.data,end="--->")
            ptr=ptr.next
        print()
    def search(self,key):
        ptr=self.head
        while((ptr is not None)
        and(ptr.data !=key)):
            ptr=ptr.next
        if(ptr is None):
            print("key not found")
        else:
            print("key found")
    def delete(self):
        ptr=self.head
        if(ptr is None):
            print("empty lis")
        else:
            print("node value deleted is",ptr.data)
            self.head=ptr.next
list=slinkedlist()
n=int(input("how many nodes ypu want to enter:"))
for i in range(n):
    value=int(input("enter node value"))
    if(i==0):
        list.head=node(value)
    else:
        n1=node(value)
        n1.next=list.head
        list.head=n1
list.listprint()
print("enter 1 tp search""\n" "2 to delete")
print("3 to print""\n""4 to stop")
choice=int(input("input choice"))
while(choice==1 or choice==2 or choice==3 or choice==4):
    if(choice==1):
        key=int(input("enter key to search:"))
        list.search(key)
    elif(choice==2):
        list.delete()
    elif(choice==3):
        list.list print()
    elif(choice==4):
        break
    choice=int(input("\n input chice:"))
    print("----end----")

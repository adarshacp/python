class queue:
    def __init__(self,size):
        self.size=size
        self.q=[]

    def isempty(self):
        return len(self.q)==0
    def dequeue(self):
        if self.isempty():
            print("underflow")
        else:
            print("removing elemnt:",self.q.pop(0))
    def insert_queue(self):
        if len(self.q)==self.size:
            print("overflow")
        else:
            value=int(input("enter item to insert:"))
            print("inserting element:",value)
            self.q.append(value)
    def display(self):
        if self.isempty():
            print("queue is empty")
        else:
            print('the queue is:',self.q)

qu=queue(2)
while True:
    print("enter 1 to insert 2 to delete 3 to display")
    choice=int(input("Input choice:"))

    if choice==1:
        qu.insert_queue()
    elif choice==2:
        qu.dequeue()
    elif choice==3:
        qu.display()
    else:
        break
print("--End--")

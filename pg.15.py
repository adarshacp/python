class queue:
    def __init__(self,size):
        self.q=[]
        self.capacity=size
        self.front=-1
        self.rear=-1

    def isempty(self):
        return(self.front==-1)
    def dequeue(self):
        if self.isempty():
            print("queue underflow!")
        else:
            print("removing elemnt...",self.q[self.front])
            if(self.rear==self.front):
                self.front=-1
                self.rear=-1
                self.q.clear()
            else:
                self.front=self.front+1

    def insertqueue(self):
        if(self.rear==self.capacity-1):
            print("overflow!")
            return
        else:
            value=int(input("enter item to search"))
            print('inserting elemnt',value)
            self.rear=self.rear+1
            self.q.append(value)
            if(self.front==-1):
                self.front=0
    def display(self):
        if self.isempty():
            print("queue empty")
            return
        print('the queue is',end='|')
        i=self.front
        while i<=self.rear:
            print(self.q[i],end='|')
            i=i+1

qu=queue(3)
print("enter 1 to insert 2 to pop 3 to display 4 to stop")
choice=int(input("Input Choice:"))
while(choice==1 or choice==2 or choice==3):
    if(choice==1):
        qu.insertqueue()
    elif(choice==2):
        qu.dequeue()
    elif(choice==3):
        qu.display()
    else:
        break
    print()
    print("enter 1 to insert 2 to pop 3 to display 4 to stop")
    choice=int(input("\nInput Choice:"))
    print("----end----")
    

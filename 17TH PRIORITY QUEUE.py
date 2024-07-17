class priorityqueue(object):
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return len(self.queue)==0
    def insert(self,data):
        self.queue.append(data)

        

    def delete(self):
        max_idx=0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[max_idx]:
                max_idx=i
        item=self.queue[max_idx]
        del self.queue[max_idx]
        return item

myqueue=priorityqueue()
n=int(input("Enter the size of the q:"))
print("Higher the value higher is the priority")
for i in range(n):
    e=int(input("enter element to insert into priority q:"))
    myqueue.insert(e)
print("queue created")
print(myqueue.queue)
print("deletion from priority queue happenes in the order")

while not myqueue.isEmpty():
    print(myqueue.delete())

class priorityqueue(object):
    def __init__(self):
        self.queue=[]

    def isempty(self):
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
n=int(input("enter the size of queue:"))
print("higher the value higher is the priority")
for i in range(n):
    e=int(input("enter elemnt to priority:"))
    myqueue.insert(e)
print("queue created")
print(myqueue.queue)
print("delelte on from priority queue happens in the order")
while not myqueue.isempty():
    print(myqueue.delete())

import time
import sys
start=time.time()
class add:
    def __init__(self):
        self.n1=1
        self.n2=2
        self.n3=3
        self.n4=4
        self.n5=5

    def display(self):
        print("the numbers are:",self.n1,self.n2,self.n3,self.n4,self.n5)

    def find_sum(self):
        self.sum=float(self.n1+self.n2+self.n3+self.n4+self.n5)
        print("sum of the nuber is:",self.sum)

c1=add()
c1.display()
c1.find_sum()
space=sys.getsizeof(c1)
print("the space utilized for:",space)
e=time.time()
print("the time taken for execution:",e-start)

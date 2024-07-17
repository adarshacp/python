import time
import sys
import array as arr
start=time.time()
class array:
    def __init__(self):
        self.a=arr.array("i",[1,2,3,4,5,])
        self.sum=0
    def display(self):
            for i in range(0,5):
                print(self.a[i],end="")
            print()
    def find_sum(self):
            for i in range(0,5):
                self.sum=self.sum+self.a[i]
            print("sum=",self.sum)
c1=array()
c1.display()
c1.find_sum()
end=time.time()
print("time taken",end-start)
space=sys.getsizeof(c1)
print("space utilixed ",space)

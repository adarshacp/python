import math
from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[10,20,30,40,50]
y=[]
print(len(x))
for i in range(len(x)):
    a=math.log2(x[i])
    y.append(a)
print(y)
plt.plot(x,y,'b',label='binary search',linewidth=2)
plt.title("binary search time complexity o(log2(n))")
plt.legend()
plt.ylabel('o(log2(n))')
plt.xlabel('n')
plt.show()

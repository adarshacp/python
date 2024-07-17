import math
from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[10,20,30,40,50]
y=[]
print(len(x))
for i in range(len(x)):
    a=(x[i])*math_log2(x[i])
    y.append(a)
    print(y)
plt.plot(x,y,'b',label='Merge Sort',linewidth=2)
plt.title("insertion Sort time complexity o(n^2)")
plt.legend()
plt.ylabel('o(n *log2(n))')
plt.xlabel('n')
plt.show()

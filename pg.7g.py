from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[10,20,30,40,50]
y=[]
print(len(x))
for i in range(len(x)):
    a=x[i]*x[i]
    y.append(a)
    print(y)
plt.plot(x,y,'b',label='Selection sort',linewidth=2)
plt.plot("Selectio sort time complexity o(n^2)")
plt.legend()
plt.ylabel('o(n^2)')
plt.xlabel('n')
plt.show()

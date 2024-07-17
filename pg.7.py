a=list()
n=int(input("enter the number of elements to be sorted:"))
print(" ")
for i in range(n):
      e=int(input("enter the number:"))
      a.append(e)
for i in range(len(a)):
      min_idx=i
      for j in range(i+1,len(a)):
            if a[j]<a[min_idx]:
                  min_idx=j
      a[min_idx],a[i]=a[i],a[min_idx]
print("\n sorted list")
print(a)

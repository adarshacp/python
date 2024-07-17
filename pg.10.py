def mergesort(array):
    if len(array)>1:
        r=len(array)//2
        l=array[:r]
        m=array[r:]

        mergesort(l)
        mergesort(m)
        i=j=k=0
        while i<len(l)and j<len(m):
            if l[i] <m[j]:
                array[k]=l[i]
                i=i+1
            else:
                array[k]=m[j]
                j=j+1
            k=k+1
        
        while i<len(l):
            array[k]=l[i]
            i=i+1
            k=k+1
            
        while j<len(m):
            array[k]=m[j]
            j=j+1
            k=k+1
array=list()
a=int(input("enter the size of array:"))
for i in range(a):
    b=int(input('enter the number:'))
    array.append(b)
mergesort(array)
print("\n sorted array")
print(array)

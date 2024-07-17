def insertion_sort(arr):
    for i in range(0,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
arr=list()
n=int(input("enter the number ofe elemnt to be sorted:"))
print(" ")
for i in range(n):
    ele=int(input("enter the elemnt:"))
    arr.append(e)
insertion_sort(arr)
print("\n sorted list")
print(arr)

def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
print("BUBBLESORT")
arr=list()
n=int(input("enter the number to be sorted:"))
for i in range(n):
    ele=int(input("enter the number:"))
    arr.append(ele)
print("unsorted array is",arr)
bubblesort(arr)
print("sorted array is",arr)

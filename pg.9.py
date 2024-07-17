def binary_search(arr,l,r,x):
    if r>=l:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    else:
        return -1
arr=[2,3,4,10,40]
print(arr)
x=int(input("enter the element to search:"))
result=binary_search(arr,0, len(arr)-1,x)
if result !=-1:
    print("elemnt is present at index %d" %result)
else:
    print("elemnt is not present in array")
    

def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
print("LINEARSEARCH")
arr=list()
n=int(input("enter the number of elemnts you want enter:"))
for i in range(n):
    ele=int(input("enter the number:"))
    arr.append(ele)
print("inputed array is:",arr)
key=int(input("enter the number you want to search:"))
found=linearsearch(arr, key)
if found==-1:
    print("the key not found")
else:
    print("the key found at position:",found)

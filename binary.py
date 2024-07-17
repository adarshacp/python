class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root  is None:
        return Node(key)
    if root.val==key:
        return root
    if key>root.val:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root
def search(root,key):
    if root is None:
        print("key not present in the tree")
        return root
    if root.val==key:
        print(key,"is present in the tree")
        return root
    if root.val<key:
        return search(root.right,key)
    else:
        return search(root.left,key)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' , ')
        inorder(root.right)
r=None
n=int(input("how many nodes u want in the tree:"))
val=int(input("input data for root node:"))
r=Node(val)
while n>1:
    val=int(input("enter value to insert:"))
    r=insert(r,val)
    n=n-1
print("tree contens")
inorder(r)

ch=int(input("enter 1 to search 2 to exit :"))
while ch==1:
    key=int(input("input value to search:"))
    search(r,key)
    ch=int(input("enter 1 to search 2 to exit:"))
        

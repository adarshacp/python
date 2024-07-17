#Implementation of Depth first Search
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# Function to insert given key as a node
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if key > root.val:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

# Recursive function to traverse BST in inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = ',')
        inorder(root.right)
        
# Recursive function to traverse BST in postorder        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end = ',')

# Recursive function to traverse BST in preorder        
def preorder(root):
    if root:
        print(root.val, end = ',') 
        preorder(root.left)
        preorder(root.right)
 
#Driver program
r = None
n = int(input("how many nodes you want in the tree? :"))
val = int(input("input data for root node :"))
r = Node(val)
while n > 1:
    val = int(input("input value to insert :"))
    r = insert(r, val)
    n=n-1
 
# Depth First Search of the BST
print("Tree created :")
print("\n Postorder traversal")
postorder(r)
print("\n Preorder traversal")
preorder(r)
print("\n Inorder traversal")
inorder(r)   


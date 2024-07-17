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

def bfs_tree(root):
    if not root:
        return

    queue = [root]  # Initialize a queue with the root node

    while queue:
        current = queue.pop(0)  # Dequeue the current node
        print(current.val)  # Process the current node

        if current.left:
            queue.append(current.left)  # Enqueue the left child
        if current.right:
            queue.append(current.right)  # Enqueue the right child


#Driver program
r = None
n = int(input("how many nodes you want in the tree? :"))
val = int(input("input data for root node :"))
r = Node(val)
while n > 1:
    val = int(input("input value to insert :"))
    r = insert(r, val)
    n=n-1
print("Tree created :")
# Breadth First Search of the BST
bfs_tree(r)


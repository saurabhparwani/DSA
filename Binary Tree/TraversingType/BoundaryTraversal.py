class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def BuildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.right = Node(10)
    root.right.right.left = Node(11)
    root.left.left.right.left = Node(12)
    root.left.left.right.right = Node(13)
    root.right.right.left.left = Node(14)
    return root

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

# Method to print the Left Boundary for non leaf nodes.
def printLeftBoundary(root):

    # Base Case if root is Null or leaf node.
    if root is None or isLeaf(root):
        return

    # Print the Current Node as left traversal is in top down manner.
    print(root.data,end=" ")

    if root.left:
        printLeftBoundary(root.left)
    else:
        printLeftBoundary(root.right)

# Method to print the Right Boundary for non leaf nodes.
def printRightBoundary(root):

    # Base Case
    if root is None  or isLeaf(root):
        return

    if root.right:
        printRightBoundary(root.right)
    else:
        printRightBoundary(root.left)

    # Print the node value after recursive call as we are printing this in bottom up manner.
    print(root.data, end =" ")

# Method to print the Leaf Nodes.
def printLeafNodes(root):
    if root:
        # Traverse the tree in inorder manner and print only leaf nodes.
        printLeafNodes(root.left)

        if root.left == None and root.right == None:
            print(root.data,end=" ")

        printLeafNodes(root.right)


# Method to Check that whether a node is leaf or not.
def isLeaf(root):

    if root is None:
        return True

    if root.left == None and root.right == None:
        return True

    return False

# Method to Print the Boundary Traversal of a Binary tree.
# Divide the Problem Statement into four steps.
# 1. Print the root node.
# 2. Print the left Boundary from the root node in the top down manner.
# 3. Print all leaf nodes in the order of inorder traversal.
# 4. Print the right boundary from the root node in the bottom up manner.
def printBoundaryTraversal(root):

    # Check for the Null case.
    if root:
        print(root.data,end=" ")  # Print the root Node

    # Edge Case  if only root node is present in tree then no need of further process.
    if not (root.left or root.right):
        return

    # Print the Left Boundary
    printLeftBoundary(root.left)

    # Print the Leaf Nodes in the  order  of inorder traversal.
    printLeafNodes(root)

    # Print the Right Boundary
    printRightBoundary(root.right)



# Driver Code
root = BuildTree()
printBoundaryTraversal(root)
print()


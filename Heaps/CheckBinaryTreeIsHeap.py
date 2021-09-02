# Problem Statement : Check that a given Binary tree is heap or not.
# https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-heap/

# This Problem also can be solve by Iterative way by the slight modification in the code of
# checking complete binary tree. We have to just place a check on left & right keys.

# Method to check that tree is a complete tree or not. TC = O(N) SC = O(N)
def checkCompeteTree(root):

    if root is None:
        return True
    queue = []
    queue.append(root)
    flag = False

    while len(queue):
        node = queue.pop(0)
        if node.left:

            if flag: return False
            queue.append(node.left)
        else:
            flag = True

        if node.right:

            if flag:
                return False
            queue.append(node.right)
        else:
            flag = True

    return True

# Method to check that Binary tree is heap of not. Steps
# 1 .First check whether tree is a complete tree or not.
# 2. If it is complete tree then check for every node that whether it is satisfying the heap property or not .
# TC = O(N) + O(N) = O(N) , SC = O(N)
def checkHeap(root):

    if root == None:  # Base Case : If root is None then it's already a heap.
        return  True

    if not checkCompeteTree(root):  # If tree is not complete tree then return false.
        return False

    flag = True

    # Check that root data is greater than left child's data.
    if root.left and root.data < root.left.data:
        flag =  False

    # Check that root data is greater than right child's data.
    if root.right and root.data < root.right.data:
        flag = False

    # Check for left & right Subtree.
    return flag and checkHeap(root.left) and checkHeap(root.right)


class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():
    root = Node(5)
    root.left = Node(2)
    root.right = Node(3)
    return root


# Driver Method
root = buildTree()

if checkHeap(root):
    print("Binary Tree is a heap")
else:
    print("Binary tree is not a heap")
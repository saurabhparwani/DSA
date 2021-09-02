from collections import deque

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)

def BuildTree():
    root=Node(50)
    root.left=Node(20)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right=Node(80)
    root.right.left=Node(60)
    root.right.right=Node(100)
    return root

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

def inOrderRecursive(root):
    if root:
        inOrderRecursive(root.left)
        print(root.data,end=" ")
        inOrderRecursive(root.right)

def postOrderRecursive(root):
    if root:
        postOrderRecursive(root.left)
        postOrderRecursive(root.right)
        print(root.data,end=" ")


def postOrderIterative(root):
    if root:
        s1=[]
        s2=[]
        s1.append(root)

        while s1:
            node=s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)

            if node.right:
                s1.append(node.right)

        while s2:
            node=s2.pop()
            print(node.data,end=" ")

def preOrderIterative(root):
    if root:
        stack=[]
        stack.append(root)
        while len(stack)>0:
            node=stack.pop()
            print(node.data,end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def inOrderIterative(root):
    if root:
        stack=[]
        stack.append(root)
        current=root.left
        while len(stack)> 0 or current:
            if current:
                stack.append(current)
                current=current.left
            else:
                node=stack.pop()
                print(node.data,end=" ")
                current=node.right


# Utility method which will print the current node if the level is 1 else it will call left & right subtree by decrementing the level by 1.

# Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n) time where n is the number of nodes in the skewed tree.
# So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).
# Space Complexity: O(n) in worst case. For a skewed tree, printGivenLevel() uses O(n) space for call stack.
# For a Balanced tree, call stack uses O(log n) space, (i.e., height of the balanced tree).

def printNodesatCurrentlevel(node,level):

    # base Case
    if node is None:
        return

    if level == 1:
        print(node.data,end = " ")
    elif level > 1:
        printNodesatCurrentlevel(node.left,level-1)
        printNodesatCurrentlevel(node.right,level-1)

# Wrapper method which will call recursive method that will print node at current level.
def printGivenLevel(root):
    if root:
        # Get the height of tree.
        h = height(root)

        # Print nodes at each level starting from level 1.
        for i in range(1,h+1):
            printNodesatCurrentlevel(root,i)

# Recursive Method for Calculating the height of binary Tree
# TC = O(N)
# SC = O(N) for stack space
def height(root):

    # Base Case
    if root is None:
        return 0

    # Get the Left & right subtree  height
    left = height(root.left)
    right = height(root.right)

    # Return the Maximum height
    return max(left,right)+1

# Level Order Traversal Using deque.
# Time Complexity: O(n) where n is number of nodes in the binary tree
# Space Complexity: O(n) where n is number of nodes in the binary tree
def levelorderItrative(root):
    if root is not None:
        l=deque()
        l.append(root)
        while l:
            node=l.popleft()
            if node is not None:
                print(node.data,end=" ")
                if node.left is not None:l.append(node.left)
                if node.right is not None:l.append(node.right)

root=BuildTree()

preOrderRecusrsive(root)
print()
preOrderIterative(root)
print()
inOrderRecursive(root)
print()
inOrderIterative(root)
print()
postOrderRecursive(root)
print()
postOrderIterative(root)
print()
levelorderItrative(root)
print()
printGivenLevel(root)


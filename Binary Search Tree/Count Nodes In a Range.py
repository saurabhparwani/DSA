# Problem Statement : https://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/

# Method 1 Simple Traversal method , O(N) but for balanced bst we can improve the algorithm so we will implement that algorithm.


# Recursive Method to get count of all the nodes which lie in the range from L to H.
# TC = O(H+K) , Worst Case : O(N) in Case of Skewed tree.
# SC = O(H) For Recursion .
def getCountInRange(root,l,h):

    if root == None: # Base Case
        return 0

    # Special Base Case if root data is equal to low & high then simply return 1 no , need of going into the left & right Subtree.
    if root.data == l and root.data == h:
        return  1

    if root.data >= l and root.data <= h:     # If root data lies between l & h.
        return  1 + getCountInRange(root.left,l,h) + getCountInRange(root.right,l,h)

    if root.data < l:  # If low is greater than root data that means we have to find only in right subtree as all the left tree will be small than root data.
        return getCountInRange(root.right,l,h)

    if root.data > h: # If root data is bigger than high that means we have to find only in left subtree as al the right subtree will be greater than root data.
        return getCountInRange(root.left,l,h)

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.right = Node(7)

    return root

# Driver Code

root = buildTree()

l = 2
h = 8

print("Count Of nodes between {} {} is {} ".format(l,h,getCountInRange(root,l,h)))

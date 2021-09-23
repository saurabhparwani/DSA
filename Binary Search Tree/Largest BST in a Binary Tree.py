# Problem Statement : Largest BST in Binary Tree.

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self,isBST=0,size=0,min=0,max=0):
        self.isBST = isBST
        self.size = size
        self.minn = min
        self.maxx = max


def buildTree():
    root = Node(50)
    root.left = Node(10)
    root.right = Node(60)
    root.left.left = Node(5)
    root.left.right = Node(20)
    root.right.left = Node(55)
    root.right.left.left = Node(45)
    root.right.right = Node(70)
    root.right.right.left = Node(65)
    root.right.right.right = Node(80)

    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end = " ")
        inOrder(root.right)


# TC = O(N) , We are Simply Traversing the Binary Tree in the Post Order manner.
# SC = O(H) , Height of the Binary Tree.
def largestBSTUtil(root):

    # Base Case If the root is None. Simply return the isBST True with Size 0 with min element as +10000 and max element as -10000.
    if root == None:
        bst = BST(True,0,10000,-10000)
        return bst

    # Test For Left & Right Subtree.
    left = largestBSTUtil(root.left)
    right = largestBSTUtil(root.right)

    # IF left & Right Both are BST and left's Subtree maximum value is less than root data
    # & right subtree minimum value is greater than root data then it means whole tree is BST . Simply add the size of left & right Subtree + 1.

    bst = BST()
    bst.minn = min(min(left.minn, right.minn), root.data)
    bst.maxx = max(max(left.maxx, right.maxx), root.data)
    bst.size = 1 + left.size + right.size

    if left.isBST and right.isBST and left.maxx < root.data and right.minn > root.data:
        bst.isBST = True
    else:
        bst.isBST = False
        bst.size = max(left.size, right.size)

    return bst
# Wrapper Method to wrap the recursive code & then return the size of maximum BST.

def largestBST(root):
    bst = largestBSTUtil(root)
    return bst.size


# Driver Code
root  = buildTree()

# inOrder(root)
# print()
print("Size of the largest BST in the Binary Tree is {} ".format(largestBST(root)))

# Problem Statement : https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
# Given a binary tree, find if it is height balanced or not.
# A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree.


# Optimize method to check  Tree is balanced or not.
# TC = O(N) , SC = O(N)
def checkbalanceTreeOptimized(root,height):

    # Base Case
    if root is None:
        height.h = 0
        return True

    left_height = Height()
    right_height = Height()

    lh = checkbalanceTreeOptimized(root.left,left_height)
    rh = checkbalanceTreeOptimized(root.right,right_height)

    height.h = max(left_height.h,right_height.h)+1

    if abs(left_height.h-right_height.h) <= 1:
        return lh and rh

    return False


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left),height(root.right))

# Method to check that whether a tree is balanced or not.Steps
# 1. Calculate left & right height and calculate their absolute diff , it should be <=1.
# 2. Now check for left & subtree and then return true or false.
# TC = O(N*N) as we are calculating heights again & again . SC = O(1) (Not Including Stack space)
# We can improve this by calculating height in the same recursive call as of Balanced tree call (Same which we done for Diameter in Binary tree).
def checkBalancedTree(root):

    if root is None: return True

    left_height = height(root.left)
    right_left = height(root.right)
    flag = True

    # If absolute diff between heights is greater than 1.
    if abs(left_height-right_left) > 1:
        flag = False

    # Check for left & right subtree.
    return flag and checkBalancedTree(root.left) and checkBalancedTree(root.right)


class Height(object):
    def __int__(self):
        self.h = 0

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def buildTree():
    root = Node(10)
    root.left = Node(20)
    root.left.right = Node(60)
    root.left.left = Node(40)
    root.right = Node(30)
    return root

# Driver Method
root = buildTree()

# Non Optimized
if checkBalancedTree(root):
    print("Binary Tree is a balanced tree")
else:
    print("Binary tree is not a balanced tree")

# Optimized
if checkbalanceTreeOptimized(root,Height()):
    print("Binary Tree is a balanced tree")
else:
    print("Binary tree is not a balanced tree")
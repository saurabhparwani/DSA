#Problem Statement : Check whether a Binary tree is complete binary tree or not.
# https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/
# https://www.geeksforgeeks.org/check-whether-binary-tree-complete-not-set-2-recursive-solution/

# Tree node structure

# Helper Method to count the total nodes in array.
def countNodes(root):
    if root is None:
        return 0
    return  1 + countNodes(root.left)+countNodes(root.right)

# Recursive Method to check for complete binary tree. Steps are following.
# A complete binary tree can be represent in an array like root index is i , left child 2*i+1, right child = 2*i+2
# Solution Link : https://www.geeksforgeeks.org/check-whether-binary-tree-complete-not-set-2-recursive-solution/
# TC = O(N) , SC = (1) , Ignoring the stack space

def checkCompleteRecursive(root,index,total_nodes):

    if root is None:
        return True

    if index >= total_nodes:  # If the index of current node is greater than or equal than total_nodes.
        return False

    return (checkCompleteRecursive(root.left,2*index+1,total_nodes) and
           checkCompleteRecursive(root.right,2*index+2,total_nodes))

def checkCompleteBinaryTreeRecursive(root):

    if root is None:return  True

    total_nodes = countNodes(root)
    return  checkCompleteRecursive(root,0,total_nodes)



# Iterative Method to check for complete binary tree. Steps are following
# 1. We will find the first Non full node ( which has only one child or not.) and then if the flag is true
# and we have find the left or right child of the node then we can say that tree is not a complete binary tree.
# Solution Link : https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/
# TC : O(N) SC = O(N) for Queue.
def checkCompleteBinaryTree(root):

    if root:
        queue = []
        queue.append(root)
        flag = False

        while len(queue):
            # Pop the first Node.
            node = queue.pop(0)

            if node.left:

                #If we found a left child of node after finding the non full node then simply return false.
                if flag:
                    return False
                queue.append(node.left)
            else:
                flag = True  # We have found our first non full node.

            if node.right:
                # If we found a left child of node after finding the non full node then simply return false.
                if flag:
                    return False
                queue.append(node.right)
            else:
                flag = True

        return True

class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def buildTree():
    root = Node(37)
    root.left = Node(12)
    root.right = Node(12)
    root.right.left = Node(24)
    root.right.right = Node(72)
    root.left.left = Node(76)
    root.left.right = Node(71)
    root.left.left.left = Node(65)
    root.left.right.left = Node(24)
    root.left.right.right = Node(21)
    return  root

# Driver Program
root = buildTree()

# Check with the Iterative way.
if checkCompleteBinaryTree(root):
    print("Tree is Complete Binary tree")
else:
    print("Tree is not complete Binary Tree")

#Check with the Recursive Way.
if checkCompleteBinaryTreeRecursive(root):
    print("Tree is Complete Binary tree")
else:
    print("Tree is not complete Binary Tree")



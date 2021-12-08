# Similar Problem : https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/
# Actual Problem : Check if two trees are mirror or each other or not.
# https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/

# Method to Check for Mirror tree or Not
# Steps : 1. Base Case If both roots are None then return true.
#           2. If one is Not none than return (false)
#           3. Check for left & right Subtree.
def checkMirror(root1,root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return  root1.data == root2.data and checkMirror(root1.left,root2.right) and checkMirror(root1.right,root2.left)



# Method to iteratively check that both trees are mirror tree or not. Steps
# 1. We will do inorder traversal of a tree and reverse inorder traversal of another tree.
# 2. In inorder traversal left - node - right and in reverse right - node - left will be the sequence so
# we will  check that node value should be equal as both nodes are mirror of each other.
# https://www.geeksforgeeks.org/iterative-method-check-two-trees-mirror/
def checkMirror_Iterative(root1,root2):
    if root1 and root2 :  # Check for Base Case
        stack1 = []
        stack2 = []
        node_1 = root1
        node_2 = root2
        while 1:
            while node_1 and node_2: # Inorder traversal till we find the root node,and check that both node value is same or not.
                if node_1.data != node_2.data:
                    return False
                stack1.append(node_1)
                stack2.append(node_2)
                node_1 = node_1.left   # Inorder Traversal
                node_2 = node_2.right  # Reverse Inorder Traversal

            # This loop breaks means we reached None nodes in both the trees. If any of the node is Not None then simply return False.

            if not (node_1 is None and node_2 is None):
                return False

            if not(len(stack1) == 0 and len(stack2) == 0):
                node_1 = stack1.pop()
                node_2 = stack2.pop()

                # Now we have visited the node so now assign the last nodes which comes in inorder traversal.
                node_1 = node_1.right  # Inorder
                node_2 = node_2.left   # Reverse Inorder

            else:
                break

        return True
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)

def BuildTree1():
    root1 = Node(1)
    root1.left = Node(3)
    root1.right = Node(2)
    root1.right.left =Node(5)
    root1.right.right = Node(4)
    return root1

def BuildTree2():
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    return root2


# Driver Code

root1 = BuildTree1()
root2 = BuildTree2()

if checkMirror(root1,root2):
    print("Both tree are mirror of each other")
else:
    print("Tree are not mirror of each other")

if checkMirror_Iterative(root1,root2):
    print("Both tree are mirror of each other")
else:
    print("Tree are not mirror of each other")
# Problem Statement : https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/
# Method to Convert a Binary tree into Sum Tree.
def toSumTree(root):
    if root is None:        # Base case
        return 0

    old_data = root.data    # Store Old data
    root.data = toSumTree(root.left)  + toSumTree(root.right) # Update the Root value as left

    return root.data + old_data
class Node(object):

    def  __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def buildTree():
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    return root


# Problem : To Check that Given Tree is Sum Tree or not.

# Method 1 : Get the sum of nodes in the left subtree and right subtree.
# Check if the sum calculated is equal to the root’s data. Also, recursively check if the left and right subtrees are SumTrees.
# TC = O(N*N) , SC = O(N)

global  flag
flag = True

def sumTreeUtil(root,flag):

    if root == None:     # Base Case when root is None simply return 0
        return 0

    if root.left == None and root.right == None:  # If root is leaf node then simply return root's data
        return root.data


    if not flag[0]: # If flag is already False then simply return 0 , no need for further recursive calls.
        return 0

    # Call the method for left & right Subtree.
    leftdata = sumTreeUtil(root.left,flag)
    rightdata = sumTreeUtil(root.right,flag)

    if root.data != leftdata + rightdata:  # If root data is not equal to the  left & right Subtree then update the flag.
        flag[0] = False

    return leftdata + rightdata + root.data    # Simply Return the leftSUm + RightSUm + root.data as the total sum of any side.




# Method 2 :
 # First Check for left Subtree & Right Subtree that  are they Sumtree or not , then simply return the left + right  + root.data
# IF at any step tree is not Sum tree then simply update the flag to False.
def checkSumTree(root):
    flag = [True]
    sumTreeUtil(root,flag)
    return flag[0]



# Driver Code
root = buildTree()

if checkSumTree(root):
    print("Given Tree is the Sum tree")
else:
    print("Tree is not Sum tree")






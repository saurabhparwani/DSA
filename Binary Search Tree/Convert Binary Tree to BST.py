# Problem Link : https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/

class  Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def arrayToBST(root,inorder):
    if root:

        stack = []
        index = 0  # To Update the data in the Original Binary Tree.
        curr = root
        stack.append(curr)
        curr = curr.left

        while stack or curr:

            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()

                # Update the Data & Increment the Index
                if index < len(inorder):
                    curr.data = inorder[index]
                    index += 1

                curr = curr.right

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data,end = " ")
        printInOrder(root.right)

# Helper Method to Store the in order Traversal of a binary tree.
def inorderRecursive(root,inorder):
    if root:
        inorderRecursive(root.left,inorder)
        inorder.append(root.data)
        inorderRecursive(root.right,inorder)


# Method to Convert Binary Tree into Binary Search Tree.
# TC  = O(N) + O(NLogN) + O(N)  ~~ O(NLogN)
# SC = O(N)
def binaryTreeToBST(root):

    if root:     # Check Base Case
        inorder = []

        # Store the Inorder traversal of a binary tree.
        inorderRecursive(root,inorder)

        inorder.sort()  # Sort The inorder array.

        arrayToBST(root,inorder)


# Driver Code
root = Node(10)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(4)


# Convert binary tree to BST & Print the updated tree.
binaryTreeToBST(root)
printInOrder(root)
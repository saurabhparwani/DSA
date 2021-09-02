# Problem Statement : https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/

# Recursive method to make Complete binary tree.
# TC = O(N) , SC = O(1)
def makeCompleteBinaryTree(arr,root,i,n):

    if i < n:

        root = Node(arr[i])  # Make root Node

        root.left = makeCompleteBinaryTree(arr,root.left,2*i+1,n)  # Set Left child of root as 2*i+1

        root.right = makeCompleteBinaryTree(arr,root.right,2*i+2,n)# Set Right child of root as 2*i+2

    return root

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)


# Driver Code
arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
n = len(arr)
root = None
root = makeCompleteBinaryTree(arr, root, 0, n)
preOrderRecusrsive(root)
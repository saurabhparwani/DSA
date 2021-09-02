# Problem Statement : https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
def BuildTree():
    root = Node(4)
    root.left=Node(2)
    root.left.left=Node(7)
    root.left.right=Node(1)
    root.right=Node(5)
    root.right.left=Node(2)
    root.right.right=Node(3)
    root.left.right.left=Node(6)
    return root

# Helper recursive Method to find the Sum of Longest path from root to leaf node.
def findmaxSum(root, curr_sum, arr, level):

        # Base case is root is null simply return.
        if root is None:
            return

        # If root is leaf node then calculate the maximum sum.
        if root.left is None and root.right is None:

            # If condition to check that current path is longest path & new Sum is bigger than existing max sum.
            if curr_sum + root.data > arr[0] and level >= arr[1]:
                arr[0] = curr_sum + root.data
                arr[1] = level

        # Else find maxSum recursively for left & right child.
        findmaxSum(root.left, curr_sum + root.data, arr, level + 1)
        findmaxSum(root.right, curr_sum + root.data, arr, level + 1)


# Method to find the maximum sum on longest path from root to leaf.
def sumOfLongRootToLeafPath(root):
        if root:
            # Initialize global variables to store max_sum & max_level.
            arr = [-1000, -1]
            findmaxSum(root, 0, arr, 0)
            return arr[0]
        return 0


# Driver Code
root = BuildTree()
print("Sum of Longest Path from root to leaf {}".format(sumOfLongRootToLeafPath(root)))


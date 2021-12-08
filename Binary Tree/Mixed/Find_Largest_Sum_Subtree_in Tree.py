# Problem Statement : https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/

# This method is Using Postorder traversal like finding sum of left subtree & then sum of right subtree
# and then adding it with the root.node
def findMaxSum(root,ans):

    # Base Case if root is None
    if root is None:
        return 0

    # Find the Sum of subtree whose root is current node by adding root.data with left & right subtree sum.
    curr_sum = root.data + findMaxSum(root.left,ans) + findMaxSum(root.right,ans)

    # Update the Maximum sum if it is larger than existing sum.
    ans[0] = max(curr_sum,ans[0])

    # Return the total sum found of subtree rooted at current node.
    return curr_sum
# Method to find the maximum sum of all subtree in binary tree.
# This method will use a helper method  which will find sum of all subtrees in given tree and update the
# maximum sum as per max sum found.
# TC = O(N),SC = O(N) ,We are doing only post order traversal and O(N) space for recursive stack function call.
def findMaxSumSubtree(root):
    if root:
        ans = [-99999]
        findMaxSum(root,ans)
        return ans[0]

    # If tree is Null the return 0.
    return 0

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
def BuildTree():
    root = Node(1)
    root.left=Node(-2)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right=Node(3)
    root.right.left=Node(-6)
    root.right.right=Node(2)
    # root.left.right.left=Node(6)
    return root


# Driver Code
root = BuildTree()
print("Maximum Sum of subtree in given Binary tree is {}".format(findMaxSumSubtree(root)))
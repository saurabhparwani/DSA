# Problem Statement :  https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1#

class Node(object):

    def  __init__(self,data):
        self.data = data
        self.left = self.right = None

# Method to find Kth Maximum we will do the reverse in order traversal and then we will count every node
# If the node count == k then it means this is the desired element if K is bigger than total nodes in tree then simply return -1.

# TC = O(N) , SC = O(1)
def reverseInorder(root, count, k):

        # Base Case for not to call unnecessary recursive calls.
        if root is None or count[0] >= k:
            return
        # Reverse Level order traversal , call right child before left child.
        if root:
            reverseInorder(root.right, count, k)
            count[0] += 1
            if count[0] == k:
                count[1] = root.data
                return
            reverseInorder(root.left, count, k)

def kthLargest(root, k):
    # Initialize count array to store present node count & that particular node data.
    count = [0, -9999]
    reverseInorder(root, count, k)

    # If K is bigger than total nodes in the tree.
    if count[1] != -9999:
        return count[1]

    return -1


def inorder(root,count,k):

    # Base Case for not to call unnecessary recursive calls.
    if root is None or count[0] >= k:
        return

    # Reverse Level order traversal , call right child before left child.
    if root:
        reverseInorder(root.left, count, k)
        count[0] += 1
        if count[0] == k:
            count[1] = root.data
            return
        reverseInorder(root.right, count, k)


def KthSMallest(root,k):

    # Initialize count array to store present node count & that particular node data.
    count = [0, -9999]
    inorder(root, count, k)

    # If K is bigger than total nodes in the tree.
    if count[1] != -9999:
        return count[1]

    return -1

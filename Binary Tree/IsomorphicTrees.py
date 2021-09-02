# Problem Statement : https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1

# Method to Check that both trees are isomorphic to each other or not.
# TC = O(N) , SC = O(1)
def isIsomorphic(root1,root2):

    if root1 == None and root2 == None:  # If both roots are None than tree are isomorphic,
        return True

    if root1 == None or root2 == None:   # If any of the root is not None then return False.
        return False

    if root1.data != root2.data:  # If data of both root not same then also return false.
        return False

    # Now Check for (Left- Left or Left- Right) and (Right - Left or Right - Right) combination for left & right subtree.

    return ((isIsomorphic(root1.left,root2.left) or isIsomorphic(root1.left,root2.right)) and
            (isIsomorphic(root1.right,root2.right) or isIsomorphic(root1.right, root2.left)))




class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)

def BuildTree1():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left =Node(4)
    # root1.right.right = Node(4)
    return root1

def BuildTree2():
    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.right = Node(4)
    # root2.left.right = Node(5)
    return root2


# Driver Code
root1 = BuildTree1()
root2 = BuildTree2()

if isIsomorphic(root1,root2):
    print("Both tree are Isomorphic")
else:
    print("Tree are not Isomorphic")
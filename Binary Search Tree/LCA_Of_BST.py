# Problem Statement : https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def makeBST():
    root = Node(100)
    root.left = Node(80)
    root.left.right = Node(90)
    root.left.left = Node(50)
    root.left.left.right = Node(70)
    root.right = Node(150)
    root.right.left = Node(120)
    root.right.right = Node(180)
    root.right.right.right = Node(200)
    return root

# Recursive method to find LCA of two nodes in BST.
# TC = O(h) , SC = O(h) For recursion Call stack ,else constant
def findLCA(root,n1,n2):
    if root is None:
        return None

    # If root data is larger than Both the data then LCA will be on left side of the root.
    if root.data > n1 and root.data > n2:
        return findLCA(root.left,n1,n2)

    # If root data is less than both numbers then it means definitely LCA will be in the right part of the root.
    if root.data < n1 and root.data < n2:
        return findLCA(root.right,n1,n2)

    # Else in this case either root.data is == n1 or n2 or root.data is between n1 & n2 then definitely that node
    #  is the LCA.
    return root

# Iterative ,method to find LCA of two nodes.

def findLCA_Iterative(root,n1,n2):
    if root:

        while root:
            if root.data > n1 and root.data > n2:
                root = root.left

            elif root.data < n1 and root.data < n2:
                root = root.right

            else:break

        return root







# Driver Code
root = makeBST()

lca = findLCA(root,180,200)
if lca:print("LCA is {}".format(lca.data))
else:print("LCA not found")

lca_2 = findLCA_Iterative(root,80,120)
if lca_2:print("LCA is {}".format(lca_2.data))
else:print("LCA not found")



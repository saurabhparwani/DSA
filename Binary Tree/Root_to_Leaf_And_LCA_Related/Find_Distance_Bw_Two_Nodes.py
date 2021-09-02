# Problem Statement : https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/

class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def buildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

# Method 1 : Fnd the Distance(root,node1) + Distance(root,node2) - 2*Distance(root,lca)

# Method 2 : Find the LCA of both nodes and then return Distance(LCA,node1) + Distance(LCA,node2).

# Helper Method to find the lca of two nodes in a Binary tree.
def lca(root,n1,n2,v):

    # Base Case
    if root == None: return  False

    # If first node is found.
    if root.data == n1:
        v[0] = True
        return root

    if root.data == n2:
        v[1] = True
        return root

    left_lca = lca(root.left,n1,n2,v)
    right_lca = lca(root.right,n1,n2,v)

    if left_lca and right_lca:
        return root

    if left_lca:return left_lca
    if right_lca:return right_lca

# Helper method to find that does given node exist in tree whose root is passed in method i.e root.
def findNode(root,n):
    # Base Case
    if root == None: return False

    # If n is found at current node or left or right side.
    if root.data == n or findNode(root.left,n) or findNode(root.right,n):
        return True

    return False

# Helper method to find the distance of a node from given node.
def findDistance(root,n,distance):
    # Base Case
    if root == None: return 0

    if root.data == n:
        return distance

    # Return the max distance of a node.
    return  max(findDistance(root.left,n,distance+1),findDistance(root.right,n,distance+1))


# Utility Method to find the LCA of two nodes in Binary Tree , only when both node exist in tree.
def lca_Utility(root,n1,n2):
    v = [False,False]
    lca_node = lca(root,n1,n2,v)

    # If LCA is Found ( 2 & 3 condition is necessary for case when both nodes are on same path.
    if ((v[0] and v[1]) or (v[0] and findNode(lca_node,n2)) or (v[1] and findNode(lca_node,n1))):
        return lca_node

    return None


# Method to find the Distance b/w two nodes in binary tree.
def findDistanceBetweenTwoNodes(root,n1,n2):

    if root:
        lca_node = lca_Utility(root,n1,n2)

        if lca_node:
            return findDistance(lca_node,n1,0) + findDistance(lca_node,n2,0)

        return -1

# Driver Code
root = buildTree()
dist = findDistanceBetweenTwoNodes(root,4,9)
print("Distance between both nodes {}".format(dist))

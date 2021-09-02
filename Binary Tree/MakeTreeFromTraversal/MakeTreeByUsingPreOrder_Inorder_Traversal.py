class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive Method to Build Binary Tree using inorder and preorder array.
# This method will recursively call this method for ledt & right subtree.
def buildTreeHelper(inorder, preorder, m, start, end):

    global preIndex
    if start > end: return None

    if preIndex >= len(inorder): return None

    # Make current node from pre order as root Node.
    node = Node(preorder[preIndex])
    preIndex += 1

    if start == end : return node

    # Get the index of root node from in order array so we can recursively call the method.
    index = m[node.data]

    # Call for Left Subtree
    node.left = buildTreeHelper(inorder, preorder, m, start, index - 1)

    # Call for Right Subtree
    node.right = buildTreeHelper(inorder, preorder, m,index + 1, end)

    return node


def buildTree(inorder, preorder,m):

    # Store the index of elements in inorder array.
    for i in range(len(inorder)):
        m[inorder[i]] = i

    return buildTreeHelper(inorder, preorder, m,0, len(inorder) - 1)


def preorderTraversal(node):
    if node:
        print(node.data, end=" ")
        preorderTraversal(node.left)
        preorderTraversal(node.right)


inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
preIndex = 0
global m
m = {}
root = buildTree(inorder, preorder,m)
preorderTraversal(root)
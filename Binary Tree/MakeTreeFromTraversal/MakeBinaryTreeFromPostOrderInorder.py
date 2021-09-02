class Node(object):
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right  = None

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data,end = " ")
        inorderTraversal(root.right)


# Recursive Method to Make tree . It will Make curent post_index element as root element an then recursively call this same method for left & right subtree.

def buildTreeHelper(inorder,postorder,m,low,high):

    # Declare Post Index as Global
    global  post_index

    # Base Case
    if low > high or post_index < 0:
        return None

    # Make Current Node as root and decrease the post index by 1 so that we can pick next element in next call.
    # Find index of current element in inorder array so that we can make left & right subtree.

    ele = postorder[post_index]
    root = Node(ele)
    index = m[ele]
    post_index -= 1

    # If node does not have left or right subtree then return node itself
    if low == high:
        return root

    # Call for Right Subtree of root
    root.right = buildTreeHelper(inorder, postorder, m, index + 1, high)

    # Call for Left Subtree of root
    root.left = buildTreeHelper(inorder,postorder,m,low,index-1)
    return root

# Method to make tree. This method will store the index of each element in inorder traversal and
# then it will call to Utility Helper Recursive Method to build Tree. It will also have 1 global varibale post_index which will start to point from last element in post order traversal.
def buildTree(inorder,postorder,m):

    # Store the Index of each element in map for fast access.
    for i in range(len(inorder)):
        m[inorder[i]] = i

    return buildTreeHelper(inorder,postorder,m,0,len(postorder)-1)



# Driver Code
inorder = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]

post_index = len(postorder) -1

global m
m={}

root = buildTree(inorder,postorder,m)
inorderTraversal(root)
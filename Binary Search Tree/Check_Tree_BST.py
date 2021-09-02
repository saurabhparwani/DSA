# Problem Statement : Check that Binary tree is BST or not.
# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createTree():
    root = Node(50)
    root.left = Node(30)
    root.left.right = Node(40)
    root.left.left = Node(10)
    root.right = Node(80)
    root.right.right = Node(100)
    root.right.left = Node(70)
    return root

# Method 1 Using In order Traversal , as we know that BST gives sorted array so we will traverse the array
# inorder and find the curr element should be greater than previous element in BST assuming all ele are unique.
# TC = O(N) , SC = O(H) where h is the height of tree.
def isBST_UsingInorder(root):
    if root:

        prev_ele = -100000
        stack = []
        stack.append(root)
        root = root.left

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                # Check for BST condition here ans if it's fine then traverse further else return False.
                if root.data > prev_ele:
                    prev_ele = root.data
                    root = root.right
                else:
                    return False

        # If In order traverse done completely then return true.
        return True


    # Bcoz Null Tree is also a type of BST.
    return True

# Recursive method to check that binary tree is BST or not. If it is a null node then return true.
# If root value is less than min value or greater than max value than return false.
# Else check for left & right subtree.
def isBST_Recursion(root,min,max):

    # Base case if root is Null then return true as null node is also type of BST.
    if root is None:
        return True

    # If root data is less than it's left node or greater than it's right node.
    if root.data < min or root.data > max:
        return False

    # check for left & right subtree.
    return isBST_Recursion(root.left,min,root.data) and isBST_Recursion(root.right,root.data,max)

# Driver Method to check BST.
root = createTree()

# Check using iterative way.
if isBST_UsingInorder(root): print("Tree is a binary search tree")
else: print("Tree is not a binary search tree")


# Check Using recursive Way
if isBST_Recursion(root,-99999,9999):print("Tree is a binary search tree")
else:print("Tree is not a binary search tree")

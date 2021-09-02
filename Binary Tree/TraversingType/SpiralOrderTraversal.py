# Problem  Statement : Print Spiral Order Traversal or Zigzag order traversal.
class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

# Helper Method to make Binary Tree
def BuildTree():
    root=Node(50)
    root.left=Node(20)
    root.left.left=Node(10)
    root.left.left.left=Node(8)
    root.left.left.right=Node(12)
    root.left.right=Node(30)
    root.left.right.left=Node(25)
    root.left.right.right=Node(35)
    root.right=Node(80)
    root.right.left=Node(60)
    root.right.left.left=Node(55)
    root.right.left.right=Node(65)
    root.right.right=Node(100)
    root.right.right.left=Node(105)
    root.right.right.right=Node(110)
    return root

# Method to calculate height of a tree.
def height(root):

    if root is None:
        return 0

    left  = height(root.left)
    right = height(root.right)

    return max(left,right) + 1

# This Method will print given level according to the flag value.
# For true flag it will process left child first and then right child and vice - versa.
def printGivenLevel(root,level,flag):
    if root is None:
        return

    if level == 1:
        print(root.data,end = " ")

    elif level > 1:
        # Traverse from Left to Right
        if flag:
            printGivenLevel(root.left,level-1,flag)
            printGivenLevel(root.right,level-1,flag)

        # Traverse from Right to Left
        else:
            printGivenLevel(root.right,level-1,flag)
            printGivenLevel(root.left,level-1,flag)

# We can use normal level order traversal to print the spiral order we just need a trick.
# We will pass a flag to print a level in Left to right and then will toggle that flag so now in next iteration we will be printing Right to left.
# We will start from Left to Right Direction

# Time Complexity  : Worst Case O(N*N) When tree is Skewed
# Space Complexity : O(N) For stack space.
def printLevelOrderTraversal(root):

    h = height(root)
    flag = True
    for i in range(1,h+1):
        # Print the Current Level
        printGivenLevel(root,i,flag)

        # Toggle the flag
        flag = not flag



# Method to Print Spiral Order Traversal of a Binary Tree .
# This tree will use two stacks to print nodes in tree .
#  We will maintain a flag which will indicate direction of Traversal  Left to Right or Right to left.
# For Left to right traversal we will Process left subtree first & then right Subtree.
# For Right to left traversal we will process right subtree first

# Time Complexity = O(N)
# Space Complexity = O(N) for stacks
def spiralOrderTraversal(root):

    # Check for Null Condition.
    if root:

        # Create two Stacks
        s1 = []
        s2 =[]

        # We will Pop from stack1 if direction is Left to right & pop from stack2 if direction is Right to Left.
        # Push root to the stack 1
        s1.append(root)

        # Loop Till data is available in any of the Stacks.
        while s1 or s2 :

            # Print in the Direction of Left to right
            while s1:
                node = s1.pop()
                print(node.data,end = " ")

                if node.left:
                    s2.append(node.left)

                if node.right:
                    s2.append(node.right)

            # Print in the Direction of Right to Left. In this Mode we will process Right child first and then left child.
            while s2:
                node = s2.pop()
                print(node.data,end = " ")

                if node.right:
                    s1.append(node.right)

                if node.left:
                    s1.append(node.left)

# Driver Code
root = BuildTree()
spiralOrderTraversal(root)
print()
spiralOrderTraversal(root)

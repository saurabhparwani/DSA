class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
def BuildTree():
    root=Node(50)
    root.left=Node(20)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right=Node(80)
    root.right.left=Node(60)
    root.right.right=Node(100)
    return root


# Program to Print Reverse Level Order Traversal of a Binary Tree using iteration & recursion.
# It is similar to level order traversal with a slight change.
# Here in Recursive Method we will start Printing from last level & in Iterative method instead of printing popped item we will Push that into stack.
# Also in iterative method right node will be inserted in queue first before left subtree to maintain the sequence.

# Print Reverse level Order Traversal using a deque & Stack.
# Time Complexity will be O(N) as we are traversing binary tree only once.
# Space Complexity will be O(N) for stack & queue.
def print_Reverse_Level_Order_Traversal_Iterative(root):

    if root:

        queue = []
        stack = []
        queue.append(root)

        # Push Element in queue 1 by 1 .
        while queue :

            # Pop the First node from queue and instead of printing it put it in Stack.
            node = queue.pop(0)
            if node:
                stack.append(node)

            # Push Right child & left child after right child in Queue. ( That's the trick )

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

        # Now Print Element stored in stack.

        while stack :
            node = stack.pop()
            print(node.data,end=" ")
        print()

# Worst Case time Complexity will be O(N*N) for Skewed tree as Print Given Level will take O(n) time for Printing nodes at current level and there are N nodes.
# Space Complexity will be O(N) for recursive call stack.
# Print root starting from last level.
def printRootatCurrentLevel(root,level):

    # Base Case
    if root is None:
        return
    # if the current level is 1
    if level == 1:
        print(root.data,end= " ")
    elif level >1 :
        printRootatCurrentLevel(root.left,level-1)
        printRootatCurrentLevel(root.right,level-1)


# Method to Print Reverse Level Order Traversal of a binary tree .
# It will start printing nodes from last level
def printReverseLevelOrderTraversal(root):

    h = height(root)

    for i in range(h,0,-1):
        printRootatCurrentLevel(root,i)

    print()

# Method to fetch the height of Binary Tree
def height(root):
    if root is None:
        return 0

    left = height(root.left)
    right = height(root.right)

    return max(left,right) + 1


# Driver Method
root = BuildTree()
printReverseLevelOrderTraversal(root)
print_Reverse_Level_Order_Traversal_Iterative(root)
# Problem Statement : https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/

class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def preOrder(root):

    if root != None:
        print(root.data,end = ' ')
        preOrder(root.left)
        preOrder(root.right)


# Helper Method to find the index of bracket where left subtree is ending.
def findIndex(str,start_index,end_index):
    # Base Case
    if start_index > end_index:
        return  -1

    # Stack to find the index of corresponding  ).
    stack = []
    for i in range(start_index,end_index+1):

        if str[i] == '(':
            stack.append('(')
        elif str[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()

                if len(stack) == 0:
                    return i
    return -1



# Method to build the tree from String & bracket representation.
# First element will be always root and then we will find left & right substring.
def buildTreeFromString(str,start_index,end_index):

    # Base Case
    if start_index > end_index:
        return None

    # Create the first element as the root of the string.
    root = Node(ord(str[start_index]) - ord('0'))

    index = -1
    # Check that left or right subtree exist of not
    if start_index+1 <= end_index and str[start_index+1] == '(':
        index = findIndex(str,start_index+1,end_index)

    if index!= -1:
        root.left = buildTreeFromString(str,start_index+2,index-1)

        root.right = buildTreeFromString(str,index+2,end_index-1)

    return root


# Driver Method
str = '4(2(3)(1))(6(5))'
root = buildTreeFromString(str,0,len(str)-1)
preOrder(root)

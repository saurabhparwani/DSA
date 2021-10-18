# Problem Statement :  https://www.geeksforgeeks.org/find-duplicate-subtrees/


class newNode(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(2)
    root.right.left.left = newNode(4)
    root.right.right = newNode(4)
    return root

def inOrder(root,h):
    # Base case, if root is None then simply return empty string.
    if root is None:
        return ''

    leftStr = inOrder(root.left,h)

    stri = leftStr + str(root.data)

    rightStr = inOrder(root.right, h,)

    stri = stri + rightStr

    # Now Store the String in the Hashmap , if it is already available then Simply Print the root of this Subtree.
    # Print only 1 time if in case subtree exist more than 2 times.
    if stri in h:
        if h[stri] == 1:
            print(root.data,end = ' ')
        h[stri] += 1

    else:
        h[stri] = 1

    return stri

def printAllDuplicateSubtree(root):
    h = {}
    inOrder(root,h)


# Driver Code
root = buildTree()
printAllDuplicateSubtree(root)
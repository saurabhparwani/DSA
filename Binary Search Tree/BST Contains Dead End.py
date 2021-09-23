# Problem Statement : https://www.geeksforgeeks.org/check-whether-bst-contains-dead-end-not/
# Video Solution : https://www.youtube.com/watch?v=HOP6fucDVTM

class  Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():
    root = Node(8)
    root.left = Node(5)
    root.right = Node(11)
    root.left.left  = Node(2)
    root.left.right = Node(7)
    root.left.left.right = Node(3)
    root.left.left.right.right = Node(4)

    return root


# TC = O(N) We are simply traversing the tree.
# SC = O(H) For Recursion Space.
def checkDeadEnd(root,low,high,ans):

    if root is None: # Base Case
        return

    if ans[0]:  # If We have already found the dead end then no need of searching more.
        return


    # If current node is leaf node.
    if root.left is None and root.right is None:

        # For a root to be dead end left & right will be equal so that we won't be able to insert any element in the left & right side.
        # Also second condition is applcable only when tree can contain only positive numbers.
        if low == high or high == 1:
            ans[0] = True
            return

    # Check for left & right Subtree.
    checkDeadEnd(root.left,low,root.data -1,ans)
    checkDeadEnd(root.right,root.data+1,high,ans)
def hasDeadEnd(root):

    ans = [False]

    checkDeadEnd(root,-10000,10000,ans)

    if ans[0]:
        return True
    else:
        return False


# Driver Code

root  = buildTree()

if hasDeadEnd(root):
    print("Given tree has dead end")
else:
    print("Given tree don't have any dead end")

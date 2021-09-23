# Problem Statement : https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/

class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():

    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)

    return root

def printKPathUtil(root,path,k):

    if root is None:       # Base Case
        return

    # Add Current Node to the path.
    path.append(root.data)

    # Now Traverse in the Left & Right Subtree.
    printKPathUtil(root.left,path,k)
    printKPathUtil(root.right,path,k)

    # Now When the Both Recursion Call Finished then Calculate sum of the path ending at the current Node.
    sum = 0

    for i in range(len(path)-1 , -1 , -1):   # Traverse in the reverse direction as we are finding path ending at the current node.

        sum += path[i]

        if sum == k:      # If Sum becomes equal to the K then print the current path.
            for j in range(i,len(path)):
                print(path[j],end= " ")
            print()


    # Remove the Current Node from the Path as we are done for this Node.
    path.pop()


# TC = O(N*H*H) as maximum size of path vector can be H.
# SC = O(H)  For Storing the path .
def printKPath(root,k):
    path = []
    printKPathUtil(root,path,k)



# Driver Code
root = buildTree()
k = 5
printKPath(root,k)



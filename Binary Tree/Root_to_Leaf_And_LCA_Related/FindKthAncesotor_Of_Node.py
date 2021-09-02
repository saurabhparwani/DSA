#  Problem Statement:  https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/

class newNode(object):
    # Constructor to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def makeTree():
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    return root

# Method 1 :  Using BFS approach to find the Kth parent of the node. We will store every parent of node in our ancestors_arr.
# This method will work only assuming that node data is in between 1 to n.
# TC = O(N) , SC = O(N) for storing the parent node of each node.

# Method to generate parent Array.
def generateParentArray(root,ancestors):
    if root:
        ancestors[root.data] = -1
        queue = [root]

        while queue:
            node = queue[0]
            queue.pop(0)

            if node.left:
                ancestors[node.left.data] = node.data
                queue.append(node.left)

            if node.right:
                ancestors[node.right.data] = node.data
                queue.append(node.right)

def findKthAncestors_BFS(root,node,n,k):
    if root:
        ancestors = [0]*(n+1)
        generateParentArray(root,ancestors)
        count = 0

        while node != -1:
            node = ancestors[node]
            count+=1

            if count==k:
                break

        return node

# Method 2 : Find the node whose Kth ancestors we want to find and then traverse Kth step up in ancestors tree.
def findKthAncestore_DFS(root,node):

    global  k
    if root == None:
        return False

    if root.data == node:
        k = k-1
        return True

    else:
        # If ancestor found on left side.
        left_flag = findKthAncestore_DFS(root.left,node)
        if left_flag:

            if k == 0:
                print(root.data,end = " ")
                return False
            k -= 1
            return True

        # If ancestor found on right side.
        right_flag = findKthAncestore_DFS(root.right,node)
        if right_flag:

            if k == 0:
                print(root.data,end=" ")
                return False
            k -= 1
            return True

# Method 3 : Find the Kth ancestor node using DFS.
def findKthAncestor_DFS_new(root,node,k):

    # Base Case
    if root == None: return None

    if (root.data == node) or  findKthAncestor_DFS_new(root.left,node,k)  or findKthAncestor_DFS_new(root.right,node,k):

        # If k is greater than 0 then do K = K-1
        if k[0] > 0:
            k[0] -= 1

        elif k[0] == 0:
            print("Kth ancestor of the node is {}".format(root.data))

            # Return None to stop further backtracking.
            return None

        return root


# Driver Code
root = makeTree()
n = 5
k = 1
loc = k
node = 5

# Check Using 1st method.
k_th_ancestor = findKthAncestors_BFS(root,node,n,k)
print("{}th ancestor of {} is {}".format(k,node,k_th_ancestor))

# Check Using 2nd method.
flag = findKthAncestore_DFS(root,node)
if flag:print("Ancestor doesn't exist.")
else:print("is the " + str(loc) +"th ancestor of [" + str(node) + "]")

# Check Using 3rd method.
parent = findKthAncestor_DFS_new(root,5,[1])

if parent:print("Ancestor does not exist")


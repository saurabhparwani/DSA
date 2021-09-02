class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Recursive Method to find LCA of a binary tree assuming that both nodes A & B exist in binary tree. This method will not work if any of the node
# does not exist.
# TC : O(N) Single Traversal
# SC : O(1)  Not considering the extra space for recursion call stack.
def findLCA(root,A,B):

    # Base Case
    if root is None:
        return None

    # If the root's key matches any of the A or B's key.
    if root.key == A or root.key == B:
        return root

    # Find the A or B on the left side & right side .
    left_lca = findLCA(root.left,A,B)
    right_lca = findLCA(root.right,A,B)

    # If Both are not null that means root is the diversion point.
    if left_lca and right_lca :
        return root

    # If any of the above node is None then return not none value.
    if left_lca:
        return left_lca
    else:
        return right_lca

# Helper method to find the path of a number from the root.
def findPath(root,path,n):

    # Base Case if the root is null then Path will not exist.
    if root is None:
        return False

    # if the root is not None then append root to the path list.
    path.append(root.key)

    # If the root.key is same as the n , then no need to traverse further as this will be terminating point for the path.
    if root.key == n:
        return True

    # If the root.key is not equal to the n then find the path in left or right side and if path exists in any of the sides then we will return true.

    if ((root.left != None and findPath(root.left,path,n)) or (root.right != None and findPath(root.right,path,n))):
        return True

    # If the Path does not exist either in left or right side then pop the existing path and return false.
    path.pop()
    return False

# Another Approach to find LCA of  Binary Tree using extra space.
# Store the Path from root to n1 & root to n2.
# If any of the path does not exist then means any of the node is not available then LCA will not be available and we will return -1.
# Else traverse the Path array till both path value are same & return the last same value just before the mismatch.

def findLCA_Using_Path(root,n1,n2):

    # initialize path array to store Path
    path1 = []
    path2 =[]

    # If any of the both given value path does not exist then we will return -1
    if ((not findPath(root,path1,n1)) or (not findPath(root,path2,n2))):
        return -1

    # If both path exist then return the last match value from both path array.
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i+=1

    return path1[i-1]

# Driver Code to Check

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# LCA using No extra space  recursive approach.
print("LCA(4,5) = ", findLCA(root, 4, 5).key)
print("LCA(4,6) = ", findLCA(root, 4, 6).key)
print("LCA(3,4) = ", findLCA(root, 3, 4).key)
print("LCA(2,4) = ", findLCA(root, 2, 4).key)

print('------------------------------------',end='\n')
# LCA using the extra space path matching method.
print("LCA(4,5) = ", findLCA_Using_Path(root, 4, 5))
print("LCA(4,6) = ", findLCA_Using_Path(root, 4, 6))
print("LCA(3,4) = ", findLCA_Using_Path(root, 3, 4))
print("LCA(2,4) = ", findLCA_Using_Path(root, 2, 4))
print("LCA(4,10) = ", findLCA_Using_Path(root, 4, 10))

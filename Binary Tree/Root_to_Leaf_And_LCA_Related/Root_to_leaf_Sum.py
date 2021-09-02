class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

# Global Array variable to count ancestors.
ancestors_count = [0]
def BuildTree():
    root=Node(50)
    root.left=Node(20)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right=Node(80)
    root.right.left=Node(60)
    root.right.right=Node(100)
    # root.left.right.left = Node(200)
    return root

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

def root_to_leaf_sum(root,sum):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(sum+root.data , end=" ")
        return

    root_to_leaf_sum(root.left,sum+root.data)
    root_to_leaf_sum(root.right,sum+root.data)

# Another Extended Problem . Print all root to leaf paths.
# TC =O(N) , SC = O(N) For Storing the Root to leaf path.
def printAllRootToLeavePaths(root,path):
    if root is None:
        return

    if root.left is None and root.right is None:
        path.append(root.data)
        print(path)
        path.pop()
        return

    path.append(root.data)
    printAllRootToLeavePaths(root.left,path)
    printAllRootToLeavePaths(root.right,path)
    path.pop()

# Another extended question. Print the root to given node path.
# This method will return the path of root to given node and it will return [] is root is not present.
def printRoottoNodePath(root,k,path):

    if root is None:
        return False

    path.append(root.data)
    if root.data == k:
        return True

    left = printRoottoNodePath(root.left,k,path)
    if left:
        return True
    right = printRoottoNodePath(root.right,k,path)
    if right:
        return True
    path.pop()
    return False

# Another Extended Problem. Print all ancestors of a binary tree.
def printAllAncestors(root,k):
    if root == None:
        return False

    if root.data == k:
        return True

    left = printAllAncestors(root.left,k)
    if left:
        ancestors_count[0]+=1
        print("Ancestors {}".format(ancestors_count[0])+" {}".format(root.data))
        return True

    right = printAllAncestors(root.right,k)
    if right:
        ancestors_count[0]+=1
        print("Ancestors {}".format(ancestors_count[0]) + " {}".format(root.data))
        return True

    return False

# Driver Code

roor = BuildTree()
preOrderRecusrsive(roor)
print()
root_to_leaf_sum(roor,0)
print()
printAllRootToLeavePaths(roor,[])
path = []


printRoottoNodePath(roor,10,path)
print(path)

if not printAllAncestors(roor,60):
    print("No Ancestors Found")


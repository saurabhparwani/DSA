# Problem Statement : Create BST from PreOrder Tree Travsersal
# Problem Link : https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/

# Method 1 ( O(n2) time complexity )
# The first element of preorder traversal is always root. We first construct the root. Then we find the index of the first element
# which is greater than the root. Let the index be ‘i’. The values between root and ‘i’ will be part of the left subtree,
# and the values between ‘i+1’ and ‘n-1’ will be part of the right subtree. Divide given pre[] at index “i”
# and recur for left and right sub-trees.


# Method 2 ( O(n) time complexity )
# The trick is to set a range {min .. max} for every node. Initialize the range as {INT_MIN .. INT_MAX}.
# The first node will definitely be in range, so create a root node. To construct the left subtree, set the range as {INT_MIN …root->data}.
# If a value is in the range {INT_MIN .. root->data},
# the values are part of the left subtree. To construct the right subtree, set the range as {root->data..max .. INT_MAX}.

INT_MIN = float("-infinity")
INT_MAX = float("infinity")
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inOrderTree(root):
    if root:
        inOrderTree(root.left)
        print(root.data,end= ' ')
        inOrderTree(root.right)


# TC = O(N)
def constructTreeUtil(pre,key,mini,max,size,pre_index):

    if pre_index[0] >= size:      # Base case if the index reaches to the last of the input array.
        return None

    root = None

    # Check if the key lies in the min - max range then only we can make this key as the root of the Subtree.
    if key > mini and key < max:
        root = Node(key)       # Make the root node & increase the index in the current array element.
        pre_index[0] += 1

        # Now make left & right subtree after checking the Size with index to avoid array out of bound exception.
        if pre_index[0] < size:
            root.left = constructTreeUtil(pre, pre[pre_index[0]], mini, key, size, pre_index)

        if pre_index[0] < size:
            root.right = constructTreeUtil(pre,pre[pre_index[0]],key,max,size,pre_index)

    return root


def constructBST(preorder):
    pre_index = [0]  # To store the index of current element.
    size = len(preorder)
    root = constructTreeUtil(preorder,preorder[0],INT_MIN,INT_MAX,size,pre_index)
    return root




# Driver Code
pre = [10, 5, 1, 7, 40, 50]
root = constructBST(pre)
inOrderTree(root)
print()



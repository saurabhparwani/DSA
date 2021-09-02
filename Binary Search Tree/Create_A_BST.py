class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):

    def __init__(self):
        self.root = None

    def inorderTraversal(self):
        if self.root:
            stack = []
            curr = self.root
            stack.append(curr)
            curr = curr.left

            while stack or curr:

                # Add Current node to stack and traverse till the leftmost node.
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop(-1)
                    print(curr.data,end=" ")
                    curr = curr.right
            print()

    # Method to Create a root node.
    def createBST(self,arr):
        for ele in arr:
            self.insertInBST(ele)

    def getRoot(self):
        return self.root

    # Helper Method.
    def insert(self,root,data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left  = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)

        return root

    # Method to insert the element in BST assuming that all tree elements are distinct.
    def insertInBST(self,data):
        self.root  = self.insert(self.root,data)

    # Iterative Method to find a key in binary search tree.
    def findKeyIterative(self,key):
        curr = self.root
        # Traverse BST till key is not found or null node found.
        while curr and curr.data != key :
            # If key is small then root then search in left otherwise search in right side.
            if key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # Recursive method to find a key in a binary search tree.
    def findKey(self,root,key):

        # If root is Null then return False.
        if root is None: return False

        # If root data is equal to key then also return true.
        if root.data == key: return True

        #If root.data > key then traverse in left else right
        if root.data > key:
            return self.findKey(root.left,key)
        else:
            return self.findKey(root.right,key)

    # Iterative Method to find Minimum element Iterative way.
    # This can be solve via Iterative order traversal just return the first element in the iterative order .
    # But in this method we are traversing to the leftmost node in the bst.
    def findMin(self):
        curr = self.root
        if curr:
            # This will find the leftest node in the BST, which is also first node in the inorder traversal.
            while curr.left is not None:
                curr = curr.left
            return curr
        else: return None

    def findMinRecursive(self,root):
        if root is None:
            return -1
        # if root has the left child then go to the left child.
        if root.left:
            return self.findMinRecursive(root.left)

        return root.data

    # Iterative Method to find Maximum element Iterative way.
    # This can be solve via Iterative order traversal just return the last element in the iterative order .
    # But in this method we are traversing to the rightMost node in the bst.
    def findMax(self):
        curr = self.root
        if curr:
            # This will find the rightmost node in the BST, which is also last node in the in order traversal.
            while curr.right is not None:
                curr = curr.right
            return curr
        else:
            return None

    def findMaxRecursive(self,root):
        if root is None:
            return -1
        # If root has the right child then go to right most node.
        if root.right:
            return self.findMaxRecursive(root.right)

        return root.data


    def findMinNode(self,root):
        curr = root
        while curr.left != None:
            curr = curr.left
        return curr

    # Method to delete a node in BST.
    def delete(self,root,key):
        # Base Case
        if root is None:
            return root

        # If Key is not equal to root.data then traverse left or right based on the BST property.
        if root.data > key:
            root.left = self.delete(root.left, key)
            return root

        elif root.data < key:
            root.right = self.delete(root.right, key)
            return root

        # If we reach this point this means root.data == key.

        # Case 1 If node which we want to delete is leaf node , then simply return None.
        if root.left is None and root.right is None:
            return None

        # Case 2 If node which we want to delete have left or right child.
        # If root has right child.
        if root.left is None:
            temp = root.right
            root = None
            return temp
        # If root has left child.
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Case 3 Root which we want to delete has both left & right child.
        # So now find the in order successor of the node which we want to find.

        # Now find the inorder successor and simultaneously store the parent of each successor .
        # Inorder successor will be always leftest node so we can set left child of it's parent Null.
        succParent = root
        succ = root.right

        while succ.left:
            succParent = succ
            succ = succ.left

        # If root which we want to delete is not the successor parent ,
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        root.data = succ.data
        return root

    # Method to delete a node from binary search tree.
    # Worst Case TC : O(H) where H is the height of tree , in case of skewed tree it will be O(N).
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

    # Wrapper Method to delete a node.
    def deleteNode(self,key):
        self.root = self.delete(self.root,key)


# Driver Method
bst_root = BST()
bst_root.createBST([70,15,25,10,6,65,100,80,120,135,150,145,170,3,180])
bst_root.inorderTraversal()

# Find the Key in BST through Iterative Manner.
# if bst_root.findKeyIterative(30):
#     print("\nGiven Key exist in BST")
# else:
#     print("\nGiven Key does not exist in BST.")

# # Find the Key in BST through recursive way.
# if bst_root.findKey(bst_root.getRoot(),15):
#     print("\nGiven Key exist in BST")
# else:
#     print("\nGiven Key does not exist in BST.")


# # Find the Minimum element through Iterative way.
# min_ele_node = bst_root.findMin()
# if min_ele_node: print("Minimum element in BST {}".format(min_ele_node.data))
# else:print("BST is None")
#
# # Find the Maximum element through Iterative way.
# max_ele_node = bst_root.findMax()
# if max_ele_node: print("Maximum element in BST {}".format(max_ele_node.data))
# else:print("BST is None")

# Find the Minimum & Maximum element in BST through recursion.
# print("Minimum element in BST is {}".format(bst_root.findMinRecursive(bst_root.getRoot())))
# print("Maximum element in BST is {}".format(bst_root.findMaxRecursive(bst_root.getRoot())))

# Delete a Node
bst_root.deleteNode(150)
bst_root.inorderTraversal()






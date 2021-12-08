# Problem Statement : https://www.techiedelight.com/place-convert-given-binary-tree-to-doubly-linked-list/
# Similar Problem : https://www.geeksforgeeks.org/flatten-bst-to-sorted-list-decreasing-order/?ref=rp
# Video Solution : https://www.youtube.com/watch?v=WVFk9DwRgpY&t=501s

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Helper function to print a given doubly linked list
def printDLL(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.right

def buildTree():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)
    #
    # root = Node(1)
    # root.right = Node(2)
    # root.right.right = Node(3)
    # root.right.right.right = Node(4)
    return root


# Method to Convert the Binary Tree into Doubly Linked list.
# TC = O(N) , For Inorder Traversal
# SC = O(H) , Height of the binary tree for recursive stack.
def convert(root,head):
    # Base Case
    if root is None:
        return head

    # Convert The right Subtree First.
    head = convert(root.right,head)

    # Now point Root's right/next pointer to the newly created linked list from right Subtree.
    root.right = head

    # If head of linked list created from right side is not null then
    #  set Left/Prev of this head of right linked list point to the root of current node.
    if head:
        head.left = root

    # Now Set Current root as the head of new  updated linked list.
    head = root

    # Now Convert for the left Subtree & return the DLL head.
    return convert(root.left,head)




# Utility Method to convert a binary tree into DLL.
def convertToDLL(root):
    head = None
    return convert(root,head)

# class BLL(object):
#     def __init__(self):
#         self.head =None
#         self.tail = None
#
# def solve(root,head,prev,f):
#
#     # Base Case
#     if root is None:return
#
#     # Call for left Subtree
#     solve(root.left,head,prev,f)
#
#     # If it's the first node in the in order traversal then assign prev next to the same node.
#     if f == 0:
#         f = 1
#         head = root
#         prev = root
#         # print(root.data)
#
#
#     # Else Set prev's next to the root Node.
#     # Root's Prev node to the previous node.
#     # Set Prev to the new Prev.
#     else:
#         prev.right = root
#         root.left = prev
#         # print(root.data)
#         prev = root
#
#     # Call for right Subtree
#     solve(root.right,head,prev,f)
#     return head
#
# def convert_To_DLL(root):
#      head = prev   = None
#      f = 0
#      return solve(root,head,prev,f)

# Driver Code
root = buildTree()

head = convertToDLL(root)
printDLL(head)


# head = convert_To_DLL(root)
# printDLL(head)
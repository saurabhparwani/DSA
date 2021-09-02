from collections import defaultdict

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hd = 0

    def __str__(self):
        return str(self.data)

def BuildTree():
    root = Node(50)
    root.left = Node(20)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right = Node(80)
    root.right.left = Node(60)
    root.right.right = Node(100)
    # root.left.right.left = Node(200)
    return root

# Method to Print top view of a Binary Tree Using Level Order Traversal
# This will a have a map which will store the first node at a unique Horizontal distance.
def printVertcialOrder(root):
    if root is None:
        return

    # Put root in the Queue with HD 0. And initialize map
    que = []
    map = defaultdict(list)
    root.hd = 0
    que.append(root)

    # Level Order Traversal
    while que:
        node = que.pop(0)
        hd = node.hd

        # If existing hd is not in map then store HD in map and proceed

        map[hd].append(node.data)

        if node.left:
            node.left.hd = hd - 1
            que.append(node.left)

        if node.right:
            node.right.hd = hd + 1
            que.append(node.right)


    for i in sorted(map):
        print(map[i], end = " ")


# Driver Code
root = BuildTree()
printVertcialOrder(root)
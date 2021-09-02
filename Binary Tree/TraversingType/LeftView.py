class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def BuildTree():
    root=Node(50)
    root.left=Node(20)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right=Node(80)
    root.right.left=Node(60)
    root.right.right=Node(100)
    root.left.right.left = Node(150)
    return root

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)


# Iterative Method to Print Left View Of Binary Tree
# Left View : First Node at each level
def leftViewIterative(root):
    if root is None:
        print("Root is Null")
        return
    queue = []
    queue.append(root)

    while queue:
         count = len(queue)
         size = count
         while count > 0:

            # Pop first element from Queue
            node = queue.pop(0)

            # TO Check basically it is First Node or Not
            if size == count:
                print(node.data, end =" ")

            # Decrease the Count
            count -= 1

            # Add Left and Right node to Queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    print()


# Recursive Method to Print Left view of Binary Tree
# In this Method we will print first node  of each level  and to track the new maximum level we will use a variable.

max_level = [0]  # Global Variable to track maximum level

def leftViewRecursive(root,current_level):
    if root is None:
        return

    if current_level > max_level[0] and root:
        print(root.data,end=" ")
        max_level[0] = current_level

    # Call Same Recursive Function for Left Subtree First then for right Subtree and increase the level by 1

    leftViewRecursive(root.left,current_level+1)
    leftViewRecursive(root.right,current_level+1)


roor = BuildTree()
preOrderRecusrsive(roor)
print()
print("Left View of Binary Tree Iterative")
leftViewIterative(roor)
print("Left View of Binary Tree Recursive")
leftViewRecursive(roor,1)






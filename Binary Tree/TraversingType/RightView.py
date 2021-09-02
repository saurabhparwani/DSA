class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def BuildTree():
    root = Node(50)
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


# Iterative Method to Print Right  View Of Binary Tree
# Right  View : Last Node at each level
def rightViewIterative(root):
    if root is None:
        print("Root is Null")
        return
    queue = []
    queue.append(root)

    while queue:

         count = len(queue)
         while count > 0:

            # Pop first element from Queue
            node = queue.pop(0)

            # To Check basically it is last Node or Not
            if count==1:
                print(node.data, end =" ")

            # Decrease the Count
            count -= 1

            # Add Left and Right node to Queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    print()



# Recursive Method to Print Right view of Binary Tree
# In this Method we will print first node  of each level (Calling Right Node First)  and to track the new maximum level we will use a variable.

max_level = [0]  # Global Variable to track maximum level

def  rightViewRecursive(root,current_level):
    if root is None:
        return

    if current_level > max_level[0] and root:
        print(root.data,end=" ")
        max_level[0] = current_level


    # Call Same Recursive Function for Right Subtree First then for Left Subtree and increase the level by 1

    rightViewRecursive(root.right,current_level+1)
    rightViewRecursive(root.left,current_level+1)



roor = BuildTree()
preOrderRecusrsive(roor)
print()
print("Right View of Binary Tree Iterative")
rightViewIterative(roor)
print("Right View of Binary Tree Recursive")
rightViewRecursive(roor,1)
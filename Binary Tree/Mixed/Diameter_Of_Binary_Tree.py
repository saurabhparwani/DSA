class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)

def BuildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

class Height(object):

    def __init__(self):
        self.h = 0

    def __str__(self):
        return self.h


# Diameter of the binary Tree will be Maximum of
#  1. Left Diameter of  Tree's left subtree
#  2. Right Diameter of Tree's right subtree
#  3. Left height + Right height + 1 of binary tree.

def height(root):
    if root is None :
        return 0
    return max(height(root.left),height(root.right)) + 1


# Time Complexity is O(N*N) as we are calling height function again and again .
# We can reduce this N*N complexity to N by calculating height & diameter in same recursive call.

def diameter(root):
    if root is None:
        return 0

    # Get the Left & Rigth Height
    left_height = height(root.left)

    right_height = height(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return  max(left_height+right_height+1, max(left_diameter,right_diameter))

# Time Complexity is O(N) as we are calling diameter & Height function in same method .

def diameterOptimized(root,height):
    # Base Condition
    if root is None:
        height.h =0
        return 0

    # Initialize the left height
    left_height = Height()
    right_height = Height()


    # Get the Left & Right Diameter

    left_diameter = diameterOptimized(root.left,left_height)
    right_diameter = diameterOptimized(root.right,right_height)

    height.h = max(left_height.h,right_height.h)+1

    return  max(left_height.h+right_height.h+1 , max (left_diameter, right_diameter))


# Driver Code
root = BuildTree()
print(diameter(root))
print(diameterOptimized(root,Height()))
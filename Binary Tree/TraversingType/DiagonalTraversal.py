from collections import defaultdict
from collections import deque
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
def BuildTree():
    root=Node(8)
    root.left=Node(3)
    root.left.left=Node(1)
    root.right=Node(10)
    root.right.left=Node(6)
    root.right.left.left = Node(4)
    root.right.left.right = Node(7)
    root.right.right=Node(14)
    root.right.right.left = Node(13)
    return root
def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

# Helper method which is doing Basically Pre order traversal and storing the nodes value based upon the key.
def diagonalTraversalHelper(root, d, slope):
    if root:
        try:
            d[slope].append(root.data)
        except KeyError:
            d[slope] = root.data

        diagonalTraversalHelper(root.left, d, slope + 1)

        diagonalTraversalHelper(root.right, d, slope)

# Method 1 : By Using Recursion , left node will be present on the next diagonal but the right node will be available
#            on the same slope so left will be slope +1 and right slope will be same as parent node.
#            We can also solve this problem by using iterative method using Queue.
#            TC = O(NLogN)   Because it takes O(LogN) time to insert element in ordered map and there are total N nodes.
#            SC = O(N) For the Map
def diagonalTraversal(root):
    if root:
        d = defaultdict(list)
        # Start the Helper Method from root.
        diagonalTraversalHelper(root, d, 0)

        # Print the Output
        for i in d:
            for j in d[i]:
                print(j, end=" ")
            print()

# Method 2 : Using Queue
# Efficient method to traverse the tree in diagonal manner . In this we will use queue and check that if left child is present then
# we will insert that into queue else we will simply assign the root.right to root as it's lying on same slope.
# TC = O(2N) = O(N) As max we can traverse each node twice. SC = O(N) For Queue.
def diagonalTraversalEfficient(root):
    # Check for Root None condition and initialize the variables
    if root:
        queue = deque()
        node = root
        count = 0

        while node:
            # Print the Node
            print(node.data,end=" ")

            # If node has left child then store that into queue  for next slope processing.
            if node.left:
                queue.append(node.left)
                count += 1

            # If node has right element means there exist element on same slope so process it first.
            if node.right:
                node = node.right
            # Else Elements on same slope does not exist so process the next slope's elements.
            else:
                # If elements exist in Queue then pop it.
                if count >0:
                    node = queue.popleft()
                    count-=1
                # Else mark current node as None and then process further.
                else:
                    node = None


# Problem Statement : https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
root = BuildTree()
print("PreOrder Traversal : ",end="\n")
preOrderRecusrsive(root)
print("\n\nDiagonal Traversal : ",end="\n")
diagonalTraversal(root)

print("\nEfficient Diagonal Traversal : ",end="\n")
diagonalTraversalEfficient(root)
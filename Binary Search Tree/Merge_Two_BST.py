# Problem Statement : https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createBST1():
    root = Node(100)
    root.left = Node(50)
    root.right = Node(300)
    root.left.left = Node(20)
    root.left.right = Node(70)
    return root

def createBST2():
    root = Node(80)
    root.left = Node(40)
    root.right = Node(120)
    return root

# Method 1 : Do In order traversal of 1st tree and store it in the 1st array & then do In order traversal of 2nd tree and store it in 2nd list.
# Now Merge both the array into the 1 array. This way time is O(M+N) and Space is also O(M+N) as we are traversing the both tree .

# Method 2 :Optimized Method TC = O(H1 + H2) SC = O(M+N) In single Traversal.
def inordertraversal(root1,root2,stack1,stack2,answer):
    if root1 and root2:
         curr1 = root1
         curr2 = root2
         stack1.append(curr1)
         stack2.append(curr2)

         curr1 = curr1.left
         curr2 = curr2.left

         while curr1 or curr2 or stack1 or stack2:
             # print(answer)
             while curr1:       # Traverse Till Any of the Node is having Values
                stack1.append(curr1)
                curr1 = curr1.left

             while curr2:
                 stack2.append(curr2)
                 curr2 = curr2.left


             # If second stack is empty or element at first stack is smaller then element at second stack.
             if (not stack2) or (stack1 and stack1[-1].data <= stack2[-1].data):
                 curr1 = stack1.pop()
                 answer.append(curr1.data)
                 curr1 = curr1.right

             # If element at first stack is bigger than element at second stack.
             else:
                 curr2 = stack2.pop()
                 answer.append(curr2.data)
                 curr2 = curr2.right

def mergeTwoBST(root1,root2):

    answer = []  # Answer Array to append .
    stack1 = []
    stack2 = []
    inordertraversal(root1,root2,stack1,stack2,answer)
    return  answer

# Driver Code

root1 = createBST1()
root2 = createBST2()


ans = mergeTwoBST(root1,root2)
print(ans)
